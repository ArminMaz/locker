from rest_framework import serializers
from .models import Member, Entry
from datetime import datetime

# class MemberCreateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Member
#         fields = '__all__'

#
# class MemberDetailSerializer(serializers.ModelSerializer):
#     entry = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='date'
#     )
#
#     class Meta:
#         model = Member
#         fields = ('name', 'student_id', 'uid', 'join_date', 'entry')


class EntrySerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField

    class Meta:
        model = Entry
        fields = ('member', 'uid', 'date', 'approved')

    def create(self, validated_data):
        approved = validated_data['approved']
        uid = validated_data['uid']
        date = datetime.now()
        try:
            member = Member.objects.get(uid=uid)
            return Entry.objects.create(member=member, uid=uid, approved=approved, date=date)
        except:
            return Entry.objects.create(member=None, uid=uid, approved=approved, date=date)


class UIDListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('uid', )

