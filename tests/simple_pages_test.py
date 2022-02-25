"""This test the homepage"""
import datetime
from os import getenv

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/page1">Page 1</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Page 2</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Page 3</a>' in response.data
    assert b'<a class="nav-link" href="/page4">Page 4</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Page 1" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Page 2" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Page 3" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Page 4" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404

def test_context_variables_environment(client):
    """This test checks if the environment is printed"""
    response = client.get("/")
    env = getenv('FLASK_ENV', None)
    test_string = f"Environment: {env}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

def test_context_variables_year(client):
    """This tests checks if the copyright and current year are printed"""
    response = client.get("/")
    current_date_time = datetime.datetime.now()
    date = current_date_time.date()
    year = date.strftime("%Y")
    test_string = f"Copyright: {year}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data
