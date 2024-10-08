from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *

def home(request):
    polls=Poll.objects.all()
    return render(request,'home.html',{'polls':polls})
def create(request):
    if request.method=='POST':
        question=request.POST.get('question')
        poll=Poll.objects.create(question=question)
        options_list=request.POST.getlist('options')
        no_of_options=int(request.POST.get('numOptions',0))
        for i in range(no_of_options):
            opt_text=options_list[i] if i<len(options_list) else ''
            if opt_text:
                Option.objects.create(poll=poll,text=opt_text)
        return redirect('polls:results',poll.id)

    return render(request,'create.html')
def vote(request,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    print(poll)
    if request.method=='POST':
        option_id=request.POST.get('option')
        option=get_object_or_404(Option,pk=option_id)
        option.votes+=1
        option.save()
        return redirect('polls:results',poll.id)
    options=poll.options.all()

    return render(request,'vote.html',{'poll':poll,'options':options})
def results(request,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    options=poll.options.all()

    return render(request,'results.html',{'poll':poll,'options':options})
def delete(request,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    if poll:
        poll.delete()
        return redirect('polls:home')
    return render(request,'home.html')