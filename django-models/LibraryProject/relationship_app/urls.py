from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

app_name = 'relationship_app'
# URL patterns for the relationship app
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
    path('register/', views.register_view, name='register'),
]
