from django.contrib.auth.models import AbstractUser
from django.db import models
import json

# # Inherits from django's AbstractUser model
class User(AbstractUser):
    # unique email
    email = models.EmailField(unique = True)
    # unique Username
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    # Date of birth
    DOB = models.DateField(null=True)
    # Profile picture
    image = models.ImageField(upload_to='profile_pic', default='default.png')

    def __str__(self):
        return self.username
    
    def to_dict(self):
        return {
            'email': self.email,
            'username': self.username,
            'DOB': self.DOB,
            'image':json.dumps(str(self.image))
        }

    def get_username(self):
        return self.username
    

class Bid(models.Model):
    #highest bider
    bidder = models.ForeignKey(User, on_delete= models.CASCADE)
    #bid
    value = models.DecimalField(max_digits= 8, decimal_places= 2)


class Item(models.Model):
    # name
    name = models.CharField(max_length=50)
    # description
    desc = models.CharField(max_length=500)
    # Start time
    start_time = models.DateTimeField()
    # End time
    end_time = models.DateTimeField()
    # starting price
    start_price = models.DecimalField(max_digits= 8, decimal_places= 2)
    #current bid
    cur_price = models.DecimalField(max_digits= 8, decimal_places= 2)
    #image of item
    image = models.ImageField(upload_to='item_img')
    #seller of item
    seller = models.ForeignKey(User, on_delete = models.CASCADE )
    #current highest bid
    cur_bid = models.ForeignKey(Bid, on_delete = models.CASCADE, blank = True, null = True)
    #keep track of if winner has been informed
    winner_informed = models.BooleanField(default=False)



    def __str__ (self):
        return self.name

    def newBid(self, value):
        cur_price = value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'start_price': self.start_price,
            'cur_price': self.cur_price,
            'image': json.dumps(str(self.image))
            ##'seller': self.seller,
        }



# class Listings(models.Model):

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, blank=True)
    asker = models.ForeignKey(User, on_delete= models.SET('Deleted User'))
    #item the question is for
    item = models.ForeignKey(Item, on_delete = models.CASCADE )

    def __str__(self):
        return self.question

    def newAnswer(self, value):
        answer = value