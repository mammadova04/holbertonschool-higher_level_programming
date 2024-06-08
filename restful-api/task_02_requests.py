#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Print the status code of the response
    print(f'Status Code: {response.status_code}')
    
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Iterate through the parsed JSON data and print titles
        for post in posts:
            print(post['title'])
    else:
        print('Failed to retrieve posts')

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Create a list of dictionaries with selected keys
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write data to a CSV file
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
    else:
        print('Failed to retrieve posts')

