def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return

def get_next_page_url(page):
	start_index = page.find("<a href=")
	start_quote = page.find('"',start_index)
	end_quote = page.find('"',start_quote+1)
	url = page[start_quote+1:end_quote]
	return url,end_quote


def print_all_links(page):
	li = []
	while True:
		url,end_index = get_next_page_url(page)
		if url:
			li.append(url)
			page = page[end_index:]
#			print li
		else:
			break
	return li

page = get_page('file:///home/ankit/ubuntudata/images/pro.html')
li = print_all_links(page)
print li
