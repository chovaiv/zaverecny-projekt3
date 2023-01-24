from django.contrib import admin
from django.urls import include, path
from graf import views
from django.conf import settings
from django.conf.urls.static import static
from graf.views import Index
from graf.views import PieAndDoughnutChartView
from graf.views import BarChartView, Index, Test, Stacked
from django.contrib import admin
from django.urls import include, path
from graf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('Pie/', PieAndDoughnutChartView.as_view(template_name='grafy/pie.html')),
    path('Bar/', BarChartView.as_view(template_name='grafy/bar.html')),
    path('Line/', BarChartView.as_view(template_name='grafy/line.html')),

    path('Stacked/', Stacked.as_view(template_name='grafy/Stacked.html')),
    path('Pie/create/', views.create),
    path('Doughnut/create/', views.create),
    path('Bar/createBar/', views.createBar),
    path('Pie/delete/<int:id>/', views.delete, name='odstranit'),
    path('Doughnut/delete/<int:id>/', views.delete, name='odstranit'),
    path('Pie/update/<int:id>/', views.update),
    path('Doughnut/update/<int:id>/', views.update),
    path('Doughnut/', PieAndDoughnutChartView.as_view(template_name='grafy/doughnut.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Index.as_view, name='index'),
    path('Pie/pridat_objekt/', views.pridat_objekt, name='pridat_objekt'),
    path('Pie/odstranit/<int:id>/', views.odstranit, name='odstranit'),
    path('Pie/<int:id>', views.upravit_objekt, name='upravit_objekt'),
    path('test', Test.as_view(template_name='grafy/test.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    