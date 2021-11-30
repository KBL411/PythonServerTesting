import pytest
import app
import requests


def test_correct_mean():
    assert requests.get('http://localhost:5000/mean?list=1&list=2&list=3&list=4').content == 2.5


def test_url_up():
    assert requests.get('http://localhost:5000').status_code == 200, "The website is not up"
