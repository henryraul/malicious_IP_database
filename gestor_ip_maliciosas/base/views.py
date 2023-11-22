#from django.contrib.auth import authenticate

from django.shortcuts import redirect
from rest_framework import status
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.views import Token
from rest_framework.authtoken.views import ObtainAuthToken
#from apps.users.api.serializers import UserTokenSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
       
        if login_serializer.is_valid():
            print("valido")
            user = login_serializer.validated_data['user']
            token,created = Token.objects.get_or_create(user = user)
            user_serializer = UserTokenSerializer(user)
            if not created:
                token.delete()
                token = Token.objects.create(user = user)

            return Response({'token':token.key,
                             'user': user_serializer.data,
                             },
                             status = status.HTTP_201_CREATED)
        else:
            return Response({'error':'Nombre de usuario o contrasena incorrectos'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Hola desde response'}, status=status.HTTP_200_OK)
            

def my_logout(request):
    logout(request)
    return redirect('/')


'''
from apps.users.api.serializers import (
    CustomTokenObtainPairSerializer, CustomUserSerializer
)
from apps.users.models import User

class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user = UserTokenSerializer().Meta.model.objects.filter(username = username).first())
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas'
            }, status = status.HTTP_400_BAD_REQUEST)

class Logout(APIView):

    def get(self,request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user

                all_session = Session.objects.filter(expire_date__gte = datetime.now())
 
                if all_session.exists():
        
                    for session in all_session:
                 
                        session_data = session.get_decoded()
                    
                        if user.id == int(session_data.get('_auth_user_id')):
                          
                            session.delete()
                          
            
                token.delete()
               

                session_message = 'Sesiones de usuarios eliminadas'
                token_message = 'Token eliminado'
                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_201_CREATED)
            return Response({'error': '34No se ha encontrado un usuario con estas credenciales'}, status = status.HTTP_201_CREATED)
                        
        except:
            return Response({'error': '->No se ha encontrado token en la peticion'}, status = status.HTTP_201_CREATED)

       '''



