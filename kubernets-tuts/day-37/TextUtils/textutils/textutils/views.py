# # Ye file mne bnai h   --> Karan Singh

from django.http import HttpResponse
from django.shortcuts import render

#
# def index(request):
#     return HttpResponse('''
#     <a href="https://google.com">Enter Google </a> <br>
#     <a href="https://github.com">Open Github </a> <br>
#     <a href="https://facebook.com">Open Facebook </a> <br>
#     <a href="https://instagram.com">Open Instagram </a> <br>
#     <a href="https://codewithharry.com"> Open Code With Harry</a> <br>
#
#     ''')
#
# def about(request):
#     return HttpResponse("About Mr. Robot")


# introducing pipes in django

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    djtext= request.GET.get('rempunc_text', 'default')
    rempunc=request.GET.get('rempunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlinerem=request.GET.get('newlinerem','off')
    extraspacerem = request.GET.get('extraspacerem','off')
    charcount=request.GET.get('charcount','off')
    print(djtext)
    # return HttpResponse('''Removing punctutaions <br> <br>
    #                     <a href="/"> BAck To home </a> ''')
    analyzed = ""

    if rempunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+= char;
        params={'purpose':'removepunc','analyzed_text':analyzed}


    djtext=analyzed
    if fullcaps=="on" :
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Capitilizing...', 'analyzed_text': analyzed}


    djtext = analyzed
    if(newlinerem=="on"):
        for char in djtext:
            if (char != '\n'):
                analyzed+=char
        params = {'purpose': 'Removing New Lines..', 'analyzed_text': analyzed}


    djtext = analyzed
    if(extraspacerem=="on"):
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char
        params = {'purpose': 'Removing Extra Spaces..', 'analyzed_text': analyzed}


    djtext = analyzed
    if(charcount=="on"):
        counter=0
        for char in djtext:
            counter+=1
        params = {'purpose': 'Counting Charactars..', 'analyzed_text': counter}

    print(analyzed)
    return render(request, 'analyze.html', params)


def about(request):
    para={'purpose': 'About wala page thi h kya?'}
    return render(request, 'about.html', para)


# def capsfirst(request):
#     return HttpResponse(''' Capitilize First <br> <br>
#                         <a href="/"> BAck To home </a> ''')
#
# def extraspaceremove(request):
#     return HttpResponse(''' ExtraspaceRemove <br> <br>
#                         <a href="/"> BAck To home </a> ''')
#
# def newlineremove(request):
#     return HttpResponse(''' newlineremove <br> <br>
#                         <a href="/"> BAck To home </a> ''')
#
# def charcount(request):
#     return HttpResponse(''' charcount <br> <br>
#                         <a href="/"> BAck To home </a> ''')

