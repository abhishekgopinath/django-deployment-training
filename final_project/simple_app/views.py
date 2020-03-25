from django.shortcuts import render
from simple_app.forms import UserInfoForm, UserProfileInfoForm

# Create your views here.


def index(request):
    return render(request, 'simple_app/index.html')


def register(request):
    registered = False

    if(request.method == "POST"):
        user_info = UserInfoForm(data=request.POST)
        profile_info = UserProfileInfoForm(data=request.POST)

        if user_info.is_valid() and profile_info.is_valid():
            user = user_info.save()
            user.set_password(user.password)
            user.save()

            profile = profile_info.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print('One of the forms is not valid..Below are the error details:\n')
            print(user_info.errors, profile_info.errors)

    else:
        user_info = UserInfoForm()
        profile_info = UserProfileInfoForm()

    return render(request, 'simple_app/registration.html', {'registered': registered, 'user_form': user_info, 'profile_form': profile_info})
