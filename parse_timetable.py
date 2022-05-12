# import asyncio
# from aiogram import types

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# to delete msg after some period of time  STEP-1
# async def delete_later(message: types.Message, period: int) -> None:
#     await asyncio.sleep(period)
#     await message.delete()


async def parse(class_, call):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    driver.get("https://ttpu.edupage.org/timetable/")
    driver.implicitly_wait(15)

    await call.message.answer("𝟹, 𝟸, 𝟷 ...")
    print("open")
    # to delete msg after some period of time  STEP-2
    # asyncio.create_task(delete_later(msg, 1))

    driver.refresh()
    time.sleep(2)
    print("refresh")

    classes_btn = driver.find_element(
        by=By.XPATH,
        value='/html/body/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/span[1]')
    classes_btn.click()

    time.sleep(2)

    classes = driver.find_elements(by=By.CSS_SELECTOR, value=".dropDownPanel.asc-context-menu a")

    counter = 0
    print(class_)
    for c in classes:
        if c.text == class_:
            c.click()
        counter += 1

    # click cookie button
    driver.find_element(by=By.CLASS_NAME, value='eu-cookie-closeBtn').click()

    # await call.message.answer("...")
    # asyncio.create_task(delete_later(msg, 1))

    time.sleep(0.8)
    driver.set_window_size(700, 770)
    driver.save_screenshot('image.png')
    driver.close()
