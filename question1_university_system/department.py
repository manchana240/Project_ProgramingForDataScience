"""
Student classes for University Management System
Implements Student hierarchy with course enrollment and GPA tracking.
"""

from person import Person
from datetime import datetime
from typing import List, Dict, Optional


class Course:
    """
    Represents a university course.
    
    Attributes:
        course_code (str): Unique course identifier
        course_name (str): Name of the course
        credits (int): Number of credit hours
        prerequisites (list): List of prerequisite course codes
        max_enrollment (int): Maximum number of students
    """
    
    def __init__(self, course_code, course_name, credits, prerequisites=None, max_enrollment=30):
        """Initialize a Course object."""
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.prerequisites = prerequisites or []
        self.max_enrollment = max_enrollment
        self.enrolled_students = []
        self.instructor = None
    
    def __str__(self):
        return f"{self.course_code}: {self.course_name} ({self.credits} credits)"


class Student(Person):
    """
    Base Student class with enrollment and GPA tracking capabilities.
    
    Attributes:
        student_id (str): Unique student identifier
        major (str): Student's major field of study
        enrollment_date (datetime): Date of enrollment
        enrolled_courses (dict): Dictionary of enrolled courses with grades
        gpa_history (list): GPA history by semester
        academic_status (str): Current academic standing
    """
    
    def __init__(self, name, email, phone, major, **kwargs):
        """
        Initialize a Student object.
        
        Args:
            name (str): Full name
            email (str): Email address
            phone (str): Phone number
            major (str): Major field of study
            **kwargs: Additional arguments for Person class
        """
        super().__init__(name, email, phone, **kwargs)
        self._student_id = f"STU{self.person_id}"
        self._major = self._validate_major(major)
        self._enrollment_date = datetime.now()
        self._enrolled_courses = {}  # {course_code: {'course': Course, 'grade': float, 'semester': str}}
        self._gpa_history = []  # [{'semester': str, 'gpa': float, 'credits': int}]
        self._academic_status = "Good Standing"
        self._total_credits = 0
    
    # Properties with validation
    @property
    def student_id(self):
        """Get student ID (read-only)."""
        return self._student_id
    
    @property
    def major(self):
        """Get major."""
        return self._major
    
    @major.setter
    def major(self, value):
        """Set major with validation."""
        self._major = self._validate_major(value)
    
    @property
    def academic_status(self):
        """Get academic status."""
        return self._academic_status
    
    @property
    def total_credits(self):
        """Get total credits earned."""
        return self._total_credits
    
    def _validate_major(self, major):
        """Validate major input."""
        if not major or not isinstance(major, str):
            raise ValueError("Major must be a non-empty string")
        return major.strip().title()
    
    def _validate_grade(self, grade):
        """Validate grade input (0.0-4.0 scale)."""
        try:
            grade_float = float(grade)
            if not 0.0 <= grade_float <= 4.0:
                raise ValueError("Grade must be between 0.0 and 4.0")
            return grade_float
        except (TypeError, ValueError):
            raise ValueError("Grade must be a valid number between 0.0 and 4.0")
    
    def enroll_course(self, course: Course, semester: str = None) -> bool:
        """
        Enroll student in a course.
        
        Args:
            course (Course): Course object to enroll in
            semester (str, optional): Semester identifier
            
        Returns:
            bool: True if enrollment successful, False otherwise
        """
        try:
            # Check if already enrolled
            if course.course_code in self._enrolled_courses:
                print(f"Already enrolled in {course.course_code}")
                return False
            
            # Check enrollment limits
            if len(course.enrolled_students) >= course.max_enrollment:
                print(f"Course {course.course_code} is full")
                return False
            
            # Check prerequisites
            if not self._check_prerequisites(course.prerequisites):
                print(f"Prerequisites not met for {course.course_code}")
                return False
            
            # Enroll student
            semester = semester or self._get_current_semester()
            self._enrolled_courses[course.course_code] = {
                'course': course,
                'grade': None,
                'semester': semester,
                'status': 'Enrolled'
            }
            
            course.enrolled_students.append(self.student_id)
            print(f"Successfully enrolled in {course.course_code}")
            return True
            
        except Exception as e:
            print(f"Enrollment failed: {e}")
            return False
    
    def drop_course(self, course_code: str) -> bool:
        """
        Drop a course.
        
        Args:
            course_code (str): Code of the course to drop
            
        Returns:
            bool: True if drop successful, False otherwise
        """
        try:
            if course_code not in self._enrolled_courses:
                print(f"Not enrolled in course {course_code}")
                return False
            
            # Remove from enrolled courses
            course = self._enrolled_courses[course_code]['course']
            del self._enrolled_courses[course_code]
            
            # Remove from course enrollment list
            if self.student_id in course.enrolled_students:
                course.enrolled_students.remove(self.student_id)
            
            print(f"Successfully dropped {course_code}")
            return True
            
        except Exception as e:
            print(f"Drop failed: {e}")
            return False
    
    def add_grade(self, course_code: str, grade: float) -> bool:
        """
        Add grade for a completed course.
        
        Args:
            course_code (str): Course code
            grade (float): Grade on 4.0 scale
            
        Returns:
            bool: True if grade added successfully
        """
        try:
            if course_code not in self._enrolled_courses:
                print(f"Not enrolled in course {course_code}")
                return False
            
            validated_grade = self._validate_grade(grade)
            self._enrolled_courses[course_code]['grade'] = validated_grade
            self._enrolled_courses[course_code]['status'] = 'Completed'
            
            # Add credits to total
            course = self._enrolled_courses[course_code]['course']
            self._total_credits += course.credits
            
            print(f"Grade {validated_grade} added for {course_code}")
            return True
            
        except Exception as e:
            print(f"Adding grade failed: {e}")
            return False
    
    def calculate_gpa(self, semester: str = None) -> float:
        """
        Calculate GPA for a specific semester or overall.
        
        Args:
            semester (str, optional): Specific semester, None for overall GPA
            
        Returns:
            float: Calculated GPA
        """
        total_points = 0.0
        total_credits = 0
        
        for course_info in self._enrolled_courses.values():
            # Filter by semester if specified
            if semester and course_info['semester'] != semester:
                continue
            
            # Only count courses with grades
            if course_info['grade'] is not None:
                credits = course_info['course'].credits
                grade = course_info['grade']
                total_points += grade * credits
                total_credits += credits
        
        if total_credits == 0:
            return 0.0
        
        gpa = round(total_points / total_credits, 2)
        
        # Update GPA history if calculating overall GPA
        if semester is None:
            self._update_gpa_history(gpa, total_credits)
        
        return gpa
    
    def get_academic_status(self) -> str:
        """
        Determine academic status based on GPA.
        
        Returns:
            str: Academic status
        """
        current_gpa = self.calculate_gpa()
        
        if current_gpa >= 3.5:
            self._academic_status = "Dean's List"
        elif current_gpa >= 2.0:
            self._academic_status = "Good Standing"
        elif current_gpa >= 1.0:
            self._academic_status = "Academic Probation"
        else:
            self._academic_status = "Academic Suspension"
        
        return self._academic_status
    
    def _check_prerequisites(self, prerequisites: List[str]) -> bool:
        """Check if student has completed prerequisites."""
        if not prerequisites:
            return True
        
        completed_courses = [
            code for code, info in self._enrolled_courses.items()
            if info['grade'] is not None and info['grade'] >= 2.0
        ]
        
        return all(prereq in completed_courses for prereq in prerequisites)
    
    def _get_current_semester(self) -> str:
        """Get current semester identifier."""
        now = datetime.now()
        year = now.year
        if now.month >= 8:
            return f"Fall {year}"
        elif now.month >= 5:
            return f"Summer {year}"
        else:
            return f"Spring {year}"
    
    def _update_gpa_history(self, gpa: float, credits: int):
        """Update GPA history."""
        current_semester = self._get_current_semester()
        
        # Update or add current semester GPA
        for record in self._gpa_history:
            if record['semester'] == current_semester:
                record['gpa'] = gpa
                record['credits'] = credits
                return
        
        # Add new semester record
        self._gpa_history.append({
            'semester': current_semester,
            'gpa': gpa,
            'credits': credits
        })
    
    def get_transcript(self) -> Dict:
        """Get student transcript information."""
        return {
            'student_info': self.get_basic_info(),
            'major': self.major,
            'total_credits': self.total_credits,
            'current_gpa': self.calculate_gpa(),
            'academic_status': self.get_academic_status(),
            'courses': {
                code: {
                    'course_name': info['course'].course_name,
                    'credits': info['course'].credits,
                    'grade': info['grade'],
                    'semester': info['semester'],
                    'status': info['status']
                }
                for code, info in self._enrolled_courses.items()
            },
            'gpa_history': self._gpa_history
        }
    
    def get_responsibilities(self):
        """Get student responsibilities."""
        return [
            "Attend classes regularly",
            "Complete assignments and projects",
            "Maintain academic standards",
            "Follow university policies",
            f"Complete degree requirements in {self.major}"
        ]
    
    def get_role(self):
        """Get role type."""
        return "Student"


