from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class framework:

    def __init__ (self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.url = "https://scholar.google.com/schhp?hl=en&as_sdt=0"

        self.method = [By.LINK_TEXT, By.ID, By.TAG_NAME]

    def run(self):
        self.search_on_google_scholar()
        results = self.list_results()
        articles = results.find_elements_by_class_name("gs_ri")
        for article in articles:
            try:
                header = article.find_element_by_tag_name("a")
                header.click()
            except:
                self.driver.quit()

    def search_on_google_scholar(self):
        self.driver.get(self.url)
        print(self.driver.title)
        search = self.driver.find_element_by_name("q")
        search.send_keys(input("Search field: "))
        search.send_keys(Keys.RETURN)
        link = self.driver.find_element_by_link_text("Since 2020")
        link.click()

    def list_results(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "gs_res_ccl_mid"))
                )
        except:
            self.driver.quit()
        return element

    def get_article_headers(self):
        results = self.list_results()
        articles = results.find_elements_by_class_name("gs_ri")
        for article in articles:
            header = article.find_element_by_tag_name("a")
            print(header.text)

    def terminate(self):
        self.driver.quit()
            

if __name__ == "__main__":
    t1 = time.perf_counter()
    prog = framework()
    prog.run()
    prog.terminate()
    t2 = time.perf_counter()
    print("Time elapsed: %.2f" %(t2-t1))
