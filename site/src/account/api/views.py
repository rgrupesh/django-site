from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from account.api.serializers import RegistrationSerializers


@api_view(['POST',])
def registration_view(request):

    serializer = RegistrationSerializers(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'successfully registered new user'
        data['email'] = account.email
        data['username'] = account.username
    else:
        data = serializer.errors
    return Response(data)

