from playwright.sync_api import sync_playwright, expect

def test_youtube_search_and_play():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Open YouTube
        page.goto("https://www.youtube.com", wait_until="domcontentloaded", timeout=60000)

        # 2. Handle consent safely (if present)
        try:
            page.locator("button:has-text('Accept')").click(timeout=5000)
        except:
            pass  # no consent popup

        # 3. WAIT for search box (this is the key fix)
        search_box = page.locator("input[name='search_query']")
        expect(search_box).to_be_visible(timeout=15000)

        # 4. Search
        search_box.fill("Playwright python")
        search_box.press("Enter")

        # 5. Wait for results
        page.wait_for_selector("ytd-video-renderer", timeout=15000)

        # 6. Click first video
        page.locator("ytd-video-renderer a#thumbnail").first.click()

        # 7. Let video play
        page.wait_for_timeout(5000)

        context.close()
        browser.close()
