import requests

# The URL to send the GET request to
url = "https://www.hellofresh.com/gw/recipes/recipes/search?author=gourmet&country=US&locale=en-US&skip=1&sort=-date&take=400"

# HTTP headers for Authorization
headers = {
    "authorization": ""
}

# Sending the GET request
response = requests.get(url, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    data = response.text
    with open("out.json", "w") as f:
        f.write(data)
        f.close()
else:
    print("Failed:", response.status_code, response.text)
