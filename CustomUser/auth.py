from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

CustomUser = get_user_model()


class EmailAndLoginAuthBackend(ModelBackend):
    """
    Проверяем есть ли пользователь с таким логином или емейлом,
    если такой пользователь есть -> логиним
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(Q(username=username) | Q(email__iexact=username))
            if user.check_password(password):
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
