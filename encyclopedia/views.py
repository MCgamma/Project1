from django.shortcuts import render

from . import util
import markdown2
from markdown2 import markdown_path


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):      # There is a problem with capital letters

    if name in util.list_entries():
        file = markdown2.markdown(markdown_path(f"./entries/{name}.md"))
        return render(request, "encyclopedia/exist.html", {
            "name":name, "file":file
        })

    else:
        return render(request, "encyclopedia/exist.html", {
            "name": name
        } )
        


