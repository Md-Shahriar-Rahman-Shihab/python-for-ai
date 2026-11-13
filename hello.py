# print("Hello world!")
# print("I am learning Python for AI!!")
# print("My name is Shihab")
# print("Today is a great day to code!")

# -------------------------------------------

import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


# --------------------------------------------------------


user_name = input("What is your name? ")
user_age = 25
next_year_age = user_age + 1
print(f"Hello, my name is {user_name} and I am {user_age} years old. Next year {user_name} will be {next_year_age}")

