from semanticscholar import SemanticScholar #pip install semanticscholar
s2_api_key = 'my key'
#sch = SemanticScholar(api_key=s2_api_key, timeout=30)
sch = SemanticScholar(timeout=120) # not sure why api key is not needed. 

name = 'Stephen Gilbert'
results = sch.search_author(name, limit=1000) #search for author
print(f"{len(results.raw_data)} authors found for {name}")

data = results.raw_data # raw_data is a bit of a hack, but it works. 0 for only the first author

affiliations = 'Iowa State University'

# Function to filter the list based on 'affiliations'
def filter_by_affiliation(lst, affiliation):
    return [item for item in lst if item.get('affiliations') == [affiliation]]
    
# Filter the list to get dictionaries with 'affiliations' as ['Iowa State University']
filtered_data = filter_by_affiliation(data, affiliations)
papers_list = [item['papers'] for item in filtered_data]

for item in filtered_data: paper = item['papers']
paper_with_openaccess = []
paper_without_openaccess = []
for items in paper:
    if items['isOpenAccess'] == True:
        paper_with_openaccess.append(items)
    else:
        paper_without_openaccess.append(items)
print(f"{len(paper_with_openaccess)} papers found for paper with {affiliations} affiliation that is open access.") 

for k in paper_with_openaccess:
    print(f"The paper: \n{items['title']}\nhas the following Abstract:\n {items['abstract']} \n")









