
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.request_omie import omie_request_all_pages

class Updates(APIView):
    # serializer_class = ''
    # lookup_url_kwarg = 'entitiy'
    def post(self,request):
        all = omie_request_all_pages(
            PAGE_SIZE=500,
            end_point='geral/clientes/',
            call='ListarClientes',
            extra_params={
                "apenas_importado_api": "N",
                # "exibir_caracteristicas": "S"
            },
            return_field='clientes_cadastro'
        )

