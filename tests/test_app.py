from playwright.sync_api import Page, expect

def test_get_albums(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")

    expect(page.locator("h1")).to_have_text("Albums")

    first_album_block = page.locator("div").nth(0)
    expect(first_album_block).to_contain_text("Title: Doolittle")
    expect(first_album_block).to_contain_text("Released: 1989")

    first_album_block = page.locator("div").nth(-1)
    expect(first_album_block).to_contain_text("Title: Ring Ring")
    expect(first_album_block).to_contain_text("Released: 1973")

def test_get_album_by_id_1(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/1")

    expect(page.locator("h1")).to_have_text("Doolittle")
    p_block = page.locator("p")
    
    expect(p_block).to_contain_text("Release year: 1989")
    expect(p_block).to_contain_text("Artist: Pixies")

def test_get_album_by_id_2(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/2")

    expect(page.locator("h1")).to_have_text("Surfer Rosa")
    p_block = page.locator("p")
    
    expect(p_block).to_contain_text("Release year: 1988")
    expect(p_block).to_contain_text("Artist: Pixies")

def test_get_album_by_id_3(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/3")

    expect(page.locator("h1")).to_have_text("Waterloo")
    p_block = page.locator("p")
    
    expect(p_block).to_contain_text("Release year: 1974")
    expect(p_block).to_contain_text("Artist: ABBA")