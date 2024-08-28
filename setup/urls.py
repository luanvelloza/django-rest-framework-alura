from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from school.views import StudentViewSet, CourseViewSet

router = routers.DefaultRouter()

router.register('students', StudentViewSet, 'students')
router.register('courses', CourseViewSet, 'courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
