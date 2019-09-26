import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

login_data = {
    'bounce': " ",
    'hash': " ",
    'login_email': 'brian.clauser@mhc.org',
    'login_password': '*****************'
}
with requests.Session() as s:
    url = "https://mhcdev.com/login"
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    login_data['token'] = soup.find('input', attrs={'name': 'token'})['value']

    r = s.post(url, data=login_data, headers=headers)

print(soup.contents)


#/admin/members/health_system/296093/joins/entities