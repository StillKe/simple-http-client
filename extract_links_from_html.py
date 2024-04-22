import urllib3
from lxml import html

# Fetch HTML content using urllib3 and store the response in the variable 'r'
http = urllib3.PoolManager()
r = http.request('GET', 'https://yasoob.me/2018/06/20/an-intro-to-web-scraping-with-lxml-and-python/')

# Decode the response data and extract links
data_string = r.data.decode('utf-8', errors='ignore')
tree = html.fromstring(data_string)
links = tree.xpath('//a')

# Print the extracted links
for link in links:
    print(link.get('href'))
