from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic

from .models import TitleSet


#for test
def result(request, title_set_id):
    title_set = get_object_or_404(TitleSet, pk=title_set_id)
    return JsonResponse({"data": {"title": title_set.title, "text": title_set.text}}, safe=False)


class ListTitleView(generic.ListView):
    model = TitleSet
    template_name = 'dynamic_data/title_set/list.html'
    context_object_name = 'title_set_list'

class DetailTitleView(generic.DetailView):
    model = TitleSet
    template_name = 'dynamic_data/title_set/detail.html'
    context_object_name = 'title_set'

class ResultTitleView(generic.DetailView):
    model = TitleSet
    template_name = 'dynamic_data/title_set/result.html'
    context_object_name = 'title_set'


def index(request):
    return render(request, 'dynamic_data/index.html', {})


# def list_title(request):
#     title_set_list = TitleSet.objects.all()
#     context = {
#         'title_set_list': title_set_list,
#     }
#     return render(request, 'dynamic_data/title_set/list.html', context)


# def detail_title(request, title_set_id):
#     title_set = get_object_or_404(TitleSet, pk=title_set_id)
#     return render(request, 'dynamic_data/title_set/detail.html', {'title_set': title_set})


def edit_title(request, title_set_id):
    title_set = get_object_or_404(TitleSet, pk=title_set_id)
    if request.POST['title'] == "":
        return render(request, 'dynamic_data/title_set/detail.html', {
            'title_set': title_set,
            'error_message': "第一标题输入不可为空"
        })
    else:
        title_set.title = request.POST['title']
        title_set.text = request.POST['text']
        title_set.save()
        return HttpResponseRedirect(reverse('dd:resultTitle', args=(title_set.id,)))


# def result_title(request, title_set_id):
#     title_set = get_object_or_404(TitleSet, pk=title_set_id)
#     return render(request, 'dynamic_data/title_set/result.html', {'title_set': title_set})