class UndergraduateStudent(Student):
    """
    Undergraduate student with specific requirements and limitations.
    
    Additional Attributes:
        class_year (str): Freshman, Sophomore, Junior, Senior
        max_credits_per_semester (int): Maximum credits allowed per semester
        advisor (str): Academic advisor name
    """
    
    def __init__(self, name, email, phone, major, class_year="Freshman", **kwargs):
        """Initialize UndergraduateStudent."""
        super().__init__(name, email, phone, major, **kwargs)
        self._student_id = f"UG{self.person_id}"
        self._class_year = class_year
        self._max_credits_per_semester = 18
        self._advisor = None
        self._graduation_requirements = {
            'min_credits': 120,
            'min_gpa': 2.0,
            'major_credits': 36
        }
    
    @property
    def class_year(self):
        """Get class year."""
        return self._class_year
    
    @class_year.setter
    def class_year(self, value):
        """Set class year with validation."""
        valid_years = ["Freshman", "Sophomore", "Junior", "Senior"]
        if value not in valid_years:
            raise ValueError(f"Class year must be one of: {valid_years}")
        self._class_year = value
    
    def calculate_workload(self) -> int:
        """Calculate current semester workload."""
        current_semester = self._get_current_semester()
        credits = sum(
            info['course'].credits
            for info in self._enrolled_courses.values()
            if info['semester'] == current_semester and info['status'] == 'Enrolled'
        )
        return credits
    
    def can_graduate(self) -> bool:
        """Check if student meets graduation requirements."""
        return (
            self.total_credits >= self._graduation_requirements['min_credits'] and
            self.calculate_gpa() >= self._graduation_requirements['min_gpa']
        )
    
    def get_role(self):
        """Get role type."""
        return f"Undergraduate Student ({self.class_year})"


