from django.http import JsonResponse
from .models import FinishedProduct,RawMaterial
from .serializers import FinishSerializer,RawmatSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# format=none>
@api_view(["GET", "POST", "PUT", "DELETE"])
def Finished_view(request, id=None):
    if request.method == "POST":
        serializer = FinishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        if id:
            service = FinishedProduct.objects.get(pk=id)
        else:
            service = FinishedProduct.objects.all()
    except FinishedProduct.DoesNotExist:
        if request.method in ["GET", "PUT", "DELETE"]:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        if id:
            serializer = FinishSerializer(service)
        else:
            serializer = FinishSerializer(service, many=True)
        return JsonResponse({"data": serializer.data})

    if request.method == "PUT":
        serializer = FinishSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     



@api_view(["GET", "POST", "PUT", "DELETE"])
def raw_view(request, id=None):
    if request.method == "POST":
        serializer = RawmatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        if id:
            service = RawMaterial.objects.get(pk=id)
        else:
            service = RawMaterial.objects.all()
    except RawMaterial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = RawmatSerializer(service, many=True if not id else False)
        return JsonResponse({"data": serializer.data})

    if request.method == "PUT":
        serializer = RawmatSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.