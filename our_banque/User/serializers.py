from rest_framework import serializers
from .models import ManagementUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()

"""
this class (RegisterUserSerializer) transform the json data in django object and django object in json data
this class verify again the validity of data and when i'm using (get_user_model), the password will be hashed

"""
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta :
        model = ManagementUser
        fields = ["first_name","last_name","phone_number", "email","username","password"]
        extra_kwargs = {
            "password" : {"write_only":True}
        }
    def validated_data(self, value):
        if not value :
            raise ValidationError('all fields are required ')
        return value
    def create(self, validated_data):
        try :
            user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data["email"],
            username = validated_data["username"],
            password = validated_data["password"]
        )
            return user
        except ValidationError as e:
            raise ValidationError(str(e))
        except Exception as e:
            raise ValidationError(f"An error occurred: {str(e)}")

"""
this class make the authentication of user with email and password

"""
class AutheticateUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        try :
            email = data["email"]
            password = data["password"]
            user_authenticated = authenticate(
                email=email,
                password=password
            )
            if not user_authenticated :
                raise ValidationError("the email or password is invalid  :")
        except ValidationError as e :
            raise ValidationError(str(e))
    