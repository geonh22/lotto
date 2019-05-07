from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):
    number_list = list()
    for i in range(0,6):
        number = request.GET['number'+str(i+1)]
        if number =='':
            return redirect('home')
        