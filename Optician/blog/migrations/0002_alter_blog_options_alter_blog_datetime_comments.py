# Generated by Django 5.0.6 on 2024-06-29 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(verbose_name='datetime of tche blog cart'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Comment name')),
                ('email', models.EmailField(max_length=254, verbose_name='Comment email')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oment_of_th_blog', to='blog.blog')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
