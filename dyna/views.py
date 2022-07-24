from django.shortcuts import render
from .models import TestModel,TestForm
# Create your views here.


def testView(request):
    context = {}
    skill_formset = TestForm(request.POST or None)

    if skill_formset.is_valid():
        skill_formset.save()

    context['skill_formset'] = skill_formset

    return render(request,'test.html',context)