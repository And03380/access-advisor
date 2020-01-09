import requests 
import schedule
import time

while True:
    requests.get('https://api.github.com')
    time.sleep(10)
