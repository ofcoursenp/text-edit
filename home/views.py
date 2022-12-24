from django.shortcuts import render

# Create your views here.

def index(req):
    if req.POST.get('text'):
        text = req.POST.get('text')
        punc = req.POST.get('r p','off')
        space = req.POST.get('r s','off')
        newtext = text
        if punc == "on":
            splittext = [*newtext]
            newtext = ''
            for i in splittext:
                if i == "!" or i == ":":
                    continue
                else:
                    newtext = newtext + i
        if space == "on":
            splittext = [*newtext]
            newtext = '' 
            for i in splittext:
                if i == " " or i == "  ":
                    continue
                else:
                    newtext = newtext + i    
        dfiles = {'textf':newtext,}
        print(req.POST.get('text'))
        print(newtext)
        return render(req,'result.html',dfiles)
    return render(req,'index.html',)


def result(req):
    return render(req,'result.html')