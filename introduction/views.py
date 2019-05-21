from django.shortcuts import render

# Create your views here.

def introduction(request):
    return render(request, 'lion_first/introduction.html')