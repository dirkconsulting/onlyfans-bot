import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import ONLYFANS_EMAIL, ONLYFANS_PASSWORD, PROXIES_FILE
from database import get_random_message

### --- PROXY SETUP --- ###
def get_proxy():
    """Obtiene un proxy aleatorio desde el archivo."""
    with open(PROXIES_FILE, "r") as file:
        proxies = file.readlines()
    return random.choice(proxies).strip()

### --- LOGIN --- ###
def login_onlyfans():
    """Login a OnlyFans con Selenium y Proxy."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f'--proxy-server={get_proxy()}')

    driver = webdriver.Chrome(options=options)
    driver.get("https://onlyfans.com/")

    time.sleep(5)
    driver.find_element(By.NAME, "email").send_keys(ONLYFANS_EMAIL)
    driver.find_element(By.NAME, "password").send_keys(ONLYFANS_PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(10)

    return driver

### --- ONLINE USERS --- ###
def get_online_users(driver):
    """Obtiene la lista de usuarios online."""
    driver.get("https://onlyfans.com/my/chats")
    time.sleep(5)
    users = driver.find_elements(By.XPATH, "//div[contains(@class, 'status-online')]")
    return [user.text.strip() for user in users if user.text.strip()]

def detect_new_online_users(driver, prev_online_users):
    """Detecta usuarios que se han conectado recientemente."""
    current_online_users = set(get_online_users(driver))
    new_online_users = current_online_users - prev_online_users
    return new_online_users

### --- SUBSCRIBERS --- ###
def get_subscribers(driver):
    """Obtiene la lista de suscriptores activos."""
    driver.get("https://onlyfans.com/my/subscribers/active")
    time.sleep(5)
    subscribers = driver.find_elements(By.XPATH, "//div[@class='g-user-name']")
    return [sub.text.strip() for sub in subscribers if sub.text.strip()]

### --- MENSAJES --- ###
def send_message(driver, username, message):
    """Envía un mensaje a un usuario específico."""
    driver.get(f"https://onlyfans.com/my/chats/{username}")
    time.sleep(5)
    chat_input = driver.find_element(By.XPATH, "//textarea[contains(@class, 'chat-input')]")
    chat_input.send_keys(message)
    chat_input.send_keys(Keys.RETURN)
    print(f"✅ Mensaje enviado a {username}:\n{message}")

def send_welcome_message(driver, username):
    """Envía un mensaje de bienvenida único a un nuevo suscriptor."""
    message = get_random_message("Welcome Messages", username)
    send_message(driver, username, message)

def send_engagement_message(driver, username):
    """Envía un mensaje de interacción para mantener la conversación activa."""
    message = get_random_message("Engagement Messages", username)
    send_message(driver, username, message)
