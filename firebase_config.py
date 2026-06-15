import requests

# ✅ Your correct Firebase Realtime Database URL
FIREBASE_URL = "https://safespot-c5e02-default-rtdb.europe-west1.firebasedatabase.app"

def get_data(path):
    """
    Fetch data from Firebase at /path
    Example: get_data("spots/Liverpool")
    """
    url = f"{FIREBASE_URL}/{path}.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("❌ Firebase GET error:", response.text)
            return None
    except Exception as e:
        print("🔥 GET request failed:", e)
        return None


def save_data(path, data):
    """
    Save or update data using PATCH
    Example: save_data("spots/Liverpool", { "spot1": {...} })
    """
    url = f"{FIREBASE_URL}/{path}.json"
    try:
        response = requests.patch(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print("❌ Firebase PATCH error:", response.text)
            return None
    except Exception as e:
        print("🔥 PATCH request failed:", e)
        return None


def delete_data(path):
    """
    Delete a node
    Example: delete_data("spots/Liverpool/spot1")
    """
    url = f"{FIREBASE_URL}/{path}.json"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            print("❌ Firebase DELETE error:", response.text)
            return False
    except Exception as e:
        print("🔥 DELETE request failed:", e)
        return False


def initialize_firebase():
    """
    Initialize Firebase connection.
    Called when the app starts or when AddSpotScreen is created.
    """
    try:
        # Test connection by fetching a small piece of data
        response = requests.get(f"{FIREBASE_URL}/.json?shallow=true")
        if response.status_code == 200:
            print("✅ Firebase connection initialized successfully")
            return True
        else:
            print("❌ Firebase connection failed:", response.text)
            return False
    except Exception as e:
        print("🔥 Firebase initialization failed:", e)
        return False


def save_spot_to_firebase(city, name, description):
    """
    Save a new safe spot to Firebase
    Args:
        city: The city where the spot is located
        name: Name of the safe spot
        description: Description of the safe spot
    Returns:
        Dictionary with 'success' and 'message' keys
    """
    try:
        # Create spot data
        spot_data = {
            "name": name,
            "description": description
        }
        
        # Save to Firebase under spots/<city>/<name>
        path = f"spots/{city}/{name}"
        result = save_data(path, spot_data)
        
        if result is not None:
            return {
                "success": True,
                "message": f"✅ '{name}' saved to {city}!"
            }
        else:
            return {
                "success": False,
                "message": "❌ Failed to save spot. Please try again."
            }
    except Exception as e:
        print(f"🔥 Error saving spot: {e}")
        return {
            "success": False,
            "message": f"❌ Error: {str(e)}"
        }
