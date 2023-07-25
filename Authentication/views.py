from django.shortcuts import render, redirect

def UserSignup(request):
    return render(request,'signup.html',{})