import requests
import csv

API_KEY = 'api_key'
SEARCH_QUERY = 'Gilbert'

def fetch_papers(api_key, query):
    base_url = 'https://core.ac.uk:443/api-v2/articles/search'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'apiKey': api_key,
        'query': query
    }

    response = requests.post(base_url, headers=headers, json=data)  
    # it says unauthorized
    # used .GET where it says Method not allowed
    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        print('Failed to fetch data. Status code:', response.status_code)
        print('Response:', response.json())
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Paper Title', 'Authors']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for paper in data:
            title = paper.get('title', '')
            all_authors = paper.get('author', [])
            authors = ', '.join(author['name'] for author in all_authors)
            writer.writerow({'Paper Title': title, 'Authors': authors})

if __name__ == "__main__":
    papers = fetch_papers(API_KEY, SEARCH_QUERY)

    if papers:
        save_to_csv(papers, 'papers.csv')
        print('Data saved to papers.csv.')
    else:
        print('No data fetched.')