from django.shortcuts import render
from .models import product
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import generics
def input(request):
    return render(request,'input.html')
def insert(request):
    pid1=int(request.GET['t1'])
    pname1=request.GET['t2']
    f=product(pid=pid1,pname=pname1)
    f.save()
    return render(request,'links.html')
def display(request):
    recs=product.objects.all()
    return render(request,'display.html',{'records':recs})
def productlist(APIView):
    def get(self,request,format=None):
        products=product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)




# Create your views here.
