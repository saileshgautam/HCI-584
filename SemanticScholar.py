import requests
import csv

API_KEY = 'I have the key'

def search_papers_by_author(author_name):
    base_url = 'https://api.semanticscholar.org/graph/v1/author/'
    headers = {
        'Accept': 'application/json',
        'x-api-key': API_KEY
    }

    params = {
        'author': author_name,
        'limit': 10
    }

    response = requests.post(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('papers', [])
    else:
        print('Error:', response.status_code)
        return []

def save_to_csv(papers, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Paper Title', 'Authors', 'Year', 'Abstract']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for paper in papers:
            writer.writerow({
                'Paper Title': paper.get('title', ''),
                'Authors': ', '.join(author['name'] for author in paper.get('authors', [])),
                'Year': str(paper.get('year', '')),
                'Abstract': paper.get('abstract', '')
            })

if __name__ == "__main__":
    author_name = 'Gilbert'
    papers = search_papers_by_author(author_name)

    if papers:
        save_to_csv(papers, 'papers_by_author.csv')
        print('Data saved to papers_by_author.csv.')
    else:
        print('No papers found for the author.')
