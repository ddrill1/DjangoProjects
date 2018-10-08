from django.shortcuts import render
#from d2App.models import User
from d2App.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request, 'd2App/index.html')

def users(request):
    f = NewUserForm()

    if request.method == 'POST':
        f = NewUserForm(request.POST)

        if f.is_valid():
            f.save(commit=True)
            return index(request)
        else:
            print('NO!')

    return render(request, 'd2App/users.html', {'f':f})
