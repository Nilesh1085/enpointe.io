from django.test import TestCase
from employees.models import Employee
from rest_framework.test import APITestCase
from rest_framework import status


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Jay Pathare",
            email="jay.pathare@example.com",
            department="IT",
            salary=60000,
            joining_date="2023-06-01"
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, "Jay Pathare")
        self.assertEqual(self.employee.email, "jay.pathare@example.com")
        

class EmployeeAPITest(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Tanmay Guru",
            email="tanmay.guru@example.com",
            department="HR",
            salary=55000,
            joining_date="2022-09-15"
        )
        self.valid_payload = {
            "name": "New Employee",
            "email": "new.employee@example.com",
            "department": "Finance",
            "salary": 75000,
            "joining_date": "2024-02-06"
        }

    def test_get_employees(self):
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        response = self.client.post("/api/employees/", self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employee_by_id(self):
        response = self.client.get(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        updated_data = {"name": "Updated Tanmay", "email": "tanmay.guru@example.com", "department": "HR", "salary": 58000, "joining_date": "2022-09-15"}
        response = self.client.put(f"/api/employees/{self.employee.id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        response = self.client.delete(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)        
