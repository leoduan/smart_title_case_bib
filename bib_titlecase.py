#!/usr/bin/env python3
# coding: utf-8


from titlecase import titlecase


import bibtexparser


from bibtexparser.bwriter import BibTexWriter


import sys

filename = sys.argv[1]

with open(filename) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)


def addCurlyBracketAndTitleCase(s):
    if s[0]!="{":
        s = "{"+s
    if s[-1]!="}":
        s = s+"}"
    return titlecase(s)


for entry in bib_database.entries:
    entry['title'] = addCurlyBracketAndTitleCase(entry['title'] )
    try:
        entry['booktitle'] = addCurlyBracketAndTitleCase(entry['booktitle'] )
    except KeyError:
        None
    try:
        entry['author'] = entry['author'].strip()
    except KeyError:
        None
    try:
        entry['journal']= titlecase(entry['journal'])
    except KeyError:
        None

newFileName = ''.join(filename.split(".")[:-1])+"_fixed.bib"

writer = BibTexWriter()
# writer.indent = '    '     # indent entries with 4 spaces instead of one
# writer.comma_first = True  # place the comma at the beginning of the line
with open(newFileName, 'w') as bibfile:
    bibfile.write(writer.write(bib_database))

