from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Menu, Booking


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    success = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = BookingForm()
    context = {'form': form, 'success': success}
    return render(request, 'book.html', context)


def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_data})


def display_menu_item(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk) if pk else ''
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid credentials or insufficient permissions'
    return render(request, 'dashboard_login.html', {'error': error})


def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')


@login_required(login_url='/dashboard/login/')
def dashboard(request):
    bookings = Booking.objects.all().order_by('date', 'time')
    menu_items = Menu.objects.all().order_by('category', 'name')
    context = {
        'bookings': bookings,
        'menu_items': menu_items,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='/dashboard/login/')
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
    return redirect('dashboard')


@login_required(login_url='/dashboard/login/')
def delete_menu_item(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        menu_item.delete()
    return redirect('dashboard')

@login_required(login_url='/dashboard/login/')
def add_menu_item(request):
    from django.forms import ModelForm
    from .models import Menu

    class MenuItemForm(ModelForm):
        class Meta:
            model = Menu
            fields = ['name', 'category', 'price', 'featured', 'menu_item_description', 'image']

    form = MenuItemForm()
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'dashboard_menu_form.html', {'form': form, 'title': 'Add Menu Item'})


@login_required(login_url='/dashboard/login/')
def edit_menu_item(request, pk):
    from django.forms import ModelForm
    from .models import Menu

    class MenuItemForm(ModelForm):
        class Meta:
            model = Menu
            fields = ['name', 'category', 'price', 'featured', 'menu_item_description', 'image']

    menu_item = get_object_or_404(Menu, pk=pk)
    form = MenuItemForm(instance=menu_item)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'dashboard_menu_form.html', {'form': form, 'title': 'Edit Menu Item'})

@login_required(login_url='/dashboard/login/')
def add_booking(request):
    form = BookingForm()
    success = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'dashboard_booking_form.html', {'form': form, 'title': 'Add Reservation'})