import requests
import json

# Define the API endpoint URL
url = 'https://xtz0k606uxfcqt-8000.proxy.runpod.net'  # Replace with your actual endpoint URL

# Define the JSON data
data = {
    "input": {
        "prompt": "building 8 stories",
        "num_inference_steps": 25,
        "refiner_inference_steps": 50,
        "width": 1024,
        "height": 1024,
        "guidance_scale": 7.5,
        "num_images": 1
    }
}

# Convert the data to a JSON string
json_data = json.dumps(data)

# Set the headers for the request (if needed)
headers = {
    'Content-Type': 'application/json',
    # Add any other headers you may need
}

# Send the POST request with the JSON data
response = requests.post(url, data=json_data, headers=headers)

# Check the response status
if response.status_code == 200:
    # Request was successful
    result = response.json()  # Parse the response JSON
    print(result)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging
