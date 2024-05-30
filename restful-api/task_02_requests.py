import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code and titles of the posts.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    data = response.json()
    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them into a CSV file.
    Each post is represented as a dictionary with keys 'id', 'title', and 'body'.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    structured_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in data]

    with open("posts.csv", "w", newline="") as csv_file:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(structured_data)
