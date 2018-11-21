from core.models import User
from django.http import JsonResponse
from api.functions import string_to_boolean
from core.serializers import UserSerializerView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions 


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def get_user_detail_view(request,id):
    try :
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        data = {
                "success" : False,
                "errors" : "User is invalid"
        }
        return Response(data)
    else:
        serializer = UserSerializerView(user)
        return Response(serializer.data)
