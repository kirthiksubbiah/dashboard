from playwright.sync_api import sync_playwright, expect

def test_create_ticket_like_jira():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Open Jira-like demo app
        page.goto("https://demo.playwright.dev/todomvc", timeout=60000)

        # 2. Create a "ticket"
        ticket_title = "Fix login bug - Thala Ajith release"
        new_ticket_input = page.locator("input.new-todo")

        expect(new_ticket_input).to_be_visible()
        new_ticket_input.fill(ticket_title)
        new_ticket_input.press("Enter")

        # 3. Verify ticket is created 
        ticket = page.locator("li").filter(
            has=page.locator("label", has_text=ticket_title)
        )
        expect(ticket).to_be_visible()

        # 4. Mark ticket as Done
        ticket.locator("input.toggle").click()

        # 5. Assert ticket is completed
        expect(ticket).to_have_class("completed")

        page.wait_for_timeout(3000)

        context.close()
        browser.close()
