from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from typing import Optional, Union
import os
import time
import random
import json


def get_data(
        url: str,
        driver_path: Union[os.PathLike, str],
        max_delay: int = 15
) -> Optional[str]:
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument('--headless')

        service = Service(driver_path)

        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)
        driver.maximize_window()

        delay = random.randint(0, max_delay)
        print(f'\nDelay for a {delay} seconds at \n{url}...')
        time.sleep(delay)

        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        new_cookies = driver.get_cookies()
        new_cookies = json.dumps(new_cookies)
        time.sleep(1)
    except Exception as ex:
        print(ex)
        new_cookies = None
    finally:
        driver.close()
        driver.quit()
        return new_cookies
