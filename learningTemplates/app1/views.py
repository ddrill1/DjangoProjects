from django.shortcuts import render

# Create your views here.
def index(request):
    contextDict = {'text':'hello', 'number':100}
    return render(request, 'app1/index.html', contextDict)

def other(request):
    return render(request, 'app1/other.html')

def relative(request):
    return render(request, 'app1/relative_url.html')
