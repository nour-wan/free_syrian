from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from freename.models import FreeName
from .serializer import FreeNameSerializer
from rest_framework.views import APIView

# Create your views here.
class AddView(generics.ListAPIView):  
    def post(self,request):
        serializer = FreeNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()           
            return Response({
                'message' : 'name was added successfully',
                'data' : {}
            },status=status.HTTP_200_OK)
        return Response({
                'message' : 'missing fields',
                'data' : {}
            },status=status.HTTP_400_BAD_REQUEST) 
        
        
class GetView(generics.ListAPIView):    
    def get(self,request):
        nameFree=FreeName.objects.all()
        serializer = FreeNameSerializer(nameFree,many=True)
        # print(categories)
        return Response({
            'message' : 'name get successfully',
            "data":serializer.data
            },status=status.HTTP_200_OK) 
        
        
class SearchView(generics.ListAPIView):  
    def post(self,request):
        name = request.data.get('name')
        if name:
            data1 =  FreeName.objects.filter(name__icontains=name)
            serializer = FreeNameSerializer(data1,many=True)
            return Response({
            'message' : 'name get successfully',
            "data":serializer.data
            },status=status.HTTP_200_OK) 
            
    
             
    
