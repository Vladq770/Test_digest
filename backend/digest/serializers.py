from rest_framework import serializers

from core.serializers import UserSerializer, PostSerializer
from .models import Digest


class DigestSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Digest
        fields = "__all__"