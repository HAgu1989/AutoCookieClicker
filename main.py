import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

os.environ['PATH'] += r"C:\Users\User\Desktop\GoogleDrive"
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

actions = ActionChains(driver)

bigCookie = driver.find_element(By.ID, "bigCookie")


# The game handles integers in very convoluted way , we need to clean them up

def cookie_count():
    cookies1 = driver.find_element(By.ID, "cookies")
    cookies_count1 = cookies1.text.split(" ")[0]
    cookies_count2 = cookies_count1.replace(",", "")
    cookies_count3 = cookies_count2.replace(".", "")
    return int(cookies_count3)


def building_price(b_id):
    try:
        b_price = driver.find_element(By.ID, "productPrice" + str(b_id)).text
        b_price2 = b_price.split(" ")[0]
        b_price3 = b_price2.replace(",", "")
        b_price4 = b_price3.replace(".", "")
        return int(b_price4)
    # We need those expectations on start buildings aren't visible and send None values which break the program
    except NoSuchElementException:
        pass
    except ValueError:
        pass


while 1 == 1:
    actions.click(bigCookie)
    actions.perform()

    # We check how many cookies we have to not iterate through loop unnecessarily, only when we have enough cookies
    #  to afford some upgrades

    if cookie_count() > building_price(0):

        # We try to upgrade special section first cheapest upgrade have always ID "upgrade0"

        try:
            actions.move_to_element(driver.find_element(By.ID, "upgrade0"))
            actions.click()
            actions.perform()
        except NoSuchElementException:
            pass

        # We take only unlocked buildings in to list and iterate them

        buildings = driver.find_elements(By.XPATH, '//div[@class="product unlocked enabled"]')

        # We iterate list in descending order to make sure that most expensive buildings are bought

        for building in buildings[::-1]:
            actions.move_to_element(building)
            actions.click(building)
