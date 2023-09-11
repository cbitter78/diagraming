# Draw.io Automation

Sometimes you want to update or create a diagram from data. You can do this with draw.io. There are a few quirks but overall it works fine.  You can check out the examples in this folder. I really like how you can arrange and tweak draw.io files.  I think my workflow will be to use `create.py` to start then `update_existing.py` as needed.

These are stand-alone scripts, so I do repeat code.  This is intentional.

## Update

[update_existing.py](./update_existing.py) will read in [data.csv](./data.csv) and then update the file [existing.drawio](./existing.drawio) based on the nodes ids in that diagram mapping to node_id column.  Each node is updated with new data.  The data is displayed in the node label via [placeholders](https://www.drawio.com/blog/placeholder-scope).  It will create new nodes if a node is not found.  It then writes out a file existing.drawio.svg  It can write out a standard drawio file but I like the svg version in VS Code.

## Create

[create.py](./create.py) will read data in [data.csv](./data.csv) and then and then create a new file from it.  That file is named created.drawio.svg
