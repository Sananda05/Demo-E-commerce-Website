from django.shortcuts import render

from .models import ProductInfo

# Create your views here.

def homePageView(request):

        if request.method == "GET":

            # product_list = ProductInfo.objects.all()
            # print(product_list)

            return render(request, "Views/HomePage/Home.html")


