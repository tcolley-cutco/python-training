from threading import Thread
import requests
from datetime import datetime


def slow_method():
    requests.get('http://www.google.com')
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print("Hello, This is ")


def fake_http_call():
    thread = Thread(target=slow_method)
    thread.start()

    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))

    return "Dog"


def main():
    result = fake_http_call()
    print(result)


main()
