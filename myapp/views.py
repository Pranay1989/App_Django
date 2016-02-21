from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post
import datetime


def retrieve(request):
    id = eval("request." + request.method + "['_id']")
    post = Post.objects(id='_id')[0]
    
    if request.method == 'POST':
        return render_to_response(template, params, context_instance=RequestContext(post.first_name))
    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['_id']")

    if request.method == 'POST':
        post = Post.objects(id='_id')[0]
        post.delete() 
        template = 'index.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        params = { '_id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))


def add(request):
    if request.method == 'POST':
        # insert field values and save to mongo
        post.id = request.POST['_id']
        post.full_name = request.POST['full_name']
        post.phone_number = request.POST['phone_number']
        post.email = request.POST['email']
        post.save()
        params = {'Posts': Post.objects} 

    elif request.method == 'GET':
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))


