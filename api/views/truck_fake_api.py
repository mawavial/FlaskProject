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


def get_truck_by_id(truck_id):
    """
    trucks --> get a single truck by id
    Args:
        truck_id(int):
    Return:
        trucks(dict): a single truck
    """
    for truck in trucks_json:
        if truck["id"] == int(truck_id):
            return jsonify(truck)
    return jsonify(None)


def save_truck(truck):
    """
    book --> a single book
    Args:
        truck(truck):
    Return:
        truck(dict): the created truck
    """
    truck_to_save = truck.json
    trucks_json.append(truck_to_save)
    return jsonify({"message": "The object was saved successfully"})


def delete_truck(truck_id):
    """
    book --> a single book
    Args:
        truck_id(int):
    """
    book_json = request.json
    books.append(book_json)
    return jsonify({"message": "The object was saved successfully"})
