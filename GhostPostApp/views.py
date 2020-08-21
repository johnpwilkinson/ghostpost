from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import AddPostForm
from .models import Posts
from django.contrib import messages 
# Create your views here.
def index(request):
    posts = Posts.objects.order_by('-submission_time')
    return render(request, 'index.html', {'posts': posts})

def roasts(request):
    roasts = Posts.objects.filter(boast_or_roast=True).order_by('-submission_time')
    return render(request, 'index.html', {'posts': roasts})
def boasts(request):
    boasts = Posts.objects.filter(boast_or_roast=False).order_by('-submission_time')
    return render(request, 'index.html', {'posts': boasts})

def top_posts(request):
    posts = sorted(Posts.objects.all(), key=lambda m: m.total_votes, reverse=True)
    return render(request, 'index.html', {'posts': posts})

def post(request):

    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                new_post = Posts.objects.create(
                    post_content=data.get('post'),
                    boast_or_roast=data.get('boast_or_roast'),
    
                )
                messages.info(request, f'Secret Link : http://localhost:8000/private/{new_post.secret}')
                return HttpResponseRedirect(reverse('homepage'))
               
    form = AddPostForm()
    return render(request, 'post.html', {'form': form} )

def upvote(request, post_id):
    post = Posts.objects.get(pk=post_id)
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def downvote(request, post_id):
    post = Posts.objects.get(pk=post_id)
    post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def public(request, post_id):
    post = Posts.objects.filter(id=post_id)
    return render(request, 'index.html', {'posts': post})

def private(request, secret):
    post = Posts.objects.filter(secret=secret)
    return render(request, 'index.html', {'posts': post, 'private':True })

def delete(request, secret):
    post = Posts.objects.get(secret=secret)
    post.delete()
    return HttpResponseRedirect(reverse('homepage'))
