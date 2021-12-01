import pytest
import app
import requests
import time


def test_url_up():
    assert requests.get('http://localhost:5000').status_code == 200, "The website is not up"


def test_correct_mean():
    assert float(requests.get('http://localhost:5000/mean?list=1&list=2&list=3&list=4').content) == 2.5


def test_requests_time():
    timer = time.time()
    for i in range(1000):
        requests.get('http://localhost:5000/mean?list=1&list=2&list=3&list=4')
    duration = time.time() - timer
    assert (duration / 1000) < 100
