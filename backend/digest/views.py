from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import *


@api_view(['POST'])
def create_digest(request):
    mes, code = create_digest_service((request.query_params).dict())
    return Response(mes, code)