from django.shortcuts import render
from .models import Hiretuber
from django.contrib import messages
# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        email = request.POST['email']

        # TODO: do all sanitization
        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name,
                              city=city, state=state, message=message, phone=phone, user_id=user_id, email=email)
        hiretuber.save()
        messages.success(request, 'Thans for reaching out!')
        return redirect('youtubers')
