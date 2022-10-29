
from ctypes import sizeof
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    'january': 'eat no meat for the entire month',
    'february': 'walk at least 20 min every day',
    'march': 'walk at least 20 min every day',
    'april': 'walk at least 20 min every day',
    'may': 'walk at least 20 min every day',
    'june': 'walk at least 20 min every day',
    'july': 'walk at least 20 min every day',
    'august': 'walk at least 20 min every day',
    'september': 'walk at least 20 min every day',
    'october': 'walk at least 20 min every day',
    'november': 'walk at least 20 min every day',
    'december': 'walk at least 20 min every day',
}

response_not_found_message = 'invalid option'

# Create your views here.


def monthly_challenge_by_number(request, month):
    if month > 0 and month <= len(monthly_challenges):
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        return HttpResponseRedirect('/challenges/' + redirect_month)
    else:
        return HttpResponseNotFound(response_not_found_message)


def monthly_challenge(request, month):
    challenge_text = None
    # switch = {
    #     'january': 'eat no meat for the entire month',
    #     'february': 'walk at least 20 min every day',
    # }
    # return HttpResponse(switch.get(month, 'invalid option'))
    # if month == 'january':
    #     challenge_text = 'eat no meat for the entire month'
    # elif month == 'february':
    #     challenge_text = 'walk at least 20 min every day'
    # else:
    #     return HttpResponseNotFound('invalid option')
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound(response_not_found_message)
