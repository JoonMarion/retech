from django.shortcuts import render


# Create your views here.
#  view para home
def home(request):
    return render(request, 'index.html')
