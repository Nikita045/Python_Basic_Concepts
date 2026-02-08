#JSON stands for JavaScript Object Notation and is a lightweight format for storing and
# transporting data. JSON is often used when data is sent from a server to a web page.
# Read JSON file: json.load() parses JSON from file object
import json
# Read YAML file using ruamel.yaml library
from ruamel.yaml import YAML

# Read existing content
with open("filename.json", "r") as f:
    content = json.load(f)
    print(content)
"""
# Modify / add data
content.update({
    "name": "Joe",
    "age": 30,
    "city": "Bangalore",
    "state": "Karnataka",
    "Country": "India"
})

# Write back to file
with open("filename.json", "a") as f:
    json.dump(content, f, indent=2)
print(content)"""



with open("filename.yaml") as f:
    yaml=YAML()  # Create YAML parser instance
    yaml.load(f)  # Parse YAML and return Python dict/list
