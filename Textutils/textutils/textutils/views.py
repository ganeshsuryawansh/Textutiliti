# i have created this file - ganesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')

    # check checkbox value;
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    Extraspaceremover = request.POST.get('Extraspaceremover','off')
    locase = request.POST.get('locase','off')
    charcount = request.POST.get('charcount','off')

    # check which checkbox is on
    if(removepunc == "on"):
        punctuations = '''!()-[]{};: |'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if(locase=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()

        params = {'purpose': 'Changed to Lowercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(Extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount == "on"):
        analyzed = len(djtext)
        print(analyzed)
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}

    if(removepunc == "off" and newlineremover == "off" and charcount == "off" and Extraspaceremover == "off" and locase =="off" and fullcaps =="off" ):
        return HttpResponse("<h1><i> Error: Please select any operation and try again </i> </h1>")


    return render(request, 'analyze.html', params)
