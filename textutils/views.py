from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def analyzed(request):
    djtext=request.POST.get('text','default')
    upper=request.POST.get('upper','off')
    lower=request.POST.get('lower','off')
    scount=request.POST.get('scount','off')
    punc=request.POST.get('punc','off')
    
    if upper=='on':
        nikal=str(djtext).upper()
        params = {'later': 'Capital Latters', 'result': nikal}

    if lower=='on':
        nikal=str(djtext).lower()
        params = {'later': 'Small Latters', 'result': nikal}
    
    if scount=='on':
        nikal=len(str(djtext))
        params = {'later': 'Number of Characters Present in line', 'result': f'The Total Number Of Characters is : {nikal}'}

    if punc=="on":
        s='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        nikal=''
        for char in djtext:
            if char not in s:
                nikal=nikal+char
        params = {'later': 'Text Without Punctuations', 'result': nikal}

    if upper!='on' and lower!='on' and scount!='on' and punc!='on':
        return render (request , 'Error.html')
    
    return render(request, 'Analyzed.html', params)