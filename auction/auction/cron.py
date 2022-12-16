from django.core.mail import EmailMessage
from django.core.mail import send_mail
from auctionApp.models import *
from django.utils.timezone import make_aware
from datetime import datetime

def my_cron_job():
    """msg = EmailMessage(
        'Test Email',
        'This is a test message sent from the django server',
        to=['nauticaldemon@gmail.com'],
    )
    msg.send()"""

    email = ""
    name = ""
    itemName = ""
    itemPrice = ""

    items = Item.objects.all()
    currentTime = make_aware(datetime.now())
    for i in items:
        if i.end_time <= currentTime:
            if i.cur_bid != None:
                email = (str)(i.cur_bid.bidder.email)
                name = (str)(i.cur_bid.bidder.first_name)
                itemName = (str)(i.name)
                itemPrice = (float)(i.cur_bid.value)
                send_mail(
                    'Congratulations {}'.format(name),
                    """Hi {_name},
                    You have successfully bid on {_itemName} and won. Please proceed with your purchase for {_itemPrice}
                    """.format(_name = name, _itemName = itemName, _itemPrice = itemPrice),
                    'newdjangobay@gmail.com',
                    [email],
                    fail_silently=False,
                )

        print("Mail sent!")

    