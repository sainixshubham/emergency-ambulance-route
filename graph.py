# graph.py

# Weighted Graph representing city roads

city_graph = {
    "Accident Point": {
        "Sector 10": 2,
        "Sector 15": 5
    },

    "Sector 10": {
        "Accident Point": 2,
        "Sector 15": 1,
        "Sector 20": 4
    },

    "Sector 15": {
        "Accident Point": 5,
        "Sector 10": 1,
        "Sector 20": 2
    },

    "Sector 20": {
        "Sector 10": 4,
        "Sector 15": 2,
        "Hospital A": 3,
        "Hospital B": 5
    },

    "Hospital A": {
        "Sector 20": 3
    },

    "Hospital B": {
        "Sector 20": 5
    }
}