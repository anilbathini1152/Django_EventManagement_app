# Generated by Django 3.1.5 on 2021-02-03 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IsOrganiser',
            fields=[
                ('id', models.FloatField(primary_key=True, serialize=False)),
                ('status', models.FloatField()),
            ],
            options={
                'db_table': 'is_organiser',
                'managed': True,
            },
        ),
    ]
