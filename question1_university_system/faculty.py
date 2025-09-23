"""
Faculty classes for University Management System
Implements Faculty hierarchy with polymorphic behavior and workload calculation.
"""

from person import Person
from datetime import datetime
from typing import List, Dict, Optional


class Faculty(Person):
    """
    Base Faculty class representing all teaching staff.
    
    Attributes:
        faculty_id (str): Unique faculty identifier
        department (str): Department affiliation
        hire_date (datetime): Date of hiring
        salary (float): Annual salary
        office_location (str): Office room/building
        courses_taught (list): List of courses currently teaching
        office_hours (dict): Office hours schedule
    """
    
    def __init__(self, name, email, phone, department, salary=50000.0, office_location="", **kwargs):
        """
        Initialize a Faculty object.
        
        Args:
            name (str): Full name
            email (str): Email address
            phone (str): Phone number
            department (str): Department name
            salary (float, optional): Annual salary
            office_location (str, optional): Office location
            **kwargs: Additional arguments for Person class
        """
        super().__init__(name, email, phone, **kwargs)
        self._faculty_id = f"FAC{self.person_id}"
        self._department = self._validate_department(department)
        self._hire_date = datetime.now()
        self._salary = self._validate_salary(salary)
        self._office_location = office_location
        self._courses_taught = []
        self._office_hours = {}  # {'day': ['time_start', 'time_end']}
        self._research_interests = []
        self._publications = []
    
    # Properties with validation
    @property
    def faculty_id(self):
        """Get faculty ID (read-only)."""
        return self._faculty_id
    
    @property
    def department(self):
        """Get department."""
        return self._department
    
    @department.setter
    def department(self, value):
        """Set department with validation."""
        self._department = self._validate_department(value)
    
    @property
    def salary(self):
        """Get salary."""
        return self._salary
    
    @salary.setter
    def salary(self, value):
        """Set salary with validation."""
        self._salary = self._validate_salary(value)
    
    @property
    def office_location(self):
        """Get office location."""
        return self._office_location
    
    @office_location.setter
    def office_location(self, value):
        """Set office location."""
        self._office_location = value
    
    @property
    def courses_taught(self):
        """Get list of courses taught."""
        return self._courses_taught.copy()
    
    def _validate_department(self, department):
        """Validate department input."""
        if not department or not isinstance(department, str):
            raise ValueError("Department must be a non-empty string")
        return department.strip().title()
    
    def _validate_salary(self, salary):
        """Validate salary input."""
        try:
            salary_float = float(salary)
            if salary_float < 0:
                raise ValueError("Salary cannot be negative")
            return salary_float
        except (TypeError, ValueError):
            raise ValueError("Salary must be a valid number")
    
    def assign_course(self, course) -> bool:
        """
        Assign a course to this faculty member.
        
        Args:
            course: Course object to assign
            
        Returns:
            bool: True if assignment successful
        """
        try:
            if course.course_code in [c.course_code for c in self._courses_taught]:
                print(f"Already teaching {course.course_code}")
                return False
            
            self._courses_taught.append(course)
            course.instructor = self
            print(f"Assigned to teach {course.course_code}")
            return True
            
        except Exception as e:
            print(f"Course assignment failed: {e}")
            return False
    
    def remove_course(self, course_code: str) -> bool:
        """
        Remove a course assignment.
        
        Args:
            course_code (str): Course code to remove
            
        Returns:
            bool: True if removal successful
        """
        try:
            for course in self._courses_taught:
                if course.course_code == course_code:
                    self._courses_taught.remove(course)
                    course.instructor = None
                    print(f"Removed from teaching {course_code}")
                    return True
            
            print(f"Not currently teaching {course_code}")
            return False
            
        except Exception as e:
            print(f"Course removal failed: {e}")
            return False
    
    def set_office_hours(self, day: str, start_time: str, end_time: str):
        """
        Set office hours for a specific day.
        
        Args:
            day (str): Day of the week
            start_time (str): Start time (e.g., "10:00 AM")
            end_time (str): End time (e.g., "12:00 PM")
        """
        valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if day.title() not in valid_days:
            raise ValueError(f"Day must be one of: {valid_days}")
        
        self._office_hours[day.title()] = {'start': start_time, 'end': end_time}
    
    def add_research_interest(self, interest: str):
        """Add a research interest."""
        if interest and interest not in self._research_interests:
            self._research_interests.append(interest)
    
    def add_publication(self, title: str, journal: str = "", year: int = None):
        """Add a publication."""
        publication = {
            'title': title,
            'journal': journal,
            'year': year or datetime.now().year,
            'date_added': datetime.now()
        }
        self._publications.append(publication)