from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response



class Productcrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PSD=ProductSerializer(PQS,many=True)
        return Response(PSD.data)
    
    def post(self,request,id):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'Product is Created'})
        return Response({'failed':'Product is failed'})
    
    def put(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'Product is updated'})
        return Response({'failed':'Product is not updated'})

    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PO.Pnmae=request.data['Pname']
        PO.save()
        return Response({'success':'Data is partially updated'})
    
    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'success':'product is delted'})