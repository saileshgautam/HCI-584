# Semantic Scholar Paper Search

The Semantic Scholar Paper Search website allows you to search for articles by the author's name using Semantic Scholar. It can search all the articles within Semantic Scholar and display the papers based on filters such as Affiliation and Open Access.

## Features

- Search articles by Author's name.
- Filter papers based on Affiliation and Open Access.
- Display paper title, publication date, abstract, download link, and viewable link.
- Sort displayed papers in ascending and descending alphabetic order.

## Prerequisites

Make sure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/)

## Requirements

- Flask
- Semantic Scholar

## Installation

1. Clone the repository to your local machine.
   ```bash
   git clone <repository_url>
2. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt

## Usage

1. Launch the application by running the main.py file.

   ```bash
   python main.py
2. Open your web browser and go to [http://127.0.0.1:5001](http://127.0.0.1:5001).

3. Type the desired author name and affiliation associated with the author.

4. Click the "Search" button to retrieve information based on the search.

5. Change the "Sort by" function with four options:
   - Sort in ascending English alphabets (A to Z).
   - Sort in descending English alphabets (Z to A).
   - Sort in ascending published date.
   - Sort in descending published date.

6. Click on the link to open the website.

7. Click on the download link to download the paper to your device.
## User Interface
### Website Main Page
![Main Page Image](Images/Main%20Page.png)
### Searching papers without affiliation
![Main Page Image](Images/Without%20Affiliation.png)
### Searching papers with affiliation
![Main Page Image](Images/With%20Affiliation.png)
### Error Message if numeric value is given for search
![Main Page Image](Images/Error%20Message.png)
### Sorting
![Main Page Image](Images/Sorting.png)
