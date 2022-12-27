from django.shortcuts import render, redirect, HttpResponse
from .models import Contact
from django.contrib import messages
from . import speech
import os
from . import transcribe


def home(request):
    return render(request, "braille/home.html")


def on_speak_now(request):
    language = speech.launch_project()
    transcribe.do_transcribe(language)
    context = {'transcribed': transcribe.display_transcribed()}
    return render(request, "braille/home.html", context)

def download_file(request, *args, **kwargs):
    response = HttpResponse(transcribe.display_transcribed(), content_type='text/plain')
    response['Content-Length'] = os.path.getsize('transcribed.txt')
    response['Content-Length'] = 'text/plain; charset=utf-8'
    response['Content-Disposition'] = 'inline; filename=' + os.path.basename('transcribed.txt')
    return response


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone-number']
        message = request.POST['message']
        if str(name) == '' or str(email) == '' or str(len(phone_number)) == 0 or str(message) == '':
            messages.warning(
                request, 'Please enter the details before submmiting.')
            return redirect('contact')
        elif len(name) > 50:
            messages.warning(request, 'Maximum 50 characters allowed of name.')
            return redirect('contact')
        elif len(phone_number) != 10 or not str(phone_number).isdigit():
            messages.warning(request, 'Phone number is wrong.')
            return redirect('contact')
        else:
            contact = Contact(name=name, email=email,
                              phone_number=phone_number, message=message)
            contact.save()
            messages.success(
                request, 'Your message has been successfully recorded. We will talk to you soon.')
            return redirect('/')
    return render(request, 'users/contact.html')


