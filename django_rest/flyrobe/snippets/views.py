from django.shortcuts import render

from snippets.models import Snippets 
from snippets.serializers import SnippetSerializer

# Create your views here.


from rest_framework import generics

from rest_framework import	 viewsets


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# class SnippetsList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippets.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ------------------------------------------------------------------------------------------------------------------
# class SnippetsList(generics.ListCreateAPIView):
# 	queryset=Snippets.objects.all()
# 	serializer_class=SnippetSerializer



# class SnippetsDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset=Snippets.objects.all()
# 	serializer_class=SnippetSerializer


# -----------------------------------------------------------------------------------------------------------------------
class SnippetViewSet(viewsets.ModelViewSet):
	queryset=Snippets.objects.all()
	serializer_class=SnippetSerializer
