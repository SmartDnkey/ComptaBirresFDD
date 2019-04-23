
from django.views.generic import TemplateView
from ComptaBirres.models import Edicio, Birra, Tirador
from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import date
from ComptaBirres.controller import addNewBirra
import requests


class ApiView(TemplateView):
    template_name = ''

    def get(self, request):
        edicio = Edicio.objects.get(edicio=date.today().year)

        return HttpResponse(edicio.totalBirres)

class ApiTiradorView(TemplateView):
    template_name = ''

    def get(self, request):
        ip = request.META.get('REMOTE_ADDR')
        tirador = Tirador.objects.get(ip=ip)
        edicio = Edicio.objects.get(edicio=date.today().year)
        addNewBirra(tirador, edicio)

        return HttpResponse(tirador.totalBirresTirador)



class ComptaBirresView(TemplateView):

    template_name = 'ComptaBirres.html'


    def get(self, request):

        edicio = Edicio.objects.get(edicio=date.today().year)

        context = {'totalBirres': edicio.totalBirres,
                   'edicio': edicio.edicio,
                   'llista': list}
        return self.render_to_response(context)



class ComptaBirresClientView(TemplateView):

    template_name = 'Client.html'

    def get(self, request, *args, **kwargs):



        ip = request.META.get('REMOTE_ADDR')
        edicio = Edicio.objects.get(edicio=date.today().year)

        try:
            tirador = Tirador.objects.get(ip=ip)
        except:

            tirador = Tirador(ip=ip)
            tirador.save()


        context = {'totalBirresTirador': tirador.totalBirresTirador,
                   'tirador': tirador.name,
                   'ip': tirador.ip,

                   }

        return self.render_to_response(context)



