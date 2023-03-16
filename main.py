import base64
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image


driver = webdriver.Chrome()
driver.get("https://future-elms.com/login")

x = 0
while True:
    input("next ? \n")
    l = []
    count = driver.find_element(
        by=By.CSS_SELECTOR, value="#page_count").get_attribute("innerHTML")
    count = int(count)
    nxt = driver.find_element(by=By.CSS_SELECTOR, value="#next")

    print("starting scripe wait ....")
    while (x < count):
        time.sleep(1)
        x += 1

        canvas = driver.find_element(by=By.CSS_SELECTOR, value="#the-canvas")

        driver.execute_script(
            "document.getElementById('the-canvas').style.filter = 'blur(0)';")
        canvas_base64 = driver.execute_script(
            "return arguments[0].toDataURL('image/png').substring(21);", canvas)
        canvas_png = base64.b64decode(canvas_base64)
        with open(str(x)+".png", 'wb') as f:
            f.write(canvas_png)

        image = Image.open(str(x)+".png")
        l.append(image.convert('RGB'))
        nxt.click()
        time.sleep(1)

    print("creating pdf ..... ")
    l[0].save(r'lec .pdf', save_all=True, append_images=l)
    print("remove additional img ....")
    for i in range(1, count+1):
        os.remove(str(i)+".png")
