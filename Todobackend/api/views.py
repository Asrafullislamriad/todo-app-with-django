
from django.shortcuts import render
 
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Contact
from api.serializers import ContactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics




 

class BlogList(APIView):
 
    def get(self, request, format=None):
        Contacts = Contact.objects.all()
        serializer = ContactSerializer(Contacts, many=True)
        return Response( serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class  ApiDetail(APIView):
    """
    Retrieve, update or delete a Contact instance.
    """
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Contact = self.get_object(pk)
        serializer = ContactSerializer(Contact)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Contact = self.get_object(pk)
        serializer = ContactSerializer(Contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Contact = self.get_object(pk)
        Contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)