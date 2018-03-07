# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):
	def validate_login(self, post_data):
		errors = []
		if len(self.filter(email=post_data['email'])) > 0:
			user = self.filter(email=post_data['email'])[0]
			if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
				errors.append('Password incorrect')
				return errors
		else:
			errors.append('Email incorrect')	
		if errors:
			return errors
		return user

	def validator(self, postData):
		errors = {}
		if len(postData['name']) < 2:
			errors['name'] = "Name too Short Homie!"
		if not re.match(EMAIL_REGEX, postData['email']):
			errors['email'] = "Email is janky!"
		if len(postData['password']) < 2:
			errors['password'] = "Password too short Homie!"
		if postData['password'] != postData['password2']:
			errors['password2'] = "Password doesn't match Homie!"			
		return errors
		

class User(models.Model):
	name = models.CharField(max_length = 255)
	alias = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	friends = models.ManyToManyField("self", blank = True)
	bday = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()

	def __unicode__(self):
		return 'id: {}, name: {}, alias: {}, email: {}, password: {}, friends: {}'.format(self.id, self.name, self.alias, self.email, self.password, self.friends)