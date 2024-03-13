from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

airport_codes = ["PTY", "SJO", "SXM", "SJU", "PUJ", "SDQ", "MBJ", "CUN", "MEX", "GDL",
                 "MTY", "MZT", "SJD", "PVR", "NAS", "HRL", "UIO", "PVR", "PAP", "YVR",
                 "YUL", "YYZ", "MDE", "BOG", "CTG", "KIN", "STI", "FDF"]

chrome_driver_path = "D:\Programming\chromedriver_win32\chromedriver.exe"
edge_driver_path = "D:\Programming\edgedriver_win64\msedgedriver.exe"


# URL of the webpage
class FlightSearch:
    def __init__(self, departure, destination, departure_date, return_date):
        self.departure = departure
        self.index = 0
        self.departure_date = departure_date
        self.return_date = return_date
        self.destination = destination
        self.fake_leg_date = return_date.split('-')
        self.fake_leg_date[-1] = str(int(self.fake_leg_date[-1]) + 1)
        self.fake_leg_date = "-".join(self.fake_leg_date)
        for airport in airport_codes:
            url = f"https://www.kayak.com/flights/{self.departure}-{self.destination}/{self.departure_date}/{self.destination}-" \
                  f"{self.departure}/{self.return_date}/{self.departure}-{airport}/{self.fake_leg_date}/business?sort=price_a"
            try:
                if self.index%2==0:
                # Open the webpage
                    driver_chrome = webdriver.Chrome(chrome_driver_path)
                    driver_chrome.get(url)

                    # Find the element with class "f8F1-price-text"
                    price_element = driver_chrome.find_element(By.CLASS_NAME, "f8F1-price-text")

                    # Extract the text from the element
                    price_value = price_element.text.strip()

                    print(f"Price value({airport}):", price_value)

                    # Close the browser
                    driver_chrome.delete_all_cookies()
                    driver_chrome.quit()
                else:
                # Open the webpage
                    driver_edge = webdriver.Edge(edge_driver_path)
                    driver_edge.get(url)

                    # Find the element with class "f8F1-price-text"
                    price_element = driver_edge.find_element(By.CLASS_NAME, "f8F1-price-text")

                    # Extract the text from the element
                    price_value = price_element.text.strip()

                    print(f"Price value({airport}):", price_value)

                    # Close the browser
                    driver_edge.delete_all_cookies()
                    driver_edge.quit()
                self.index += 1
                time.sleep(10)

            except:
                continue
