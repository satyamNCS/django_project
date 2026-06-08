from rest_framework.response import Response
from rest_framework.views import APIView
from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.models import Student, College
from service.Serializers import StudentSerializers


class StudentRestCtl(BaseRestCtl):
    def get_model(self):
        return Student

    def get_serializer_class(self):
        return StudentSerializers


class StudentPreloadRestCtl(APIView):
    def get(self, _request):
        colleges = [{"id": c.get_key(), "value": c.get_value()} for c in College.objects.order_by("name")]
        data = {"colleges": colleges}
        return Response({"error": False, "message": "", "data": data})
