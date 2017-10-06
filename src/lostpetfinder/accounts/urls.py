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
from accounts import views as account_view

"""
General account URLs
"""
urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^profile/$',
        TemplateView.as_view(template_name='accounts/profile.html'),
        name='profile'),
    url(r'^profile/edit$', account_view.update_profile, name='edit'),
    url(r'^profile/deactivate$', account_view.deactivate, name='deactivate'),
]

"""
Admin page URLs
"""
urlpatterns += [
    url(r'^admin/$', account_view.user_list, name='users_list'),
    url(r'^admin/users/create/$', account_view.user_create, name='user_create'),
    url(r'^admin/users/(?P<pk>\d+)/update/$', account_view.user_update, name='user_update'),
    url(r'^admin/users/(?P<pk>\d+)/delete/$', account_view.user_delete, name='user_delete'),
]

"""
Account registration URLs
"""
urlpatterns += [
    url(r'^register/$', account_view.register, name='register'),
    url(r'^account-activation-sent/$',
        TemplateView.as_view(template_name='accounts/account_activation_sent.html'),
        name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_view.activate, name='activate'),
]

"""
Password change URLs
"""
urlpatterns += [
    url(r'^password/$',
        PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        name='password_change'),
    url(r'^password/done/$',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),
]

"""
Password reset URLs
"""
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
