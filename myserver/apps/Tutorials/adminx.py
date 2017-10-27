import xadmin
from .models import TutorialsTeacher,TutorialsVedio


class TutorialsTeacherAdmin(object):
    list_display = ["name", "imageUrl", "desc", "add_time"]
    list_filter = ["name", "add_time"]
    search_fields = ['name', ]


class TutorialsVedioAdmin(object):
    list_display = ["name", "htmlString", "click_num", "fav_num", "is_new", "is_hot", "add_time", "video_front_image"]
    list_filter = ["name", "add_time", "click_num", "fav_num", "is_new", "is_hot"]
    search_fields = ['name', ]


xadmin.site.register(TutorialsTeacher, TutorialsTeacherAdmin)
xadmin.site.register(TutorialsVedio, TutorialsVedioAdmin)