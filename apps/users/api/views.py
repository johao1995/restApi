from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from apps.users.models import User
from rest_framework import status

# decorator
from rest_framework.decorators import api_view

@api_view(['GET'])
def ListUser(request):
    if request.method == "GET":
        user = User.objects.all()
        user_serializer = UserSerializer(instance=user, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def DetailUser(request,pk):
    user=User.objects.filter(pk=pk).first()
    if user is not None:
        user_serializer=UserSerializer(user)
        return Response({
                "message":f"Deatil User {user.email}",
                "data":user_serializer.data
            },status=status.HTTP_200_OK)
    else:
        return Response({"message":f"No existe codigo {pk}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def CreateUser(request):
    if request.method == "POST":
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                "message": "Created",
                "data": user_serializer.data
            })
        else:
            return Response({
                "message":user_serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def UpdateUser(request,pk):
    user=User.objects.filter(pk=pk).first()
    if user is not None:
        user_serializer=UserSerializer(instance=user,data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                "message":f"Actualizado {user.email}"
            },status=status.HTTP_200_OK)
        else:
            return Response({
                "messafe":user_serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            "message":f"No existe el usuario con codigo:{pk}"
        },status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteUser(request,pk):
    user=User.objects.filter(pk=pk).first()
    if user is not None:
        user.delete()
        return Response({
            "message":f"Usuario elimiand {user}"
        })
    else:
        return Response({
            "message":"Error no existe el codigo {pk}"
        })

