# Diagraming

Diagrams are a way to make ideas tangible.  When creating software and systems us humans need to work together.  This means passing ideas between us.  To do that we need ways to make these ideas tangible.  Diagrams are one way to do this.  Diagrams help us reason about complicated problems in abstract ways and helps understand the problem domain.

## Caution

A word of caution, diagrams are not the only way.  We should not relay on just a picture.  A single picture to explain a complex process tends to have lower levels of success unless you are IKEA. :)


## Rot

## Architecture 

Is an Architecture Diagram or a collection of Diagrams.  I would say no.  I think an architecture would use diagrams to communicate the architecture.  To do this effectively I have found that one set of diagrams is insufficient.

I find that a global view of the system Context is helpful to see where the major Containers and how they relate to each other. Then I want to “zoom in” to each container to see the components and their relationship that make it up. Finally, I want to “zoom in” again to see what the makes up the components. In most cases this is Code.

I used the word zoom in intentionally.   A good architecture can use diagrams much like Google Earth uses maps.  You can zoom in and out as you want a global view or if you want to get all the way down to street view.

This is the C4 model. Context, Containers, Components, and Code.  Visit [c4model.com](https://c4model.com/).  Make sure to give the site a read and even watch the video.  It is really good!

## Rot

Like fruit or Costco bread Architectures start to rot the day they are created.  There is lots of thought out there on why this happens.  In my experience the two main factors that I have found are distance and discipline.   Distance happens when the architecture lives in a different place from the software.  I have seen this with wiki and Share Point.  To help solve this locate the Architecture as close to the code as you can.  This might look like the Context and Component layers in a git repo in the same organization and the Component and Code layers next to the code.  With the architecture co-located with the code you can help with discipline with code reviews, CICD actions, and other goodies.  This will not solve the problem.  I have found that it makes things better.  It’s just a bonus that your architecture can now be versioned, tagged, and released.

## Tools

Do we need to use the C4 tools?  I think they are good.  However, like all tools in the physical and software world, one is never the right fit for all jobs.  Or we would call them Tool.  Not Tools.

I struggled with the C4 [Structurizr](https://structurizr.com/) Domain Specific Language.  I love the idea of defining the diagram domain and then creating views.  I ran into issues where the DSL and tooling got in the way.  I believe in keeping things as simple as I can especially in tooling.  I ended up adopting the philosophy and implementing it using what ever tool set worked best.

### TLDR

I think [mermaid](#mermaid) is extremely useful for Component and Context C4 diagrams using mermaid-c4.  However, I do not limit myself to the c4 stencil kit.  To me the c4 philosophy is not limited to a set of graphics.  I tend to favor them because they make sense, but I would feel free to use any stencil.  When using mermaid I favor embedding them directly in markdown and keeping them simple.  I favor more diagrams than large diagrams leveraging markdown to add context.   This makes the diagrams easy to maintain and review.  Check out the examples in the [mermaid folder](./mermaid/)

For a zoom out at the Context, Containers layers I find myself wanting something more free from.  If I can keep it simple in mermaid I will.  If not, then draw.io seems to be a good solution.   Code reviews are not as easy, however Context, Containers layers tend to change much less than the other layers and this seems to work well.   In the end all diagrams are rendered to markdown and are easy to consume in github.  You can also automate draw.io.  See [./drawio/automation](./drawio/automation/README.md)

Do continue to read how I landed on this tool combo.

### Tool Selection

For me a diagram tool should:


- Not require a license to be installed on my computer.  This stops open source and is you work in a big company you must wait to buy software, install it, pay for it every year.  For me this is a deal breaker.  I will not use any diagraming tool that requires a license.  It’s not kind to others when they can’t open the file.
- Be Operating System agnostic.  It should work on Mac, Linux, Windows, (extra points for mobile operating systems)
- Be visualized directly in VSCode.  This is a list of what I value, I use VSCode and therefore I value VSCode plugins.
- Defined in a way that can be easily code reviewed.  If the diagram is text, then it lends itself to a code review.  However, if it is complex text then you did not do yourself any favors.
- Rendered into your documentation for you.   If your diagrams show up in your markdown files as nice graphics with little effort all the better.  If they plug into other rendering engines like, make docs then you are winning! If you have to build a CICD pipeline for them, you may want to consider the cost of explaining how it works to new contributors vs the benefit.
- Supports C4: I think the C4 philosophy is worth while and I want to use it in my diagrams.

I have scored each tool I have used in the past here.   These are my own opinions.  My scoring is on a scale of Very Good, Good, Maybe, Meh, Ok, Poor, Very Poor and Hard NO!

#### Viso

- License:  Fail: Requires a license. It is true you can sort of use Viso in Office 365 but it is not the same.
- OS agnostic: Fail: Windows only.
- VSCode Plugin: Fail:  Not that I could find.
- Code Review: Fail:  It’s a binary file.
- Rendered: Very Poor: You could create a CICD pipeline to export the file as a graphic.  You could use something like [this](https://gist.github.com/mjul/5212271) but you would need a CICD runner with VISO, PowerShell and Windows.
- Supports C4: Meh!  Via importing external packages.

Total Score: Hard NO!


#### Omnigraffle

- License:  Fail: Requires a license.
- OS agnostic: Fail: Mac only.
- VSCode Plugin: Fail:  Not that I could find.
- Code Review: Fail:  It’s a binary file.
- Rendered: Very Poor: You could create a CICD pipeline to export the file as a graphic.  You could use something like [this](https://github.com/fikovnik/omnigraffle-export/blob/master/README.md) but you would need a CICD runner with Omnigraffle, AppleScript on a Mac.
- Supports C4: Meh!  Via importing external packages.

Total Score: Hard NO!

#### Draw.io (local files)

- License:  Very Good:  Open Source
- OS agnostic: Very Good: Runs on everything.  You can download it [here](https://github.com/jgraph/drawio-desktop/releases).  You can use it in a browser but then the diagrams are not next to the code.
- VSCode Plugin: Very Good: You can get it [here](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
- Code Review: OK: Draw.io files are text, but they are complex text.  With CICD like actions the PR includes a graphic file that can easily be inspected as a graphic.   This is an [example](https://github.com/cbitter78/diagraming/pull/1)
- Rendered: Very Good: The github html pipeline supports draw.io svg and png rendering.  All you need to do is just name the file in the repo. name.drawio.svg or name.drawio.png.   The VSCode plugin will treat it like a normal draw.io file.   You can then just include it with a markdown image tag.   The local VSCode plugin will render it real time and github also renders it.  Check out [this repo](https://github.com/philip-gai/github-drawio-demo) for more info.  You can also check out the [drawio/](./drawio/) folder for examples.
- Supports C4: Good  There is a C4 template set out of the box.  Its quite easy to use.

Total Score: Very Good

#### Structurizr

- License:  Very Good:  Open Source
- OS agnostic: Very Good:  Offers a Docker Container and many plugins that run on most anything. (Not model)
- VSCode Plugin: Not Great.  There is syntax highlighting which did not really work.  You can’t see your diagrams in a preview.  There is a small exception to this if you use mermaid (more below) however if you get the DSL wrong the error is not helpful and you spend hours trying to figure out what line is missing a quotation mark.
- Code Review: Good:  The DSL is in text, and you can read it.  It’s not simple but not complex
- Rendered: Meh!: You can create a CICD pipeline that can call the Structurizr cli or un the Structurizr docker container.  I did not love the Structurizr docker container web site, so I give it a Meh!
- Supports C4: Very Good!  Umm.. Yes it had better!  :)

Total Score: Maybe

#### Mermaid

- License:  Very Good:  Open Source
- OS agnostic: Very Good: Runs on everything. (Not model)
- VSCode Plugin: Very Good:  There are many.  I used this [one](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) that plugs right into the markdown preview.
- Code Review: **ToDo** @cbitter78
- Rendered: Very Good: [Mermaid](https://mermaid.js.org/intro/) graphs in the Markdown are automatically rendered into embedded diagrams in markdown files by the github enterprise [GitHub’s HTML pipeline](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/).  This means that embed Mermaid diagrams in a .md file will be converted into a graph when pushed to github.
- Supports C4: Good: Supported via [mermaid - c4](https://mermaid.js.org/syntax/c4c.html).  However, if there is c4 DSL issue, finding the error is very hard.  Sinse this is the same with Structurizr, I would not say it's mermaid fault.  Just know it's a thing.

Total Score: Very Good

#### PlantUML

- License:  Very Good:  Open Source
- OS agnostic: Very Good: Runs on everything. (Not model)
- VSCode Plugin: Very Good:  There are many.  I used this [one](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
- Code Review: Very Good: It is simple text.
- Rendered: Poor: Native markdown support is not there. You can create a CICD Pipeline.  I plan to add one to this project.  You have the same challenge of teaching people how it works.
- Supports C4: Very Good: Supported via [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML)

Total Score: Good
Note: I really do like PlantUML.  It is quite a lot like Mermaid and in some ways better.  I scored it lower than Mermaid only because of the native github.com HTML pipeline support.
