// Initialize Map
const map = L.map("map").setView([30.7333, 76.7794], 13);

// OpenStreetMap tiles
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

// Demo locations (illustrative coordinates)
const locations = {
    "Accident Point": [30.7410, 76.7680],
    "Sector 10": [30.7460, 76.7820],
    "Sector 15": [30.7350, 76.7900],
    "Sector 20": [30.7250, 76.7800],
    "Hospital A": [30.7200, 76.7900],
    "Hospital B": [30.7150, 76.7700]
};

// Map layers
let markers = [];
let routeLine = null;


// Find Shortest Route Button
document.getElementById("findRoute").addEventListener("click", async function () {

    const start = document.getElementById("start").value;
    const resultsDiv = document.getElementById("results");

    if (!start) {
        resultsDiv.innerHTML = "Please select an emergency location!";
        return;
    }

    resultsDiv.innerHTML = "Calculating shortest routes...";

    try {

        const response = await fetch("http://127.0.0.1:5000/find-route", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                start: start
            })
        });

        if (!response.ok) {
            throw new Error("Backend request failed");
        }

        const data = await response.json();

        if (!data.best_route) {
            resultsDiv.innerHTML = "No available hospital route found.";
            return;
        }

        // Display all hospital routes
        resultsDiv.innerHTML = "";

        data.routes.forEach((route, index) => {

            const card = document.createElement("div");
            card.className = "hospital-result";

            card.innerHTML = `
                <h3>${index === 0 ? "🏆 Best Route: " : ""}${route.hospital}</h3>
                <p><b>Route:</b> ${route.path.join(" → ")}</p>
                <p><b>Distance:</b> ${route.distance} km</p>
            `;

            resultsDiv.appendChild(card);
        });

        // Draw best route on map
        showRoute(data.best_route);

    } catch (error) {

        console.error(error);

        resultsDiv.innerHTML =
            "Unable to connect to backend. Please check Flask server.";
    }

});


// Display route on map
function showRoute(route) {

    // Remove old markers
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];

    if (routeLine) {
        map.removeLayer(routeLine);
    }

    const routeCoordinates = route.path.map(location => locations[location]);

    // Add markers
    route.path.forEach(location => {

        const coordinates = locations[location];

        const marker = L.marker(coordinates)
            .addTo(map)
            .bindPopup(location);

        markers.push(marker);
    });

    // Draw route line
    routeLine = L.polyline(routeCoordinates, {
        color: "red",
        weight: 5
    }).addTo(map);

    map.fitBounds(routeLine.getBounds(), {
        padding: [40, 40]
    });
}