# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('preview', models.TextField()),
                ('body', models.TextField()),
                ('imagen', models.ImageField(upload_to=b'Blogfiles')),
                ('personal', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('face', models.TextField(null=True, blank=True)),
                ('twitter', models.TextField(null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('imagen', models.ImageField(upload_to=b'perfilfile')),
                ('User', models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(related_name='creator', to='blog.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
