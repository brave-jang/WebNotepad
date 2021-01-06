from django.shortcuts import render
from .models import Notepad

# Create your views here.
def memo_list(request):
    note = Notepad.objects.all()
    return render(request, "notepad/memo_list.html", {'note':note})


def memo_write(request):
    if request.method == "GET":
        return render(request, "notepad/memo_write.html")
    else:
        req_title = request.POST.get('title', None)
        req_content = request.POST.get('content', None)

        note = Notepad(
            title = req_title,
            content = req_content,
        )

        note.save()
        
    return render(request, "notepad/memo_write.html")