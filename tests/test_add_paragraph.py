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
    act_text = page.locator('#paragraph-text-act-input')
    expect(act_text).to_have_value('This is a very nice test paragraph.')
    
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
    act_text = page.locator('#paragraph-text-act-input')
    expect(act_text).to_have_value('This is a very nice test paragraph. More text.')
    
    # Go to edit_base page and click on add paragraph button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-par img')
    page.wait_for_timeout(100)
    
    # Click on the text box and type some text and click the Add button
    page.click('#paragraph-text-input')
    page.keyboard.type('This is another lovely test paragraph.')
    page.click('.paragraph-text-box button:has-text("Preview Paragraph")')
    act_text = page.locator('#paragraph-text-act-input')
    expect(act_text).to_have_value('This is another lovely test paragraph.')
    
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
    act_text = page.locator('#paragraph-text-act-input')
    expect(act_text).to_have_value('This is another lovely test paragraph. More text.')
    
    # Click the Save Paragraph button
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("New paragraph [ Next Paragraph More ] added successfully.")')
    expect(success_msg).to_be_visible()
    new_paragraph = page.locator('.paragraph-click-box').nth(-1)
    expect(new_paragraph).to_be_visible()
    expect(new_paragraph).to_contain_text('Next Paragraph More')
    expect(new_paragraph).to_contain_text('This is another lovely test paragraph. More text.')


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
    new_paragraph = page.locator('.paragraph-click-box').nth(-1)
    expect(new_paragraph).to_contain_text('Test Paragraph')
    expect(new_paragraph).to_contain_text('This is a wonderful test paragraph. [input: ##cn] [variables: **fe]')
    
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


def test_edit_paragraph_working(reseed_base_data, page, test_web_address):
    
    # Go to edit_base page and click on the 'Experiences' paragraph
    page.goto(f"http://{test_web_address}/edit_base")
    page.locator('.paragraph-click-box').nth(1).click()
    page.wait_for_timeout(100)
    
    # Click the edit button and type ' More' in the name box and press Enter
    page.click('.paragraph-name-box img')
    page.keyboard.type(' More')
    page.keyboard.press('Enter')
    act_input = page.locator('#paragraph-name-act-input')
    expect(act_input).to_have_value('Experiences More')
    
    # Click the Save Paragraph button
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("Paragraph [ Experiences More ] updated successfully.")')
    expect(success_msg).to_be_visible()
    new_paragraph = page.locator('.paragraph-click-box').nth(1)
    expect(new_paragraph).to_be_visible()
    expect(new_paragraph).to_contain_text('Experiences More')
    
    # Go to edit_base page and click on the 'Experiences' input
    page.locator('.paragraph-click-box').nth(1).click()
    page.wait_for_timeout(100)
    
    # Click the edit button and type some more text in the text box and press Enter
    page.click('.paragraph-text-box img')
    page.keyboard.type(' This **fe is another ##cn sentence.')
    page.keyboard.press('Enter')
    act_text = page.locator('#paragraph-text-act-input')
    expect(act_text).to_have_value('Deal relate individual attorney. Want will attack check dark **mo charge white. Customer challenge rich **be trade exactly. Western deal writer small. Decade you rock else. Shoulder little white prevent western public **do. Interesting wear chair really wish Democrat discover. Nothing wife too front heart than church pull. Police civil before team society ##jf common strategy. Rather traditional eye less even including. And then the end. This **fe is another ##cn sentence.')

    # Click the Save Input button
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    page_title = page.locator('text="Your Base Data"')
    expect(page_title).to_be_visible()
    success_msg = page.locator('.success:has-text("Paragraph [ Experiences More ] updated successfully.")')
    expect(success_msg).to_be_visible()
    updated_paragraph = page.locator('.paragraph-click-box').nth(1)
    expect(updated_paragraph).to_be_visible()
    expect(updated_paragraph).to_contain_text('Deal relate individual attorney. Want will attack check dark **mo charge white. Customer challenge rich **be trade exactly. Western deal writer small. Decade you rock else. Shoulder little white prevent western public **do. Interesting wear chair really wish Democrat discover. Nothing wife too front heart than church pull. Police civil before team society ##jf common strategy. Rather traditional eye less even including. And then the end. This **fe is another ##cn sentence.')


