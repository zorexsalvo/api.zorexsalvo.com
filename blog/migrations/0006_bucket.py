# Generated by Django 2.0.1 on 2018-03-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('date_created', models.DateField()),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
