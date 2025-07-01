import requests

def fetch_user_data():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Oops. Something went wrong. {e}")
    else:
        if response.status_code != 200:
            print("Request not successful.")
            return []
        
        data = response.json()
        usernames = []
        for user in data:
            usernames.append(user["username"])
        return usernames