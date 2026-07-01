import requests

FIREBASE_URL = "https://safespot-4f250-default-rtdb.europe-west1.firebasedatabase.app"

data = {
    "liverpool": {
        "s01": {
            "name": "Central Library",
            "description": "Warm, free WiFi, safe.",
            "location": "Central Library, Liverpool"
        },
        "s02": {
            "name": "Lime Street Station Concourse",
            "description": "Public, staffed, sheltered.",
            "location": "Lime Street Station, Liverpool"
        },
        "s03": {
            "name": "Whitechapel Centre Day Service",
            "description": "Food & support during open hours.",
            "location": "Whitechapel Centre, Liverpool"
        },
        "s04": {
            "name": "Liverpool One Public Seating",
            "description": "Public benches with CCTV.",
            "location": "Liverpool ONE, Liverpool"
        }
    },
    "manchester": {
        "s01": {
            "name": "Piccadilly Gardens",
            "description": "Public, central, open visibility.",
            "location": "Piccadilly Gardens, Manchester"
        },
        "s02": {
            "name": "Victoria Station Concourse",
            "description": "Inside public concourse, CCTV.",
            "location": "Victoria Station, Manchester"
        },
        "s03": {
            "name": "Manchester Central Library",
            "description": "Warm, free WiFi, quiet safe space.",
            "location": "Manchester Central Library"
        },
        "s04": {
            "name": "Arndale Food Court Seating",
            "description": "Indoor seating, busy & secure.",
            "location": "Manchester Arndale"
        }
    }
}

url = f"{FIREBASE_URL}/spots.json"

response = requests.patch(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)

if response.status_code == 200:
    print("Safe spots uploaded successfully.")
else:
    print("Upload failed.")
