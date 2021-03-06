# Generated by Django 3.0.6 on 2020-05-24 19:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('starter', models.TextField(blank=True, null=True)),
                ('content', models.TextField()),
                ('theme', models.CharField(blank=True, choices=[('LI', 'LITERATURE'), ('FI', 'FILMS'), ('GA', 'GAMES'), ('MU', 'MUSIC'), ('NE', 'NEWS')], default='LI', max_length=2, null=True)),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2020, 5, 24, 22, 30, 58, 198592))),
                ('reading_time', models.IntegerField(blank=True, default=5, null=True)),
                ('views_amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='')),
                ('is_main', models.BooleanField(default=True)),
                ('brightness', models.PositiveSmallIntegerField(default=100)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='articles.Article')),
            ],
        ),
    ]
