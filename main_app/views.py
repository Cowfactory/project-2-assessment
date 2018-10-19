from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetForm

# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    totalQuantity = 0
    for widget in widgets:
        totalQuantity += widget.quantity

    if request.method == 'POST':
        form = WidgetForm(request.POST)
        form.save()
        return HttpResponseRedirect('/')

    else:
        form = WidgetForm()
        return render(request, 'home.html', {'widgets': widgets, 'form': form, 'totalQuantity': totalQuantity})

def deleteWidget(request, widget_id):
    print(widget_id)

class WidgetDelete(DeleteView):
    model = Widget
    success_url = "/" 
