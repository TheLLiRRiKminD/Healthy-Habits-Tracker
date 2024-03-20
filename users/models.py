from django.db import models
from django.contrib.auth.models import AbstractUser


# Определение модели пользователей, наследующей абстрактную модель пользователя
class Users(AbstractUser):
    # Убираем поле "username", так как мы будем использовать "email" вместо него
    username = None

    # Поле для хранения электронной почты пользователя (уникальное)
    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты пользователя")

    # Поле для хранения идентификатора чата (может быть пустым)
    chat_id = models.IntegerField(unique=True, blank=True, null=True, default=None)

    # Поле для хранения имени пользователя в Telegram (уникальное)
    telegram_user_name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    # Указываем, что поле "email" будет использоваться для идентификации пользователя
    USERNAME_FIELD = "email"

    # Поля, которые будут запрашиваться при создании пользователя через команду createsuperuser
    REQUIRED_FIELDS = []

    # Метод для представления модели в виде строки
    def __str__(self):
        return f"{self.email}"

    # Метаданные модели
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'
