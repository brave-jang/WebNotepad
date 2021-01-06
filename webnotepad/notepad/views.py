from django.shortcuts import redirect, render
from .models import Notepad
from .forms import NotepadForm

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


def memo_detail(request, post_id):
    note = Notepad.objects.get(pk=post_id)
    return render(request, "notepad/memo_detail.html", {'note':note})


def memo_edit(request, post_id):
    if request.method == "GET":
        note = Notepad.objects.get(pk=post_id)
        return render(request, "notepad/memo_edit.html", {'note':note})
    else:
        note = Notepad.objects.get(pk=post_id)
        form = NotepadForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect("notepad:detail", post_id)