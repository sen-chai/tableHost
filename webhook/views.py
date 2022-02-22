from urllib.parse import quote_from_bytes
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        print(' -------------------')
        print("Data received from Webhook is: ", request.body)
        print(' -------------------')
        return HttpResponse("Webhook received!")

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from api.models import PedidoPendencia
from datetime import date

class WebhookEtapas(APIView):
    def post(self,request):
        r = json.loads(request.body)

        topic = r["topic"]
        id_pedido = r["event"]["idPedido"]
        numero_pedido = r["event"]["numeroPedido"]
        etapa = r["event"]["etapa"]
        author = r["author"]["name"]

        if etapa == "20":

            today = date.today()
            today = today.strftime("%d/%m/%Y")
            queryset = PedidoPendencia.objects.filter(liberado_por=author,data_liberado=today)

            return Response({'message':"webhook received"},status=status.HTTP_200_OK)