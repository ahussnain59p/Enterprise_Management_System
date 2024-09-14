"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from service import views3
from customer import views1
from enterprise import views2
from stock import views4
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("chat/", include("chatapp.urls")),  # Replace 'myapp' with your app name
    # path('admin/', admin.site.urls),
    path("admin/", admin.site.urls),
    path("service/", views3.service_list),
    path("serviced/<int:id>/", views3.details),
    path("signup/", views3.Sign_up),
    path("signin/", views3.Sign_In),
    path("finishproduct/", views4.Finished_view),
    path("rawmaterial/", views4.raw_view),
    path("finishproduct/<int:id>", views4.Finished_view),
    path("rawmaterial/<int:id>", views4.raw_view),
    path("employee/", views2.employee_view),
    path("employee/<int:id>", views2.employee_view),
    path("manufacture/", views2.manufacture_view),
    path("manufacture/<int:id>", views2.manufacture_view),
    path("sale/<int:id>", views2.sale_view),
    path("sale/", views2.sale_view),
    path("customerinfo/<int:id>", views1.customer_info),
    path("customerinfo/", views1.customer_info),
    path("customer/mail", views1.Send_mail),
    path("custenquiry/<int:id>", views1.customer_enquiry),
    path("custenquiry/", views1.customer_enquiry),
]

urlpattern = format_suffix_patterns(urlpatterns)
