from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

schifting = "750"
play = True
while play : 
    # Maak een webdriver object aan (bijvoorbeeld voor Chrome)
    url = "https://clubbrugge.lt.acemlnc.com/Prod/link-tracker?redirectUrl=aHR0cHMlM0ElMkYlMkZjbHViYnJ1Z2dlLnR5cGVmb3JtLmNvbSUyRnRvJTJGd1o5bVI4NnQ=&sig=BzYepxt3Y2CzmmgeEyApWbjNrprL2ViPyCxRK8EHEo1Z&iat=1712401541&a=%7C%7C254557789%7C%7C&account=clubbrugge%2Eactivehosted%2Ecom&email=I7OHyI8SLBXrsktkZLnBzZboaoWktWnsdD%2BXRX0SaDXWs%2BeHwL%2Br%3AGK4wikFgRzK4TYui3%2Bq5dpk%2FpcrrIoPn&s=885347e8826a78a5a74cd49574e9ef3c&i=536A573A5A9735"

    driver = webdriver.Chrome()
    driver.get(url)
# Open de gewenste URL


# Wacht tot het element zichtbaar is
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-qa="start-button"]'))
    )

    # Klik op het element
    element.click()

    # Wacht tot het invoerveld zichtbaar is
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.InputField-sc-__sc-26uh88-0.blihGL'))
    )
    # Voeg tekst toe aan het invoerveld
    input_field.send_keys("Jose")

    # Druk op Enter
    input_field.send_keys(Keys.ENTER)
    # Wacht even om het resultaat te bekijken

    # Wacht tot het tweede invoerveld zichtbaar is
    second_input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.InputWrapper-sc-__sc-26uh88-1.iApDbT input.InputField-sc-__sc-26uh88-0.blihGL'))
    )

    # Voeg tekst toe aan het tweede invoerveld
    second_input_field.send_keys("Delanoie")

    # Druk op Enter
    second_input_field.send_keys(Keys.ENTER)

    # Wacht tot het invoerveld zichtbaar is
    date_input_day = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="date-input-day"]'))
    )

    # Klik op het invoerveld
    date_input_day.click()

    # Voeg de datum in
    date_input_day.send_keys("13")
    date_input_month = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="date-input-month"]'))
    )
    date_input_month.send_keys("10")
    date_input_year = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="date-input-year"]'))
    )
    date_input_year.send_keys("2004")
    # Druk op Enter

    date_input_year.send_keys(Keys.ENTER)

    # Wacht tot het invoerveld zichtbaar is
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
    )

    # Wis eventuele bestaande tekst in het invoerveld
    email_input.clear()

    # Voeg je e-mailadres toe aan het invoerveld
    email_input.send_keys("e-mail")
    email_input.send_keys(Keys.ENTER)



    # Wacht tot het invoerveld zichtbaar is
    winnaar_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
    )

    # Wis eventuele bestaande tekst in het invoerveld
    winnaar_input.clear()

    # Voeg je e-mailadres toe aan het invoerveld
    winnaar_input.send_keys("Andreas Skov Olsen")
    winnaar_input.send_keys(Keys.ENTER)


    schifting_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'blihGL'))
    )

    schifting_input.clear()
    # Voeg je e-mailadres toe aan het invoerveld
    schifting_input.send_keys(schifting)

    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-qa="submit-button deep-purple-submit-button"]'))
    )

    button.click()

    # Sluit de browser
    driver.quit()
    getal = int(schifting)
    getal += 750
    schifting = str(getal)
    if getal >= 50000 :
        break
