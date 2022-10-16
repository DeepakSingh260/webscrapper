try:
    from selenium import webdriver 
except:
    print("no module name selenoum")

import asyncio
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
options = Options()
options.binary_location  = r"C:\Program Files\Mozilla Firefox\firefox.exe"
options.headless = True

async def func(query):
    print("flipkart function called")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.flipkart.com/search?q="+query)
    el = WebDriverWait(driver,timeout=10).until(lambda d: d.find_elements(By.CLASS_NAME,"_1AtVbE"))
    link = []
    for i in el:
        try:
            # print("var",i.find_element(By.CLASS_NAME ,"a-link-normal").get_attribute("href"))
            if i.find_element(By.CLASS_NAME ,"_30jeq3 ").text == '':
                pass
                print("pass")
                
            else:
                link.append([i.find_element(By.CLASS_NAME ,"_1fQZEK").get_attribute("href"),i.find_element(By.CLASS_NAME ,"_4rR01T").text,i.find_element(By.CLASS_NAME ,"_30jeq3").text])
        except:
            pass  
    
    for i in range(len(link)):
        lk = link[i][2][1:]
        lk = lk.split(",")
        st = ''
        for s in lk:
            st+=s
        if st!='':
            link[i][2] = int(st)
        
    link.sort(key=lambda row: (row[2]))
    [print("flipkart.in" , lk[1] , lk[2]) for lk in link]
loop= asyncio.get_event_loop()
try:
        str = input("enter you query: ")
        st = str.split(" ")
        str = ""
        for s in st:
            str = str+"+"+s
        obj = loop.create_task(func(str))
        loop.run_until_complete(obj)
finally:
    loop.close()