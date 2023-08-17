from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json


def toJson(twelve_words, sui_adress, private_key):
    try:
        with open('data.json', 'r') as json_file:
            file_content = json_file.read()
            existing_data = json.loads(
                file_content) if file_content.strip() else []
    except FileNotFoundError:
        existing_data = []

    json_str = [twelve_words, sui_adress, private_key]
    existing_data.append(json_str)

    with open('data.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    print(f"{k + 1} Аккаунтов сделано")


def registration():
    try:
        chromedriver_path = 'chromedriver.exe'
        service = Service(chromedriver_path)
        service.start()
        options = webdriver.ChromeOptions()
        options.add_extension('sui.crx')
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(options=options, service=service)
        time.sleep(3)
        current_window = driver.window_handles[1]
        driver.switch_to.window(current_window)
        driver.get(
            "chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html#/initialize/create")
        time.sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(
            '~?nGn#?bbBD*')  # your password
        driver.find_element(By.NAME, 'confirmPassword').send_keys(
            '~?nGn#?bbBD*')  # your password
        driver.find_element(By.CSS_SELECTOR, '#root > div > div.flex.flex-col.flex-nowrap.rounded-20.items-center.bg-sui-lightest.shadow-wallet-content.p-7\.5.pt-10.flex-grow.w-full.max-h-popup-height.max-w-popup-width.overflow-auto > form > div > fieldset > label.flex.items-center.justify-center.h-5.my-5.text-gray-75.gap-1\.25.relative.cursor-pointer > div').click()
        driver.find_element(By.CLASS_NAME, 'truncate').click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, 'block').click()
        element = driver.find_element(By.CSS_SELECTOR, '#root > div > div.flex.flex-col.flex-nowrap.rounded-20.items-center.bg-sui-lightest.shadow-wallet-content.p-7\.5.pt-10.flex-grow.w-full.max-h-popup-height.max-w-popup-width.overflow-auto > div.flex.flex-col.flex-nowrap.flex-grow.h-full.w-full > div > div.flex.flex-col.flex-nowrap.items-stretch.gap-2.bg-white.border.border-solid.border-gray-60.rounded-lg.overflow-hidden.py-4.px-5 > div.break-all.relative > div.absolute.top-0 > div')
        twelve_words = element.text
        driver.find_element(By.CSS_SELECTOR, '#root > div > div.flex.flex-col.flex-nowrap.rounded-20.items-center.bg-sui-lightest.shadow-wallet-content.p-7\.5.pt-10.flex-grow.w-full.max-h-popup-height.max-w-popup-width.overflow-auto > div.flex.flex-col.flex-nowrap.flex-grow.h-full.w-full > div > div.w-full.text-left.flex.mt-5.mb- > label > span > svg').click()
        driver.find_element(By.LINK_TEXT, 'Open Sui Wallet').click()
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, '#overlay-portal-container > div > div > div > div.flex.flex-col.items-center.gap-4.\[-webkit-text-stroke\:1px_black\].w-full.mt-5 > button > svg').click()
        time.sleep(1)
        driver.get(
            "chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html#/apps?menu=%2F")
        time.sleep(1)
        driver.find_element(
            By.LINK_TEXT, 'View account on Sui Explorer').click()
        time.sleep(3)
        current_window = driver.window_handles[2]
        driver.switch_to.window(current_window)
        new_element = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[1]/main/section[1]/div/div/div/div[2]/div/div[2]/div/h3')
        sui_adress = new_element.text
        driver.get(
            "chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html#/apps?menu=%2Faccounts")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div/div/div[1]/div/div/div[2]/div/div/div/div').click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Export Private Key').click()
        time.sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(
            '~?nGn#?bbBD*')  # your password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#root > div > div.Ko3uxRpBu3XDuvyJ9mY7.U1WLVDx4AoEMWfPf52fD > div > div > form > div.flex.flex-nowrap.gap-3\.75.self-stretch > button.transition.no-underline.outline-none.group.flex.flex-row.flex-nowrap.items-center.justify-center.gap-2.cursor-pointer.text-body.font-semibold.max-w-full.min-w-0.w-full.bg-hero-dark.text-white.border-none.hover\:bg-hero.focus\:bg-hero.visited\:text-white.active\:text-white\/70.disabled\:bg-hero-darkest.disabled\:text-white.disabled\:opacity-40.h-10.px-5.rounded-xl > div.truncate').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#root > div > div.Ko3uxRpBu3XDuvyJ9mY7.U1WLVDx4AoEMWfPf52fD > div > div > div.flex.flex-col.justify-items-stretch.flex-1.px-2\.5 > div > div.flex.flex-col.flex-nowrap.items-stretch.gap-2.bg-white.border.border-solid.border-gray-60.rounded-lg.overflow-hidden.py-4.px-5 > div.flex.flex-row.flex-nowrap.items-center.justify-between > div:nth-child(2) > button > div').click()
        element = driver.find_element(By.CSS_SELECTOR, '#root > div > div.Ko3uxRpBu3XDuvyJ9mY7.U1WLVDx4AoEMWfPf52fD > div > div > div.flex.flex-col.justify-items-stretch.flex-1.px-2\.5 > div > div.flex.flex-col.flex-nowrap.items-stretch.gap-2.bg-white.border.border-solid.border-gray-60.rounded-lg.overflow-hidden.py-4.px-5 > div.break-all.relative > div.absolute.top-0 > div')
        private_key = element.text
        toJson(twelve_words, sui_adress, private_key)
    except:
        pass


def main():
    global k
    k = 0
    times = int(input("How many account do you need? Integer: "))
    while k < times:
        registration()
        k += 1


if __name__ == "__main__":
    main()
