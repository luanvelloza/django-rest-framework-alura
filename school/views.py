from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListEnrollmentByStudentSerializer, ListEnrollmentByCourseSerializer, StudentSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from school.throttles import EnrollmentAnonRateThrottle

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    #serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'cpf']
    search_fields = ['name', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    throttle_classes = [UserRateThrottle, EnrollmentAnonRateThrottle]
    queryset = Enrollment.objects.all().order_by('id')
    serializer_class = EnrollmentSerializer

class ListEnrollmentByStudent(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListEnrollmentByStudentSerializer

class ListEnrollmentByCourse(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListEnrollmentByCourseSerializer
