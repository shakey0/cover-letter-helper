from playwright.sync_api import expect


def test_add_varibles_set_working(reseed_base_data, page, test_web_address):
    
    # Go to edit_base page and click on add variables set button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-var img')
    page.wait_for_timeout(100)
    
    # Type 'Test Set' in the name box (already in focus) and press Enter
    page.keyboard.type('Test Set')
    page.keyboard.press('Enter')
    act_input = page.locator('#list-name-act-input')
    expect(act_input).to_have_value('Test Set')
    
    # Type 'ts' in the code box (already in focus) and press Enter
    page.keyboard.type('ts')
    page.keyboard.press('Enter')
    act_code = page.locator('#var-code-act-input')
    expect(act_code).to_have_value('**ts')
    
    # Add 3 variable words (input already in focus)
    page.keyboard.type('Cat')
    page.keyboard.press('Enter')
    page.keyboard.type('Dog')
    page.keyboard.press('Enter')
    page.keyboard.type('Rabbit')
    page.keyboard.press('Enter')
    var_boxes = page.locator('.var-box').all_text_contents()
    assert var_boxes == ['Catx', 'Dogx', 'Rabbitx']
    
    # Click the edit button and type ' More' in the name box and press Enter
    page.click('.list-name-box img')
    page.keyboard.type(' More')
    page.keyboard.press('Enter')
    act_input = page.locator('#list-name-act-input')
    expect(act_input).to_have_value('Test Set More')
    
    # Add another variable word (input already in focus)
    page.keyboard.type('Mouse')
    page.keyboard.press('Enter')
    var_boxes = page.locator('.var-box').all_text_contents()
    assert var_boxes == ['Catx', 'Dogx', 'Rabbitx', 'Mousex']
    
    # Click the edit button and type 'm' in the code box and press Enter
    page.click('.var-code-box img')
    page.keyboard.type('m')
    page.keyboard.press('Enter')
    act_code = page.locator('#var-code-act-input')
    expect(act_code).to_have_value('**tsm')
    
    # Add another variable word (input already in focus)
    page.keyboard.type('Deer')
    page.keyboard.press('Enter')
    var_boxes = page.locator('.var-box').all_text_contents()
    assert var_boxes == ['Catx', 'Dogx', 'Rabbitx', 'Mousex', 'Deerx']
    
    # Go to edit_base page and click on add variables set button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-var img')
    page.wait_for_timeout(100)
    
    # Click on the code box and type 'ns' and click the Add button
    page.click('#var-code-input')
    page.keyboard.type('ns')
    page.click('.var-code-box button:has-text("Add")')
    act_code = page.locator('#var-code-act-input')
    expect(act_code).to_have_value('**ns')
    
    # Add 2 variable words (input already in focus)
    page.keyboard.type('Lion')
    page.click('.add-var-box button:has-text("Add")')
    page.keyboard.type('Tiger')
    page.click('.add-var-box button:has-text("Add")')
    var_boxes = page.locator('.var-box').all_text_contents()
    assert var_boxes == ['Lionx', 'Tigerx']
    
    # Click on the name box and type 'Next Set' in the name box and click the Add button
    page.click('#list-name-input')
    page.keyboard.type('Next Set')
    page.click('.list-name-box button:has-text("Add")')
    act_input = page.locator('#list-name-act-input')
    expect(act_input).to_have_value('Next Set')
    
    # Add another variable word (input already in focus)
    page.keyboard.type('Hawk')
    page.click('.add-var-box button:has-text("Add")')
    var_boxes = page.locator('.var-box').all_text_contents()
    assert var_boxes == ['Lionx', 'Tigerx', 'Hawkx']
    
    # Go to edit_base page and click on add variables set button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-var img')
    page.wait_for_timeout(100)
    
    # Click on the var box and type 'Eagle' and press Enter
    page.click('#var-input')
    page.keyboard.type('Eagle')
    page.keyboard.press('Enter')
    page.keyboard.type('Parrot')
    page.keyboard.press('Enter')
    
    # Click on the code box and type 'ps' and press Enter
    page.click('#var-code-input')
    page.keyboard.type('bi')
    page.keyboard.press('Enter')
    
    # Click on the name box and type 'Birds' and press Enter
    page.click('#list-name-input')
    page.keyboard.type('Birds')
    page.keyboard.press('Enter')
    
    # Add 2 variable words (input already in focus)
    page.keyboard.type('Owl')
    page.keyboard.press('Enter')
    page.keyboard.type('Crow')
    page.keyboard.press('Enter')
    
    #Click the checkboxes for the first and third variable words
    var_box_checkboxes = page.locator('.var-box input[type="checkbox"]').all()
    var_box_checkboxes[0].check()
    var_box_checkboxes[2].check()
    
    # Click the Save List button
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("New variables set [ Birds - **bi ] added successfully.")')
    expect(success_msg).to_be_visible()
    new_set = page.locator('.variables-click-box').nth(-1)
    expect(new_set).to_be_visible()
    expect(new_set).to_contain_text('**bi - Birds')
    expect(new_set).to_contain_text('Eagle✔\nParrot\nOwl✔\nCrow')


