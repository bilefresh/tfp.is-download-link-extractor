"""
Created by Farouk Bilesanmi
"""
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

def tfp(site):
    start = datetime.datetime.now()
    pattern = r"(\(File size\).+\(.+\))"
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path="C:\\Users\\Farouk\\Desktop\\python projects\\chromedriver.exe", options=options)

    browser.get("https://tfp.is/?s="+site)
    search = browser.find_element_by_class_name("post-title")
    title = search.find_element_by_tag_name("a")
    title.click()
    te = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/article/div/div[2]")
    ty = te.text
    main = browser.find_element_by_link_text("Download Now")
    browser.execute_script("arguments[0].click();", main)
    browser.switch_to.window(browser.window_handles[-1]) 
    browser.find_element_by_xpath("/html/body/div[1]/form/p[1]/input").send_keys("tfpdl",Keys.RETURN)
    
    try:
        pat = r"(\'.+,)"
        browser.find_element_by_partial_link_text("firefiles").click()
        time.sleep(3)
        browser.switch_to.window(browser.window_handles[-1])
        btn1 = browser.find_element_by_id("method_free")
        browser.execute_script("arguments[0].click();", btn1) 
        btn2 = browser.find_element_by_id("downloadbtn")
        browser.execute_script("arguments[0].click();", btn2) 
        time.sleep(1)
        btn3 = browser.find_element_by_id("downloadbtn")
        li = btn3.get_attribute("onclick")
        lin = re.search(pat, li)
        link = str(lin.groups())
        link = str(link).replace("'","").replace(',','').replace('("','').replace('")','')
        #print(link)
        stop = datetime.datetime.now()
        result = stop - start
        print(result, 'seconds')
        browser.quit()
        return link

    except:
        try:
            browser.find_element_by_partial_link_text("bayfiles").click()
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[-1])
            titl = browser.find_element_by_tag_name("h1")
            jj = titl.text
            hh = browser.find_element_by_id("download-url")
            link = hh.get_attribute("href")
            stop = datetime.datetime.now()
            result = stop - start
            print(result, 'seconds')
            browser.quit()
            #print(link)
            return link
        except:
            gg = browser.find_element_by_partial_link_text("zippyshare")
            link = gg.get_attribute("href")
            print(link)
            gg.click()
            browser.switch_to.window(browser.window_handles[-1]) 
            jj = browser.find_element_by_id("dlbutton")
            linkk = jj.get_attribute("href")
            #print(linkk)
            #jj.click()
            browser.quit()
            stop = datetime.datetime.now()
            result = stop - start
            print(result, 'seconds')
            return linkk
ss = input("Enter what you want to download: ")
print(tfp(ss))
input("Press Enter to close.....")
