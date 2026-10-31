# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS

from algorithm import dijkstra
from hospitals import get_all_hospitals, get_available_hospitals

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Emergency Ambulance Route Finder API is running"
    })


@app.route("/hospitals", methods=["GET"])
def hospitals():
    return jsonify(get_all_hospitals())


@app.route("/find-route", methods=["POST"])
def find_route():

    data = request.get_json()

    start = data.get("start")
    available_hospitals = get_available_hospitals()

    results = []

    for hospital in available_hospitals:

        path, distance = dijkstra(
            start,
            hospital["location"]
        )

        if path is not None:
            results.append({
                "hospital": hospital["name"],
                "path": path,
                "distance": distance
            })

    results.sort(key=lambda x: x["distance"])

    return jsonify({
        "routes": results,
        "best_route": results[0] if results else None
    })


if __name__ == "__main__":
    app.run(debug=True)