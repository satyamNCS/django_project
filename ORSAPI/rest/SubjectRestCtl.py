from rest_framework.response import Response
from rest_framework.views import APIView
from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.models import Subject, Course
from service.Serializers import SubjectSerializers


class SubjectRestCtl(BaseRestCtl):
    def get_model(self):
        return Subject

    def get_serializer_class(self):
        return SubjectSerializers


class SubjectPreloadRestCtl(APIView):
    def get(self, _request):
        courses = [{"id": c.get_key(), "value": c.get_value()} for c in Course.objects.order_by("name")]
        data = {"courses": courses}
        return Response({"error": False, "message": "", "data": data})
