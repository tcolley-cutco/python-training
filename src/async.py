from threading import Thread
import requests
from datetime import datetime


def slow_method():
    requests.get('http://www.google.com')
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print("Hello, This is ")


def main():
    thread = Thread(target=slow_method)
    thread.start()

    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print("Dog")


main()

