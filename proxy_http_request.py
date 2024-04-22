import urllib3

# Disable proxy usage by passing None for the proxy URL
pool = urllib3.PoolManager()

# Make a GET request to https://www.google.com/ without using a proxy
response = pool.request('GET', 'https://www.google.com/')

# Print the response data
print(response.data)
