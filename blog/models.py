from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Usuario(models.Model):
    # TODO: Define fields here

    User = models.ForeignKey(User,null=False, blank=False, related_name='creator')
    name = models.TextField(null=True, blank=True)
    face = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to = 'perfilfile', null=False, blank=False)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __unicode__(self):
        return u'%s' % self.name


    # TODO: Define custom methods here



class Blog(models.Model):
    # TODO: Define fields here

    author = models.ForeignKey(Usuario,null=False, blank=False, related_name='creator')
    title = models.TextField(null=False, blank=False)
    preview = models.TextField(null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    imagen = models.ImageField(upload_to = 'Blogfiles', null=False, blank=False)
    personal = models.BooleanField(default=False, blank=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __unicode__(self):
        return u'%s' % self.title

    # TODO: Define custom methods here

    