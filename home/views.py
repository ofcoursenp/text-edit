from django.shortcuts import render

# Create your views here.

def index(req):
    if req.POST.get('text'):
        text = req.POST.get('text')
        whattodo = 'r p'
        newtext = ""
        if whattodo[0] == "r":
            if whattodo[2] == 'p':
                splittext = [*text]
                for i in splittext:
                    if i == "!" or i == ":":
                        continue
                    else:
                        newtext = newtext + i
        dfiles = {'text':newtext,}
        print(req.POST.get('text'))
        print(newtext)
        return render(req,'index.html',dfiles)
    return render(req,'index.html',)