class GraduateStudent(Student):
    """
    Graduate student with research focus and thesis requirements.
    
    Additional Attributes:
        degree_type (str): Masters or PhD
        thesis_advisor (str): Research advisor
        thesis_topic (str): Research topic
        committee_members (list): Thesis committee members
    """
    
    def __init__(self, name, email, phone, major, degree_type="Masters", **kwargs):
        """Initialize GraduateStudent."""
        super().__init__(name, email, phone, major, **kwargs)
        self._student_id = f"GR{self.person_id}"
        self._degree_type = degree_type
        self._thesis_advisor = None
        self._thesis_topic = None
        self._committee_members = []
        self._research_credits = 0
        
        # Different requirements based on degree type
        if degree_type == "PhD":
            self._graduation_requirements = {
                'min_credits': 72,
                'min_gpa': 3.0,
                'research_credits': 24
            }
        else:  # Masters
            self._graduation_requirements = {
                'min_credits': 36,
                'min_gpa': 3.0,
                'research_credits': 6
            }
    
    @property
    def degree_type(self):
        """Get degree type."""
        return self._degree_type
    
    @property
    def thesis_advisor(self):
        """Get thesis advisor."""
        return self._thesis_advisor
    
    @thesis_advisor.setter
    def thesis_advisor(self, advisor):
        """Set thesis advisor."""
        self._thesis_advisor = advisor
    
    def calculate_workload(self) -> Dict:
        """Calculate graduate student workload including research."""
        coursework_credits = sum(
            info['course'].credits
            for info in self._enrolled_courses.values()
            if 'Research' not in info['course'].course_name
        )
        
        research_credits = sum(
            info['course'].credits
            for info in self._enrolled_courses.values()
            if 'Research' in info['course'].course_name
        )
        
        return {
            'coursework_credits': coursework_credits,
            'research_credits': research_credits,
            'total_credits': coursework_credits + research_credits
        }
    
    def can_graduate(self) -> bool:
        """Check if graduate student meets graduation requirements."""
        workload = self.calculate_workload()
        return (
            self.total_credits >= self._graduation_requirements['min_credits'] and
            self.calculate_gpa() >= self._graduation_requirements['min_gpa'] and
            workload['research_credits'] >= self._graduation_requirements['research_credits']
        )
    
    def get_role(self):
        """Get role type."""
        return f"Graduate Student ({self._degree_type})"
    
    def get_responsibilities(self):
        """Get graduate student responsibilities."""
        base_responsibilities = super().get_responsibilities()
        grad_responsibilities = [
            "Conduct original research",
            "Work with thesis advisor",
            "Present research findings",
            "Complete thesis/dissertation"
        ]
        return base_responsibilities + grad_responsibilities


