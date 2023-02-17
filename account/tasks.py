
from celery import shared_task
from django.conf import settings
from blog.models import *
from core.models import Subscriber
from django.template.loader import render_to_string
from  django.core.mail import EmailMultiAlternatives
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

@shared_task(name='sw')
def send_mail_to_subscribers():
    today = datetime.date.today() + datetime.timedelta(1)
    week_ago = today - datetime.timedelta(7)
    blogs = Blog.objects.all()[0:4]
    email_list=Subscriber.objects.filter(is_active=True).values_list('email',flat=True)
    message = render_to_string('blog-list.html', {
                'posts': blogs,
            })
    subject = "Most Review Blogs"
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'html'
    mail.send()