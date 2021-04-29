from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from cakes_user.serializers import  UserDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cakesdata.models import *
from cakes_user.models import UserDetails
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView

#
# class AddToCart(APIView):
#
#
#     def post(self,request,pk):

