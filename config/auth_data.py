# Данные для авторизации с зарегистрированным пользователем
import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
valid_password_for_phone = os.getenv('valid_password_for_phone')
valid_login = os.getenv('valid_login')
new_valid_password = os.getenv('new_valid_password')