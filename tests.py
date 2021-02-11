import sender
import pytest
import requests_mock

"""Run tests
Prerequisites (ubuntu):
apt-get install python-pip python-dev -y
pip install virtualenv
virtualenv venv
pip install -r requirements.txt (from this repo)

Prerequisites (windows):
tbd (install python and requirements)

Run example:  pytest -v tests.py
"""


def test_check_no_values():
    exp_text = "Please specify number of requests and endpoint"
    try:
        sender.Sender("", "").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))


def test_check_no_count():
    exp_text = "Please specify number of requests and endpoint"
    try:
        sender.Sender("", "f").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))


def test_check_no_endpoint():
    exp_text = "Please specify number of requests and endpoint"
    try:
        sender.Sender(5, "").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))


def test_check_count_str():
    exp_text = "Count must be integer"
    try:
        sender.Sender("5", "http://ff").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))


def test_check_invalid_url():
    exp_text = "Incorrect endpoint"
    try:
        sender.Sender(6, "ff").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))


def test_check_positive():
    with requests_mock.Mocker() as m:
        m.post('http://site.com', text='random')
        sender.Sender(6, "http://site.com").send()
