# Author: Jean-Grégoire Ducoin
import csv
import os
import numpy as np
import sys

authors = [
{'name': 'J.-G.~Ducoin', 'affiliations': ["Sorbonne Universit\\'e, CNRS, UMR 7095, Institut d’Astrophysique de Paris, 98 bis bd Arago, 75014 Paris, France"], 'email': 'ducoin@IAP.FR'},
{'name': 'S.~Antier', 'affiliations': ["Artemis, Observatoire de la C\\^ote d'Azur, Universit\\'e C\\^ote d'Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'sarah.antier@OCA.EU', 'orcid': '0000-0002-7686-3334'},
]


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

if nature_style:
    author_list = []

    for author in authors:
        author_institutions = author["affiliations"]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('%s$^{%s}$' % (author["name"], ",".join([str(x+1) for x in indices])))


    
    print(", ".join(author_list))
    
    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('$^{%s}$ %s' % (str(ii+1), institution))
    print("\n".join(institution_list)) 
    
    print("--------")
    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('\item %s' % (institution))
    print("\n".join(institution_list))
    
if spie_style:
    author_list = []
    for author in authors:
        author_institutions = author["affiliations"]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('\\author[%s]{%s}' % (",".join([str(x+1) for x in indices]), author["name"]))

    print("\n".join(author_list))

    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('\\affil[%s]{%s}' % (str(ii+1), institution))
    print("\n".join(institution_list))

fieldnames = ["name", "email", "affiliations", "orcid"]
with open('authors.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(authors)
