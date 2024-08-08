ich = {
    "name": "Tobias Nawa",
    "alter": 37,
    "job": "Solutionarchitect",
    "selbstständig": True,
    "faehigkeiten": [
        "python",
        "aws"
    ]
}

print(ich["name"])
ich["name"] = "Tobias"
print(ich["name"])

for key, value in ich.items():
    print("Key:", key, "Value:", value)