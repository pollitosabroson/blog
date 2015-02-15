from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ParseError
from taggit.models import Tag
from blog.models import *

class BlogSerilaizer(serializers.ModelSerializer):

	class Meta:
		models = Blog

class UsuarioSerilaizer(serializers.ModelSerializer):

	class Meta:
		models = Usuario