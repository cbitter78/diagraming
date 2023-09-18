#!/usr/bin/env python3

import csv
from N2G import drawio_diagram
from html import escape

# The metaEdit=1 sets the edit data dialog box as the default action when you click on the node in draw.io
NODE_STYLE='rounded=1;whiteSpace=wrap;html=1;align=left;spacingLeft=5;metaEdit=1;'
NODE_LABEL = '''
Name:    &emsp; %name%<br>
Location:&emsp; %location%<br>
Hobby:   &emsp; %hobby%
'''

def read_csv_file(filename):
    rows = []
    with open(filename, 'r') as csv_file:
        for row in csv.DictReader(csv_file):
            rows.append(row)
        return rows

if __name__ == "__main__":
    g = {
        'nodes':[],
        'links':[] # Dont use this but you can defined links (it draws arrows) see https://n2g.readthedocs.io/en/latest/diagram_plugins/DrawIo%20Module.html#loading-graph-from-dictionary
    }

    rows = read_csv_file("data.csv")
    for r in rows:
        g['nodes'].append({'id': r['node_id'], 'data':r, 'label': escape(NODE_LABEL), 'style': NODE_STYLE, 'placeholders': "1" })

    diagram = drawio_diagram()
    diagram.from_dict(g, width=300, height=200, diagram_name="data.csv")
    diagram.layout(algo="kk")
    diagram.dump_file(filename="created.drawio.svg", folder="./")
