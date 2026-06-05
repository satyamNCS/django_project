from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.models import Subject
from service.Serializers import SubjectSerializers


class SubjectCtl(BaseRestCtl):
    def get_model(self):
        return Subject

    def get_serializer_class(self):
        return SubjectSerializers
