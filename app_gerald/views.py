from django.shortcuts import render, redirect
from django.views import generic

from django.views.decorators.http import require_POST

from .models import Person
from .forms import FinderForm


def index(request):
    return render(request, 'app_gerald/index.html', {'start':0})


class PersonListView(generic.ListView):
    template_name = 'app_gerald/list.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Person.objects.all()[:3]


class PersonView(generic.DetailView):
    model = Person
    template_name = 'app_gerald/person.html'


class GetWomanView(generic.ListView):
    template_name = 'app_gerald/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Person.objects.filter(sex__exact='f')


# Правители
class GetKing(generic.ListView):
    template_name = 'app_gerald/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Person.objects.filter(start_of_government__gt=-1)


# Романовы за последние два века
class GetRomansInLast(generic.ListView):
    template_name = 'app_gerald/list.html'
    context_object_name = 'list'

    def get_queryset(self):
        return None


def find(request):

    form = FinderForm()

    context = {'form': form}
    return render(request, 'app_gerald/find.html', context)

@require_POST
def find_person(request):
    form = FinderForm(request.POST)

    if form.is_valid():
        pass

    print(request.POST['text'])

    return redirect('find')
