from django.conf.urls import url
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from accounts.views import register, activate, update_profile, deactivate

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^profile/$',
        TemplateView.as_view(template_name='accounts/profile.html'),
        name='profile'),
    url(r'^profile/edit$', update_profile, name='edit'),
    url(r'^profile/deactivate$', deactivate, name='deactivate'),
]

urlpatterns += [
    url(r'^register/$', register, name='register'),
    url(r'^account-activation-sent/$',
        TemplateView.as_view(template_name='accounts/account_activation_sent.html'),
        name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]

urlpatterns += [
    url(r'^password/$',
        PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        name='password_change'),
    url(r'^password/done/$',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),
]

urlpatterns += [
    url(r'^reset/$',
        PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
