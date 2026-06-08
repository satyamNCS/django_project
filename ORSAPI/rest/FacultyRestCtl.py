from rest_framework.response import Response
from rest_framework.views import APIView
from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.models import Faculty, College, Course
from service.Serializers import FacultySerializers


class FacultyRestCtl(BaseRestCtl):
    def get_model(self):
        return Faculty

    def get_serializer_class(self):
        return FacultySerializers


class FacultyPreloadRestCtl(APIView):
    def get(self, _request):
        data = {
            "colleges": [{"id": c.get_key(), "value": c.get_value()} for c in College.objects.order_by("name")],
            "courses":  [{"id": c.get_key(), "value": c.get_value()} for c in Course.objects.order_by("name")],
        }
        return Response({"error": False, "message": "", "data": data})
