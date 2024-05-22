import sys, random, py, pytest, json, os
from playwright.sync_api import sync_playwright
from xprocess import ProcessStarter


@pytest.fixture(scope="function")
def reseed_base_data():
    data = None
    with open ("tests/base_data_seed.json", "r") as base_data_file:
        data = json.load(base_data_file)
    with open("lib/base_data.json", "w") as base_data_file:
        json.dump(data, base_data_file, indent=4)


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def test_web_address(xprocess):
    python_executable = sys.executable
    app_file = py.path.local(__file__).dirpath("../app.py")
    port = str(random.randint(4000, 4999))
    class Starter(ProcessStarter):
        env = {"PORT": port, "APP_ENV": "test", "ROOT_DIR": os.getcwd()}
        pattern = "Debugger PIN"
        args = [python_executable, app_file]

    xprocess.ensure("flask_test_server", Starter)

    yield f"localhost:{port}"

    xprocess.getinfo("flask_test_server").terminate()
