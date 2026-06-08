from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.models import College
from service.Serializers import CollegeSerializers


class CollegeRestCtl(BaseRestCtl):
    def get_model(self):
        return College

    def get_serializer_class(self):
        return CollegeSerializers
