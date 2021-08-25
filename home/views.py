from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserDataForm , UserDataCheck 
import re
from .models import UserData
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout
import os , io
import json
from rest_framework.parsers import JSONParser

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def register(request):
    if request.session.has_key('logged_user'):
         return render(request, "chatroom.html")
    else:
        context ={}
        form = UserDataForm()
        return render(request, "index.html", {"context":form})


def save_username(request):
    if request.session.has_key('logged_user'):
         return render(request, "chatroom.html")
    else:
        if request.method == "POST":
            try:
                username = request.POST['username']
                password = request.POST['password']
                if len(username) >= 10:
                    context ={}
                    form = UserDataForm()
                    return render(request, "index.html", {"context":form,"error":"wowo slow down huge name that's impossible"})
                if len(password) >= 9:
                    context ={}
                    form = UserDataForm()
                    return render(request, "index.html", {"context":form,"error":"You cannot remeber that long password"})
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                if (regex.search(username) == None):
                    print("Username is accepted")
                else:
                    context ={}
                    form = UserDataForm()
                    return render(request, "index.html", {"context":form,"error":"username not valid"})
                form = UserDataForm(request.POST or None)
                if form.is_valid():
                    # form.save()
                    sign_up = form.save(commit=False)
                    sign_up.password = make_password(form.cleaned_data['password'])
                    sign_up.status = 1
                    sign_up.save()
                else:
                    context ={}
                    form = UserDataForm()
                    return render(request, "index.html", {"context":form,"error":"username already existed"})
                context ={}
                form = UserDataCheck()
                message = {
                    "context": form,
                    "message": username+" registered"
                }
                return render(request, "login.html", message)
            except:
                context ={}
                form = UserDataForm()
                return render(request, "index.html", {"context":form,"error":"Something went wrong"})
        else:
            return redirect("/")


def login(request):
    if request.session.has_key('logged_user'):
         return render(request, "chatroom.html")
    else:
        context ={}
        form = UserDataCheck()
        return render(request, "login.html", {"context":form})

def check_login(request):
    if request.session.has_key('logged_user'):
         return render(request, "chatroom.html")
    else:
        if request.method == "POST":
            try:
                username_ = request.POST['username']
                password__ = request.POST['password']
                passs = UserData.objects.filter(username=username_).values("password").first()
                user = check_password(password__, passs["password"])
                if user is True:
                    print("logged")
                    request.session['logged_user'] = username_
                    return redirect("/chat_group")
                else:
                    context ={}
                    form = UserDataCheck()
                    message = {
                        "context": form,
                        "error": "Username or password wrong"
                    }
                    return render(request, "login.html", message)
                return redirect("/login")
            except:
                context ={}
                form = UserDataCheck()
                message = {
                    "context": form,
                    "error": "There was Error"
                }
                return render(request, "login.html", message)
        else:
            return redirect("/login")



from django.contrib import messages
def logout_view(request):
    logout(request)
    messages.error(request,"Did you like it")
    return redirect("/login")



def home(request):
    if request.session.has_key('logged_user'):
        username = request.session['logged_user']
        return render(request, "chatroom.html",{"username":username})
    else:
        return redirect("/")

from home.models import MessageData
def message(request):
    if request.session.has_key('logged_user'):
        username = request.session['logged_user']
        # print(username)
        if request.method == "POST":
            try:
                json_data = request.body
                stream = io.BytesIO(json_data)
                message_ = JSONParser().parse(stream)
                from datetime import datetime
                send_data = {}
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                send_data["username"] = username
                send_data["message"] = message_["mes"]
                send_data["time"] = current_time
                message = MessageData(username=username, message=message_["mes"])
                message.save(send_data)
                # print("save")
                return redirect("/")
            except:
                # print("not save")
                return redirect("/")
    else:
        return redirect("/")


from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def message_return(request):
    try:
        if request.session.has_key('logged_user'):
            data = list(MessageData.objects.values())
            # print(data)
            # return redirect("/")
            return Response(data, status=status.HTTP_200_OK)
        else:
             return redirect("/")
    except:
        return redirect("/")
        # return Response({"message": "Something went wrong in space"}, status=status.HTTP_400_BAD_REQUEST)


