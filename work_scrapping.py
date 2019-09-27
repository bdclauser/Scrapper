from urllib.request import Request, urlopen
from datetime import datetime
import request
from bs4 import BeautifulSoup
import csv

# add the correct User-Agent
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

# the company page you're about to scrape
req = Request('https://angel.co/uber')
web_byte = urlopen(req).read()
company_page = web_byte.decode('utf-8')

#company_page = 'https://mhcdev.com/login'

# open the page
page_request = request.Request(company_page, headers=headers)
page = request.urlopen(page_request)

# parse the html using beautiful soup
html_content = BeautifulSoup(page, 'html.parser')

# we parse the title
title = html_content.find('h1')
title = title.text.strip()
print(title)

# we parse the description
description = html_content.find('h2', attrs={'class': 'js-startup_high_concept'})
description = description.text.strip()
print(description)

# we extract the website
website = html_content.find('a', attrs={'class': 'company_url'})
website = website['href'].strip()
print(website)

# open a csv with the append (a) parameter. We also save the date which is always a good indicator.
with open('angel.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([title, description, website, datetime.now()])

# login_data = {
#     'bounce': " ",
#     'hash': " ",
#     'login_email': 'brian.clauser@mhc.org',
#     'login_password': '*****************'
# }
# with request.Session() as s:
#     url = "https://mhcdev.com/login"
#     r = s.get(url, headers=headers)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     login_data['token'] = soup.find('input', attrs={'name': 'token'})['value']
#
#     r = s.post(url, data=login_data, headers=headers)
#
# print(soup.contents)
#
# # /admin/members/health_system/296093/joins/entities
