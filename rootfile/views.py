from django.shortcuts import render, redirect

props = {
    "title": "Home",
    "page_name": "Dashboard",
    "subpage_name": "Default Dashboard"
}


def index(request):
    return render(request, 'index.html', context=props)



