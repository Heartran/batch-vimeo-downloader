from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def get_vimeo_links(folder_url, username, password):
    # Configura il driver di Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Esegui Chrome in modalità headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Accedi a Vimeo
        driver.get("https://vimeo.com/log_in")
        time.sleep(3)

        # Inserisci username e password
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        email_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)  # Attendi l'accesso

        # Naviga verso la cartella
        driver.get(folder_url)
        time.sleep(5)  # Attendi il caricamento della pagina

        # Scorri verso il basso per caricare i video
        scroll_pause_time = 3
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Trova tutti i link dei video
        video_links = []
        elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/videos/")]')
        for element in elements:
            href = element.get_attribute('href')
            if href:
                video_links.append(href)

        # Rimuovi eventuali duplicati
        video_links = list(set(video_links))

        # Scrivi i link nel file vimeo_links.txt
        output_file = os.path.join(os.getcwd(), 'vimeo_links.txt')
        with open(output_file, 'w') as file:
            for video_link in video_links:
                file.write(video_link + '\n')

        print(f"{len(video_links)} link(s) trovati e salvati in vimeo_links.txt.")

    except Exception as e:
        print(f"Errore durante l'estrazione dei link: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    folder_url = input("Inserisci l'URL della cartella Vimeo: ")
    username = input("Inserisci il tuo username Vimeo: ")
    password = input("Inserisci la tua password Vimeo: ")
    get_vimeo_links(folder_url, username, password)
https://vimeo.com/user/84128503/folder/13897576