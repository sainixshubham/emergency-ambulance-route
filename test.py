from algorithm import dijkstra

path, distance = dijkstra(
    "Accident Point",
    "Hospital A"
)

print("Shortest Route:", path)
print("Total Distance:", distance, "KM")