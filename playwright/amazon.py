from playwright.sync_api import Page

def test_amazon(page: Page):
    page.goto("https://www.amazon.in", wait_until="domcontentloaded")

    # Search
    page.fill("#twotabsearchtextbox", "gift voucher")
    page.click("#nav-search-submit-button")

    # Wait for results
    page.wait_for_selector("div.s-main-slot")

    # Get first product title
    first_product = page.locator(
        "div.s-main-slot div[data-component-type='s-search-result'] h2 span"
    ).first

    product_name = first_product.inner_text()
    print(f"First product name: {product_name}")

    # Keep browser open for observation
    page.wait_for_timeout(10000)
