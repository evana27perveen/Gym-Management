from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from App_auth.models import MemberModel, AdminModel


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_trainer(user):
    return user.groups.filter(name='TRAINER').exists()


def is_member(user):
    return user.groups.filter(name='MEMBER').exists()


def index(request):
    return render(request, 'App_main/index.html')


@login_required(login_url='App_auth:login')
@user_passes_test(is_member)
def member_dashboard(request):
    profile = MemberModel.objects.get(user=request.user)
    content = {
        'profile': profile,
    }
    return render(request, 'App_main/member_dashboard.html', context=content)


@login_required(login_url='App_auth:login')
@user_passes_test(is_member)
def health_check(request):
    return render(request, 'App_main/health_check.html')


@login_required(login_url='App_auth:login')
@user_passes_test(is_member)
def diet_chart(request):
    return render(request, 'App_main/diet_chart.html')



# ------------------------------------------------member end-------------------------------------------
# ------------------------------------------------admin start-------------------------------------------

@login_required(login_url='App_auth:login')
@user_passes_test(is_admin)
def admin_dashboard(request):
    profile = AdminModel.objects.get(user=request.user)
    members = MemberModel.objects.all()
    content = {
        'profile': profile,
        'members': members.count(),
    }
    return render(request, 'App_main/admin_dashboard.html', context=content)


@login_required(login_url='App_auth:login')
@user_passes_test(is_admin)
def assign_trainers(request):
    members = MemberModel.objects.filter(my_trainer=None)
    content = {
        'members': members,
    }
    return render(request, 'App_main/assign_trainers.html', context=content)


@login_required(login_url='App_auth:login')
@user_passes_test(is_admin)
def total_members(request):
    members = MemberModel.objects.all()
    content = {
        'members': members
    }
    return render(request, 'App_main/total_members.html', context=content)
