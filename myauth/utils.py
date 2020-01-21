from .serializers import GetFullUserSerializer

def custom_jwt_response_handler(token, user=None, request=None):
    print("@@@@@@@@@@@@@@@@@@@@@@@@")
    print(token)
    print(user)
    print(request)
    return {
        'token': token,
        'user': GetFullUserSerializer(user, context={'request': request}).data
    }