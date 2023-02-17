from django.db.models.signals import pre_save, post_save, m2m_changed
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from blog.models import Blog


# @receiver(pre_save, sender = Blog)
# def my_callback(sender, instance, *args, **kwargs):
#     instance.slug_az = slugify(instance.title_az)
#     instance.slug_en = slugify(instance.title_en)


@receiver(post_save, sender = Blog)
def my_callback(sender, instance ,*args, **kwargs):
   slug=slugify(instance.title) + '-' + str(instance.id)
   if not slug == instance.slug:
     instance.slug = slug
     instance.save()
   
   