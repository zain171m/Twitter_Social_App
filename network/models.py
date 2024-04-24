from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField(upload_to='network/files/profile_pictures/', blank=True, null=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Creater")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} posted {self.text} on {self.created_at}"
    
    def num_likes(self):
        return Like.objects.filter(Post_Liked=self).count()
    
    def liked_or_not(self):
        return Like.objects.filter(Liker = request.user, Post_Liked = self).exists()

    
    def serialize(self):
        return {
            "id": self.id,
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "email": self.user.email,
                # Include other user fields as needed
            },
            "text": self.text, 
            "num_likes": self.num_likes()  # Include the number of likes
        }
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Commentator")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commented_post")
    comment_text = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented {self.comment_text} on {self.post.id}"
    
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "Follower")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "Followed")
    followed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} followed {self.followed.username} on {self.followed_at}"
    

class Like(models.Model):
    Liker = models.ForeignKey(User, on_delete = models.CASCADE, related_name= "Liker")
    Post_Liked = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="post_liked")
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Liker.username} liked {self.Post_Liked.id} on {self.liked_at}"
    