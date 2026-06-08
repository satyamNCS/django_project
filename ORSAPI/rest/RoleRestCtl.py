from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.models import Role
from service.Serializers import RoleSerializers


class RoleRestCtl(BaseRestCtl):
    def get_model(self):
        return Role

    def get_serializer_class(self):
        return RoleSerializers
