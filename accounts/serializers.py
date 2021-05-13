from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'user_type',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        if (validated_data['user_type'] == 'TEACH'):
            group = Group.objects.get(name__iexact='teacher')
            user.groups.add(group)
        else:
            group = Group.objects.get(name__iexact='student')
            user.groups.add(group)
        user.save()
        # print(validated_data)
        # print(**validated_data)
        profile = UserProfile.objects.create(user=user,  **validated_data)
        profile.save()
        return profile
