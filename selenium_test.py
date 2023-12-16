from time import sleep

from selenium import webdriver
# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Если у вас установлен другой браузер - импортируйте нужный драйвер.
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.opera import OperaDriverManager

DJANGO_URL = 'http://51.250.32.149/'
USERNAME = 'test_parser_user'
PASSWORD = 'testpassword'
PAUSE_DURATION_SECONDS = 1

if __name__ == '__main__':
    # Проверка и установка (или обновление) драйвера для Chrome через
    # DriverManager.
    service = Service(executable_path=ChromeDriverManager().install())
    # Запуск веб-драйвера для Chrome.
    driver = webdriver.Chrome(service=service)

    # Открытие страницы по заданному адресу.
    driver.get(DJANGO_URL)
    # Развёртывание окна на полный экран.
    driver.maximize_window()
    # Здесь и далее паузы, чтобы рассмотреть происходящее.
    sleep(PAUSE_DURATION_SECONDS)

    # Поиск в содержимом страницы поля для логина.
    # Возможные варианты для поиска:
    # ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT,
    # NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR
    username_input = driver.find_element(By.NAME, 'username')
    # Ввод логина при помощи имитации ввода с клавиатуры.
    username_input.send_keys(USERNAME)
    sleep(PAUSE_DURATION_SECONDS)

    # Поиска поля для пароля.
    password_input = driver.find_element(By.NAME, 'password')
    # Ввод пароля.
    password_input.send_keys(PASSWORD)
    sleep(PAUSE_DURATION_SECONDS)

    # Поиск кнопки "Войти".
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    # Эмуляция щелчка мышью.
    submit_button.click()
    sleep(PAUSE_DURATION_SECONDS)

    # Сохранение скриншота страницы с заданным именем.
    driver.save_screenshot('screenshot.png')
    sleep(PAUSE_DURATION_SECONDS)

    # Поиск первого поста на странице по классу.
    first_post = driver.find_element(By.CLASS_NAME, 'card-text')
    # Вывод текста найденного элемента в терминал.
    print(first_post.text)
    # Закрытие веб-драйвера.
    driver.quit()
