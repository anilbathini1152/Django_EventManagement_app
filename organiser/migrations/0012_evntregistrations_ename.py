# Generated by Django 3.1.5 on 2021-02-11 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0011_auto_20210210_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='evntregistrations',
            name='ename',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
