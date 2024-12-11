import os
import allure
import pytest
from pytest import hookimpl
from playwright.sync_api import sync_playwright

headless = False

ENV_URL = "https://tracelo-git-reversly20-small-saas.vercel.app/"


@pytest.fixture(scope="session")
@allure.title(f"Set up browser: {os.getenv('BROWSER')}")
def browser(request):
    with sync_playwright() as p:
        browser_type = os.getenv("BROWSER", "chromium")
        if browser_type == "firefox":
            browser = getattr(p, browser_type).launch(headless=headless)
        if browser_type == "webkit":
            browser = getattr(p, browser_type).launch(headless=headless)
        if browser_type == "chromium":
            browser = getattr(p, browser_type).launch(headless=headless, channel='chrome')
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(request, browser):
    trace_path = f"artifacts/traces/{request.node.name}.zip"
    context = browser.new_context(viewport={"width": 1440, "height": 1080}, record_video_dir="artifacts/videos/")
    context.tracing.start(name=f"{request.node.name}.zip", screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path=trace_path)
    context.close()
    if not request.node.rep_call.failed:
        if os.path.exists(trace_path):
            os.remove(trace_path)


@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"artifacts/screenshots/{request.node.name}.png", full_page=True)
    page.close()
    if request.node.rep_call.failed:
        page.video.save_as(path=f"artifacts/videos/{request.node.name}.webm")


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
@allure.title("Failed test artifacts")
def artifacts(request):
    yield
    if request.node.rep_call.failed:
        allure.attach.file(f"artifacts/screenshots/{request.node.name}.png", name="screenshot",
                           attachment_type=allure.attachment_type.PNG)
        allure.attach.file(f"artifacts/videos/{request.node.name}.webm", name="video",
                           attachment_type=allure.attachment_type.WEBM)
        allure.attach.file(f"artifacts/traces/{request.node.name}.zip", name="trace", extension="zip")