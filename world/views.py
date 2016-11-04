from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime


def toppage(request):
    print('-' * 40)
    print(request.session.session_key)
    print('-' * 40)

    # response = HttpResponse('<strong>hello</strong>')
    #response.status_code = 200
    #return response
    ctx = {
        'msg': '반갑습니다, 여러분',
    }
    return render(request, 'toppage.html', ctx)

