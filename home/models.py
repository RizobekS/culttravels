from ckeditor_uploader.fields import RichTextUploadingField
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import FileField
from django.utils import timezone
from django_resized import ResizedImageField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError("Telefon raqam yozilish kerak!")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.CharField(blank=False, null=False, max_length=600)
    phone = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if 80 > len(self.password):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class FAQ(models.Model):
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    question_en = models.TextField(blank=True, null=True)
    question_uz = models.TextField(blank=True, null=True)
    question_ru = models.TextField(blank=True, null=True)

    answer_en = models.TextField(blank=True, null=True)
    answer_uz = models.TextField(blank=True, null=True)
    answer_ru = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_en


class Tours(models.Model):
    class Meta:
        verbose_name = 'Tours'
        verbose_name_plural = 'Tours'

    title_en = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_uz = models.CharField(max_length=255, null=True)

    description_en = RichTextUploadingField(null=True, blank=True)
    description_ru = RichTextUploadingField(null=True, blank=True)
    description_uz = RichTextUploadingField(null=True)

    value = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True,
                                validators=[MinValueValidator(0), MaxValueValidator(999999999)])

    date = models.DateField(null=True)

    views = models.IntegerField(default=0, null=True, blank=True)

    image = ResizedImageField(upload_to='tours/images/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                              null=True, blank=True, quality=65, force_format='JPEG')

    image_uz = ResizedImageField(upload_to='tours/images/',
                                 validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                                 null=True, blank=True, quality=65, force_format='JPEG')

    image_ru = ResizedImageField(upload_to='tours/images/',
                                 validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                                 null=True, blank=True, quality=65, force_format='JPEG')

    video_title = models.CharField(max_length=255, null=True, blank=True)
    video = FileField(upload_to='tours/videos/',
                      validators=[
                          FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                      null=True, blank=True)

    video_title_uz = models.CharField(max_length=255, null=True, blank=True)
    video_uz = FileField(upload_to='tours/videos/',
                         validators=[
                             FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                         null=True, blank=True)

    video_title_ru = models.CharField(max_length=255, null=True, blank=True)
    video_ru = FileField(upload_to='tours/videos/',
                         validators=[
                             FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                         null=True, blank=True)

    extra_img_one = ResizedImageField(upload_to='tours/extra/images',
                                      validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                      null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_two = ResizedImageField(upload_to='tours/extra/images',
                                      validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                      null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_three = ResizedImageField(upload_to='tours/extra/images',
                                        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                        null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_four = ResizedImageField(upload_to='tours/extra/images',
                                       validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                       null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_five = ResizedImageField(upload_to='tours/extra/images',
                                       validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                       null=True, blank=True, quality=65, force_format='JPEG')

    english = models.BooleanField(blank=True, default=1)

    russian = models.BooleanField(blank=True, default=1)

    uzbek = models.BooleanField(blank=True, default=1)

    def __str__(self):
        return self.title_ru


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    message = models.CharField(max_length=1000, blank=True)
    received_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # for moderator
    reply_subject = models.CharField(max_length=255, blank=True, null=True)
    reply_message = models.CharField(max_length=1000, blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.reply_subject and self.reply_message:
            self.replied_date = timezone.now()
            send_mail(self.reply_subject, self.reply_message, EMAIL_HOST_USER, [self.email], fail_silently=False)
            super(Contact, self).save()
        else:
            super(Contact, self).save()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    class Meta:
        verbose_name = "Reservations"
        verbose_name_plural = "Reservation"

    tours = models.ForeignKey(Tours, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    message = models.CharField(max_length=1000, blank=True)
    received_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # for moderator
    reply_subject = models.CharField(max_length=255, blank=True, null=True)
    reply_message = models.CharField(max_length=1000, blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.reply_subject and self.reply_message:
            self.replied_date = timezone.now()
            send_mail(self.reply_subject, self.reply_message, EMAIL_HOST_USER, [self.email], fail_silently=False)
            super(Reservation, self).save()
        else:
            super(Reservation, self).save()

    def __str__(self):
        return self.name


class MyTours(models.Model):
    PAYMENT_STATUS = (
        ("new", "Yangi"),
        ("paid", "To'landi"),
        ("canceled", "Bekor qilindi")
    )

    PAYMENT_TYPE = (
        ('payme', 'Payme'),
        ('click', 'Click')
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title_en = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_uz = models.CharField(max_length=255, null=True)

    description_en = RichTextUploadingField(null=True, blank=True)
    description_ru = RichTextUploadingField(null=True, blank=True)
    description_uz = RichTextUploadingField(null=True)

    value = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True,
                                validators=[MinValueValidator(0), MaxValueValidator(999999999)])

    image = ResizedImageField(upload_to='tours/images/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                              null=True, blank=True, quality=65, force_format='JPEG')

    image_uz = ResizedImageField(upload_to='tours/images/',
                                 validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                                 null=True, blank=True, quality=65, force_format='JPEG')

    image_ru = ResizedImageField(upload_to='tours/images/',
                                 validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                                 null=True, blank=True, quality=65, force_format='JPEG')

    video_title = models.CharField(max_length=255, null=True, blank=True)
    video = FileField(upload_to='tours/videos/',
                      validators=[
                          FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                      null=True, blank=True)

    video_title_uz = models.CharField(max_length=255, null=True, blank=True)
    video_uz = FileField(upload_to='tours/videos/',
                         validators=[
                             FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                         null=True, blank=True)

    video_title_ru = models.CharField(max_length=255, null=True, blank=True)
    video_ru = FileField(upload_to='tours/videos/',
                         validators=[
                             FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                         null=True, blank=True)

    extra_img_one = ResizedImageField(upload_to='tours/extra/images',
                                      validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                      null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_two = ResizedImageField(upload_to='tours/extra/images',
                                      validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                      null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_three = ResizedImageField(upload_to='tours/extra/images',
                                        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                        null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_four = ResizedImageField(upload_to='tours/extra/images',
                                       validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                       null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_five = ResizedImageField(upload_to='tours/extra/images',
                                       validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                       null=True, blank=True, quality=65, force_format='JPEG')

    english = models.BooleanField(blank=True, default=1)

    russian = models.BooleanField(blank=True, default=1)

    uzbek = models.BooleanField(blank=True, default=1)

    total_price = models.CharField(max_length=300)
    payment_status = models.CharField(max_length=300, choices=PAYMENT_STATUS)
    payment_type = models.CharField(max_length=300, choices=PAYMENT_TYPE)
    payment_time = models.TimeField(auto_now_add=True)
    payment_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'My Tours'
        verbose_name_plural = 'My Tours'

    def __str__(self):
        return self.title_ru
