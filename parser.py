from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def opensite():
    print("Запуск...")
    options = ChromeOptions()
    options.headless = True
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1024, 768)
    #    url = str(sys.argv[1])
    url = "https://vkusvill.ru/goods/moloko-parmalat-ultrapasterizovannoe-3-5-200-ml-32130.html"
    driver.get(url)
    driver.find_element(By.CLASS_NAME,"CartButton__inner").click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "js-delivery__shopselect--form-address")))
    element = driver.find_element(By.CLASS_NAME, "js-delivery__shopselect--form-address")
    time.sleep(1)
    deliveryaddress = input("Введи адрес доставки: ")
    element.send_keys(f"{deliveryaddress}")
    print("")
    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, "VV_Input__Clear")
    ac = ActionChains(driver)
    ac.move_to_element(element).send_keys('\ue015').send_keys('\ue007').perform()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"VV_RWayChoiceModal__ButtonWrp").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"VV_Button._desktop-lg._tablet-lg._mobile-md.js-delivery__shopselect-terms-accept._block").click()
    time.sleep(5)
    url = "https://vkusvill.ru/cart/"
    driver.get(url)

    try:
        element = driver.find_element(By.CLASS_NAME,"ProductCards__item.swiper-slide.swiper-slide-active")
        grrenlabels = element.get_attribute("aria-label").split("/")
        maxgreenlabels = int(grrenlabels[-1])
        driver.find_element(By.CLASS_NAME, "OrderFormProdSliderSwiper.swiper-container.js-order-form-green-labels-slider.swiper-container-initialized.swiper-container-horizontal.swiper-container-pointer-events.swiper-container-free-mode").value_of_css_property("width: 1500px")

        print(f"= = = = Найдено {maxgreenlabels} зеленых ценников = = = =") #беру количество карточек товаров из рубрики "зеленые ценники"

        time.sleep(2)
        for i in range(maxgreenlabels):
            print("Карточка товара номер ", i+1)
            element = driver.find_element(By.XPATH, f"/html/body/div[2]/main/div[1]/div[1]/form/div/div[2]/div[9]/div[3]/div/div/div[{i+1}]/div/div/div[2]/a")
            print(element.get_attribute("title"))
            price = driver.find_element(By.XPATH, f"/html/body/div[2]/main/div[1]/div[1]/form/div/div[2]/div[9]/div[3]/div/div/div[{i+1}]/div/div/div[2]/div[1]/span[1]/span[1]")
            print(price.text if price.text != "" else "Нет цены")
            print("===========================")
            time.sleep(1)
    except:
        print("Не могу найти зеленые ценники. Возможно, сейчас их нет или что-то другое пошло не так")
    driver.quit()


if __name__ == '__main__':
    opensite()

