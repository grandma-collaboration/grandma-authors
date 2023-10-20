
import numpy as np
import re

def convert_multiple_authors(input_string):
    # Define regular expressions to extract the author's ORCID, name, and affiliations
    author_pattern = r'\\author(?:\[(\d{4}-\d{4}-\d{4}-\d{3}[0-9X])\])?\{(.+?)\}'
    affiliation_pattern = r'\\affiliation\{(.+?)\}'

    # Split the input into lines
    lines = input_string.strip().split('\n')

    author_list = []
    current_author = None

    for line in lines:
        # Check if the line matches the author pattern
        author_match = re.match(author_pattern, line)
        if author_match:
            # If a new author is encountered, save the previous author's information
            if current_author is not None:
                author_list.append(current_author)

            # Extract ORCID and name for the new author
            orcid = author_match.group(1) if author_match.group(1) else ''
            name = author_match.group(2)

            # Create a new author dictionary
            current_author = {
                'name': name,
                'email': '',  # You can set the email as needed
                'orcid': orcid,
                'affiliations': []
            }
        else:
            # Check if the line contains an affiliation and add it to the current author's affiliations
            affiliation_match = re.match(affiliation_pattern, line)
            if affiliation_match and current_author is not None:
                current_author['affiliations'].append(affiliation_match.group(1))

    # Add the last author's information
    if current_author is not None:
        author_list.append(current_author)

    return author_list

filename = "authors_GRB230812B.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

authors = convert_multiple_authors("\n".join(lines))

institution_list_ordered = []
for author in authors:
    institutions = author["affiliations"]
    for institution in institutions:
        if institution in institution_list_ordered: continue
        institution_list_ordered.append(institution)

print('--------')
print(f"Total {len(authors)} authors")

mnras_style = True
nature_style = False
spie_style = False

if mnras_style:
    author_list = []

    for ii, author in enumerate(authors):
        author_institutions = author["affiliations"]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('%s$^{%s}$' % (author["name"], ",".join([str(x+1) for x in indices])))
        if np.mod(ii, 4) == 0 and ii > 0:
            author_list.append('\\newauthor')


    print(", ".join(author_list))

    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('$^{%s}$ %s' % (str(ii+1), institution))
    print("\\\\ \n".join(institution_list))

    print("--------")
    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('\item %s' % (institution))
    print("\n".join(institution_list))


