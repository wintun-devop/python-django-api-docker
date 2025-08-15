from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404,render,redirect
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from .serializers import YourItemSerlizer
#from .models import YourItemModel
from ..serializers import ProductSerializer
from ..models import Product
import uuid

# Create your views here.
class ProductViews(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id=None):
        if id is not None:
            try:
                # validate uuid object
                uuid_obj = uuid.UUID(id)
                item = get_object_or_404(Product, id=uuid_obj)
                serializer = ProductSerializer(item)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"status": "error", "message": "Invalid ID on UUID format"}, status=status.HTTP_400_BAD_REQUEST)
            except Product.DoesNotExist:
                return Response({"status": "error", "message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            items = Product.objects.all()
            serializer = ProductSerializer(items, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def put(self, request, id=None):
        if id is None:
            return Response({"status": "error", "message": "Missing product ID"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            item = Product.objects.get(id=id)
            serializer = ProductSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({"status": "error", "message": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"status": "error", "message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id=None):
        item = get_object_or_404(Product, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})