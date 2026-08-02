from apps.bookmodule.models import Book, Address, Student
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Department, Course

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


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def searchBooks(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    return render(request, 'bookmodule/search.html')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') 
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def task1_query(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})


def task2_query(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})


def task3_query(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def task4_query(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})


def task5_query(request):
    aggregates = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'aggregates': aggregates})


def task7_query(request):
    student_count_by_city = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'cities': student_count_by_city})



def lab9_task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9_task1.html', {'departments': departments})


def lab9_task2(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9_task2.html', {'courses': courses})



def lab9_task3(request):
    departments = Department.objects.all()
    results = []
    for dept in departments:
        oldest_student = Student.objects.filter(department=dept).order_by('id').first()
        results.append({
            'department': dept.name,
            'student': oldest_student
        })
    return render(request, 'bookmodule/lab9_task3.html', {'results': results})



def lab9_task4(request):
    departments = Department.objects.annotate(student_count=Count('student')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/lab9_task4.html', {'departments': departments})