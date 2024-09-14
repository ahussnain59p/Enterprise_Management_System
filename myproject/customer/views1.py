from django.http import JsonResponse
from .models import CustomerInfo,CustomerEnquiry
from .serializers import CinfoSerializer,CenqSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Template, Context
@api_view(["POST"])
def Send_mail(request):
    if request.method == "POST":
        dynamic_value = request.data.get('dynamic_value')  
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Email Template</title>
        </head>
        <body>
            <h2>Hello!</h2>
            <p>This is a sample email content constructed dynamically.</p>
            <p>You can include dynamic content here:</p>
            <p>Dynamic Value: {dynamic_value}</p>
            <p>Feel free to customize this template according to your needs.</p>
        </body>
        </html>
        """
        template = Template(html_content)
        context = Context({'context_variable': dynamic_value})
        html_message = template.render(context)
        plain_message = strip_tags(html_message)
        subject = 'Subject Example'
        from_email = 'ahussnain67h@gmail.com'
        recipient_list = ['aligroup70@gmail.com']
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
        return Response({'message': 'Email sent successfully'})
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "POST", "PUT", "DELETE"])
def customer_info(request, id=None):
    if request.method == "POST":
        serializer = CinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        if id:
            service = CustomerInfo.objects.get(pk=id)
        else:
            service = CustomerInfo.objects.all()
    except CustomerInfo.DoesNotExist:
        if request.method in ["GET", "PUT", "DELETE"]:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CinfoSerializer(service, many=True if not id else False)
        return JsonResponse({"data": serializer.data})
    if request.method == "PUT":
        if not id:
            return Response({"detail": "ID must be provided for update."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CinfoSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        if not id:
            return Response({"detail": "ID must be provided for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     

@api_view(["GET", "POST", "PUT", "DELETE"])
def customer_enquiry(request, id=None):
    if request.method == "POST":
        serializer = CenqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        if id:
            service = CustomerEnquiry.objects.get(pk=id)
        else:
            service = CustomerEnquiry.objects.all()
    except CustomerEnquiry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        if id:
            serializer = CenqSerializer(service)
        else:
            serializer = CenqSerializer(service, many=True)
        return Response({"data": serializer.data})

    if request.method == "PUT":
        serializer = CenqSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        if id:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET", "POST", "PUT", "DELETE"])
def customer_enquiry(request, id=None):
    if request.method == "POST":
        serializer = CenqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        if id:
            service = CustomerEnquiry.objects.get(pk=id)
        else:
            service = CustomerEnquiry.objects.all()
    except CustomerEnquiry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        if id:
            serializer = CenqSerializer(service)
            return Response({"data": serializer.data})
        else:
            serializer = CenqSerializer(service, many=True)
            return Response({"data": serializer.data})
    if request.method == "PUT":
        serializer = CenqSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)