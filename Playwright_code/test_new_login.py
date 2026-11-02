from time import time

from playwright.async_api import Page
from playwright.sync_api import expect


def test_login(page: Page):
    page.goto("https://with-bugs.practicesoftwaretesting.com/#/contact")
    page.locator("#first_name").fill("John")
    page.locator("#last_name").fill("Doe")
    page.locator("#email").fill("manojseela@gmail.com")
    page.locator("#subject").select_option("customer-service")
    page.locator("#message").fill("I want to test the application and report the bugs and want to report the bugs I want to test the application and report")
    page.locator("#attachment").click()
    page.get_by_role("button",name="Send").click()
    expect(page.get_by_text("Thanks for your message! We will contact you shortly."))



def test_invalid_login(page: Page):
    page.goto("https://with-bugs.practicesoftwaretesting.com/#/contact")
    page.locator("#first_name").fill("")
    page.locator("#last_name").fill("Doe")
    page.locator("#email").fill("manojseela@gmail.com")
    page.locator("#subject").select_option("customer-service")
    page.locator("#message").fill("I want to test the application and report the bugs and want to report the bugs I want to test the application and report")
    page.locator("#attachment").click()
    page.get_by_role("button",name="Send").click()


def test_new_login(page: Page):
    try:
        page.goto("https://with-bugs.practicesoftwaretesting.com/#/contact")
        page.locator("#first_name").fill("John")
        page.locator("#last_name").fill("Doe")
        page.locator("#email").fill("manojseela@gmail.com")
        page.locator("#subject").select_option("customer-service")
        page.locator("#message").fill(
            "I want to test the application and report the bugs and want to report the bugs I want to test the application and report")
        page.locator("#attachment").click()
        page.get_by_role("button", name="Send").click()
        expect(page.get_by_text("Thanks for your message! We will contact you shortly."))
        page.screenshot(path="new_order_success__.png", full_page=True)

    except Exception:
        page.screenshot(path="order_failure__.png", full_page=True)
        raise

