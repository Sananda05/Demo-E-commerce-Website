from django.shortcuts import redirect, render

# from .models import ProductInfo

# Create your views here.

def homePageView(request):

    if request.session.get('check') == 'okay':

        if request.method == "GET":

            # product_list = ProductInfo.objects.all()
            # print(product_list)

            return render(request, "Views/HomePage/Home.html")
    else:
        print(request.session.get('check'))
        return redirect("/")        


