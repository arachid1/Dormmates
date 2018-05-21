from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Matt Kim'

    args = {'name': name, 'numbers': numbers}
    return render(request, 'accounts/login.html', args)
