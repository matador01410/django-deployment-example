from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app.forms import NewUserForms
# Create your views here.

def index(requset):
    webpages_list = AccessRecord.objects.order_by('date')
    access_record_dict = {'access_records': webpages_list}
    # for_insert = {'insert_me' : 'Test!'}
    return render(requset, 'first_app/index.html', context=access_record_dict)
    # return HttpResponse("Hello World!")

def users(request):
    users_list = User.objects.order_by('last_name')
    users_dict = {'users': users_list}
    return render(request, 'first_app/users.html', context=users_dict)


def signup(request):
    form = NewUserForms
    if request.method == 'POST':
        form = NewUserForms(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'first_app/signup.html', {'form': form})
