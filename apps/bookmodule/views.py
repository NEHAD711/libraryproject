from django.shortcuts import render

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def html5_links(request):
    return render(request, 'bookmodule/html5/links.html')

def html5_listing(request):
    return render(request, 'bookmodule/html5/listing.html')

def html5_tables(request):
    return render(request, 'bookmodule/html5/tables.html')

def text_formatting(request):
    return render(request, 'bookmodule/html5/text.html')