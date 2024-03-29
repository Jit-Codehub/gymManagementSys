from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    validity_days=models.IntegerField(null=True)

    def __str__(self):
        return self.title


class SubPlanFeature(models.Model):
    subplan = models.ManyToManyField(SubPlan)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PlanDiscount(models.Model):
    subPlan = models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
    total_months = models.IntegerField()
    total_discount = models.IntegerField()

    def __str__(self):
        return str(self.total_months)



class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=150)
    address = models.TextField()
    img=models.ImageField(upload_to="subs/")

    def __str__(self):
        return str(self.user)

    def image_tag(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="80"')
        else:
            return 'no-image'


@receiver(post_save, sender=User)
def create_subscriber(sender, instance, created, **kwargs):
    if created:
        Subscriber.objects.create(user=instance)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubPlan, on_delete=models.CASCADE)
    price = models.CharField(max_length=150)
    reg_date = models.DateField(auto_now_add=True, null=True)



class Trainer(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,null=True)
    pwd = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=100)
    address = models.TextField()
    is_active = models.BooleanField(default=False)
    detail = models.TextField()
    img=models.ImageField(upload_to="trainers/")
    facebook = models.CharField(max_length=100,null=True)
    twitter = models.CharField(max_length=100,null=True)
    youtube = models.CharField(max_length=100,null=True)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

    def image_tag(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="80"')
        else:
            return 'no-image'


class Notify(models.Model):
    notify_detail = models.CharField(max_length=100)
    read_by_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    read_by_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.notify_detail



class AssignSubscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)



class TrainerSalary(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    amt=models.IntegerField()
    amt_date=models.DateField()
    remarks=models.TextField(blank=True)

    class Meta:
        verbose_name_plural='Trainer Salary'

    def __str__(self):
        return str(self.trainer.full_name)
  


