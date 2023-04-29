from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate= 0.15
def index(request):
    return HttpResponse("this is a site to calculate tax.")
def calc_tax(request , number):
    num_tax = float(number)*(1+tax_rate)
    return HttpResponse(f"the total is {num_tax}")
def tax_rate_view(request):
    return render(request,'tax_rate.html',{'tax_rate': tax_rate})