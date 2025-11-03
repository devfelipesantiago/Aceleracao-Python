import pytest
from mocks.task_form import task_form


@pytest.fixture
def response(client):
    return client.get("task/2/form")


def test_status_response(response):
    assert response.status_code == 200


def test_task_container(response):
    assert task_form["open"] in response.text


def test_task_name(response):
    assert task_form["name"] in response.text


def test_task_status(response):
    assert task_form["status"] in response.text


def test_task_percentage(response):
    assert task_form["percentage"] in response.text


def test_task_description(response):
    assert task_form["description"] in response.text


def test_task_date(response):
    assert task_form["date"] in response.text


def test_task_responsible(response):
    assert task_form["responsible"] in response.text


def test_send_button(response):
    assert task_form["send"] in response.text


def test_close_tag(response):
    assert task_form["close"] in response.text
