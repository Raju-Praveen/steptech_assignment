from django.shortcuts import render, HttpResponse


def hello(request):
    return render(request, "hello/index.html")
