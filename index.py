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

async def func():
    print("function called")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.amazon.in/s?k=nike+jordar")
    
    el = WebDriverWait(driver,timeout=10).until(lambda d: d.find_elements(By.CLASS_NAME,"s-card-container"))
    link = []
    for i in el:
        try:
            # print("var",i.find_element(By.CLASS_NAME ,"a-link-normal").get_attribute("href"))
            if i.find_element(By.CLASS_NAME ,"a-price-whole").text == '':
                pass
            else:
                link.append([i.find_element(By.CLASS_NAME ,"a-link-normal").get_attribute("href"),"",i.find_element(By.CLASS_NAME ,"a-price-whole").text])
        except:
            pass  
    # print("link" , link)
    for i in range(len(link)):
        lk = link[i][2].split(",")
        st = ''
        for s in lk:
            st+=s
        if st!='':
            link[i][2] = int(st)
        
    link.sort(key=lambda row: (row[2]))
   
    for i in range(min(len(link),3)):

        driver.get(link[i][0])
        link[i][1] = driver.find_element(By.ID , "title").text
        print("amazon.in",link[i][1] , link[i][2])

    # [print(lk) for lk in link] 



loop= asyncio.get_event_loop()
try:
        obj = loop.create_task(func())
        loop.run_until_complete(obj)
finally:
    loop.close()

# asyncio.run(test())


