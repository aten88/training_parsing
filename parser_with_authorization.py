import requests
from bs4 import BeautifulSoup
LOGIN_URL = 'http://51.250.32.149/login/'
session = requests.session()
response = session.get(LOGIN_URL)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
form = soup.find('form')
csrf = form.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
csrf_token = session.cookies.get_dict()
data = {
    'username': 'test_parser_user',
    'password': 'testpassword',
    'csrfmiddlewaretoken': csrf,
}
response = session.post(LOGIN_URL, data=data)
response.encoding = 'utf-8'
print(response.status_code)
