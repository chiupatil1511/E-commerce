# python page for calling html pages
# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth

import random
import string
import pyrebase
config = {
  'apiKey': "AIzaSyDAr4HaMviKYieDMWqFDXbOwNXt7iG5Ksc",
  'authDomain': "ekisan-db-528b4.firebaseapp.com",
  'databaseURL': "https://ekisan-db-528b4-default-rtdb.firebaseio.com",
  'projectId': "ekisan-db-528b4",
  'storageBucket': "ekisan-db-528b4.appspot.com",
  'messagingSenderId': "221263229313",
  'appId': "1:221263229313:web:692ae298ad2b1fcf13f880",
  'measurementId': "G-GRD180ZQM6"
}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()

def index(request):
    return render(request, 'index.html')


def buying(request):
    return render(request, 'buying.html')


# def selling(request):
#     return render(request, 'AddItem1.html')


def crop(request):
    return render(request, 'crop.html')


def seedfert(request):
    return render(request, 'seedferti.html')


def risk(request):
    return render(request, 'risk.html')


def risk2(request):
    return render(request, 'risk2.html')


def risk3(request):
    return render(request, 'risk3.html')


def risk4(request):
    return render(request, 'risk4.html')


def animal(request):
    return render(request, 'animal.html')


def weather(request):
    return render(request, 'weather.html')


def program(request):
    return render(request, 'prog.html')


def contact(request):
    return render(request, 'contactUs.html')


def soil1(request):
    return render(request, 'Soil_lab.html')


def soil2(request):
    return render(request, 'Soil_lab2.html')


def soil3(request):
    return render(request, 'Soil_lab3.html')


def soil4(request):
    return render(request, 'Soil_lab4.html')


def seed1(request):
    return render(request, 'sdealer.html')


def seed2(request):
    return render(request, 'sdealer2.html')


def seed3(request):
    return render(request, 'sdealer3.html')


def seedvar(request):
    return render(request, 'svar.html')


def fert1(request):
    return render(request, 'fert.html')


def fert2(request):
    return render(request, 'fert2.html')


def fert3(request):
    return render(request, 'fert3.html')


def vert1(request):
    return render(request, 'veternity1.html')


def vert2(request):
    return render(request, 'v2.html')


def vert3(request):
    return render(request, 'v3.html')


def vert4(request):
    return render(request, 'v4.html')


def symdisease(request):
    return render(request, 'symdiseases.html')


def sd2(request):
    return render(request, 'sd2.html')


def sd3(request):
    return render(request, 'sd3.html')


def sd4(request):
    return render(request, 'sd4.html')

def farmersignin(request):
    email = request.POST.get('email')
    PW = request.POST.get('pass')
    print(type(PW))
    # PWek = str('ek'+PW)
    try:
        user = authe.sign_in_with_email_and_password(email,PW)
        # print(user)
        return render(request, "AddItem1.html")
    except:
        mes = "Invalid Credentials"
        print(mes)
        return render(request, "index.html")


def selling(request):
    curuser = authe.current_user
    if curuser:
        return render(request, 'AddItem1.html')
    else:
        return render(request, 'farmlogin.html')


def additem(request):
    lettersD = string.digits
    oid = (''.join(random.choice(lettersD) for i in range(3)))
    curuser = authe.current_user
    vname = request.POST.get('Item Name')
    vprice = request.POST.get('price')
    vquant = request.POST.get('Quantity')
    # img = request.POST.get('filename')
    # print(img)
    url = request.POST.get('url')
    print(url)
    farmid = curuser['localId']
    orderid = vname[0: 3] + oid

    productdata = {
        'Product name': vname,
        'Price(kg)': vprice,
        'Quantity(Max)': vquant,
        'url': url,
    }
    database.child('Added Items').child(farmid).child(orderid).set(productdata)
    # data = database.child('Added Items').child('Details').child(farmid).get().val()
    # print(data)
    imgurl = database.child('Added Items').child(farmid).child(orderid).child('url').get().val()
    print(imgurl)
    return render(request, "AddItem1.html",{'i':imgurl})


def cart(request):
    return render(request, 'cart.html')
