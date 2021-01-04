from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from account.api.serializers import RegistrationSerializers
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def registration_view(request):

    serializer = RegistrationSerializers(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'successfully registered new user'
        data['email'] = account.email
        data['username'] = account.username
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)
