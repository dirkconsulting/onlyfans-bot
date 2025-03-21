from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

from config import ONLYFANS_EMAIL, ONLYFANS_PASSWORD, PROXIES_FILE
from database import get_random_message
from proxy_manager import ProxyManager

# Inicializa el manejador de proxies
proxy_manager = ProxyManager(proxy_file=PROXIES_FILE)

def login_onlyfans():
    """Login en OnlyFans con Selenium + Rotación de Proxy"""
    max_retries = 3

    for attempt in range(max_retries):
        try:
            proxy = proxy_manager.get_proxy()
            print(f"[OnlyFans] Usando proxy: {proxy}")

            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument(f'--proxy-server={proxy}')

            driver = webdriver.Chrome(options=options)
            driver.get("https://onlyfans.com/")
            time.sleep(5)

            # Detectar bloqueo o captcha
            if "Access Denied" in driver.page_source or "verify" in driver.current_url:
                raise Exception("Proxy bloqueado o captcha detectado")

            driver.find_element(By.NAME, "email").send_keys(ONLYFANS_EMAIL)
            driver.find_element(By.NAME, "password").send_keys(ONLYFANS_PASSWORD)
            driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

            time.sleep(10)
            print("[OnlyFans] Login exitoso.")
            return driver

        except Exception as e:
            print(f"[ERROR LOGIN] Intento {attempt+1}/3 fallido - {e}")
            if attempt == max_retries - 1:
                raise Exception("Falló el inicio de sesión después de varios intentos.")
            time.sleep(2)

def get_online_users(driver):
    """Devuelve lista de usuarios online"""
    driver.get("https://onlyfans.com/my/chats")
    time.sleep(5)

    users = driver.find_elements(By.XPATH, "//div[contains(@class, 'status-online')]")
    return [user.text.strip() for user in users if user.text.strip()]

def detect_new_online_users(driver, prev_online_users):
    """Detecta usuarios que se han conectado recientemente"""
    current_online_users = set(get_online_users(driver))
    new_users = current_online_users - set(prev_online_users)
    return list(new_users)

def send_message(driver, username, message):
    """Envía un mensaje a un usuario"""
    driver.get(f"https://onlyfans.com/my/chats/{username}")
    time.sleep(5)

    try:
        chat_input = driver.find_element(By.XPATH, "//textarea[contains(@class, 'chat-input')]")
        chat_input.send_keys(message)
        chat_input.send_keys(Keys.RETURN)
        print(f"[OnlyFans] Mensaje enviado a {username}: {message}")
    except Exception as e:
        print(f"[ERROR AL ENVIAR A {username}] {e}")

def send_welcome_message(driver, username):
    """Envía un mensaje de bienvenida único a un nuevo suscriptor"""
    message = get_random_message("Welcome Messages", username)
    send_message(driver, username, message)

def send_engagement_message(driver, username):
    """Envía un mensaje de interacción para mantener el interés del usuario"""
    message = get_random_message("Engagement Messages", username)
    send_message(driver, username, message)

def get_subscribers(driver):
    """Devuelve la lista de suscriptores activos"""
    driver.get("https://onlyfans.com/my/subscribers/active")
    time.sleep(5)

    subscribers = driver.find_elements(By.XPATH, "//div[@class='g-user-name']")
    return [sub.text.strip() for sub in subscribers if sub.text.strip()]
