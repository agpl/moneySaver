from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime
from .models import Ticket, Item, Category
from django.db.models import Sum
from .forms import TicketForm, ItemForm
from django.shortcuts import get_object_or_404



# Create your views here.
def index(request):
    today = datetime.date.today()
    tickets = Ticket.objects.filter(date__month=today.month).order_by('-date')
    return render(request, 'index.html', {
        'tickets': tickets,
        'total': tickets.aggregate(Sum('total'))
    })

def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TicketForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ticket = Ticket(
                place = request.POST.get('place', 'brak'),
                date = request.POST.get('date'),
                serial = request.POST.get('serial', 'brak'),
                total = request.POST.get('total', 0),
            )

            ticket.save()

            Item(
                name='Inne',
                category_id=9,
                ticket_id=ticket.id,
                cost=request.POST.get('total', 0)
            ).save()
            return HttpResponseRedirect('/edit/%s' % ticket.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TicketForm()

    return render(request, 'add.html', {'form': form}, RequestContext(request))

def edit(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket.place = request.POST.get('place', 'brak')
            ticket.date = request.POST.get('date')
            ticket.serial = request.POST.get('serial', 'brak')
            ticket.total = request.POST.get('total', 0)
            ticket.save()
            return HttpResponseRedirect('/edit/%s' % ticket.id)
    else:
        form = TicketForm(instance=ticket)

    formItem = ItemForm()

    items = Item.objects.filter(ticket=ticket)
    items_array = []
    for item in items:
        tmp = {
            "id" : item.id,
            "form": ItemForm(instance=item)
        }
        items_array.append(tmp)

    return render(request, 'edit.html', {
        "form": form,
        "formItem": formItem,
        "id": ticket.id,
        "items":items_array,
    },context_instance=RequestContext(request))


def delete(request, id):
    Ticket.objects.get(id=id).delete()

    return HttpResponseRedirect('/')


def delete_item(request, id):
    item = Item.objects.get(id=id)
    ticket_id = item.ticket.id
    if item.category.id != 9:
        item.delete()

    return HttpResponseRedirect('/edit/%s' % ticket_id)


def add_item(request, ticket_id, id):
    if id == '':
        id = None

    category_id = int(request.POST.get('category'))

    if category_id != 9:
        form = ItemForm(request.POST)
        # if form.is_valid():
        ticket = Ticket.objects.get(id=ticket_id)
        Item(
            id=id,
            name=request.POST.get('name', 'brak'),
            number=float(request.POST.get('number', 1)),
            singleCost=float(request.POST.get('singleCost', 0)),
            cost=float(request.POST.get('cost', 0)),
            ticket_id=ticket_id,
            category_id=int(request.POST.get('category')),
        ).save()

        other = Item.objects.get(ticket_id=ticket_id, category_id=9)
        items_sum = Item.objects.filter(ticket_id=ticket_id).exclude(category_id=9).aggregate(Sum('cost'))['cost__sum'];
        other.cost = ticket.total - items_sum
        other.save()


    return HttpResponseRedirect('/edit/%s' % ticket_id)