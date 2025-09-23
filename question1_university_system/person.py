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