def test_save_list_disabled_when_input_boxes_are_open(reseed_base_data, page, test_web_address):
    
    # Click the Save List button without filling in any fields
    page.goto(f"http://{test_web_address}/add_variables")
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Variables List')
    
    # Fill in the name field and add one variable word and click the Save List button
    page.goto(f"http://{test_web_address}/add_variables")
    page.keyboard.type('Test Set')
    page.keyboard.press('Enter')
    page.click('#var-input')
    page.keyboard.type('Word')
    page.keyboard.press('Enter')
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Variables List')
    
    # Fill in the code field and add one variable word and click the Save List button
    page.goto(f"http://{test_web_address}/add_variables")
    page.click('#var-code-input')
    page.keyboard.type('ts')
    page.keyboard.press('Enter')
    page.keyboard.type('Word')
    page.keyboard.press('Enter')
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Variables List')
    
    # Fill in the name and code fields and click the Save List button
    page.goto(f"http://{test_web_address}/add_variables")
    page.keyboard.type('Test Set')
    page.keyboard.press('Enter')
    page.keyboard.type('ts')
    page.keyboard.press('Enter')
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Variables List')
    
    # Fill in the name and code fields and add one variable word and click the Save List button
    page.goto(f"http://{test_web_address}/add_variables")
    page.keyboard.type('Test Set')
    page.keyboard.press('Enter')
    page.keyboard.type('ts')
    page.keyboard.press('Enter')
    page.keyboard.type('Word')
    page.keyboard.press('Enter')
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('Your Base Data')


def test_add_variables_set_rejected_if_name_or_code_is_already_in_use(reseed_base_data, page, test_web_address):
    
    # Add a variables set with name 'Test Set' and code 'ts'
    page.goto(f"http://{test_web_address}/add_variables")
    page.keyboard.type('Test Set')
    page.keyboard.press('Enter')
    page.keyboard.type('ts')
    page.keyboard.press('Enter')
    page.keyboard.type('Word')
    page.keyboard.press('Enter')
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    
    # Add a variables set with the name 'Test Set'
    page.goto(f"http://{test_web_address}/add_variables")
    page.keyboard.type('Test Set')
    page.keyboard.press('Enter')
    page.keyboard.type('tt') # This code is not in use
    page.keyboard.press('Enter')
    page.keyboard.type('Word')
    page.keyboard.press('Enter')
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    expect(page.locator('.error-msg:has-text("Name already exists")')).to_be_visible()
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Variables List')
    
    # Add a variables set with the code 'ts'
    page.goto(f"http://{test_web_address}/add_variables")
    page.keyboard.type('Another Set') # This name is not in use
    page.keyboard.press('Enter')
    page.keyboard.type('ts')
    page.keyboard.press('Enter')
    page.keyboard.type('Word')
    page.keyboard.press('Enter')
    page.click('text="Save List"')
    page.wait_for_timeout(100)
    expect(page.locator('.error-msg:has-text("Code already exists")')).to_be_visible()
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Variables List')
