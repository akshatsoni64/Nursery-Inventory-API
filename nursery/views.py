from django.shortcuts import render, redirect
from django.views import View
from django.http import *
from .forms import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_details(request):
    api_urls = {
        'Available Options(Current)': '/',
        'Plants List': '/p',
        'Plant Details': '/p<int:id>',
        'Orders List': '/o',
        'Login': '/login',
        'Register': '/register',
        'Logout': '/logout'
    }
    return Response(api_urls)

class PlantViews(LoginRequiredMixin, APIView):
    login_url = '/login'
    def get(self, request, id=None):
        if id is not None:
            plant = Plant.objects.get(id = id)
            serializer = PlantSerializers(plant, many = False)
        else:
            plants = Plant.objects.all()
            serializer = PlantSerializers(plants, many = True)

        return Response(serializer.data)

    
    def post(self, request, id=None):
        form = PlantForm(request.POST or None, request.FILES or None)
        valid = form.is_valid()
        # print(valid)
        # print("\n", request.FILES)
        if valid:
            form.save()
            return Response("Plant Added Successfully")
        else:
            return Response(form.errors)

class OrderViews(LoginRequiredMixin, APIView):
    login_url = '/login'
    def get(self, request):
        usr = User.objects.get(username = request.user)
        profile = Profile.objects.get(user = usr)
        if profile.type == "customer":
            orders = Order.objects.filter(cust=profile)            
        else:
            orders = Order.objects.all()
        order_serial = OrderSerializers(orders, many = True)            
        return Response(order_serial.data)

    def post(self, request):
        context = {}
        print(request.POST)
        id = request.POST['plant_id']
        plant = Plant.objects.get(id = id)
        price = plant.price
        
        quantity = int(request.POST.get('quantity'))
        usr = User.objects.get(username=request.user)
        profile = Profile.objects.get(user=usr)
        
        if quantity <= plant.stock:
            order = Order(plant=plant, cust=profile, quantity=quantity, price=(quantity*price))
            order.save()
            stock = plant.stock - quantity
            plant.stock = stock
            plant.save()
            return Response("Order Placed Successfully")
        else:
            return Response("Required Quantity Not Available! Please Check again later!")

    def delete(self, request):
        pass

class ProfileViews(APIView):
    def get(self, request):
        return Response("POST Method Required!")

    def post(self, request):        
        profileForm = ProfileForm(request.POST)
        if profileForm.is_valid():
            user_profile_data = profileForm.save()
            user_profile_data.refresh_from_db()
            user_profile_data.profile.mobile = profileForm.cleaned_data.get('mobile')
            user_profile_data.profile.address = profileForm.cleaned_data.get('address')
            user_profile_data.profile.type = profileForm.cleaned_data.get('type')
            user_profile_data.save()
            return Response("You may login now")
        else:
            return Response(profileForm.errors)

"""
This_6464
"""
class AuthViews(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response("Already Authenticated!")
        else:
            return Response("POST Method Required!")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        context = {}
        if user is not None:
            auth.login(request, user)
            print(request.POST)
            return Response("Login Successful")
        else:
            return Response("Invalid Credentials! Please Try Again!")

def logout_view(request):
    auth.logout(request)
    return HttpResponse("You are logged out now")