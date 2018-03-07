from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User
import bcrypt



def index(request):
	
	return render(request, 'login/index.html')

def registration(request):
	errors = User.objects.validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect(index) 

	hashed = bcrypt.hashpw((request.POST['password'].encode()), bcrypt.gensalt(5))

	user = User.objects.create(
		name = request.POST['name'],
		alias = request.POST['alias'],
		email = request.POST['email'],
		bday = reques.POST['bday'],
		password = hashed,
		)
		
	request.session['user_id'] = user.id

	return redirect(success)

def login(request):
	
	result = User.objects.validate_login(request.POST)
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect('/')
	request.session['user_id'] = result.id
	messages.success(request, "Successfully logged in!")
	return redirect(success)

def success(request):
	user = User.objects.get(id=request.session['user_id'])
	friends = User.objects.get(id = user.id).friends.all()
	strangers = User.objects.exclude(friends = user)
	context = { 
		'user': user,
		'friends': friends,
		'strangers': strangers
	}
	return render(request, 'login/success.html', context)

def addfriend(request, number):
	user = User.objects.get(id = request.session['user_id'])
	friend = User.objects.get(id = number)
	user.friends.add(friend)
	print friend.friends
	return redirect(success)

def show(request, number):
	user = User.objects.get(id = number)
	context = {'user': user}
	return render(request, 'login/show.html', context)

def logout(request):
	del request.session['user_id']
	return redirect('/')

def unfriend(request, number):
	user = User.objects.get(id = request.session['user_id'])
	oldfriend = User.objects.get(id = number)
	user.friends.remove(oldfriend)
	return redirect(success)
