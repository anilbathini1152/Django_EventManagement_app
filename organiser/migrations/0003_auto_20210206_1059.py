# Generated by Django 3.1.5 on 2021-02-06 05:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0002_auto_20210206_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='evntid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
