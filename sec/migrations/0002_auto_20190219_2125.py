# Generated by Django 2.1.7 on 2019-02-19 21:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lifeuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='lifeuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                       to=settings.AUTH_USER_MODEL),
        ),
    ]
