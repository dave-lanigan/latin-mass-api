"""
Script scraps site with selenium

"""


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
import os
import time
import json
os.environ['MOZ_HEADLESS'] = '1'

"""
other:
catholicnews.com
aleteia.org
remnantnewspaper.com
osvnews.com

date, name, number
"""


url = "www.similarweb.com/website/{}/"
sites = ["churchmilitant.com", "ncregister.com",
         "lifesitenews.com", "catholicworldreport.com",
         "catholicnewsagency.com", "ewtn.com", "cruxnow.com", "catholicherald.co.uk",
         "ncronline.org", ]

vals = []
driver = webdriver.Firefox()
for site in sites:
    driver.get(url.format(site[1]))
    time.sleep(15)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    val = soup.find_all(
        class_="engagementInfo-valueNumber js-countValue")[0].text

driver.quit()


# [<span class="engagementInfo-valueNumber js-countValue">1.24M</span>, <span class="engagementInfo-valueNumber js-countValue">00:04:05</span>, <span class="engagementInfo-valueNumber js-countValue">2.77</span>, <span class="engagementInfo-valueNumber js-countValue">55.74%</span>]
