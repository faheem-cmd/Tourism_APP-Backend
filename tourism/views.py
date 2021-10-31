import users as users
from django.shortcuts import render
import status as status
from Demos.FileSecurityTest import permissions
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from .serializers import placesSerializer, RegisterSerializer, UserSerializer
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle
from .models import user, places
from .serializers import userSerializer
from .models import gallery
from .models import popular
from .serializers import popularSerializer
from .models import history
from .serializers import historySerializer
from .models import review
from .serializers import reviewSerializer

from .serializers import gallerySerializer

from .models import feedback
from .serializers import feedbackSerializer
from .models import slider
from .serializers import sliderSerializer
from .models import reels
from .serializers import reelsSerializer

from django.shortcuts import get_object_or_404

from .serializers import EmployeeSerializer
from .models import Employee

from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from drf_multiple_model.views import ObjectMultipleModelAPIView


class placesList(APIView):
    def get(self, request):
        places1 = places.objects.all()
        serializer = placesSerializer(places1, many=True, context={"request": request})
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self):
        pass


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "status": 200,
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })


class LoginAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        temp_list = super(LoginAPI, self).post(request, format=None)
        return Response({"status": 200, "data": temp_list.data})


class UserAPIView(APIView):
    serializer_class = userSerializer
    throttle_scope = "user_app"

    def get_queryset(self):
        User = user.objects.all()
        return User

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                User = user.objects.get(id=id)
                serializer = userSerializer(User)
        except:
            User = self.get_queryset()
            serializer = userSerializer(User, many=True)

        # return Response(serializer.data)
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user_data = request.data

        new_user = user.objects.create(name=user_data["name"], place=user_data[
            "place"], experience=user_data["experience"], rating=user_data["rating"],
                                       image=user_data["image"],profile=user_data["profile"])

        new_user.save()

        serializer = userSerializer(new_user)
        return Response(serializer.data)


class feedbackViews(APIView):
    def post(self, request):
        serializer = feedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class sliderList(APIView):
    def get(self, request):
        slider1 = slider.objects.all()
        serializer = sliderSerializer(slider1, many=True, context={"request": request})
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self):
        pass


class galleryList(APIView):
    def get(self, request):
        gallery1 = gallery.objects.all()
        serializer = gallerySerializer(gallery1, many=True, context={"request": request})
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self):
        pass


##CRUD OPERATIONS


class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class reelsList(APIView):
    def get(self, request):
        reels1 = reels.objects.all()
        serializer = reelsSerializer(reels1, many=True, context={"request": request})
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self):
        pass


class PopularAPIView(APIView):
    serializer_class = popularSerializer
    throttle_scope = "popular_app"

    def get_queryset(self):
        Popular = popular.objects.all()
        return Popular

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                Popular = popular.objects.get(id=id)
                serializer = popularSerializer(Popular)
        except:
            Popular = self.get_queryset()
            serializer = popularSerializer(Popular, many=True)

        # return Response(serializer.data)
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        popular_data = request.data

        new_popular = popular.objects.create(name=popular_data["name"], history=popular_data[
            "history"], )

        new_popular.save()

        serializer = popularSerializer(new_popular)
        return Response(serializer.data)




class HistoryAPIView(APIView):
    serializer_class = historySerializer
    throttle_scope = "history_app"

    def get_queryset(self):
        History = history.objects.all()
        return History

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                History = history.objects.get(id=id)
                serializer = historySerializer(History)
        except:
            History = self.get_queryset()
            serializer = historySerializer(History, many=True)

        # return Response(serializer.data)
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        history_data = request.data

        new_history = history.objects.create(name=history_data["name"],)

        new_history.save()

        serializer = historySerializer(new_history)
        return Response(serializer.data)



class ReviewAPIView(APIView):
    serializer_class = reviewSerializer
    throttle_scope = "review_app"

    def get_queryset(self):
        Review = review.objects.all()
        return Review

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                Review = review.objects.get(id=id)
                serializer = reviewSerializer(Review)
        except:
            Review = self.get_queryset()
            serializer = reviewSerializer(Review, many=True)

        # return Response(serializer.data)
        return Response({"status": 200, "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        review_data = request.data

        new_review = review.objects.create(comment=review_data["comment"],)

        new_review.save()

        serializer = reviewSerializer(new_review)
        return Response(serializer.data)
