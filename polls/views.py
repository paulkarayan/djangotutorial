from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Hello, bros. you at the poll index")

def detail(request, poll_id):
	return HttpResponse("poll %s" % poll_id)

def results(request, poll_id):
	return HttpResponse("result of poll %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("voting on poll %s" % poll_id)		