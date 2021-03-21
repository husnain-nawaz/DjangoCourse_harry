
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    lowercase=request.POST.get('lowercase','off')
    tabremover=request.POST.get('tabremover','off')
    # print(djtext)

        # punctuation remove
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # upper case
    if(fullcaps == 'on'): # elif is used before
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # new line remove
    if(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Removed New Lines space', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # space remove
    if(spaceremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != " ":
                analyzed += char
        params = {'purpose': 'space remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
        # lowercase
    if(lowercase == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed += char.lower()
        params = {'purpose': 'lower  case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # Tab Remover
    if(tabremover == 'on'):  # its not working
        analyzed = ''
        for char in djtext:
            if char != " \t":
                analyzed += char
        params = {'purpose': 'TAB remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # single space other remove
    if(extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # character counter
    if(charcounter == 'on'):
        # counter = djtext
        total = 0
        for i in djtext: # can use counter instead of djtext if uncommnet counter variable
            total += 1
 
        params = {'purpose': 'Counter character', 'analyzed_text': total}
        djtext = total
        # return render(request, 'analyze.html', params)
           
    # else:
    #     return render(request,'error.htm')
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on"
     and extraspaceremover != "on" and lowercase != "on" and charcounter != 'on' and tabremover != "on"):
        # return HttpResponse('Error bro')
        return render(request, 'error.htm')
         # give all get paarmeter correctly
        # Error only happen whwn values are empty or function is not performing 
        # counter is working if we pass value first i.e check one checkbox before atleast so it count values on bases of that checkbox output value
    return render(request, 'analyze.html', params)  # remove prams to check UnboundLocalError  error






