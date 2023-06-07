from django.shortcuts import render, redirect

from django.http import HttpResponse
from . import util
import markdown2
from markdown2 import markdown_path
from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="Search Encyclopedia")

lower = [y.casefold() for y in util.list_entries()] 
normal = util.list_entries()


def index(request):
    sublist = [util.list_entries()]
    if request.method == "POST":
        sform = SearchForm(request.POST) 
        if sform.is_valid():
            a = sform.cleaned_data["search"]
            sublist = []
            for lo in lower:
                if a.casefold() in lo:
                    sublist.append(lo)

            if a.casefold() in lower:
                           
                return redirect('encyclo:title', name = a)
            elif sublist:
                return render(request, "encyclopedia/entry_sublist.html", {
                    "entries": sublist, "form":SearchForm
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries(), "form":SearchForm   # make error with css
                })
            
                      
                
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "form":SearchForm
    })


def title(request, name):      

    if name.casefold() in (x.casefold() for x in util.list_entries()):
        b = lower.index(name.casefold())
        file = markdown2.markdown(markdown_path(f"./entries/{name}.md"))
        return render(request, "encyclopedia/exist.html", {
            "name":normal[b], "file":file
        })

    else:
        return render(request, "encyclopedia/exist.html", {
            "name": name
        } )

