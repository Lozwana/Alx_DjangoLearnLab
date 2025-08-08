from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
list_books,
LibraryDetailView,
register_view,
admin_view,
librarian_view,
member_view,
book_create,
book_update,
book_delete
)

app_name = 'relationship_app'

# Book and Library URLs
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

 # Authentication URLs using built-in class based views
 
    path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'),
    path('logout/', 
         LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'),
    path('register/', register_view, name='register'),

 # Role-based URLs
    path('admin/dashboard/', admin_view, name='admin_dashboard'),
    path('librarian/dashboard/', librarian_view, name='librarian_dashboard'),
    path('member/dashboard/', member_view, name='member_dashboard'),
    
    # Book management URLs
    path('books/add/', book_create, name='book_create'),
    path('books/<int:pk>/edit/', book_update, name='book_update'),
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),
]