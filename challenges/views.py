
from ctypes import sizeof

from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse

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
    'december': None,
}

response_not_found_message = 'invalid option'

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    if month > 0 and month <= len(monthly_challenges):
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound(response_not_found_message)


def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'challenge_text': challenge_text,
            'month': month
        })
    except:
        response_data = f'<h1>{response_not_found_message}</h1>'
        return HttpResponseNotFound(response_data)

