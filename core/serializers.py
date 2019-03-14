from rest_framework import serializers
from .models import Member


class MemberCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class MemberDetailSerializer(serializers.ModelSerializer):
    entry = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='date'
    )

    class Meta:
        model = Member
        fields = ('name', 'student_id', 'uid', 'join_date', 'entry')


class UIDListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('uid', )

