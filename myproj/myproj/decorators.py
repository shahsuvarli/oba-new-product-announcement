from django.http import HttpResponse
from django.shortcuts import redirect


# Just to make sure that if you are logged in, you cannot visit login and register views
def unauthenticated_user(view_func):
	def wrapper(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper


# only allowed user may get to this page
def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request, *args, *kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper
	return decorator


# pages where only admins have access
def admins_only(view_func):
	def wrapper(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('home')

		if group == 'admin':
			return view_func(request, *args, **kwargs)
	return wrapper








