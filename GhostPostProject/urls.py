"""GhostPostProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GhostPostApp.views import index, post, roasts, boasts, upvote, downvote, public, private, delete, top_posts
urlpatterns = [
    path('', index, name='homepage'),
    path('post/', post, name='post'),
    path('roasts/', roasts, name='roasts'),
    path('boasts/', boasts, name='boasts'),
    path('top/', top_posts, name='topposts'),
    path('upvote/<int:post_id>', upvote, name='upvote' ),
    path('delete/<slug:secret>', delete, name='delete'),
    path('downvote/<int:post_id>', downvote, name='downvote' ),
    path('public/<int:post_id>', public, name='public'),
    path('private/<slug:secret>', private, name='private'),
    path('admin/', admin.site.urls),
]
