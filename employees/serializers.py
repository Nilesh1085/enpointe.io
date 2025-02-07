from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_email(self, value):
        if self.instance is None:  # Only check uniqueness when creating
            if Employee.objects.filter(email=value).exists():
                raise serializers.ValidationError("Email must be unique.")
        return value


    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be a positive number.")
        return value