def test_delete_paragraph_working(reseed_base_data, page, test_web_address):

    # Go to edit_base page and click on add paragraph button
    page.goto(f"http://{test_web_address}/edit_base")
    page.click('.add-btn-par img')
    page.wait_for_timeout(100)
    
    # Fill in the name and text fields and click the Save Paragraph button
    page.keyboard.type('Test Paragraph')
    page.keyboard.press('Enter')
    page.keyboard.type('This is a beautiful test paragraph.')
    page.keyboard.press('Enter')
    page.click('text="Save Paragraph"')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    page_title = page.locator('.page-title')
    expect(page_title).to_have_text('Your Base Data')
    new_paragraph = page.locator('.paragraph-click-box').nth(-1)
    expect(new_paragraph).to_be_visible()
    expect(new_paragraph).to_contain_text('Test Paragraph')
    expect(new_paragraph).to_contain_text('This is a beautiful test paragraph.')
    
    # Click on the 'Test Paragraph' paragraph and click the delete button
    new_paragraph.click()
    page.wait_for_timeout(100)
    page.click('.delete-paragraph')
    delete_paragraph_box = page.locator('.delete-paragraph-box')
    expect(delete_paragraph_box).to_be_visible()
    expect(delete_paragraph_box).to_contain_text('Delete this for sure?')
    page.click('.delete-paragraph-box button:has-text("Yes")')
    page.wait_for_timeout(100)
    expect(page.locator('text="Your Base Data"')).to_be_visible()
    success_msg = page.locator('.success:has-text("Paragraph deleted successfully.")')
    expect(success_msg).to_be_visible()
    expect(page.locator('.paragraph-click-box').nth(-1)).not_to_contain_text('Test Paragraph')
    expect(page.locator('.paragraph-click-box').nth(-1)).not_to_contain_text('This is a beautiful test paragraph.')
    expect(page.locator('.paragraph-click-box').nth(-1)).to_contain_text('Skills')
    expect(page.locator('.paragraph-click-box').nth(-1)).to_contain_text('Factor international usually herself benefit though need meeting **ot. Instead personal dark would appear difference state. Culture ten represent appear allow find language **te music. Ball blood require reduce person while **fe. Court education general support best always study. Citizen memory can. Person itself letter morning return buy fund. Scene many capital money support expert ##cn. Board again candidate among child daughter their. Among event ##in although likely turn.')


def test_reorder_paragraphs_on_edit_base_page(reseed_base_data, page, test_web_address):

    # Go to edit_base page and reorder the paragraphs
    page.goto(f"http://{test_web_address}/edit_base")
    item_to_drag = page.locator('.paragraph-click-box').nth(0)
    drop_target = page.locator('.paragraph-click-box').nth(2)
    item_to_drag.drag_to(target=drop_target)
    page.screenshot(path="screenshot.png")
    item_to_drag = page.locator('.paragraph-click-box').nth(2)
    drop_target = page.locator('.paragraph-click-box').nth(0)
    item_to_drag.drag_to(target=drop_target)
    page.goto(f"http://{test_web_address}/edit_base")
    first_paragraph = page.locator('.paragraph-click-box').nth(0)
    expect(first_paragraph).to_contain_text('Skills')
    expect(first_paragraph).to_contain_text('Factor international usually herself benefit though need meeting **ot. Instead personal dark would appear difference state. Culture ten represent appear allow find language **te music. Ball blood require reduce person while **fe. Court education general support best always study. Citizen memory can. Person itself letter morning return buy fund. Scene many capital money support expert ##cn. Board again candidate among child daughter their. Among event ##in although likely turn.')
    second_paragraph = page.locator('.paragraph-click-box').nth(1)
    expect(second_paragraph).to_contain_text('Experiences')
    expect(second_paragraph).to_contain_text('Deal relate individual attorney. Want will attack check dark **mo charge white. Customer challenge rich **be trade exactly. Western deal writer small. Decade you rock else. Shoulder little white prevent western public **do. Interesting wear chair really wish Democrat discover. Nothing wife too front heart than church pull. Police civil before team society ##jf common strategy. Rather traditional eye less even including. And then the end.')
    third_paragraph = page.locator('.paragraph-click-box').nth(2)
    expect(third_paragraph).to_contain_text('Intro')
    expect(third_paragraph).to_contain_text('Official wonder result ##cn crime item be fact. Than answer happy break. Likely school turn security service perform surface. Care account how **fe figure author. Run instead evidence direction add **mo. Company experience provide reach sing. Discuss particularly these kitchen where police most. Nearly same effect. Color ##in girl generation professor writer trade result. Beyond year out ##jt challenge much over only.')
