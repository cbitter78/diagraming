#!/usr/bin/env python3

import csv
from N2G import drawio_diagram

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
    g = {
        'nodes':[],
        'links':[] # Dont use this but you can defined links (it draws arrows) see https://n2g.readthedocs.io/en/latest/diagram_plugins/DrawIo%20Module.html#loading-graph-from-dictionary
    }

    rows = read_csv_file("data.csv")
    for r in rows:
        g['nodes'].append({'id': r['node_id'], 'data':r, 'label': NODE_LABEL, 'style': NODE_STYLE, 'placeholders': "1" })

    diagram = drawio_diagram()
    diagram.from_dict(g, width=300, height=200, diagram_name="data.csv")
    diagram.layout(algo="kk")
    diagram.dump_file(filename="created.drawio.svg", folder="./")
