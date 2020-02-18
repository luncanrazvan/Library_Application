from django.shortcuts import render, redirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Book, Users, Borrowers


def index(request):
    all_posts = Book.objects.raw("select * from library_book")
    return render(request, 'index.html', {'books': all_posts})


def update(request):
    all_posts = Book.objects.raw("select * from library_book")
    return render(request, 'update.html', {'books': all_posts})


def update1(request):
    number = int(request.POST.get('search', ''))
    name = request.POST.get('name', '')
    type1 = request.POST.get('type', '')
    description = request.POST.get('description', '')
    Book.objects.filter(id=number).update(col1=name, col2=type1, col3=description)
    return redirect('library')


def print_filtered(request):
    filter_query = request.POST.get('filter', '')
    filter_name = request.POST.get('filter_type', '')
    if filter_query == "Title":
        if filter_name:
            filter_results = Book.objects.filter(title=filter_name)
            return render(request, "borrower_menu.html", {'books': filter_results})

    if filter_query == "Author":
        if filter_name:
            filter_results = Book.objects.filter(author=filter_name)
            return render(request, "borrower_menu.html", {'books': filter_results})

    if filter_query == "Subject":
        if filter_name:
            filter_results = Book.objects.filter(subject=filter_name)
            return render(request, "borrower_menu.html", {'books': filter_results})

    if filter_query == "Price":
        if filter_name:
            filter_results = Book.objects.filter(price=filter_name)
            return render(request, "borrower_menu.html", {'books': filter_results})

    return render(request, "borrower_menu.html", {'books': ""})


def add_new_book(request):
    author = request.POST.get('author', '')
    title = request.POST.get('title', '')
    subject = request.POST.get('subject', '')
    price = int(request.POST.get('price', ''))

    if author and title and subject and price:
        book = Book(title=title, author=author, subject=subject, price=price)
        book.save()
    return render(request, "librarian_add.html")


def add_new_user(request):
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    username = request.POST.get('user_name', '')
    password = request.POST.get('password', '')

    if username and password and first_name and last_name:
        user = Users(first_name=first_name, last_name=last_name, username=username, password=password)
        user.save()
    return render(request, 'account_system_add.html')


def librarian_add_user(request):
    return render(request, 'librarian_add_user.html')


def borrower_menu(request):
    return render(request, 'borrower_menu.html')


def librarian_menu(request):
    return render(request, 'librarian_menu.html')


def account_system_menu(request):
    return render(request, 'account_system_menu.html')


def librarian_add(request):
    return render(request, 'librarian_add.html')


def account_system_add(request):
    return render(request, 'account_system_add.html')


def librarian_update(request):
    all_books = Book.objects.raw("select * from library_book")
    return render(request, 'librarian_update.html', {'books': all_books})


def account_system_update(request):
    all_users = Users.objects.raw("select * from library_users")
    return render(request, 'account_system_update.html', {'users': all_users})


def account_system_delete(request):
    all_users = Book.objects.raw("select * from library_users")
    return render(request, 'account_system_delete.html', {'users': all_users})


def user_delete_action(request):
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    print(first_name, last_name)
    Users.objects.filter(first_name=first_name, last_name=last_name).delete()
    return render(request, 'account_system_delete.html')


def user_update_action(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    old_f_name = request.POST.get('old_f_name', '')
    old_l_name = request.POST.get('old_l_name', '')
    aux_credit = request.POST.get('credits', '')
    credit = 0
    print(old_f_name)
    if aux_credit:
        credit = int(aux_credit)

    if username:
        Users.objects.filter(last_name=old_l_name, first_name=old_f_name).update(username=username)

    if credit:
        Users.objects.filter(last_name=old_l_name, first_name=old_f_name).update(credit=credit)

    if password:
        Users.objects.filter(last_name=old_l_name, first_name=old_f_name).update(password=password)

    if first_name:
        Users.objects.filter(last_name=old_l_name, first_name=old_f_name).update(first_name=first_name)

    if last_name:
        Users.objects.filter(last_name=old_l_name, first_name=old_f_name).update(last_name=last_name)

    return redirect('account_system_update')


def librarian_delete(request):
    all_books = Book.objects.raw("select * from library_book")
    return render(request, 'librarian_delete.html', {'books': all_books})


def login(request):
    return render(request, 'login.html')


def update_actions(request):
    author = request.POST.get('book_author', '')
    old_title = request.POST.get('book_title_old', '')
    title_new = request.POST.get('book_title_new', '')
    subject = request.POST.get('book_subject', '')
    aux_price = request.POST.get('book_price', '')
    price = 0
    if aux_price:
        price = int(aux_price)

    if author:
        Book.objects.filter(title=old_title).update(author=author)

    if title_new:
        Book.objects.filter(title=old_title).update(title=title_new)

    if subject:
        Book.objects.filter(title=old_title).update(subject=subject)

    if price:
        Book.objects.filter(title=old_title).update(price=price)

    return redirect('librarian_update')


def check_user(request):
    user_name = request.POST.get('username', '')
    password = request.POST.get('password', '')
    number_users = Users.objects.filter(username=user_name).count()
    number_passwords = Users.objects.filter(password=password).count()

    if number_users > 0 and number_passwords > 0:
        request.session['username'] = user_name
        return render(request, "borrower_menu.html")
    else:
        return render(request, "login.html")


@csrf_exempt
def add_book_to_borrower(request):
    if request.method == 'POST':
        if 'title' in request.POST:
            title = request.POST['title']
            book = Book.objects.filter(title=title).first()
            book_price = book.price
            print(type(book))
            user = Users.objects.filter(username=request.session['username']).first()
            user_last_name = Users.objects.filter(username=request.session['username']).values_list('last_name', flat=True).first()
            user_first_name = Users.objects.filter(username=request.session['username']).values_list('first_name', flat=True).first()
            user_credit = Users.objects.filter(username=request.session['username']).values_list('credit', flat=True).first()
            if book_price <= user_credit:
                user_credit = user_credit - book_price
                Users.objects.filter(username=request.session['username']).update(credit=user_credit)
                borrower = Borrowers(book=book, users=user, first_name=user_first_name, last_name=user_last_name)
                borrower.save()
    return render(request, "borrower_menu.html")


def delete_action(request):
    title = request.POST.get('book_title', '')
    Book.objects.filter(title=title).delete()
    return redirect('librarian_delete')


def main_page(request):
    return render(request, 'mainpage.html')