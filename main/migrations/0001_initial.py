# Generated by Django 3.1.2 on 2020-11-18 06:09

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_action', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_list', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('dead_line', models.DateField()),
                ('attachments', models.FileField(blank=True, upload_to='files/')),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(max_length=150, null=True)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.status')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(blank=True, default='taskssssss', max_length=80, null=True)),
                ('dead_line', models.DateField(blank=True, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='files/')),
                ('description', models.TextField(blank=True, default='descriptionssssssss', null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, default='admin', max_length=150, null=True)),
                ('assign', models.ManyToManyField(blank=True, default=1, null=True, to=settings.AUTH_USER_MODEL)),
                ('lists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third', to='main.list')),
                ('status', models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.status')),
            ],
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_comment', to='main.task')),
            ],
        ),
        migrations.CreateModel(
            name='SubTaskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('subtask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subtask')),
            ],
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='four', to='main.task'),
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('add_date', models.DateField(auto_now_add=True)),
                ('upd_date', models.DateField(auto_now=True)),
                ('created_by', models.CharField(max_length=150)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.status')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second', to='main.space'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/')),
                ('email', models.EmailField(max_length=254)),
                ('action', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.action')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['user'],
            },
        ),
    ]
