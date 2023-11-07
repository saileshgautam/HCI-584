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

    data = results.raw_data

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
        if item['isOpenAccess'] == True and item['openAccessPdf'] is not None:
            paper_with_openaccess.append(item)
        else:
            paper_without_openaccess.append(item)
    paper_info = []
    for paper in paper_with_openaccess:
            paper_info.append({
        "title": paper["title"],
        "abstract": paper["abstract"],
        "Downloadlink": paper['openAccessPdf']['url'],
        "Link": paper['url']
        })
    return paper_info



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        author_name = request.form["author_name"]
        papers = search_paper_by_author(author_name)
        html = render_template("index.html", paper_info=papers)
        return html
    return render_template("index.html")

if __name__ == '__main__':
    app.run()