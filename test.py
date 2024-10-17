import requests
from bs4 import BeautifulSoup

# r = requests.get('http://localhost:5000/product/1')
# print(r.text)

r = requests.post('http://localhost:5000/product/', data={'name': 'iPad Pro', 'price': 999})
print(r.json())
# print(r.status_code)
# soup = BeautifulSoup(r.content,'html.parser')
# print("\n".join(soup.text.splitlines()))