# Generated by Django 5.0.6 on 2024-06-01 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('musician', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='musicians.musicianmodel')),
            ],
        ),
    ]
