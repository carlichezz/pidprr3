# views.py
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

class CustomAuthTokenView(ObtainAuthToken, ViewSet):
    @staticmethod
    def create(request):
        serializer = ObtainAuthToken().get_serializer(data=request.data,
                                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=status.HTTP_200_OK)
