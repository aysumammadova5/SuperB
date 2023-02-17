# django_celery/celery.py

import os
from celery import Celery
from django.conf import settings

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
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperB.settings")
app = Celery("SuperB")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
@shared_task()
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

# celery -A pavshop beat -l info -S django




# command1
# celery -A pavshop worker --pool=solo -l info

# command2
#  celery -A pavshop beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler