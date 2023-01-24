from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView, ListView
from .models import Graf, Bar, Typ

class Index(TemplateView):
  template_name = 'base.html'

  def get_context_data(self, **kwargs):
    context2 = super().get_context_data(**kwargs)
    context2["t"] = Typ.objects.all()
    return context2

class HomePageView(ListView):
  model = Typ
  template_name = 'base.html'

class BarChartView(TemplateView):
  template_name = 'grafy/bar.html'


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["b"] = Bar.objects.all()

    return context

class Stacked(TemplateView):
  template_name = 'grafy/stacked.html'

class PieAndDoughnutChartView(TemplateView):
  template_name = 'grafy/pie.html'

class Line(TemplateView):
  template_name = 'grafy/line.html'

class Test(TemplateView):
  template_name = 'grafy/test.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["g"] = Graf.objects.all()
    return context

def create(request):
  if request.method == "POST":
    jmeno_objektu = request.POST.get("jmeno_objektu")
    pocet_objektu = request.POST.get("pocet_objektu")
    color = request.POST.get("color")
    borderColor = request.POST.get("borderColor")
    Graf.objects.create(jmeno_objektu=jmeno_objektu, pocet_objektu=pocet_objektu, color=color, borderColor=borderColor)
  return HttpResponseRedirect("/Pie/")

def createBar(request):
  if request.method == "POST":
    jmeno = request.POST.get("jmeno")
    pocet = request.POST.get("pocet")
    Bar.objects.create(jmeno=jmeno, pocet=pocet)
  return HttpResponseRedirect("/Bar/")

def delete(request, id):
  var = Graf.objects.get(id=id)
  var.delete()
  return HttpResponseRedirect("/Pie/")



def update(request, id):
  jmeno_objektu = request.GET['jmeno_objektu']
  pocet_objektu = request.GET['pocet_objektu']
  color = request.GET['color']
  borderColor = request.GET['borderColor']
  graf = Graf.objects.get(id=id)
  graf.jmeno_objektu = jmeno_objektu
  graf.pocet_objektu = pocet_objektu
  graf.color = color
  graf.borderColor = borderColor
  graf.save()
  return HttpResponseRedirect("/Pie")

def pridat(request):
  template = loader.get_template('graf/upravit.html')
  return HttpResponse(template.render({}, request))


def pridat_objekt(request):
  x = request.POST['jmeno_objektu']
  y = request.POST['pocet_objektu']
  z = request.POST['color']
  w = request.POST['borderColor']
  test = Graf(jmeno_objektu = x, pocet_objektu = y, color = z, borderColor = w)
  test.save()
  return HttpResponseRedirect("/Pie/")

def odstranit(request, id):
  test = Graf.objects.get(id=id)
  test.delete()
  return HttpResponseRedirect("/Pie/")

def upravit(request, id):
  test = Graf.objects.get(id=id)
  context = {
    'test': test,
  }
  return HttpResponseRedirect("/Pie/")

def upravit_objekt(request, id):
  jmeno_objektu = request.POST['jmeno_objektu']
  pocet_objektu = request.POST['pocet_objektu']
  color = request.POST['color']
  borderColor = request.POST['borderColor']
  test = Graf.objects.get(id=id)
  test.jmeno_objektu = jmeno_objektu
  test.pocet_objektu = pocet_objektu
  test.color = color
  test.borderColor = borderColor
  test.save()
  return HttpResponseRedirect("/Pie/")

def upravit_objektBar(request, id):
  jmeno = request.POST['jmeno']
  pocet = request.POST['pocet']
  color = request.POST['color']
  borderColor = request.POST['borderColor']
  test = Bar.objects.get(id=id)
  test.jmeno = jmeno
  test.pocet = pocet
  test.color = color
  test.borderColor = borderColor
  test.save()
  return HttpResponseRedirect("/Bar/")