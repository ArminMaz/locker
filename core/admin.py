from django.contrib import admin
from core.models import Entry, Member
from datetime import datetime


class EntryAdmin(admin.ModelAdmin):
    list_display = ['uid', 'date', 'approved', 'member']
    list_filter = ('date', 'approved', 'member')
    actions = ['sign_up_as_member']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def sign_up_as_member(self, request, queryset):
        for obj in queryset:
            approved = obj.approved
            print(approved)
            if not approved:
                uid = obj.uid
                print(uid)
                try:
                    member = Member.objects.get(uid=uid)
                except:
                    member = Member(uid=uid)
                    member.save()
    sign_up_as_member.short_description = "Sign up the selected UIDs as members."


class MemberAdmin(admin.ModelAdmin):
    list_display = ['uid', 'join_date', 'name', 'student_id']
    list_filter = ['join_date']


admin.site.register(Entry, EntryAdmin)
admin.site.register(Member, MemberAdmin)
