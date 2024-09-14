from django.http import JsonResponse
from .models import EmployeeInfo,ManufactureInfo,SaleInfo
from .serializers import EmployeeSerializer,ManufactureSerializer,SaleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST", "PUT", "DELETE"])
def employee_view(request, id=None):
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        if id:
            service = EmployeeInfo.objects.get(pk=id)
        else:
            service = EmployeeInfo.objects.all()
    except EmployeeInfo.DoesNotExist:
        if id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if id:
            serializer = EmployeeSerializer(service)
        else:
            serializer = EmployeeSerializer(service, many=True)
        return Response({"data": serializer.data})

    if request.method == "PUT":
        if not id:
            return Response({'error': 'ID must be provided for update'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = EmployeeSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        if not id:
            return Response({'error': 'ID must be provided for delete'}, status=status.HTTP_400_BAD_REQUEST)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)














@api_view(["GET", "POST", "PUT", "DELETE"])
def manufacture_view(request, id=None):
    if request.method == "POST":
        serializer = ManufactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        if id:
            service = ManufactureInfo.objects.get(pk=id)
        else:
            service = ManufactureInfo.objects.all()
    except ManufactureInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if id:
            serializer = ManufactureSerializer(service)
        else:
            serializer = ManufactureSerializer(service, many=True)
        return Response({"data": serializer.data})

    if request.method == "PUT":
        if not id:
            return Response({'error': 'ID must be provided for update'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ManufactureSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        if not id:
            return Response({'error': 'ID must be provided for delete'}, status=status.HTTP_400_BAD_REQUEST)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST", "PUT", "DELETE"])
def sale_view(request, id=None):
    if request.method == "POST":
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle GET, PUT, DELETE methods
    try:
        if id:
            service = SaleInfo.objects.get(pk=id)
        else:
            service = SaleInfo.objects.all()
    except SaleInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if id:
            serializer = SaleSerializer(service)
        else:
            serializer = SaleSerializer(service, many=True)
        return Response({"data": serializer.data})

    if request.method == "PUT":
        if not id:
            return Response({'error': 'ID must be provided for update'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SaleSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        if not id:
            return Response({'error': 'ID must be provided for delete'}, status=status.HTTP_400_BAD_REQUEST)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
 
# Create your views here.
