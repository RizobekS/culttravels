from django.contrib import admin
from .models import CustomUserManager, User, Tours, MyTours, FAQ, Contact, Reservation


class ToursAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_uz', 'title_ru', 'value',
                    'english', 'russian', 'uzbek', 'date', 'views']

    list_editable = ['english', 'russian', 'uzbek', 'views']

    fields = ['title_uz', 'description_uz', 'image_uz', 'video_title_uz', 'video_uz',
              'title_en', 'description_en', 'image', 'video_title', 'video',
              'title_ru', 'description_ru', 'image_ru', 'video_title_ru', 'video_ru', 'value',
              'date', 'extra_img_one', 'extra_img_two', 'extra_img_three', 'extra_img_four', 'extra_img_five',
              'english', 'russian', 'uzbek']

    search_fields = ['title_en', 'title_uz', 'title_ru', 'value']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'received_date', 'replied_date', 'reply_subject',
                    'reply_message']
    search_fields = ['name', 'email', 'message']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['tours', 'name', 'email', 'message', 'received_date', 'replied_date', 'reply_subject',
                    'reply_message']
    search_fields = ['tours__title_en', 'name', 'email', 'message']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question_en', 'question_uz', 'question_ru', 'answer_en', 'answer_uz', 'answer_ru']
    search_fields = ['question_en', 'question_uz', 'question_ru']


admin.site.site_header = "Culttravels"
admin.site.register(MyTours)
admin.site.register(User)
admin.site.register(Tours, ToursAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(FAQ, FAQAdmin)
