# Generated by Django 3.2.5 on 2021-07-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_web_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]