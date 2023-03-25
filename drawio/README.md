# Draw.io Assets

Draw.io is an open source digraming program that works on Mac, Windows, Linux, Web, and just about anything else.  It is very good ad making diagrams you can control.  Its solves licensing issues caused when diagrams are written in on the OmniGravel or Vizio.

To work with these files you will want this VSCode [plugin](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio).

You can now directly edit drawio digrams and directly inbed them in your markdown files.  To do this just create a file named `file.drawio.svg` and edit it.  

If you are running in Dark Mode in VSCode or on your browser you may not get the result you expect.  You can solve this by placing a white background on your diagram or changing the drawio style.  I like the `Atlas` style.  To do this 
#. Open Command Palette (Ctrl-Shift-P)...
#. Select Draw.io: Change Theme
#. Select "Kennedy" or "Atlas"

Then create your diagram.

To include it in markdown just use a standard image tag.  This is an exmaple

![The example diagram as svg](./example.drawio.svg)

This works for github pages as well but because of path translations you need to keep the drawio file in the same folder as the markdown. 
