from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from api.v1.user.serializers import UserRegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """회원가입"""

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    """로그인"""

    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # `검증데이터`에서 값 가져오기
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # `아이디(이메일)`로 회원여부 확인
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print('User not found')
            raise AuthenticationFailed('User not found')

        # `비밀번호` 일치여부 확인
        if not user.check_password(password):
            print('Incorrect password')
            raise AuthenticationFailed('Incorrect password')

        # `유저`가 존재하고, `비밀번호`가 일치하면, `토큰` 발행
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
