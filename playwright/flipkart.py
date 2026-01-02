from playwright.sync_api import Page, expect

def test_flipkart_login_form_validation(page: Page):
    page.goto("https://www.flipkart.com/", timeout=60000)

    # Close login popup if auto-opened
    try:
        page.locator("button:has-text('✕')").click(timeout=3000)
    except:
        pass

    page.locator("text=Login").first.click()

    input_box = page.locator("input[type='text']").first
    request_otp_btn = page.locator("button:has-text('Request OTP')")

    # invalid input
    input_box.fill("12345")
    expect(request_otp_btn).to_be_disabled()

    # valid format (dummy number)
    input_box.fill("9999999999")
    expect(request_otp_btn).to_be_enabled()
