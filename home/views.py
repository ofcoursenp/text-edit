import string
from django.shortcuts import render
import string
from home.models import Text

# Create your views here.

def index(req):
    databasetexts = Text.objects.all()
    if req.POST.get('text'):
        text = req.POST.get('text')
        punc = req.POST.get('r p','off')
        space = req.POST.get('r s','off')
        capital = req.POST.get('r c','off')
        thelist = list(string.ascii_uppercase)
        newtext = text
        data = []
        for i in databasetexts:
            data.append(i)

        if punc == "on":
            newtext = text.translate(str.maketrans('', '', string.punctuation))
            print(newtext)

        if space == "on":
            splittext = [*newtext]
            newtext = '' 
            for i in splittext:
                if i == " " or i == "  ":
                    continue
                else:
                    newtext = newtext + i  
    
        if capital == "on":
            splittext = [*newtext]
            newtext = '' 
            for i in splittext:
                if i in thelist:
                    continue     
                else:
                    newtext = newtext + i     
        print(req.POST.get('text'))
        print(newtext)
        dfiles = {'textf':newtext,
                    'database':data}
        ins = Text(text=text,newtext=newtext)
        ins.save()
        return render(req,'result.html',dfiles)
    return render(req,'index.html',)


def result(req):
    return render(req,'result.html')

def help(req):
    return render(req,'help-me.html')

