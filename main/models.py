from django.db import models
from django.utils.html import mark_safe

class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img=models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="80"')
   


class Banners(models.Model):
    img=models.ImageField(upload_to="banners/")
    alt_text=models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="80"')


class Pages(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()

    def __str__(self):
        return self.title


class Faq(models.Model):
    quest = models.CharField(max_length=200)
    ans = models.TextField()

    def __str__(self):
        return self.quest


class Enquiry(models.Model):
    full_name=models.CharField(max_length=100)
    email = models.EmailField()
    detail = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img=models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="80"')

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=150)
    img=models.ImageField(upload_to="gallery_imgs/")

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="80"')


class SubPlan(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    max_member = models.IntegerField(null=True)
    highlight_status=models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title


class SubPlanFeature(models.Model):
    subplan = models.ManyToManyField(SubPlan)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


