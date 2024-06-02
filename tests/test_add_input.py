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


def test_save_input_disabled_when_input_boxes_are_open(reseed_base_data, page, test_web_address):
    
    # Click the Save Input button without filling in any fields
    page.goto(f"http://{test_web_address}/add_input")
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Input')
    
    # Fill in the name field and click the Save Input button
    page.goto(f"http://{test_web_address}/add_input")
    page.keyboard.type('Test Input')
    page.keyboard.press('Enter')
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Input')
    
    # Fill in the code field and click the Save Input button
    page.goto(f"http://{test_web_address}/add_input")
    page.click('#input-code-input')
    page.keyboard.type('ti')
    page.keyboard.press('Enter')
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Input')
    
    # Fill in the name and code fields and click the Save Input button
    page.goto(f"http://{test_web_address}/add_input")
    page.keyboard.type('Test Input')
    page.keyboard.press('Enter')
    page.keyboard.type('ti')
    page.keyboard.press('Enter')
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('Your Base Data')


def test_add_input_rejected_if_name_or_code_is_already_in_use(reseed_base_data, page, test_web_address):
    
    # Add an input with name 'Test Input' and code 'ti'
    page.goto(f"http://{test_web_address}/add_input")
    page.keyboard.type('Test Input')
    page.keyboard.press('Enter')
    page.keyboard.type('ti')
    page.keyboard.press('Enter')
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    
    # Add an input with the name 'Test Input'
    page.goto(f"http://{test_web_address}/add_input")
    page.keyboard.type('Test Input')
    page.keyboard.press('Enter')
    page.keyboard.type('te') # This code is not in use
    page.keyboard.press('Enter')
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    expect(page.locator('.error-msg:has-text("Name already exists")')).to_be_visible()
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Input')
    
    # Add an input with the code 'ti'
    page.goto(f"http://{test_web_address}/add_input")
    page.keyboard.type('Another Input') # This name is not in use
    page.keyboard.press('Enter')
    page.keyboard.type('ti')
    page.keyboard.press('Enter')
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    expect(page.locator('.error-msg:has-text("Code already exists")')).to_be_visible()
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Input')


def test_edit_input_working(reseed_base_data, page, test_web_address):
    
    # Go to edit_base page and click on the 'Industry' input
    page.goto(f"http://{test_web_address}/edit_base")
    page.locator('.input-click-box').nth(1).click()
    page.wait_for_timeout(100)

    # Click the edit button and type ' More' in the name box and press Enter
    page.click('.input-name-box img')
    page.keyboard.type(' More')
    page.keyboard.press('Enter')
    act_input = page.locator('#input-name-act-input')
    expect(act_input).to_have_value('Industry More')
    
    # Click the Save Input button
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("Input [ Industry More - ##in ] updated successfully.")')
    expect(success_msg).to_be_visible()
    updated_input = page.locator('.input-click-box').nth(1)
    expect(updated_input).to_be_visible()
    expect(updated_input).to_contain_text('##in - Industry More')
    
    # Click on the 'Industry More' input
    page.locator('.input-click-box').nth(1).click()
    page.wait_for_timeout(100)
    
    # Click the edit button and type 'm' in the code box and press Enter
    page.click('.input-code-box img')
    page.keyboard.type('m')
    page.keyboard.press('Enter')
    act_code = page.locator('#input-code-act-input')
    expect(act_code).to_have_value('##inm')
    
    # Click the Save Input button
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("Input [ Industry More - ##inm ] updated successfully.")')
    expect(success_msg).to_be_visible()
    updated_input = page.locator('.input-click-box').nth(1)
    expect(updated_input).to_be_visible()
    expect(updated_input).to_contain_text('##inm - Industry More')
    paragraph = page.locator('.paragraph-click-box').nth(0)
    expect(paragraph).to_contain_text('##inm girl')
    expect(paragraph).not_to_contain_text('##in girl')


