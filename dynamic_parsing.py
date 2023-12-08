from requests_html import HTMLSession
from bs4 import BeautifulSoup


if __name__ == '__main__':

    session = HTMLSession()
    response = session.get('https://httpbin.org/')
    response.html.render(sleep=3)
    soup = BeautifulSoup(response.html.html, 'lxml')
    swagger = soup.find(id='swagger-ui')
    print(swagger.prettify())
