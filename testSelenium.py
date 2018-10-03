from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def outputSource(text, filename):
    f = open("D:\\python\\" + filename, 'w', encoding='UTF-8')
    try:
        f.write(text)
    except Exception as e:
        print(e)
    finally:
        f.close()



def createReportFile():
    #ブラウザを立ち上げずに操作するヘッドレスモードとやらがあるそうな
    #options = Options()
    #potions.add_argument("--headless")
    #browser = webdriver.Firefox(firefox_options=options)

    browser = webdriver.Firefox()
    wait = WebDriverWait(browser, 10)
    #browser.get("http://seleniumhp.org/")
    browser.get("https://datacentersupport.lenovo.com/jp/ja/solutions/ht507201")
    wait.until(expected_conditions.presence_of_element_located((By.ID, "contentBody")))
    outputSource(browser.page_source, "test.html")
    

    #print(browser.find_element_by_tag_name("p"))

def fetchList():
    #ブラウザを立ち上げずに操作するヘッドレスモードとやらがあるそうな
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(firefox_options=options)

    #browser = webdriver.Firefox()
    wait = WebDriverWait(browser, 10)
    browser.get("https://kimkaz@jp.ibm.com:Juloct10@servicetools.lenovo.com/latesttips")
    wait.until(expected_conditions.presence_of_element_located((By.ID, "latestx")))
    #outputSource(browser.page_source, "GLOSSE.html")
    get_table_element = browser.find_element_by_tag_name("table")
    get_row_elements = get_table_element.find_elements_by_tag_name("tr")
    get_row_url = get_row_elements[2].find_elements_by_tag_name("a")

    for i in range(1, len(get_row_elements)):
        get_row_url = get_row_elements[i].find_elements_by_tag_name("a")
        
        print(get_row_elements[i].text)
        if len(get_row_url) > 0:
            print(get_row_url[1].get_attribute("href"))

        print(" ")


    
    #
    #print(get_row_elements[2].text)
    #output URL
    #print(get_row_url[1].get_attribute("href"))


if __name__ == '__main__':
    fetchList()
    print("END")
    