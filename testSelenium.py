from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def outputSource(text):
    path = "test.txt"
    f = open(path, 'w')
    f.write(text)
    f.close()


def test():
    #ブラウザを立ち上げずに操作するヘッドレスモードとやらがあるそうな
    #options = Options()
    #potions.add_argument("--headless")
    #browser = webdriver.Firefox(firefox_options=options)

    browser = webdriver.Firefox()
    wait = WebDriverWait(browser, 10)
    #browser.get("http://seleniumhp.org/")
    browser.get("https://datacentersupport.lenovo.com/jp/ja/solutions/ht507201")
    wait.until(expected_conditions.presence_of_element_located((By.ID, "contentBody")))
    outputSource(browser.page_source)
    #print(browser.find_element_by_tag_name("p"))


if __name__ == '__main__':
    test()
    