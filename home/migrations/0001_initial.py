# Generated by Django 4.1.4 on 2022-12-29 11:18

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(max_length=600)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('message', models.CharField(blank=True, max_length=1000)),
                ('received_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('reply_subject', models.CharField(blank=True, max_length=255, null=True)),
                ('reply_message', models.CharField(blank=True, max_length=1000, null=True)),
                ('replied_date', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_en', models.TextField(blank=True, null=True)),
                ('question_uz', models.TextField(blank=True, null=True)),
                ('question_ru', models.TextField(blank=True, null=True)),
                ('answer_en', models.TextField(blank=True, null=True)),
                ('answer_uz', models.TextField(blank=True, null=True)),
                ('answer_ru', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999999)])),
                ('date', models.DateField(null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])])),
                ('image_uz', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])])),
                ('image_ru', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])])),
                ('video_title', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='tours/videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])])),
                ('video_title_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('video_uz', models.FileField(blank=True, null=True, upload_to='tours/videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])])),
                ('video_title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('video_ru', models.FileField(blank=True, null=True, upload_to='tours/videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])])),
                ('extra_img_one', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/extra/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])),
                ('extra_img_two', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/extra/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])),
                ('extra_img_three', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/extra/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])),
                ('extra_img_four', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/extra/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])),
                ('extra_img_five', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=65, scale=None, size=[1920, 1080], upload_to='tours/extra/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])),
                ('english', models.BooleanField(blank=True, default=1)),
                ('russian', models.BooleanField(blank=True, default=1)),
                ('uzbek', models.BooleanField(blank=True, default=1)),
            ],
            options={
                'verbose_name': 'Tours',
                'verbose_name_plural': 'Tours',
            },
        ),
        migrations.CreateModel(
            name='MyTours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mytour', to='home.tours')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'My Tours',
                'verbose_name_plural': 'My Tours',
            },
        ),
    ]
