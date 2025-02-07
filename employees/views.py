from rest_framework import generics, filters
from rest_framework.exceptions import NotFound
from .models import Employee
from .serializers import EmployeeSerializer
import logging


logger = logging.getLogger('django')

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'salary', 'joining_date']  # Fields to allow sorting
    
    def perform_create(self, serializer):
        employee = serializer.save()
        logger.info(f'New Employee Created: {employee.name} - {employee.email}')
        

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
    def get_object(self):
        try:
            return super().get_object()
        except Employee.DoesNotExist:
            raise NotFound(detail="Employee not found.", code=404)
