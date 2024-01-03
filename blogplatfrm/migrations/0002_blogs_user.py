# Generated by Django 5.0.1 on 2024-01-03 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogplatfrm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