class SecureStudentRecord:
    """
    Secure wrapper for student records with enhanced validation and access control.
    
    This class demonstrates encapsulation principles with strict data validation
    and controlled access to student information.
    """
    
    def __init__(self, student: Student):
        """
        Initialize secure student record.
        
        Args:
            student (Student): Student object to secure
        """
        if not isinstance(student, Student):
            raise ValueError("Must provide a valid Student object")
        
        self._student = student
        self._access_log = []
        self._locked = False
        self._max_enrollment_limit = 20
    
    def get_student_info(self, requester_id: str) -> Optional[Dict]:
        """
        Get student information with access logging.
        
        Args:
            requester_id (str): ID of the person requesting information
            
        Returns:
            Dict: Student information if authorized
        """
        if self._locked:
            raise PermissionError("Student record is locked")
        
        self._log_access(requester_id, "info_access")
        return self._student.get_basic_info()
    
    def enroll_course_secure(self, course: Course, requester_id: str, semester: str = None) -> bool:
        """
        Secure course enrollment with additional validations.
        
        Args:
            course (Course): Course to enroll in
            requester_id (str): ID of person making the request
            semester (str, optional): Semester for enrollment
            
        Returns:
            bool: True if enrollment successful
        """
        try:
            # Check enrollment limits
            current_courses = len([
                info for info in self._student._enrolled_courses.values()
                if info['status'] == 'Enrolled'
            ])
            
            if current_courses >= self._max_enrollment_limit:
                raise ValueError(f"Cannot exceed {self._max_enrollment_limit} courses")
            
            # Check academic standing
            if self._student.get_academic_status() == "Academic Suspension":
                raise ValueError("Cannot enroll while on academic suspension")
            
            self._log_access(requester_id, f"course_enrollment_{course.course_code}")
            return self._student.enroll_course(course, semester)
            
        except Exception as e:
            self._log_access(requester_id, f"enrollment_failed_{e}")
            print(f"Secure enrollment failed: {e}")
            return False
    
    def update_gpa_secure(self, course_code: str, grade: float, requester_id: str) -> bool:
        """
        Secure GPA update with validation.
        
        Args:
            course_code (str): Course code
            grade (float): Grade to assign
            requester_id (str): ID of person making the request
            
        Returns:
            bool: True if update successful
        """
        try:
            # Additional validation for grade changes
            if grade < 0.0 or grade > 4.0:
                raise ValueError("Grade must be between 0.0 and 4.0")
            
            self._log_access(requester_id, f"grade_update_{course_code}_{grade}")
            return self._student.add_grade(course_code, grade)
            
        except Exception as e:
            self._log_access(requester_id, f"grade_update_failed_{e}")
            print(f"Secure grade update failed: {e}")
            return False
    
    def lock_record(self, requester_id: str):
        """Lock the student record to prevent modifications."""
        self._locked = True
        self._log_access(requester_id, "record_locked")
    
    def unlock_record(self, requester_id: str):
        """Unlock the student record."""
        self._locked = False
        self._log_access(requester_id, "record_unlocked")
    
    def _log_access(self, requester_id: str, action: str):
        """Log access to student record."""
        self._access_log.append({
            'timestamp': datetime.now(),
            'requester_id': requester_id,
            'action': action,
            'student_id': self._student.student_id
        })
    
    def get_access_log(self, requester_id: str) -> List[Dict]:
        """Get access log (administrative function)."""
        self._log_access(requester_id, "access_log_viewed")
        return self._access_log.copy()
    
    @property
    def is_locked(self) -> bool:
        """Check if record is locked."""
        return self._locked