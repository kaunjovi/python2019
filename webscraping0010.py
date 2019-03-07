from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://www.google.com")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print(html.read())

# https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-1.php
