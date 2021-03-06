# Generated by Django 2.1.2 on 2018-10-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, default='')),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('body', models.TextField(blank=True, default='')),
                ('image', models.ImageField(blank=True, default='', upload_to='post_images')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
