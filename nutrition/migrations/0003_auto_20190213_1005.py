# Generated by Django 2.1.7 on 2019-02-13 10:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nutrition', '0002_auto_20190213_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together={('name', 'owner')},
        ),
    ]