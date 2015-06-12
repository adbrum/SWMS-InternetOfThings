# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""

from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from iot.models import Sensor, ReadData


#from forms import AddEquipmentForm, FichaEquipmentForm
#from iot.models import Equipment, PhysicalCharacteristic, Voltage, Memory
def listSensors(request):
    """
    Lista todos os sensores de um equipamento registrado
    """
    
    TITULO = _(u'Equipamentos')
    
    try:
        sensores = Sensor.objects.all().order_by('name')
        tamLista = len(sensores)
    except:
        pass
    
    template = "sensor/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )


#@csrf_exempt
def sensor(request, *args, **kwargs):
    
    print'XXXXXXXXXXXXXXXXXXX: ',
    
    idSensor = kwargs["idSensor"]
    
    print'XXXXXXXXXXXXXXXXXXX ID SENSOR: ', idSensor
    
    #sensor = Sensor.objects.get(id = idSensor)
    
    #print'SENSOR DATA Sensor ID XXXXXXXXXXXXXXXXXXX: ', sensor.id
    if request.method == 'GET':
        try:
            sensorData = ReadData.objects.get(sensorId = idSensor)
        
            print'SENSOR DATA Sensor ID XXXXXXXXXXXXXXXXXXX: ', sensorData.sensorId
            idSensor = int(sensorData.sensorId)
            temp = int(sensorData.temperature)
            hum = int(sensorData.humidity)
        except:
            pass
        
        template = "sensorData/index.html"
        return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )
    #===========================================================================
    # template = "sensor/index.html"
    # return render_to_response(template,
    #                           locals(),
    #                           context_instance=RequestContext(request))
    #===========================================================================

