# print("Hello world!")
# print("I am learning Python for AI!!")
# print("My name is Shihab")
# print("Today is a great day to code!")

# -------------------------------------------

import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


