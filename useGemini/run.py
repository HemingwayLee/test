import requests
import json

def send_post_request(url, data, headers=None):
    """
    Sends a POST request to the specified URL with the given data and headers.

    Args:
        url: The URL to send the POST request to.
        data: The data to send in the request body (as a dictionary).
        headers: Optional headers to include in the request (as a dictionary).

    Returns:
        The JSON response from the server, or None if an error occurs.
    """
    try:
        # Convert the data dictionary to a JSON string
        json_data = json.dumps(data)

        # Set default headers if none are provided
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json_data, headers=headers)

        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Attempt to parse the JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}. Raw response: {response.text}") # print raw response for debugging
        return None
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return None

# Example usage
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=xxxx"  # Example API endpoint
data = {
    "contents": [{
        "parts":[{"text": "Hello"}]
    }]
}

headers = {'Content-Type': 'application/json'} #example of adding headers

response_data = send_post_request(url, data, headers)

if response_data:
    print("Response:")
    print(json.dumps(response_data, indent=4)) #pretty print the json response


