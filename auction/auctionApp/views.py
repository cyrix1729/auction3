from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from .models import *
from django.core import serializers
import json
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponseBadRequest
from django.utils.timezone import make_aware
from datetime import datetime
from django.core.mail import send_mail

def index(request):
    return HttpResponse("LISTINGS PAGE GO HERE.")

def user_api(request):
    #updating user information
    if request.method == 'PUT': 
        json_data = json.loads(request.body)
        cur_user = request.user
        #update username
        cur_user.username = json_data['username']
        #update email
        cur_user.email = json_data['email']
        #update Date of birth
        cur_user.DOB = json_data['DOB']
        cur_user.save()
        
        return HttpResponse('Updated')
    
    if request.method == 'GET':
        cur_user = request.user
        if cur_user.is_anonymous:
            return JsonResponse({
                'cur_user_data' : 'not logged in'
            })
        else:
            return JsonResponse({
                'cur_user_data' : cur_user.to_dict()
                })
               
##########################################
#Stuff By Steph
##########################################

def getQuestion(request, itemId):
    if request.method == "GET":
        cur_user = request.user
        isOwner = False

        if cur_user == Item.objects.get(id = itemId).seller:
            isOwner = True

        questionData = Question.objects.filter(item_id = itemId).values()

        data = {
            'answer' : list(questionData),
            'isOwner' : isOwner
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

def getUserQuestions(request):
    if request.method == "GET":
        cur_user = request.user
        user_id = (int)(request.user.id)
        questionData = Question.objects.filter(asker__id=user_id).values('id', 'question', 'answer')
        
        data = {}

        for i in questionData:
            data[i.get('id')] = i

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')
    
def getQuestionsAskedToUser(request):
    if request.method == "GET":
        cur_user = request.user
        user_id = (int)(request.user.id)
        data = {}
        if User.objects.filter(id = user_id).exists():
            _seller = User.objects.get(id = user_id)
            items = Item.objects.filter(seller = _seller).values('id')

            for i in items:
                _question = Question.objects.filter(item__id = i.get('id'))
                if (_question.exists()):
                    data[i.get('id')] = {
                        'question' : list(_question.values('id', 'question', 'answer')), 
                        'itemId' : i.get('id')
                    }

            if len(data) <= 0:
                data = {
                    'ObjectsFound' : False
                }
            else:
                data['ObjectsFound'] = True

        else:
            data['ObjectsFound'] = False
        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

def getItemQuestions(request, item_id):
    if request.method == "GET":
        _item = Item.objects.get(id = item_id)
        
        questionData = Question.object.filter(item = _item).values()
        
        data = {
            'questions' : list(questionData)
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')


def getItem(request, item_id):
    if request.method == "GET":
        item = Item.objects.filter(id = item_id)

        itemData = item.values('name', 'desc', 'start_time', 'end_time',
            'start_price', 'cur_price', 'image')

        data = {
            'item' : list(itemData),
            'seller' : list(User.objects.filter(
                id = item.values('seller')[0]['seller']
                ).values('first_name', 'last_name'))
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

@csrf_exempt
def postQuestion(request, item_id):
    if request.method == "POST":
        cur_user = request.user
        postData = json.loads(request.body.decode("utf-8"))
        print("posting question to database")
        _asker = User.objects.get(id = request.user.id)
        _item = Item.objects.get(id = item_id)
        _question = postData.get('question', None)

        Question.objects.create(question = _question, asker = _asker, item = _item)
        response = JsonResponse({'status' : 'question posted'})

        return response
    return HttpResponseBadRequest('Invalid request')


@csrf_exempt
def postAnswer(request, question_id):
    if request.method == "POST":
        question = Question.objects.get(id = question_id)
        postData = json.loads(request.body.decode("utf-8"))

        _answer = postData.get('answer')

        question.answer = _answer
        question.save()

        data = {
            'updated' : True
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

@csrf_exempt
def postItem(request):
    if request.method == "POST":
        cur_user = request.user
        _image = request.FILES.get('file')
        _name = request.POST.get('name')
        _desc = request.POST.get('desc')
        _start_time = make_aware(datetime.fromisoformat(request.POST.get('startTime')))
        _end_time = make_aware(datetime.fromisoformat(request.POST.get('endTime')))
        _start_price = request.POST.get('startPrice')

        _seller = cur_user
        Item.objects.create(name = _name, desc = _desc,
            start_time = _start_time, end_time = _end_time, 
            start_price = _start_price, cur_price = _start_price,
            image = _image, seller = _seller)

        data = {
            'status' : 'item added'
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

@csrf_exempt
def placeBid(request, item_id):
    if request.method == "POST":
        cur_user = request.user
        item = Item.objects.get(id = item_id)

        postData = json.loads(request.body.decode("utf-8"))

        _bid = postData.get('bid')

        data = {}
        currentTime = make_aware(datetime.now())
        if (int)(_bid) > item.cur_price and item.end_time > currentTime and item.start_time < currentTime and item.seller != cur_user:
            bid = Bid.objects.create(bidder = User.objects.get(id = cur_user.id), value = _bid)
            item.cur_price = bid.value
            item.cur_bid = bid
            item.save()

            data = {
                'status' : 'bid placed'
            }
        else:
            data = {
                'status' : 'ivalid bid'
            }

        print((str)(data))

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

##########################################
#End of Stuff by Steph
##########################################
"""
def listings_api(request) -> HttpResponse:
    itemData = Item.objects.all
    return JsonResponse({
        'item': [
            item.to_dict() for item in Item.objects.all()
        ]
    })
"""

def listings_api(request, searchData) -> HttpResponse:
    cur_user = request.user
    item = Item.objects.all()

    if searchData != "-":
        item = Item.objects.all().filter(Q(name__icontains=searchData) | Q(desc__icontains=searchData))
    
    items = []
    for i in item:
        j = i.to_dict()
        j['isOwner'] = (cur_user == i.seller)
        items.append(j)

    data = {
        'item': items
    }

    return JsonResponse(data)
