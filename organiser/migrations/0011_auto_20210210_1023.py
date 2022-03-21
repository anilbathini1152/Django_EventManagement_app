# Generated by Django 3.1.5 on 2021-02-10 04:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0010_evntregistrations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evntregistrations',
            name='regid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]