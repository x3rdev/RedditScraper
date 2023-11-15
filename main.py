import random
import time

import selenium.webdriver.common.by
from selenium import webdriver
import json


def getRedditPost():
    driver = webdriver.Firefox()
    driver.get("https://www.reddit.com/r/AmItheAsshole/.json")
    time.sleep(1)
    driver.find_element(selenium.webdriver.common.by.By.XPATH, "/html/body/div/div/nav/ul/li[2]").click()
    content = driver.find_element(selenium.webdriver.common.by.By.XPATH,
                                  '/html/body/div/div/div/div[2]/div/div/div[2]/pre').text
    data = json.loads(content)

    json.dump(content, open("./temp/data.json", "w"))

    i = int(((len(data["data"]["children"]) - 1) * random.random()) + 1)
    title = data["data"]["children"][i]["data"]["title"]
    print(title)
    text = data["data"]["children"][i]["data"]["selftext"]
    print(text)
    driver.quit()


if __name__ == '__main__':
    getRedditPost()
