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

from .views import RegisterView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^account/$', TemplateView.as_view(template_name='accounts/account.html'), name='account'),

    url(r'^password_change/$',
        PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
        name='password_change'),
    url(r'^password_change/done/$',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),

    url(r'^password_reset/$',
        PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'),
    url(r'^password_reset/done/$',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
