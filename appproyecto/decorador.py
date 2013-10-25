#coding=utf-8
from functools import wraps
from django.utils.timezone import utc

def get_user_lazy(func):
	from django.contrib.auth import get_user
	def _wrap(request, *args, **kwargs):
		request.user = get_user(request)
		return func(request, *args, **kwargs)
	return _wrap
