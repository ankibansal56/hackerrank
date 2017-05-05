import requests
from bs4 import BeautifulSoup
def get_page(breed_name):
	url = 'http://www.thekennelclub.org.uk/services/public/breed/Default.aspx'
	source_code = requests.get(url)
	plain_text = source_code.text;
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('img',{'class': 'vMid'}):
		href = link.get('src')
		print href

get_page('German')
