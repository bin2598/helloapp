from django.shortcuts import render

def home(request):
    return render(request,'hi.html')
def about(request):
    return render(request,'hii.html')


# Create your views here.
