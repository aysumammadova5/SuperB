from django.contrib.auth.views import LoginView, PasswordResetView
from .forms import RegisterForm, LoginForm
from django.utils.translation import gettext as _
from account.utils.tasks import send_confirmation_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as django_login, logout as django_logout,get_user_model
from django.contrib.auth.views import (PasswordChangeView, 
                                        PasswordResetView, 
                                        PasswordResetConfirmView, 
                                        LoginView)
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_decode
from account.utils.tokens import account_activation_token
from django.contrib import messages
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from .models import Users
from verify_email import verify_email

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')


User = get_user_model()


class UserloginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url=reverse_lazy("home")
   
    def get_success_url(self):
        return reverse_lazy("home")

    def get(self, request):
        form = self.form_class
        return render (request, self.template_name, {'form': form,})

   



class register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    

    def get_success_url(self):

        return reverse_lazy("account:login")

    def form_valid(self, form):
        result = super().form_valid(form)
        
        print(self.object)
        send_confirmation_mail(user=self.object, current_site=get_current_site(self.request))
        return result
   
   
def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('account:login'))

class ActivateAccountView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your account is activated!")
            return redirect(reverse_lazy('account:login'))
        else:
            messages.warning(request, "Something went wrong!")
            return redirect(reverse_lazy('account:login'))