def test_delete_input_working(reseed_base_data, page, test_web_address):

    # Go to edit_base page and click on add input button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-input img')
    page.wait_for_timeout(100)
    
    # Fill in the name and code fields and click the Save Input button
    page.keyboard.type('Test Input')
    page.keyboard.press('Enter')
    page.keyboard.type('ti')
    page.keyboard.press('Enter')
    page.click('text="Save Input"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('Your Base Data')
    new_input = page.locator('.input-click-box').nth(-1)
    expect(new_input).to_be_visible()
    expect(new_input).to_contain_text('##ti - Test Input')
    
    # Click on the 'Test Input' input and click the delete button
    new_input.click()
    page.wait_for_timeout(100)
    page.click('.delete-input')
    delete_input_box = page.locator('.delete-input-box')
    expect(delete_input_box).to_be_visible()
    expect(delete_input_box).to_contain_text('Delete this for sure?')
    page.click('.delete-input-box button:has-text("Yes")')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    success_msg = page.locator('.success:has-text("Input deleted successfully.")')
    expect(success_msg).to_be_visible()
    expect(page.locator('.input-click-box').nth(-1)).not_to_contain_text('##ti - Test Input')
    expect(page.locator('.input-click-box').nth(-1)).to_contain_text('##jf - Job Focus')


def test_delete_not_allowed_when_input_is_used_in_paragraph(reseed_base_data, page, test_web_address):
    
    # Go to edit_base page and click on add input button
    page.goto(f"http://{test_web_address}/edit_base")
    page.locator('.input-click-box').nth(1).click() # Click on the 'Industry More' input which is used in a paragraph
    page.wait_for_timeout(100)
    page.click('.delete-input')
    delete_input_box = page.locator('.delete-input-box')
    expect(delete_input_box).to_be_visible()
    expect(delete_input_box).to_contain_text('This input is used at least once in your paragraphs.Please remove its use in the paragraph(s) first.')


def test_reorder_inputs_on_edit_base_page(reseed_base_data, page, test_web_address):
    
    # Go to edit_base page and reorder the inputs
    page.goto(f"http://{test_web_address}/edit_base")
    item_to_drag = page.locator('.input-click-box').nth(1)
    drop_target = page.locator('.input-click-box').nth(0)
    item_to_drag.drag_to(target=drop_target)
    item_to_drag = page.locator('.input-click-box').nth(2)
    item_to_drag.drag_to(target=drop_target)
    page.goto(f"http://{test_web_address}/edit_base")
    first_input = page.locator('.input-click-box').nth(0)
    expect(first_input).to_contain_text('##jt - Job Title')
    second_input = page.locator('.input-click-box').nth(1)
    expect(second_input).to_contain_text('##in - Industry')
    third_input = page.locator('.input-click-box').nth(2)
    expect(third_input).to_contain_text('##cn - Company Name')
    fourth_input = page.locator('.input-click-box').nth(3)
    expect(fourth_input).to_contain_text('##jf - Job Focus')


def test_reorder_inputs_on_add_paragraph_page(reseed_base_data, page, test_web_address):
    
    # Go to add_paragraph page and reorder the inputs
    page.goto(f"http://{test_web_address}/add_paragraph")
    item_to_drag = page.locator('.input-click-box').nth(1)
    drop_target = page.locator('.input-click-box').nth(0)
    item_to_drag.drag_to(target=drop_target)
    item_to_drag = page.locator('.input-click-box').nth(2)
    item_to_drag.drag_to(target=drop_target)
    page.goto(f"http://{test_web_address}/edit_base")
    first_input = page.locator('.input-click-box').nth(0)
    expect(first_input).to_contain_text('##jt - Job Title')
    second_input = page.locator('.input-click-box').nth(1)
    expect(second_input).to_contain_text('##in - Industry')
    third_input = page.locator('.input-click-box').nth(2)
    expect(third_input).to_contain_text('##cn - Company Name')
    fourth_input = page.locator('.input-click-box').nth(3)
    expect(fourth_input).to_contain_text('##jf - Job Focus')
