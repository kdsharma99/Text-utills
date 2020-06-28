from django.http import HttpResponse
from django.shortcuts import render

a=0
def index(request):
    # return HttpResponse("Hello")
    return render(request,"index.html")
def punc(text):
    analyzed=""
    punctuations = '''!()-[]{;:'"\,<>./?@#$%^&*_~}'''
    for char in text:
        if char not in punctuations:
            analyzed=analyzed+char
    return analyzed
def cap(text):
    analyzed=""
    for char in text:
        analyzed=analyzed+char.upper()  
    return analyzed    
def rn(text):
    analyzed=""
    for char in text:
        if char !="\n" and char!="\r":
            analyzed=analyzed+char
    return analyzed  
def rs(text):
    analyzed=""
    for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1]==" "):
            analyzed = analyzed + char
    return analyzed
def count(text):
    analyzed=""
    analyzed="This text has "+str(len(text))+" Characters"
    return analyzed
def analyze(request):
    djtext=request.POST.get('texxt',"default")
    removepunc=request.POST.get('removepunc',"off")
    capitalizefirst=request.POST.get('capitalizefirst',"off")
    removenewline=request.POST.get('removenewline',"off")
    removespace=request.POST.get('removespace',"off")
    # countchar=request.POST.get('countchar',"off")
    a=0
    b=0
    c=0
    d=0
    if removepunc=="on":
        puncc=punc(djtext)
        a=1
    if capitalizefirst=="on":
        if a==1:
            capp=cap(puncc)
            b=1
            a=0
        else:
            capp=cap(djtext)
        analyze=capp  
    if removenewline=="on":
        if a==1:
            rnn=rn(punc)
            a=0
            c=1
        elif b==1:
            rnn=rn(capp)
            b=0
            c=1
        else:
            rnn=rn(djtext)
            c=0
        analyze=rnn
    if removespace=="on":
        if c==1:
            rss=rs(rnn)
            d=1
            c=0
        elif a==1:
            rss=rs(punc)
            d=1
            a=0
        elif b==1:
            rss=rs(capp)
            d=1
            b=0
        else:
            rss=rs(djtext)
            d=0  
        analyze=rss  
    
    if d==1:
        co=count(rss)
    elif a==1:
        co=count(punc)
    elif b==1:
        co=count(capp)
    elif c==1:
        co=count(rnn)
    else:
        co=count(djtext)
    # else :
    #     analyzed="No option is selected"
    params={"checkbox":co,"answer":analyze}
    return render(request,"analyze.html",params)
# def capitalizefirst(request):
#     return HttpResponse("capitalize first")
# def removenewline(request):
#     return HttpResponse("remove new line")
# def removespace(request):
#     return HttpResponse("remove space")
# def countchar(request):
#     return HttpResponse("count chars")