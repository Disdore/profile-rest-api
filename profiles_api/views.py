from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        "Uses HTTP methods as function (grt, post, put, delete)",
        "Is similar to a tradional Django View",
        "Gives you the most control over you application logic",
        "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})


# Create your views here.
