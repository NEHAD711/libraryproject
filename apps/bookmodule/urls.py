from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.html5_links, name='html5_links'),
    path('html5/text/formatting', views.text_formatting, name='text_formatting'),
    path('html5/listing', views.html5_listing, name='html5_listing'),
    path('html5/tables', views.html5_tables, name='html5_tables'),
    path('search/', views.searchBooks, name='searchBooks'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('lab8/task1', views.task1_query, name='lab8_task1'),
    path('lab8/task2', views.task2_query, name='lab8_task2'),
    path('lab8/task3', views.task3_query, name='lab8_task3'),
    path('lab8/task4', views.task4_query, name='lab8_task4'),
    path('lab8/task5', views.task5_query, name='lab8_task5'),
    path('lab8/task7', views.task7_query, name='lab8_task7'),
    path('lab9/task1/', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2/', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3/', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4/', views.lab9_task4, name='lab9_task4'),
]

