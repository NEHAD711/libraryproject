from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_books/', views.list_books, name='list_books'),
    path('<int:bookId>/', views.viewbook, name='view_one_book'),
    path('aboutus/', views.aboutus, name='aboutus'),
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
    
    # Part 1
    path('lab9_part1/listbooks', views.lab10_part1_listbooks, name='lab10_part1_listbooks'),
    path('lab9_part1/addbook', views.lab10_part1_addbook, name='lab10_part1_addbook'),
    path('lab9_part1/editbook/<int:id>', views.lab10_part1_editbook, name='lab10_part1_editbook'),
    path('lab9_part1/deletebook/<int:id>', views.lab10_part1_deletebook, name='lab10_part1_deletebook'),
    
    # Part 2
    path('lab9_part2/listbooks', views.lab10_part2_listbooks, name='lab10_part2_listbooks'),
    path('lab9_part2/addbook', views.lab10_part2_addbook, name='lab10_part2_addbook'),
    path('lab9_part2/editbook/<int:id>', views.lab10_part2_editbook, name='lab10_part2_editbook'),
    path('lab9_part2/deletebook/<int:id>', views.lab10_part2_deletebook, name='lab10_part2_deletebook'),

    path('lab11/task1/list', views.lab11_task1_list, name='lab11_task1_list'),
    path('lab11/task1/add', views.lab11_task1_add, name='lab11_task1_add'),
    path('lab11/task1/edit/<int:id>', views.lab11_task1_edit, name='lab11_task1_edit'),
    path('lab11/task1/delete/<int:id>', views.lab11_task1_delete, name='lab11_task1_delete'),
    path('lab11/task3/upload', views.lab11_task3_upload, name='lab11_task3_upload'),
    path('lab11/task3/list', views.profile_list, name='profile_list'),

    path('logout/', views.logout_view, name='logout'),


    path('lab13/task1', views.lab13_task1, name='lab13_task1'),
    path('lab13/task2', views.lab13_task2, name='lab13_task2'),
    path('lab13/task3', views.lab13_task3, name='lab13_task3'),
    path('lab13/task4', views.lab13_task4, name='lab13_task4'),
    path('lab13/task5', views.lab13_task5, name='lab13_task5'),  
]