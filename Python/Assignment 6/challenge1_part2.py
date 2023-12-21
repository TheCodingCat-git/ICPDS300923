# Challenge 1 Part 2

"""
    Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
"""

import json

indian_states = {
    "Andhra Pradesh": "Hyderabad",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bangalore",
    "Kerala": "Thiruvananthapuram",
    "Uttar Pradesh": "Lucknow",
    "Rajasthan": "Jaipur"
}

with open("indian_states.json", "w") as file_handler:
    file_handler.write(json.dumps(indian_states))