from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='library'),
    path('update/', views.update, name='update'),
    path('update1/', views.update1, name='update1'),
    path('print_filtered/', views.print_filtered, name='print_filtered'),
    path('main_page/', views.main_page, name='main_page'),
    path('borrower_menu/', views.borrower_menu, name='borrower_menu'),
    path('librarian_menu/', views.librarian_menu, name='librarian_menu'),
    path('librarian_add/', views.librarian_add, name='librarian_add'),
    path('add_new_book/', views.add_new_book, name='add_new_book'),
    path('librarian_update/', views.librarian_update, name='librarian_update'),
    path('update_actions/', views.update_actions, name='update_actions'),
    path('librarian_delete/', views.librarian_delete, name='librarian_delete'),
    path('delete_actions/', views.delete_action, name='delete_action'),
    path('librarian_add_user/', views.librarian_add_user, name='librarian_add_user'),
    path('account_system_menu/', views.account_system_menu, name='account_system_menu'),
    path('account_system_add/', views.account_system_add, name='account_system_add'),
    path('add_new_user/', views.add_new_user, name='add_new_user'),
    path('account_system_update/', views.account_system_update, name='account_system_update'),
    path('account_system_delete/', views.account_system_delete, name='account_system_delete'),
    path('check_user/', views.check_user, name='check_user'),
    path('login/', views.login, name='login'),
    path('add_book_to_borrower/', views.add_book_to_borrower, name='add_book_to_borrower'),
    path('user_update_action/', views.user_update_action, name='user_update_action'),
    path('user_delete_action/', views.user_delete_action, name='user_delete_action'),
]
