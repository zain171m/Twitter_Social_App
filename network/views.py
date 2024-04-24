from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
import json

from .models import *


def index(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        post_text = request.POST["post_text"]
        user = User.objects.get(pk = user_id)
        
        new_post = Post(
                user = user,
                text = post_text
            )
        new_post.save()
        #posts = Post.objects.order_by('-created_at').all()
        posts = Post.objects.annotate(num_likes=models.Count('post_liked')).order_by('-created_at').all()
        paginator = Paginator(posts, 10)  # Show 10 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        like_list = []

        likes = Like.objects.all()

        try:
            for like in likes:
                if like.Liker.id == request.user.id:
                    like_list.append(like.Post_Liked.id)
        except:
            like_list = []
        
            
        
        return render(request, "network/index.html", {'posts' : posts, "page_obj": page_obj, "like_list": like_list})
    else:
        posts = Post.objects.annotate(num_likes=models.Count('post_liked')).order_by('-created_at').all()
        paginator = Paginator(posts, 10)  # Show 2 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        like_list = []

        likes = Like.objects.all()

        try:
            for like in likes:
                if like.Liker.id == request.user.id:
                    like_list.append(like.Post_Liked.id)
        except:
            like_list = []

            
        return render(request, "network/index.html", {'posts' : posts, "page_obj": page_obj, "like_list": like_list})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        picture = request.FILES["picture"]

        # Ensure password matches confirmationss
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.picture = picture
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request, user_id):
    if request.method == "POST":
        action = request.POST["action"]
        
        following_user_id = request.POST["following_user"]
        being_followed_id = user_id
        following_user = User.objects.get(pk = following_user_id)
        being_followed = User.objects.get(pk = being_followed_id)
        if action == "Follow":
            new_follow = Follow(
                follower = following_user,
                followed = being_followed
            )
            new_follow.save()
            btn_text = "Unfollow"
        else:
            Follow.objects.get(followed = being_followed, follower = following_user).delete()
            btn_text = "Follow"

        profile_user = User.objects.get(pk = user_id)
        followers_count = Follow.objects.filter(followed = profile_user).count
        followed_count = Follow.objects.filter(follower = profile_user).count
        posts = Post.objects.filter(user = profile_user).order_by('-created_at')
        
        return render(request, "network/profile.html" , {'user': profile_user, 'followers':followers_count, 'followed':followed_count, 'posts':posts, 'btn_text': btn_text})

    else:
        profile_user = User.objects.get(pk = user_id)
        followers_count = Follow.objects.filter(followed = profile_user).count
        followed_count = Follow.objects.filter(follower = profile_user).count
        posts = Post.objects.filter(user = profile_user).order_by('-created_at')
        if Follow.objects.filter(follower = request.user, followed = profile_user).exists():
            btn_text = "Unfollow"
        else:
            btn_text = "Follow"


        return render(request, "network/profile.html" , {'user': profile_user, 'followers':followers_count, 'followed':followed_count, 'posts':posts, 'btn_text': btn_text})
    
@csrf_exempt
@login_required
def post_update(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = json.loads(request.body)

    # Get contents of post
    id = data.get("post_id", "")
    updtd_text = data.get("post_text", "")

    post = Post.objects.get(pk = id)

    post.text = updtd_text
    post.save()

    #return JsonResponse({"message": "Post Updated successfully."}, status=201)
    return JsonResponse(post.serialize())

    
@csrf_exempt
@login_required
def like_update(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    
    data = json.loads(request.body)

    
    # Get contents of post
    post_id = data.get("post_id", "")
    user_id = data.get("current_user", "")

    post = Post.objects.get(pk = post_id)
    user = User.objects.get(pk = user_id)

    if Like.objects.filter(Liker = user, Post_Liked = post).exists():
        likee = Like.objects.get(Liker = user, Post_Liked = post)
        likee.delete()
    else:
        like = Like(
            Liker = user,
            Post_Liked = post
        )
        like.save()


    return JsonResponse(post.serialize())


    '''
    post.text = updtd_text
    post.save()

    #return JsonResponse({"message": "Post Updated successfully."}, status=201)
    return JsonResponse(post.serialize())
    '''

