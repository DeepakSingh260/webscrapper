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
    driver.get("https://www.meesho.com/search?q="+query)
    el = WebDriverWait(driver,timeout=10).until(lambda d: d.find_elements(By.CLASS_NAME,"sc-dkPtyc"))
    link = []
    for i in el:
        try:
            # print("var",i.find_element(By.CLASS_NAME ,"a-link-normal").get_attribute("href"))
            if i.find_element(By.CLASS_NAME ,"BBZyK").text == '':
                pass
            else:
                link.append([i.find_element(By.TAG_NAME ,"a").get_attribute("href"),i.find_element(By.CLASS_NAME ,"NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5").text,i.find_element(By.CLASS_NAME ,"BBZyK").text])
        except:
            pass  
    [print("meesho.in" , lk[1], lk[2]) for lk in link ]
    #NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 




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