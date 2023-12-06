from flask import Flask, render_template, request, redirect, url_for

from semanticscholar import SemanticScholar

app = Flask(__name__)


def search_paper_by_author(author_name, affiliation):


    sch = SemanticScholar(timeout=120)

    results = sch.search_author(author_name, limit=1000)
    print(f"{len(results.raw_data)} authors found for {author_name}")

    data = results.raw_data
    #Check if the user gave the affiliation
    if affiliation:
        # Function to filter the list based on 'affiliation'
        def filter_by_affiliation(lst, affiliation):
            return [item for item in lst if item.get('affiliations') == [affiliation]]

        # Filter the list to get dictionaries with 'affiliations'
        filtered_data = filter_by_affiliation(data, affiliation)
        # if there is no affiliation same as given by user use the first index of a raw data as a filtered data
        if not filtered_data:
            filtered_data = [data[0]]
    else:
        #If affiliation is not given, again use the first index of raw data as a filtered data
        filtered_data = [data[0]]

    for item in filtered_data:
        articles = item['papers']

    paper_with_openaccess = []
    paper_without_openaccess = []
    
    for item in articles:
        #check if the each paper in filtered data is open access and it has url
        if item['isOpenAccess'] == True and item['openAccessPdf'] is not None: 
            paper_with_openaccess.append(item) # append it to paper with openaccess if true
        else:
            paper_without_openaccess.append(item) #otherwise
    paper_info = []
    #Made anempty list and collect the information needed to display in the website
    for paper in paper_with_openaccess:
            paper_info.append({
        "title": paper["title"],
        "abstract": paper["abstract"],
        "Downloadlink": paper['openAccessPdf']['url'],
        "Link": paper['url'],
        'year': paper['publicationDate']
        })
    return paper_info #return all the information to the main function



@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None # assign no error message at first
    if request.method == "POST":
        author_name = request.form["author_name"] # get the name of author from user
        affiliation = request.form.get("affiliation") # get the affiliation from user
        # check if the users provide numerical or alphabetical value
        if author_name.isdigit():
            error_message = "Numeric values cannot be the name of an author. Please retry with a valid name." # If True change the error message
            return render_template('index.html', author_name=author_name, affiliation=affiliation, error_message=error_message)  # render the template for the error message
        else:
            papers = search_paper_by_author(author_name, affiliation) #If given the right name, initialize search paper by author function
            #render the html file (index) based on the returned information
            html = render_template("index.html", paper_info=papers, author_name=author_name, affiliation=affiliation, error_message=error_message)
            return html
    return render_template("index.html")
'''
#This function was made to direct to the main page if error was detected. However, simpler method was made.
#Developer can use this to initialize the main page at any given point.
@app.route('/error', methods=['GET'])
def error():
    return redirect(url_for('index'))
'''
if __name__ == '__main__':
    app.run(debug=True)