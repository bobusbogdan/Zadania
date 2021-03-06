# ---------------------------------------------------------------------------#
#  Napisz program który wyszuka ostatni mecz pomiędzy 2 zespołami, po czym   #
#  wypisze date spotkania, nazwe rozgrywek w jakich rywalizowali oraz poda   #
#  końcowy wynik spotkania. Możesz zastosować pętlę.                         #
#  Oczekiwaną odpowiedzią świadczącą o wykonaniu                             #
#  zadania jest zrzut ekranu działającego kodu.                              #
# ---------------------------------------------------------------------------#
import selenium
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get("https://google.pl/")
    element = driver.find_element(By.ID, "L2AGLb")
    driver.execute_script("arguments[0].click()", element)
    klub1 = input("Podaj pierwszą drużynę: ")
    klub2 = input("Podaj drugą drużynę: ")
    wyszukiwanie = klub1 + " " + klub2 + " ostatni mecz"
    element = driver.find_element(By.CSS_SELECTOR, 'input.gLFyf.gsfi')
    driver.execute_script("arguments[0].click()", element)
    wyszukiwarka = driver.find_element(By.NAME, "q")
    wyszukiwarka.clear()
    wyszukiwarka.send_keys(wyszukiwanie)
    wyszukiwarka.send_keys(Keys.ENTER)
    try:
        tablica_wyniku = driver.find_element(By.CSS_SELECTOR, 'div.imso_mh__ma-sc-cont')
    except selenium.common.exceptions.NoSuchElementException:
        tablica_wyniku = driver.find_element(By.CSS_SELECTOR, 'div.imso_mh__ma-sc-cont')
    elementy = tablica_wyniku.find_elements(By.CSS_SELECTOR, "*")
    wynik_spotkania = ""
    for temp in elementy:
        wynik_spotkania = wynik_spotkania + str(temp.get_attribute('innerHTML'))
    druzyny = str(driver.find_element(By.CSS_SELECTOR, 'div.IkSHxd.ellipsisize').get_attribute('innerHTML')).split(" ")
    data_spotkania = str(driver.find_element(By.XPATH, '//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div/div/span[2]').get_attribute('innerHTML'))
    rozgrywki = str(driver.find_element(By.CLASS_NAME, "imso-ln").get_attribute('innerHTML'))
    print(rozgrywki + " " + data_spotkania + " ", end="")
    for e in druzyny:
        if str(e) != '–':
            print(e + " ", end="")
        else:
            print(wynik_spotkania + " ", end="")
          
