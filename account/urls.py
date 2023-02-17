from django.urls import path
from .views import register,UserloginView, logout,ActivateAccountView
from account.views import ResetPasswordView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns =[
    path('register/', register.as_view(), name = 'register' ),
    path('login/', UserloginView.as_view(), name ='login'),
    path('activate/<str:uidb64>/<str:token>/', ActivateAccountView.as_view(), name ='activate' ),
    path('logout/', logout, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]