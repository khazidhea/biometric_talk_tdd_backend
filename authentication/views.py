from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import UserSerializer


@ensure_csrf_cookie
@api_view(['GET'])
def csrf(request: Request) -> Response:
    return Response({'details': 'CSRF cookie set'})


class RegisterApi(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
