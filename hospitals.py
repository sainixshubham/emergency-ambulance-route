# hospitals.py

hospitals = [
    {
        "id": 1,
        "name": "City Care Hospital",
        "location": "Hospital A",
        "address": "Sector 20",
        "available": True
    },
    {
        "id": 2,
        "name": "Life Line Hospital",
        "location": "Hospital B",
        "address": "Sector 20",
        "available": True
    }
]


def get_all_hospitals():
    return hospitals


def get_available_hospitals():
    return [
        hospital for hospital in hospitals
        if hospital["available"]
    ]