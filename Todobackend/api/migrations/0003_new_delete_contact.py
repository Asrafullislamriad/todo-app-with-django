# Generated by Django 4.2.9 on 2024-01-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
