from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

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
    Activate new user account
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True # activate user
        user.profile.email_confirmed = True
        user.save()
        login(request, user) # automatically login activated user
        return redirect('pets:list') # Redirect to User's pets list
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
