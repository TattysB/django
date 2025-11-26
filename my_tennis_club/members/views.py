from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  
  template = loader.get_template('template.html')
  miembros = Member.objects.all().values()
  colum_firstname = Member.objects.values_list('firstname')
  records_name=Member.objects.filter(firstname='Isabella').values()
  records_AND_name_id=Member.objects.filter(firstname='Isabella',id=4).values()
  record_OR_name =Member.objects.filter(Q(firstname='Andres')| Q(firstname='Isabella')).values()
  record_like_start=Member.objects.filter(firstname__istartswith='A').values()
  record_like_end=Member.objects.filter(firstname__iendswith='S').values()
  record_like_contains=Member.objects.filter(firstname__icontains='ar').values()
  order_by_asc=Member.objects.all().order_by('firstname').values()
  order_by_desc=Member.objects.all().order_by('-firstname').values()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],  
    'miembros': miembros, 
    'colum_firstname': colum_firstname,
    'records_name': records_name,
    'records_AND_name_id': records_AND_name_id,
    'record_OR_name': record_OR_name,
    'record_like_start': record_like_start,
    'record_like_end': record_like_end,
    'record_like_contains': record_like_contains,
    'order_by_asc': order_by_asc,
    'order_by_desc': order_by_desc,
  }
  return HttpResponse(template.render(context, request))

def styled_page(request):
  template = loader.get_template('styled_page.html')
  return HttpResponse(template.render())