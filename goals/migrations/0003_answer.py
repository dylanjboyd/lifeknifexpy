# Generated by Django 2.1.7 on 2019-02-13 11:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goals', '0002_auto_20190213_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1),
                                                                       django.core.validators.MaxValueValidator(4)])),
                ('date', models.DateField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.Goal')),
            ],
        ),
    ]
