from django.shortcuts import render
from . import models
from accounts.models import Profile
from .forms import MessageForm


# Create your views here.
def ChatView(request):
    profiles = Profile.objects.all()
    profs = []
    messages = models.Message.objects.filter(sender=request.user.profile)
    messages_as_rec = models.Message.objects.filter(receiver=request.user.profile)
    for message in messages:
        profs.append(message.receiver)
    for message_rc in messages_as_rec:
        profs.append(message_rc.sender)
    return render(request, 'chat_dashboard.html', context={'profiles': profs})


def ChattingView(request, pk):
    sender = Profile.objects.get(user=request.user)
    receiver = Profile.objects.get(pk=pk)
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        message = form.save()
        message.sender = sender
        message.receiver = receiver
        message.save()
    messages = models.Message.objects.filter(sender=sender, receiver=receiver)
    return render(request, 'chat.html', context={'form': form, "messages": messages})
