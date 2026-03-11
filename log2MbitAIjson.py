import pandas as pd
import json
import time

# Load the CSV file
df = pd.read_csv("/Users/ghodg/OneDrive/_Gus2B/1-Projects/LegoBot/Log4.csv")

# Define function to generate unique ID
def generate_id():
    return int(time.time() * 1000)

# Prepare JSON structure
output_json = [{
    "icon": "Custom",  # Set a default icon
    "ID": generate_id(),
    "name": "sensor_data",  # Generic name, can be customized
    "recordings": [
        {
            "ID": generate_id(),
            "data": {
                "x": df["ang_vel"].tolist(),
                "y": df["acc_yaw"].tolist(),
                "z": df["dev"].tolist()
            }
        }
    ]
}]

# Save to JSON file
with open("Log4.json", "w") as f:
    json.dump(output_json, f, indent=4)

print("Conversion complete! JSON saved as Log.json")