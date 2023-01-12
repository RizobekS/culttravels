from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from django.utils.translation import gettext_lazy as _
from .models import FAQ, Tours, Reservation
from django.contrib.auth import login, authenticate, logout
from clickuz import ClickUz
from paycomuz import Paycom
from transaction.service import *


def index(request):
    if request.LANGUAGE_CODE == 'en':
        tours_home = Tours.objects.filter(english=True).order_by('-pk')
    elif request.LANGUAGE_CODE == 'ru':
        tours_home = Tours.objects.filter(russian=True).order_by('-pk')
    else:
        tours_home = Tours.objects.filter(uzbek=True).order_by('-pk')

    return render(request, "home/home.html", {'tours_home': tours_home[:5]})


def tours(request):
    if request.LANGUAGE_CODE == 'en':
        list_tours = Tours.objects.filter(english=True).order_by('-pk')
    elif request.LANGUAGE_CODE == 'ru':
        list_tours = Tours.objects.filter(russian=True).order_by('-pk')
    else:
        list_tours = Tours.objects.filter(uzbek=True).order_by('-pk')

    page = request.GET.get('page', 1)
    paginator = Paginator(list_tours, 10)  # number of news in each page

    try:
        list_tours = paginator.page(page)
    except PageNotAnInteger:
        list_tours = paginator.page(1)
    except EmptyPage:
        list_tours = paginator.page(paginator.num_pages)

    return render(request, 'home/tours.html', {'list_tours': list_tours})


def tours_details(request, pk):
    detail = Tours.objects.get(pk=pk)
    if request.LANGUAGE_CODE == 'en' and not detail.english:
        return HttpResponseRedirect(f"/{request.LANGUAGE_CODE}/tours/")
    elif request.LANGUAGE_CODE == 'uz' and not detail.uzbek:
        return HttpResponseRedirect(f"/{request.LANGUAGE_CODE}/tours/")
    elif request.LANGUAGE_CODE == 'ru' and not detail.russian:
        return HttpResponseRedirect(f"/{request.LANGUAGE_CODE}/tours/")

    # increment views number by one every request
    detail.views += 1
    detail.save()

    context = {
        'detail': detail
    }

    return render(request, "home/tours_details.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() and request.POST['address'] == "":
            form.save()
            name = request.POST['name']
            messages.success(request, 'Success!')
            return render(request, 'home/contact.html', {'name': name})
        else:
            name = "Ooops, something went wrong!"
            return render(request, 'home/contact.html', {'name': name})
    else:
        return render(request, 'home/contact.html', {})


def reservation(request):
    tours_list = Tours.objects.all()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid() and request.POST['address'] == "":
            form.save()
            name = request.POST['name']
            messages.success(request, 'Success!')
            return render(request, 'home/reservation.html', {'name': name, 'tour_list': tours_list})
        else:
            name = "Ooops, something went wrong!"
            return render(request, 'home/reservation.html', {'name': name, 'tour_list': tours_list})
    else:
        return render(request, 'home/reservation.html', {'tour_list': tours_list})


def faq(request):
    questions_and_answers = FAQ.objects.all().order_by('id')
    return render(request, 'home/faq.html', {'questions_and_answers': questions_and_answers})


def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(username=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, _("Username or password is incorrect!"))
    return render(request, 'registration/login.html')


# def register_view(request):
#     return render(request, 'registration/register.html')


def register_view(request):
    if request.method == "POST":
        try:
            user = User()
            user.type = 3
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.phone = request.POST.get('phone')
            user.email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                user.password = password1
                user.save()
            messages.success(request,
                             _("Successfully registered! Enter your registered phone number and password!"))
            return redirect("login")
        except Exception as e:
            print(e)
            messages.error(request, _("Username or password is incorrect!"))
    return render(request, "registration/register.html")


def dashboard(request):
    mytours = MyTours.objects.filter(user__id=request.user.id).order_by('-id')
    if request.method == 'POST':
        return redirect('tours')

    context = {
        'mytours': mytours
    }

    return render(request, 'home/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def invoice(request, id):
    mytour = MyTours.objects.get(id=id)

    context = {
        'mytour': mytour
    }
    return render(request, 'home/invoice_detail.html', context)


def mytourdetail(request, id):
    mytour = MyTours.objects.get(id=id)
    context = {
        'mytour': mytour
    }

    return render(request, 'home/mytour_detail.html', context)


@login_required(login_url='/login/')
def click_generate_url(request, amount, tour_id):
    price = amount * 1

    transaction_id = initalize_transaction_click(
        request.user,
        price,
        tour_id
    )

    generated_link = ClickUz.generate_url(
        order_id=transaction_id,
        amount=price,
        return_url='http://www.culttravels.com/dashboard/'
    )
    return redirect(generated_link)


@login_required(login_url='/login/')
def payme_generate_url(request):
    amount = request.GET.get('amount')
    tour_id = request.GET.get('tour_id')
    res = float(amount) * float(100)
    price = Decimal(str(res))
    print(price)

    transaction_id = initalize_transaction_payme(
        request.user,
        amount,
        tour_id
    )

    generated_link = Paycom().create_initialization(
        price,
        transaction_id,
        return_url="http://www.culttravels.com/dashboard/"
    )
    return redirect(generated_link)


def payment_success(request, payment_type, tour_id, user):
    tour = Tours.objects.get(id=tour_id)

    mytour = MyTours()
    mytour.user = user

    mytour.title_en = tour.title_en
    mytour.title_ru = tour.title_ru
    mytour.title_uz = tour.title_uz

    mytour.description_en = tour.description_en
    mytour.description_ru = tour.description_ru
    mytour.description_uz = tour.description_uz

    mytour.value = tour.value  # price
    mytour.image = tour.image
    mytour.image_uz = tour.image_uz
    mytour.image_ru = tour.image_ru

    mytour.payment_status = 'paid'
    mytour.payment_type = payment_type
    mytour.total_price = tour.value
    mytour.save()

    return redirect('dashboard')
