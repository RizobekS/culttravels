# Generated by Django 4.1.4 on 2022-12-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_mytours_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytours',
            name='date',
        ),
        migrations.RemoveField(
            model_name='mytours',
            name='views',
        ),
        migrations.AddField(
            model_name='mytours',
            name='payment_type',
            field=models.CharField(choices=[('payme', 'Payme'), ('click', 'Click')], default='payme', max_length=300),
            preserve_default=False,
        ),
    ]
