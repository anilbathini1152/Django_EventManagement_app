# Generated by Django 3.1.5 on 2021-02-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_isorganiser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.FloatField()),
                ('proflepic', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]
