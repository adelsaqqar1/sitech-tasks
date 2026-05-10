import requests 

base_url = "https://jsonplaceholder.typicode.com/posts"

# Function to GET a post based on the post_id
def get_post(post_id):
    print("GET")
    response = requests.get(f"{base_url}/{post_id}")
    print(response.status_code)
    print(response.json())

# Function to create a new post
def create_post():
    print("\nPOST")
    data = {
        "title": "My Task",
        "body": "Learning API",
        "userId": 1
    }
    response = requests.post(base_url, json=data)
    print(response.status_code)
    print(response.json())


# Function to update a post based on the post_id
def update_post(post_id):
    print("\nPUT")
    updated_data = {
        "title": "Updated Task",
        "body": "Updated Content",
        "userId": 1
    }
    response = requests.put(f"{base_url}/{post_id}", json=updated_data)
    print(response.status_code)
    print(response.json())


# Function to delete a post based on the post_id
def delete_post(post_id):
    print("\nDELETE")
    response = requests.delete(f"{base_url}/{post_id}")
    print(response.status_code)
    print(response.text)



get_post(1)
create_post()
update_post(1)
delete_post(1)
