from rest_framework import serializers
from school.models import Student, Course, Enrollment
from school.validators import is_name_valid, is_cpf_valid, is_phone_number_valid

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'cpf', 'birthday_date', 'phone_number']

    def validate(self, data):
        if is_name_valid(data['name']):
            raise serializers.ValidationError({'nome': 'Insira um nome sem caracteres especiais'})
        if is_cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf' : 'CPF inválido'})
        if is_phone_number_valid(data['phone_number']):
            raise serializers.ValidationError({'Numero de celular':'Insira um numero de telefone com o seguinte modelo: "99 99999-9999" '})
        return data

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []

class ListEnrollmentByStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source = 'course.description')
    period = serializers.SerializerMethodField()
    
    class Meta:
        model = Enrollment
        fields = ['course','period']

    def get_period(self, obj):
        return obj.get_period_display()
    
class ListEnrollmentByCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source = 'student.name')
    
    class Meta:
        model = Enrollment
        fields = ['student_name']