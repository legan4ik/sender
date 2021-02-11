import sender
import pytest
import requests_mock


def test_check_no_values():
    exp_text = "Please specify number of requests and endpoint"
    try:
        with requests_mock.Mocker() as m:
            m.post('http://test.com', text='dataddd')
            sender.Sender("", "").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))

def test_check_no_count():
    exp_text = "Please specify number of requests and endpoint"
    try:
        with requests_mock.Mocker() as m:
            m.post('http://test.com', text='dataddd')
            sender.Sender("", "f").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))

def test_check_no_endpoint():
    exp_text = "Please specify number of requests and endpoint"
    try:
        with requests_mock.Mocker() as m:
            m.post('http://test.com', text='dataddd')
            sender.Sender(5, "").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))

def test_check_count_str():
    exp_text = "Count must be integer"
    try:
        with requests_mock.Mocker() as m:
            m.post('http://test.com', text='dataddd')
            sender.Sender("5", "ff").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))

def test_check_count_str():
    exp_text = "Count must be integer"
    try:
        with requests_mock.Mocker() as m:
            m.post('http://test.com', text='dataddd')
            sender.Sender("5", "http://ff").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))

def test_check_invalid_url():
    exp_text = "Incorrect endpoint"
    try:
        with requests_mock.Mocker() as m:
            m.post('http://test.com', text='dataddd')
            sender.Sender(6, "ff").send()
    except Exception as e:
        if str(e) != exp_text:
            pytest.fail("Got unexpected exception: {}".format(e))

def test_check_positive():
    with requests_mock.Mocker() as m:
        m.post('http://site.com', text='random')
        sender.Sender(6, "http://site.com").send()