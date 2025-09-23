"""
Person class for University Management System
Implements the foundation for all person types in the university system.
"""

from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Person(ABC):
    """
    Abstract base class representing a person in the university system.
    
    Attributes:
        person_id (str): Unique identifier for the person
        name (str): Full name of the person
        email (str): Email address
        phone (str): Phone number
        date_of_birth (datetime): Date of birth
        address (str): Physical address
    """
    
    def __init__(self, name, email, phone, date_of_birth=None, address=""):
        """
        Initialize a Person object.
        
        Args:
            name (str): Full name of the person
            email (str): Email address
            phone (str): Phone number
            date_of_birth (datetime, optional): Date of birth
            address (str, optional): Physical address
        """
        self._person_id = str(uuid.uuid4())[:8]  # Generate unique ID
        self._name = self._validate_name(name)
        self._email = self._validate_email(email)
        self._phone = phone
        self._date_of_birth = date_of_birth
        self._address = address
        self._created_at = datetime.now()
    
    # Property getters and setters for encapsulation
    @property
    def person_id(self):
        """Get person ID """
        return self._person_id
    
    @property
    def name(self):
        """Get person name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set person name with validation."""
        self._name = self._validate_name(value)
    
    @property
    def email(self):
        """Get email address."""
        return self._email
    
    @email.setter
    def email(self, value):
        """Set email with validation."""
        self._email = self._validate_email(value)
    
    @property
    def phone(self):
        """Get phone number."""
        return self._phone
    
    @phone.setter
    def phone(self, value):
        """Set phone number."""
        self._phone = value
    
    @property
    def address(self):
        """Get address."""
        return self._address
    
    @address.setter
    def address(self, value):
        """Set address."""
        self._address = value
    
    # Validation methods
    def _validate_name(self, name):
        """Validate name input."""
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if len(name.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return name.strip().title()
    
    def _validate_email(self, email):
        """Basic email validation."""
        if not email or "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        return email.lower().strip()
    
    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def get_responsibilities(self):
        """Get the responsibilities of this person type."""
        pass
    
    @abstractmethod
    def get_role(self):
        """Get the role/type of this person."""
        pass
    
    def get_basic_info(self):
        """Get basic information about the person."""
        return {
            'person_id': self.person_id,
            'name': self.name,
            'email': self.email,
            'role': self.get_role(),
            'created_at': self._created_at.strftime('%Y-%m-%d')
        }
    
    def __str__(self):
        """String representation of the person."""
        return f"{self.get_role()}: {self.name} (ID: {self.person_id})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"{self.__class__.__name__}(name='{self.name}', email='{self.email}')"
    
    # Staff class - inherits from Person
class Staff(Person):
    """
    Represents staff members in the university.
    
    Attributes:
        staff_id (str): Unique staff identifier
        department (str): Department where staff works
        position (str): Job position/title
        salary (float): Annual salary
        hire_date (datetime): Date of hiring
    """
    
    def __init__(self, name, email, phone, department, position, salary=0.0, **kwargs):
        """
        Initialize a Staff object.
        
        Args:
            name (str): Full name
            email (str): Email address
            phone (str): Phone number
            department (str): Department name
            position (str): Job position
            salary (float, optional): Annual salary
            **kwargs: Additional arguments for Person class
        """
        super().__init__(name, email, phone, **kwargs)
        self._staff_id = f"STF{self.person_id}"
        self._department = department
        self._position = position
        self._salary = self._validate_salary(salary)
        self._hire_date = datetime.now()
    
    @property
    def staff_id(self):
        """Get staff ID (read-only)."""
        return self._staff_id
    
    @property
    def department(self):
        """Get department."""
        return self._department
    
    @department.setter
    def department(self, value):
        """Set department."""
        if not value or not isinstance(value, str):
            raise ValueError("Department must be a non-empty string")
        self._department = value
    
    @property
    def position(self):
        """Get position."""
        return self._position
    
    @position.setter
    def position(self, value):
        """Set position."""
        if not value or not isinstance(value, str):
            raise ValueError("Position must be a non-empty string")
        self._position = value
    
    @property
    def salary(self):
        """Get salary."""
        return self._salary
    
    @salary.setter
    def salary(self, value):
        """Set salary with validation."""
        self._salary = self._validate_salary(value)
    
    def _validate_salary(self, salary):
        """Validate salary input."""
        try:
            salary_float = float(salary)
            if salary_float < 0:
                raise ValueError("Salary cannot be negative")
            return salary_float
        except (TypeError, ValueError):
            raise ValueError("Salary must be a valid number")
    
    def get_responsibilities(self):
        """Get staff responsibilities."""
        return [
            f"Administrative duties in {self.department}",
            f"Support {self.position} operations",
            "Maintain university standards",
            "Assist students and faculty"
        ]
    
    def get_role(self):
        """Get role type."""
        return "Staff"
    
    def get_work_info(self):
        """Get work-related information."""
        return {
            'staff_id': self.staff_id,
            'department': self.department,
            'position': self.position,
            'salary': self.salary,
            'hire_date': self._hire_date.strftime('%Y-%m-%d')
        }
    
    def __str__(self):
        """String representation."""
        return f"Staff: {self.name} - {self.position} in {self.department}"