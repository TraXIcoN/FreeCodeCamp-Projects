
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

category_choice =(
('Electronics', 'Electronics'),
('Fashion','Fashion'),
('Homedecor', 'Homedecor'),
('Automobiles', 'Automobiles'),
('Sports equipment', 'Sports equipment'),
('Music equipment', 'Music equipment'),
('Books', 'Books'),
('Miscallenous', 'Miscallenous')
)

class User(AbstractUser, ):
    watchlist = models.ManyToManyField('Listing', related_name="w")


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    title = models.CharField(max_length=20)
    description = models.TextField()
    startbid = models.IntegerField()
    image_link = models.URLField( blank = True)
    category = models.CharField(max_length=63, blank=True, null=True, choices=category_choice)
    closed =models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.id}:{self.title}{self.description}{self.startbid}{self.category}"

class Bid(models.Model):
    amount = models.IntegerField()
    bidder = models.ForeignKey(User,on_delete=models.CASCADE, related_name="bider")
    bid = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name=  "bidamt")

class Comments(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey(User,on_delete=models.CASCADE, related_name="commenterr")
    d = models.DateTimeField(default=datetime.datetime.now)
    rlist = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name="currentcomment")
