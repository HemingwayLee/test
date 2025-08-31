import requests

# The URL you want to send a request to
url = 'https://www.youtube.com/api/timedtext?v=Bg8_h6Bt1VI&type=track&kind=asr'

# Send the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful! 🥳")
    
    # Print the full response object
    print("Response object:", response)
    
    # Print the status code
    print("Status code:", response.status_code)
    
    # Print the response content as text
    print("Response body (text):", response.text)
    
    # If the content is JSON, you can access it directly as a dictionary
    try:
        data = response.json()
        print("Response body (JSON):", data)
        # You can access specific keys like this:
        print("Title:", data.get("title"))
    except requests.exceptions.JSONDecodeError:
        print("The response is not in JSON format.")
else:
    print(f"Request failed with status code: {response.status_code} 😥")

