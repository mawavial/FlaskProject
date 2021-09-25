from flask import (Flask, jsonify, request)

trucks_json = [
    {
        'id': 0, 'model': 'fenix',
        'plate': '1485acd',
        'chassis': 'abodeofjepa1azr5',
        'manufacturer': 'ford',
        'year': '1999',
        'mileage': '36620'
    },
    {
        'id': 0, 'model': 'fenix',
        'plate': '1485acd',
        'chassis': 'abodeofjepa1azr5',
        'manufacturer': 'ford',
        'year': '1999',
        'mileage': '36620'
    }, {
        'id': 0, 'model': 'fenix',
        'plate': '1485acd',
        'chassis': 'abodeofjepa1azr5',
        'manufacturer': 'ford',
        'year': '1999',
        'mileage': '36620'
    }
]



def list_trucks():
    """
    list_trucks --> list all the books
    Args:
        None
    Return:
        books(dict): books
    """
    return jsonify()


def get_truck_by_id(book_id):
    """
    book --> a single book
    Args:
        book_id(int):
    Return:
        books(dict): a book
    """
    for book in books:
        if book["id"] == int(book_id):
            return jsonify(books)
    return jsonify(None)


def save_truck():
    """
    book --> a single book
    Args:
        book_id(int):
    Return:
        books(dict): a book
    """
    book_json = request.json
    books.append(book_json)
    return jsonify({"message": "The object was saved successfully"})


def delete_truck():
    """
    book --> a single book
    Args:
        book_id(int):
    Return:
        books(dict): a book
    """
    book_json = request.json
    books.append(book_json)
    return jsonify({"message": "The object was saved successfully"})
