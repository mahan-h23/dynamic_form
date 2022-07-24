from django.db import models



class TestModel(models.Model):
    name = models.CharField(max_length=280)
    last = models.CharField(max_length=280)
    first = models.CharField(max_length=280)



from django import forms

# create a ModelForm
# class TestForm(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = TestModel
#         fields = "__all__"


from django.forms import modelformset_factory


TestForm = modelformset_factory(
    TestModel, fields = "__all__", extra=1
)