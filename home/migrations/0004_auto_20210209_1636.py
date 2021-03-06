# Generated by Django 3.1.5 on 2021-02-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wbusers',
            fields=[
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.FloatField()),
                ('proflepic', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'wbusers',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
