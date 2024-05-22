from playwright.sync_api import expect


def test_add_input_working(reseed_base_data, page, test_web_address):
    
    # Go to edit_base page and click on add input button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-input img')
    page.wait_for_timeout(100)
    
    # Type 'Test Input' in the name box (already in focus) and press Enter
    page.keyboard.type('Test Input')
    page.keyboard.press('Enter')
    act_input = page.locator('#input-name-act-input')
    expect(act_input).to_have_value('Test Input')
    
    # Type 'ti' in the code box (already in focus) and press Enter
    page.keyboard.type('ti')
    page.keyboard.press('Enter')
    act_code = page.locator('#input-code-act-input')
    expect(act_code).to_have_value('##ti')
    
    # Click the edit button and type ' More' in the name box and press Enter
    page.click('.input-name-box img')
    page.keyboard.type(' More')
    page.keyboard.press('Enter')
    act_input = page.locator('#input-name-act-input')
    expect(act_input).to_have_value('Test Input More')
    
    # Click the edit button and type 'm' in the code box and press Enter
    page.click('.input-code-box img')
    page.keyboard.type('m')
    page.keyboard.press('Enter')
    act_code = page.locator('#input-code-act-input')
    expect(act_code).to_have_value('##tim')
    
    # Go to edit_base page and click on add input button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-input img')
    page.wait_for_timeout(100)
    
    # Click on the code box and type 'ni' and click the Add button
    page.click('#input-code-input')
    page.keyboard.type('ni')
    page.click('.input-code-box button:has-text("Add")')
    act_code = page.locator('#input-code-act-input')
    expect(act_code).to_have_value('##ni')
    
    # Type 'Next Input' in the name box (already in focus) and click the Add button
    page.keyboard.type('Next Input')
    page.click('.input-name-box button:has-text("Add")')
    act_input = page.locator('#input-name-act-input')
    expect(act_input).to_have_value('Next Input')
    
    # Click the edit button and type ' More' in the name box and click the Add button
    page.click('.input-name-box img')
    page.keyboard.type(' More')
    page.click('.input-name-box button:has-text("Add")')
    act_input = page.locator('#input-name-act-input')
    expect(act_input).to_have_value('Next Input More')
    
    # Click the edit button and type 'm' in the code box and click the Add button
    page.click('.input-code-box img')
    page.keyboard.type('m')
    page.click('.input-code-box button:has-text("Add")')
    act_code = page.locator('#input-code-act-input')
    expect(act_code).to_have_value('##nim')
    
    # Click the Save Input button
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("New input [ Next Input More - ##nim ] added successfully.")')
    expect(success_msg).to_be_visible()
    new_input = page.locator('.input-click-box').nth(-1)
    expect(new_input).to_be_visible()
    expect(new_input).to_contain_text('##nim - Next Input More')
