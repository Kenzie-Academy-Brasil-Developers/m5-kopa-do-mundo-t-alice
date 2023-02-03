from msilib.schema import Error
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Team
from django.forms.models import model_to_dict
from .utils import data_processing


# Create your views here.
class TeamView(APIView):
    def post(self, request: Request):
        try:
            data_processing(request.data)
            my_team = Team.objects.create(**request.data)
            return Response(model_to_dict(my_team), status.HTTP_201_CREATED)

        except Exception as Error:
            return Response({"error": str(Error)}, status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        try:
            my_team = list(Team.objects.values())
            return Response(my_team, status.HTTP_200_OK)

        except:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)


class TeamDetailView(APIView):
    def get(self, request: Request, my_id):

        try:
            my_team = Team.objects.get(id=my_id)
            return Response(model_to_dict(my_team), status.HTTP_200_OK)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

    def patch(self, request: Request, my_id):

        try:
            my_data = request.data
            my_team = Team.objects.get(id=my_id)
            for key, value in my_data.items():
                setattr(my_team, key, value)
            my_team.save()
            return Response(model_to_dict(my_team))

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, my_id):

        try:
            my_team = Team.objects.get(id=my_id)
            my_team.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
