import requests

# Task 1: Send a GET request to a website and print the response
response = requests.get("https://www.w3schools.com")
print("Task 1 - GET Response:\n", response.text)

# Task 2: Send a POST request with data
data = {"key1": "value1", "key2": "value2"}
response = requests.post("https://httpbin.org/post", data=data)
print("\nTask 2 - POST Response:\n", response.text)

# Task 3: Download an image from a URL
image_url = "https://www.w3schools.com/w3images/lights.jpg"
response = requests.get(image_url)

if response.status_code == 200:
    with open("downloaded_image.jpg", "wb") as f:
        f.write(response.content)
    print("\nTask 3 - Image Downloaded Successfully")

print("\nHTTP requests completed.")
