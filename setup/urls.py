from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, ListEnrollmentByStudent, ListEnrollmentByCourse

router = routers.DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/enrollments/<int:pk>', ListEnrollmentByStudent.as_view()),
    path('courses/enrollments/<int:pk>', ListEnrollmentByCourse.as_view())
]
