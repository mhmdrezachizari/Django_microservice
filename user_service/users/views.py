from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserCreateSerializer
from .producer import publish_user_created


@api_view(["POST"])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        # ارسال رویداد user.created به RabbitMQ
        event = {
            "event": "USER_CREATED",
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        publish_user_created(event)

        return Response({
            "status": "success",
            "user_id": user.id,
            "message": "User created and event published."
        }, status=201)

    return Response(serializer.errors, status=400)
