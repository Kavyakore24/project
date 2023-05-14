import csv
import xml.etree.ElementTree as ET

# parse the XML file
tree = ET.parse('A1.xml')
root = tree.getroot()

# set the namespace
ns = {'mw': 'http://www.mediawiki.org/xml/export-0.10/'}

# open a CSV file for writing
with open('data_1_new.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # write the header row
    writer.writerow(['Title', 'Author', 'Author ID', 'Date of Publication', 'ID', 'Comment', 'Comment Length', 'References/Citations'])

    # loop through each article
    for page in root.findall('mw:page', ns):

        # extract the data for each article
        title = page.find('mw:title', ns).text
        author = page.find('mw:revision/mw:contributor/mw:username', ns)
        if author is not None:
            author = author.text
        else:
            author = 'Unknown'
        author_id = page.find('mw:revision/mw:contributor/mw:id', ns)
        if author_id is not None:
            author_id = author_id.text
        else:
            author_id = 'Unknown'
        date = page.find('mw:revision/mw:timestamp', ns).text
        source = page.find('mw:id', ns).text
        comment = page.find('mw:revision/mw:comment', ns).text
        comment_length = len(comment) if comment else 0
        references = page.findall('mw:revision/mw:references/mw:ref', ns)
        if references:
            citations = len(references)
        else:
            citations = 0

        # write the data to the CSV file
        writer.writerow([title, author, author_id, date, source, comment, comment_length, citations])
