from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day

def add(request):
    #送信内容を基にフォームを作成する、POSTじゃなければ。からのフォーム
    form = DayCreateForm(request.POST or None)

    #method=POST,つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('nikki:index')

    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示する
    context = {
        'form':form
    }
    return render(request, 'nikki/day_forms.html', context)

def update(request, pk):
    #get Day base from url' pk
    day = get_object_or_404(Day, pk=pk)

    #getting Day bond to forms
    form = DayCreateForm(request.POST or None, instance=day)

    #method=POST so it do when push the send button if contents inputted haven't problem
    if request.method == 'POST' and form.is_vaild():
        form.save()
        return redirect('nikki:index')

    #When nomal pageaccece or contents inputed dosen't have mistakes
    context = {
        'form':form
    }
    return render(request, 'nikki/day_forms.html', context)

def delete(request, pk):
    #get Day base from url' pk
    day = get_object_or_404(Day, pk=pk)

    #method=POST so it do when push the send button if contents inputted haven't problem
    if request.method == 'POST':
        day.delete()
        return redirect('nikki:index')

    #When nomal pageaccece or contents inputed dosen't have mistakes
    context = {
        'day':day
    }
    return render(request, 'nikki/day_confirm_delete.html', context)
