from selenium import webdriver


# Inicjalizacja przeglądarki
driver = webdriver.Chrome()


# Przykładowe testy

# Otwarcie strony internetowej

driver.get("https://bartekb.azurewebsites.net/")

# Sprawdzenie tytułu strony

driver.get("https://bartekb.azurewebsites.net/")

assert driver.title == "Strona Bartka"

expected_title = "Home page"
actual_title = driver.title
assert expected_title in actual_title, "Oczekiwany tytuł: {expected_title}, Rzeczywisty tytuł: {actual_title}"

# Kliknięcie w odnośnik "Privacy" i sprawdzenie, czy strona przekierowuje poprawnie

driver.get("https://bartekb.azurewebsites.net/")

privacy_link = driver.find_element_by_xpath("//a[text()='Privacy']")
privacy_link.click()

assert driver.current_url == "https://bartekb.azurewebsites.net/Privacy.html"

# Zamknięcie przeglądarki
driver.quit()