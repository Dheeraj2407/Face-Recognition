# Generated by Django 2.2.4 on 2020-05-23 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('faceapp', '0016_teacherclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('classRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faceapp.ClassRoom')),
            ],
        ),
    ]
