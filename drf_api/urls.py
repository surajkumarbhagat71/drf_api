from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register('studentapi',views.StudentViewSet,basename='student')
#router.register('student',views.Studentapi)
router.register('user',views.UserCreate,basename='user')



urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include(router.urls)),
    path('studentapi',views.StudentList.as_view(),name="studentlist"),
    path('studentapicreate',views.StudentCreate.as_view(),name="studentcreate"),
    path('studentapiretrive/<int:pk>',views.StudentReriave.as_view(),name="studentretrive"),
    path('studentapiupdate/<int:pk>',views.StudentUpdate.as_view(),name="studentupdate"),
]

