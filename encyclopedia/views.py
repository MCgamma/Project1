from django.shortcuts import render, redirect


from django.http import HttpResponse, QueryDict
from . import util
import markdown2
from markdown2 import markdown_path
from django import forms
import random

class SearchForm(forms.Form):
    search = forms.CharField(label="Search Encyclopedia")




def index(request):
    sublist = util.list_entries()
    lower = [y.casefold() for y in util.list_entries()]
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
                    "entries": sublist, "form":SearchForm   # make error with css
                })
                                                  
    return render(request, "encyclopedia/index.html", {
        "entries": sublist, "form":SearchForm, "random":random.choice(sublist)
    })


def title(request, name):
    lower = [y.casefold() for y in util.list_entries()]
    sublist = util.list_entries()
    if name.casefold() in (x.casefold() for x in sublist):
        b = lower.index(name.casefold())
        file = markdown2.markdown(markdown_path(f"./entries/{name}.md"))
        return render(request, "encyclopedia/exist.html", {
            "name":sublist[b], "file":file
        })

    else:
        return render(request, "encyclopedia/exist.html", {
            "name": name
        } )



def new_page(request):
    lower = [y.casefold() for y in util.list_entries()]
    if request.method == "POST":
        p = request.POST["titlemd"]
        t = request.POST["contentmd"]
        
        if util.get_entry(p):
            return render(request, "encyclopedia/new_page.html", {
                "error_new":"error_new"
            })
        else:
            util.save_entry(p,t)
            return redirect('encyclo:title', name = p)


    return render(request, "encyclopedia/new_page.html", {
        "error_new":"no_new"
    })


def edit_page(request, tname):
    lower = [y.casefold() for y in util.list_entries()]
    if request.method == "POST":
        p = request.POST["contentmd"]
        util.save_entry(tname, p)
        return redirect('encyclo:title', name = tname)
       

    return render(request, "encyclopedia/edit_page.html", {
        "name":tname, "content":util.get_entry(tname)
    })


