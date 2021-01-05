from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
    file_path = f"blog/{str(instance.author.id)}/{str(instance.title)}-{filename}"
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=2500, null=False, blank=False)
    image = models.ImageField(
        upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(
        auto_now_add=True, verbose_name="date_updated")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # link to account model
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

# create slug for blog before passing


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)
