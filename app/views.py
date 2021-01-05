from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *

# Create your views here.

@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")


    user = authenticate(username=username, password=password)

    request.session["username"] = username

    if user is not None:
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            user_id =token.user_id
            try:
                admin_data =Adminmodel.objects.filter(user=user_id).values('id', 'adminid').get()

                if admin_data:
                    u_id = admin_data['adminid']
                    id_value = admin_data['id']

                else:
                    u_id = None
                    id_value = None

                admin_id = u_id
                admin_id_value = id_value

            except Adminmodel.DoesNotExist:
                admin_id = None
                admin_id_value = None

            user_object = User.objects.filter(id=token.user_id).values('username', 'is_active', 'is_staff'
                                                                       , 'last_name', 'first_name', 'email').get()

            request.session['auth'] = token.key

            return Response({"success": "login successfully", "token": token.key, "user_id": user_id, "admin_id_value": admin_id_value,
                             "admin_id": admin_id, "user_object": user_object})

    else:
        return Response({"error": "Invalid Username & Password"}, status=HTTP_401_UNAUTHORIZED)


# Adminmodel
class AdminmodelCreateAPIView(CreateAPIView):
    '''Create Adminmodel table'''
    queryset = Adminmodel.objects.all()
    serializer_class = AdminmodelSerializer
    authentication_classes = (TokenAuthentication,)


class AdminmodelRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    '''Retrieve, update and delete Adminmodel table'''
    queryset = Adminmodel.objects.all()
    serializer_class = AdminmodelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'adminid'

    def perform_update(self, serializer):
        return super(AdminmodelRetrieveAPIView, self).perform_update(serializer)

    def destroy(self, request, adminid):
        Adminmodel.objects.filter(adminid=adminid).delete()
        return Response(Adminmodel.objects.filter(adminid=adminid).values())


# Usermodel
class UsermodelCreateAPIView(CreateAPIView):
    '''Create Usermodel table'''
    queryset = Usermodel.objects.all()
    serializer_class = UsermodelSerializer
    authentication_classes = (TokenAuthentication,)


class UsermodelRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    '''Retrieve, update and delete Usermodel table'''
    queryset = Usermodel.objects.all()
    serializer_class = UsermodelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'userid'

    def perform_update(self, serializer):
        return super(UsermodelRetrieveAPIView, self).perform_update(serializer)

    def destroy(self, request, userid):
        Adminmodel.objects.filter(userid=userid).delete()
        return Response(Adminmodel.objects.filter(userid=userid).values())


# Movies

class MoviesCreateAPIView(CreateAPIView):
    '''Create Movies table.'''
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class MoviesListAPIView(ListAPIView):
    '''List the Movies'''
    queryset = Movies.objects.filter(is_active=True)
    serializer_class = MoviesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class MoviesRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    '''Retrieve, update and delete Movies table.'''
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'movieid'

    def perform_update(self, serializer):
        return super(MoviesRetrieveAPIView, self).perform_update(serializer)

    def destroy(self, request, movieid):
        Movies.objects.filter(movieid=movieid).update(is_active=False)
        return Response(Movies.objects.filter(movieid=movieid).values())
