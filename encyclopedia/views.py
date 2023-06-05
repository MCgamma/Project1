from django.shortcuts import render

from . import util
import markdown2
from markdown2 import markdown_path


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):      

    if name.casefold() in (x.casefold() for x in util.list_entries()):
        lower = [y.casefold() for y in util.list_entries()] 
        a = lower.index(name.casefold())
        normal = util.list_entries()
        file = markdown2.markdown(markdown_path(f"./entries/{name}.md"))
        return render(request, "encyclopedia/exist.html", {
            "name":normal[a], "file":file
        })

    else:
        return render(request, "encyclopedia/exist.html", {
            "name": name
        } )

