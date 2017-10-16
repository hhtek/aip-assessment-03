"""
Django's views definintions used to handle functions of the account application
such as login, account registration, password reset, etc.
"""
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.forms import UserRegisterForm, ProfileForm, UserForm
from accounts.tokens import account_activation_token
from accounts.models import Profile



def register(request):
    """
    Register a new user
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False # disable account
            user.save()
            current_site = get_current_site(request)
            subject = 'Lost Pet Finder - Activate your account now!'
            message = render_to_string('accounts/account_activation_email.html', {
                'protocol': request.is_secure() and 'https' or 'http',
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def activate(request, uidb64, token):
    """
    Activate new user account after user click on the activation link sent to
    their reigistered email address.
        If the activation link is correct, logout current user, and
            redirect to login page: GET /account/login/.
        If the activation link is invalid, display activation failed message.
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and not user.is_active and \
        account_activation_token.check_token(user, token):
        user.is_active = True # activate user
        user.save()
        logout(request) # automatically logout current user.
        return redirect('login') # redirect to login page
    else:
        return render(request, 'accounts/account_activation_invalid.html')

@login_required
def update_profile(request):
    """
    Update user profile such as name, email, mobile#, etc.
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'accounts/profile_edit.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
        })

@login_required
def deactivate(request):
    """
    Deactivate an user account
    """
    if request.method=='POST':
        request.user.delete()
        return redirect('home')

    return render(request,
        template_name='accounts/account_confirm_deactivate.html')

@login_required(login_url='/account/login/')
def user_list(request):
    """
    Display list of users for amin page.
    Only super user have access to this users list view.
    """
    if request.user.is_superuser:
        user_list = User.objects.all().order_by('pk')
        paginator = Paginator(user_list, 10) # show 10 users per page

        page = request.GET.get('page') # get current page# e.g. GET /account/admin/?page=1
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            users = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            users = paginator.page(paginator.num_pages)

        return render(request, 'accounts/admin_user_list.html', {'users': users})
    return redirect('pets:list')

def save_user_form(request, form, template_name):
    """
    User update function to save the form data executed by super user.
    Usage: admin page
    """
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            users = User.objects.all()
            data['html_user_list'] = render_to_string('accounts/admin_partial_user_list.html', {
                'users': users
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='/account/login/')
def user_create(request):
    """
    User creation function view for admin page
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm
    return save_user_form(request, form, 'accounts/admin_partial_user_create.html')

@login_required(login_url='/account/login/')
def user_update(request, pk):
    """
    User updation function view for admin page
    """
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
    else:
        form = UserForm(instance=user)
    return save_user_form(request, form, 'accounts/admin_partial_user_update.html')

@login_required(login_url='/account/login/')
def user_delete(request, pk):
    """
    User deletion for admin page
    """
    user = get_object_or_404(User, pk=pk)
    data = dict()
    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True
        users = User.objects.all()
        data['html_user_list'] = render_to_string('accounts/admin_partial_user_list.html', {
            'users': users
        })
    else:
        context = {'user': user}
        data['html_form'] = render_to_string('accounts/admin_partial_user_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
