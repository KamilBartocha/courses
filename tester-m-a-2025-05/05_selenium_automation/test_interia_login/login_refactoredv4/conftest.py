import pytest
import os
from datetime import datetime

SCREENSHOT_DIR = "screenshots"

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed and hasattr(item, "driver"):
        driver = item.driver
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = item.name
        filename = f"{SCREENSHOT_DIR}/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"\n📸 Screenshot saved: {filename}")
