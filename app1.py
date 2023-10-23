from flask import Flask, render_template, request

from semanticscholar import SemanticScholar

app = Flask(__name__)


def search_paper_by_author(author_name):
    # Replace 'YOUR_API_KEY' with your Semantic Scholar API key


    s2_api_key = 'my key'
    sch = SemanticScholar(timeout=120)

    #name = 'Stephen Gilbert'
    results = sch.search_author(author_name, limit=1000)
    print(f"{len(results.raw_data)} authors found for {author_name}")

    data = results.raw_data  # raw_data is a bit of a hack, but it works. 0 for only the first author

    affiliations = 'Iowa State University'

    # Function to filter the list based on 'affiliations'
    def filter_by_affiliation(lst, affiliation):
        return [item for item in lst if item.get('affiliations') == [affiliation]]

    # Filter the list to get dictionaries with 'affiliations' as ['Iowa State University']
    filtered_data = filter_by_affiliation(data, affiliations)
    for item in filtered_data: paper = item['papers']

    paper_with_openaccess = []
    paper_without_openaccess = []
    
    for item in paper:
        if item['isOpenAccess'] == True:
            paper_with_openaccess.append(item)
        else:
            paper_without_openaccess.append(item)
    
    for paper in paper_with_openaccess:
        abstract = paper['abstract']
        title = paper['title']
        return title, abstract


@app.route('/', methods=['GET', 'POST'])
def index():

    author_name = "Stephen Gilbert"  # Replace with the author's name
    if request.method == 'POST':
        author_name = request.form['author_name']
    title, abstract = search_paper_by_author(author_name)
    return render_template('index1.html', author_name=author_name, title = title, abstract = abstract)


if __name__ == '__main__':
    app.run(debug=True)