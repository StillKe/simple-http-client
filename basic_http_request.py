import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Make a GET request to https://www.google.com/
response = http.request('GET', 'https://www.google.com/')

# Print the response data
print(response.data)
