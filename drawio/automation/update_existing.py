#!/usr/bin/env python3

import csv
from N2G import drawio_diagram

FILE_TO_UPDATE = "./existing.drawio.svg"

# Escaped HTML with inline style for formatting that is used for the label
NODE_LABEL="Name:&lt;span style=&quot;white-space: pre;&quot;&gt;&#9;&lt;/span&gt;%name%&lt;br&gt;Location:&lt;span style=&quot;white-space: pre;&quot;&gt;&#9;&lt;/span&gt;%location%&lt;br&gt;Hobby:&lt;span style=&quot;white-space: pre;&quot;&gt;&#9;&lt;/span&gt;%hobby%"

# The metaEdit=1 sets the edit data dialog box as the default action when you click on the node in draw.io
NODE_STYLE='rounded=1;whiteSpace=wrap;html=1;align=left;spacingLeft=5;metaEdit=1;'

def read_csv_file(filename):
    rows = []
    with open(filename, 'r') as csv_file:
        for row in csv.DictReader(csv_file):
            rows.append(row)
        return rows


if __name__ == "__main__":
    rows = read_csv_file("data.csv")

    diagram = drawio_diagram()
    diagram.from_file("./existing.drawio")
    for r in rows:
        try:
            diagram.update_node(id = r['node_id'], data=r )
        except AttributeError:
            diagram.add_node(id = r['node_id'], data = r, label = NODE_LABEL, style = NODE_STYLE, placeholders = "1")
    diagram.dump_file(filename=FILE_TO_UPDATE, folder="./")
