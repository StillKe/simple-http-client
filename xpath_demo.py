from lxml import html

# HTML content (replace this with your HTML content)
html_content = '''
<html>
  <body>
    <div id="content">
      <h1>Welcome to XPath</h1>
      <ul class="menu">
        <li><a href="https://example.com">Home</a></li>
        <li><a href="https://example.com/about">About</a></li>
        <li><a href="https://example.com/contact">Contact</a></li>
      </ul>
      <div class="article">
        <h2>Introduction</h2>
        <p>This is a simple introduction to XPath.</p>
      </div>
    </div>
  </body>
</html>
'''

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the text content of the <h1> tag
h1_text = tree.xpath('//h1/text()')[0]
print("Title:", h1_text)

# Extract the URLs of all the links within the <ul class="menu"> element
menu_links = tree.xpath('//ul[@class="menu"]/li/a/@href')
print("Menu Links:", menu_links)
