import requests 
import schedule
import time

while True:
    requests.get('https://api.github.com')
    print(this worked)
    time.sleep(10)
