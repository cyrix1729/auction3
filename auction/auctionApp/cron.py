from django.core.mail import EmailMessage
from django.core.mail import send_mail
from auctionApp.models import *
from django.utils.timezone import make_aware
from datetime import datetime

def my_cron_job():
    email = ""
    name = ""
    itemName = ""
    itemPrice = ""

    items = Item.objects.all()
    currentTime = make_aware(datetime.now())
    for i in items:
        if i.end_time <= currentTime:
            if i.cur_bid != None:
                if not i.winner_informed:
                    email = (str)(i.cur_bid.bidder.email)
                    name = (str)(i.cur_bid.bidder.username)
                    itemName = (str)(i.name)
                    itemPrice = (float)(i.cur_bid.value)
                    send_mail(
                        'Congratulations {}'.format(name),
                        """Hi {_name},
You have successfully bid on {_itemName} and won. Please proceed with your purchase for {_itemPrice}""".format(_name = name, _itemName = itemName, _itemPrice = itemPrice),
                        'newdjangobay@gmail.com',
                        [email],
                        fail_silently=False,
                    )
                    i.winner_informed = True
                    i.save()


        print("Mail sent!")

    