from flask import (Flask, jsonify, request)

drivers_json = [
    {
        'id': '1',
        'first_name': 'ayrton',
        'last_name': 'senna',
        'drivers_license': '123124',
        'age': '23',
        'driver_since': '1999'
    },
    {
        'id': '2',
        'first_name': 'ayrton',
        'last_name': 'senna',
        'drivers_license': '123124',
        'age': '23',
        'driver_since': '1999'
    },
    {
        'id': '3',
        'first_name': 'ayrton',
        'last_name': 'senna',
        'drivers_license': '123124',
        'age': '23',
        'driver_since': '1999'
    }
]

app = Flask(__name__)

API_NAME = "/api/v1"


def list_drivers():
    """
    list_drivers --> list all the drivers
    Args:
        None
    Return:
        drivers(dict): drivers
    """
    return jsonify(drivers_json)


def get_driver_by_id(driver_id):
    """
    driver --> a single driver
    Args:
        driver_id(int):
    Return:
        driver(dict): a driver
    """
    for driver in drivers_json:
        if driver["id"] == int(driver_id):
            return jsonify(driver)
    return jsonify(None)


def save_driver(driver):
    """
    driver --> save a single driver
    Args:
        book_id(int):
    Return:
        books(dict): a book
    """
    driver = request.json
    drivers_json.append(driver)
    return jsonify({"message": "The object was successfully saved"})


def delete_driver(id):
    """
    book --> a single book
    Args:
        book_id(int):
    Return:
        books(dict): a book
    """
    drivers_json = request.json
    books.append(book_json)
    return jsonify({"message": "The object was saved successfully"})