from playwright.sync_api import expect


def test_add_paragraph_working(reseed_base_data, page, test_web_address):
    
    # Go to edit_base page and click on add paragraph button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-par img')
    page.wait_for_timeout(100)
    
    # Type 'Test Paragraph' in the name box (already in focus) and press Enter
    page.keyboard.type('Test Paragraph')
    page.keyboard.press('Enter')
    act_input = page.locator('#paragraph-name-act-input')
    expect(act_input).to_have_value('Test Paragraph')
    
    # Type some text in the text box (already in focus) and press Enter
    page.keyboard.type('This is a very nice test paragraph.')
    page.keyboard.press('Enter')
    act_code = page.locator('#paragraph-text-act-input')
    expect(act_code).to_have_value('This is a very nice test paragraph.')
    
    # Click the edit button and type ' More' in the name box and press Enter
    page.click('.paragraph-name-box img')
    page.keyboard.type(' More')
    page.keyboard.press('Enter')
    act_input = page.locator('#paragraph-name-act-input')
    expect(act_input).to_have_value('Test Paragraph More')
    
    # Click the edit button and type some more text in the text box and press Enter
    page.click('.paragraph-text-box img')
    page.keyboard.type(' More text.')
    page.keyboard.press('Enter')
    act_code = page.locator('#paragraph-text-act-input')
    expect(act_code).to_have_value('This is a very nice test paragraph. More text.')
    
    # Go to edit_base page and click on add paragraph button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-par img')
    page.wait_for_timeout(100)
    
    # Click on the text box and type some text and click the Add button
    page.click('#paragraph-text-input')
    page.keyboard.type('This is another lovely test paragraph.')
    page.click('.paragraph-text-box button:has-text("Preview Paragraph")')
    act_code = page.locator('#paragraph-text-act-input')
    expect(act_code).to_have_value('This is another lovely test paragraph.')
    
    # Type 'Next Paragraph' in the name box (already in focus) and click the Add button
    page.keyboard.type('Next Paragraph')
    page.click('.paragraph-name-box button:has-text("Add")')
    act_input = page.locator('#paragraph-name-act-input')
    expect(act_input).to_have_value('Next Paragraph')
    
    # Click the edit button and type ' More' in the name box and click the Add button
    page.click('.paragraph-name-box img')
    page.keyboard.type(' More')
    page.click('.paragraph-name-box button:has-text("Add")')
    act_input = page.locator('#paragraph-name-act-input')
    expect(act_input).to_have_value('Next Paragraph More')
    
    # Click the edit button and type some more text in the text box and click the Add button
    page.click('.paragraph-text-box img')
    page.keyboard.type(' More text.')
    page.click('.paragraph-text-box button:has-text("Preview Paragraph")')
    act_code = page.locator('#paragraph-text-act-input')
    expect(act_code).to_have_value('This is another lovely test paragraph. More text.')
    
    # Click the Save Paragraph button
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("New paragraph [ Next Paragraph More ] added successfully.")')
    expect(success_msg).to_be_visible()
    new_set = page.locator('.paragraph-click-box').nth(-1)
    expect(new_set).to_be_visible()
    expect(new_set).to_contain_text('Next Paragraph More')
    expect(new_set).to_contain_text('This is another lovely test paragraph. More text.')


def test_save_paragraph_disabled_when_input_boxes_are_open(reseed_base_data, page, test_web_address):
    
    # Click the Save Paragraph button without filling in any fields
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Paragraph')
    
    # Fill in the name field and click the Save Paragraph button
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.keyboard.type('Test Paragraph')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Paragraph')
    
    # Fill in the text field and click the Save Paragraph button
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.click('#paragraph-text-input')
    page.keyboard.type('This is a beautiful test paragraph.')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Paragraph')
    
    # Fill in the name and text fields and click the Save Paragraph button
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.keyboard.type('Test Paragraph')
    page.keyboard.press('Enter')
    page.keyboard.type('This is a beautiful test paragraph.')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('Your Base Data')


def test_add_paragraph_rejected_if_name_is_already_in_use(reseed_base_data, page, test_web_address):
    
    # Add a paragraph with name 'Test Paragraph' and some text
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.keyboard.type('Test Paragraph')
    page.keyboard.press('Enter')
    page.keyboard.type('This is a wonderful test paragraph.')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    
    # Add a paragraph with name 'Test Paragraph'
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.keyboard.type('Test Paragraph')
    page.keyboard.press('Enter')
    page.keyboard.type('This is a wonderful test paragraph.') # Paragraph text is not checked for uniqueness
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('.error-msg:has-text("Name already exists")')).to_be_visible()
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Paragraph')
    

def test_add_paragraph_rejected_if_inputs_or_variables_sets_are_not_found(reseed_base_data, page, test_web_address):
    
    # Add a paragraph with name 'Test Paragraph' and some text with an input and a variables set
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.keyboard.type('Test Paragraph')
    page.keyboard.press('Enter')
    page.keyboard.type('This is a wonderful test paragraph. [input: ##cn] [variables: **fe]')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('Your Base Data')
    new_set = page.locator('.paragraph-click-box').nth(-1)
    expect(new_set).to_contain_text('Test Paragraph')
    expect(new_set).to_contain_text('This is a wonderful test paragraph. [input: ##cn] [variables: **fe]')
    
    # Add a paragraph with name 'Test Paragraph' and some text with an input that does not exist
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.keyboard.type('Test Paragraph 2')
    page.keyboard.press('Enter')
    page.keyboard.type('This is a wonderful test paragraph. [input: ##aa] [variables: **fe]')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('.error-msg:has-text("Input \'##aa\' has not been created")')).to_be_visible()
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Paragraph')
    
    # Add a paragraph with name 'Test Paragraph' and some text with a variables set that does not exist
    page.goto(f"http://{test_web_address}/add_paragraph")
    page.keyboard.type('Test Paragraph 3')
    page.keyboard.press('Enter')
    page.keyboard.type('This is a wonderful test paragraph. [input: ##cn] [variables: **aa]')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('.error-msg:has-text("Variables set \'**aa\' has not been created")')).to_be_visible()
    expect(page.locator('text="Your Base Data"')).not_to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('New Paragraph')
