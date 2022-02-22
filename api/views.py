from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .request_omie import omie_request_all_pages

class TestView(APIView):
    def get(self,request):
        return Response({"ola":"Mensagem de boas vidas"},status=status.HTTP_200_OK)

class ViewPedidos(APIView):
    #* somente pedidos entre as etapas

    def get(self,request):
        db = omie_request_all_pages(
            PAGE_SIZE=500,
            end_point='produtos/pedido/',
            call='ListarPedidos',
            extra_params={
                "apenas_importado_api":"N" ,
                "etapa": "20"
            },
            return_field='pedido_venda_produto'
        )

        final = []
        for pedido in db:
            item = {}
            item["cenario_fiscal"] = pedido["cabecalho"]["codigo_cenario_impostos"]
            item["cod_cliente"] = pedido["cabecalho"]["codigo_cliente"]
            item["cod_pedido"] = pedido["cabecalho"]["codigo_pedido"]
            item["etapa"] = pedido["cabecalho"]["etapa"]
            item["numero_pedido"] = pedido["cabecalho"]["numero_pedido"]
            dets = pedido["det"]

            for det in dets:
                item["codigo_produto"] = det["produto"]["codigo"]
                item["quantidade"] = det["produto"]["quantidade"]
                final.append(item)

        return Response(final,status=status.HTTP_200_OK)