import bibtexparser

def bibtex_to_mla(entry):
    citation = ''
    
    # Get authors
    authors = entry.get('author', '')
    if authors:
        authors_list = [author.strip() for author in authors.replace('\n', ' ').split(' and ')]
        if len(authors_list) == 1:
            citation += authors_list[0] + '. '
        elif len(authors_list) == 2:
            citation += authors_list[0] + ' and ' + authors_list[1] + '. '
        else:
            citation += authors_list[0] + ', et al. '
    
    # Get title
    title = entry.get('title', '')
    if title:
        citation += f'"{title.strip("{}")}". '
    
    entry_type = entry.get('ENTRYTYPE', '').lower()
    
    if entry_type == 'article':
        # For journal articles
        journal = entry.get('journal', '')
        volume = entry.get('volume', '')
        number = entry.get('number', '')
        year = entry.get('year', '')
        pages = entry.get('pages', '')
        
        if journal:
            citation += f'*{journal}*, '
        if volume and number:
            citation += f'vol. {volume}, no. {number}, '
        elif volume:
            citation += f'vol. {volume}, '
        if year:
            citation += f'{year}, '
        if pages:
            citation += f'pp. {pages}.'
        else:
            citation = citation.rstrip(', ') + '.'
    
    elif entry_type == 'book':
        # For books
        publisher = entry.get('publisher', '')
        year = entry.get('year', '')
        
        if publisher:
            citation += f'{publisher}, '
        if year:
            citation += f'{year}.'
        else:
            citation = citation.rstrip(', ') + '.'
    
    elif entry_type == 'inproceedings' or entry_type == 'conference':
        # For conference papers
        booktitle = entry.get('booktitle', '')
        year = entry.get('year', '')
        pages = entry.get('pages', '')
        
        if booktitle:
            citation += f'In *{booktitle}*, '
        if year:
            citation += f'{year}, '
        if pages:
            citation += f'pp. {pages}.'
        else:
            citation = citation.rstrip(', ') + '.'
    
    else:
        # Other types can be added as needed
        citation = citation.rstrip(', ') + '.'
    
    return citation.strip()

def generate_mla_citations(bibtex_str):
    parser = bibtexparser.loads(bibtex_str)
    entries = parser.entries
    citations = []
    for entry in entries:
        mla_citation = bibtex_to_mla(entry)
        citations.append(mla_citation)
    return citations

# Example usage
if __name__ == '__main__':
    # with open("base.bib") as f:
    #     bibtex_string = f.read()
    bibtex_string = """
@inproceedings{pandit2018gdprtext,
  title={GDPRtEXT-GDPR as a linked data resource},
  author={Pandit, Harshvardhan J and Fatema, Kaniz and O’Sullivan, Declan and Lewis, Dave},
  booktitle={European Semantic Web Conference},
  pages={481--495},
  year={2018},
  organization={Springer}
}
    """
    mla_citations = generate_mla_citations(bibtex_string)
    for i, citation in enumerate(mla_citations):
        print(f"[{i+7}] {citation}")
