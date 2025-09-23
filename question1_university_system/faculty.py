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

    # Abstract methods to be overridden by subclasses
    def calculate_workload(self) -> Dict:
        """Calculate faculty workload (to be overridden)."""
        return {
            'courses': len(self._courses_taught),
            'total_students': sum(len(course.enrolled_students) for course in self._courses_taught),
            'workload_type': 'Base Faculty'
        }
    
    def get_responsibilities(self):
        """Get faculty responsibilities."""
        return [
            "Teach assigned courses",
            "Conduct research in field of expertise",
            "Serve on university committees",
            "Maintain office hours for students",
            f"Contribute to {self.department} department goals"
        ]
    
    def get_role(self):
        """Get role type."""
        return "Faculty"
    
    def get_faculty_info(self) -> Dict:
        """Get comprehensive faculty information."""
        return {
            'basic_info': self.get_basic_info(),
            'faculty_id': self.faculty_id,
            'department': self.department,
            'salary': self.salary,
            'office_location': self.office_location,
            'hire_date': self._hire_date.strftime('%Y-%m-%d'),
            'courses_taught': [course.course_code for course in self._courses_taught],
            'office_hours': self._office_hours,
            'research_interests': self._research_interests,
            'publications_count': len(self._publications),
            'workload': self.calculate_workload()
        }


class Professor(Faculty):
    """
    Full Professor with research and administrative responsibilities.
    
    Additional Attributes:
        tenure_status (bool): Whether professor has tenure
        research_grants (list): Active research grants
        phd_students (list): PhD students being supervised
        committees (list): University committees served on
    """
    
    def __init__(self, name, email, phone, department, salary=80000.0, tenure_status=False, **kwargs):
        """Initialize Professor."""
        super().__init__(name, email, phone, department, salary, **kwargs)
        self._faculty_id = f"PROF{self.person_id}"
        self._tenure_status = tenure_status
        self._research_grants = []
        self._phd_students = []
        self._committees = []
        self._max_courses_per_semester = 2  # Professors typically teach fewer courses
        self._administrative_role = None
    
    @property
    def tenure_status(self):
        """Get tenure status."""
        return self._tenure_status
    
    @tenure_status.setter
    def tenure_status(self, value):
        """Set tenure status."""
        if not isinstance(value, bool):
            raise ValueError("Tenure status must be boolean")
        self._tenure_status = value
    
    def add_research_grant(self, title: str, amount: float, funding_agency: str):
        """Add a research grant."""
        grant = {
            'title': title,
            'amount': amount,
            'funding_agency': funding_agency,
            'date_awarded': datetime.now()
        }
        self._research_grants.append(grant)
    
    def supervise_phd_student(self, student_id: str):
        """Add a PhD student to supervision list."""
        if student_id not in self._phd_students:
            self._phd_students.append(student_id)
    
    def join_committee(self, committee_name: str):
        """Join a university committee."""
        if committee_name not in self._committees:
            self._committees.append(committee_name)
    
    def calculate_workload(self) -> Dict:
        """Calculate professor workload including research and service."""
        base_workload = super().calculate_workload()
        
        # Professors have research and service responsibilities
        research_load = len(self._research_grants) * 10 + len(self._phd_students) * 5
        service_load = len(self._committees) * 3
        
        return {
            **base_workload,
            'research_grants': len(self._research_grants),
            'phd_students': len(self._phd_students),
            'committees': len(self._committees),
            'research_load_points': research_load,
            'service_load_points': service_load,
            'total_load_points': base_workload['courses'] * 20 + research_load + service_load,
            'workload_type': 'Professor'
        }
    
    def get_responsibilities(self):
        """Get professor-specific responsibilities."""
        base_responsibilities = super().get_responsibilities()
        prof_responsibilities = [
            "Lead research projects and secure funding",
            "Supervise graduate students and postdocs",
            "Publish research in peer-reviewed journals",
            "Serve on university and professional committees",
            "Mentor junior faculty members"
        ]
        return base_responsibilities + prof_responsibilities
    
    def get_role(self):
        """Get role type."""
        tenure_str = "Tenured" if self._tenure_status else "Non-Tenured"
        return f"Professor ({tenure_str})"


class Lecturer(Faculty):
    """
    Lecturer focused primarily on teaching.
    
    Additional Attributes:
        contract_type (str): Full-time, Part-time, or Adjunct
        teaching_load (int): Number of courses per semester
        professional_experience (list): Industry experience
    """
    
    def __init__(self, name, email, phone, department, contract_type="Full-time", salary=55000.0, **kwargs):
        """Initialize Lecturer."""
        super().__init__(name, email, phone, department, salary, **kwargs)
        self._faculty_id = f"LECT{self.person_id}"
        self._contract_type = self._validate_contract_type(contract_type)
        self._teaching_load = 4 if contract_type == "Full-time" else 2
        self._professional_experience = []
        self._student_evaluations = []
        
        # Set course limits based on contract type
        if contract_type == "Full-time":
            self._max_courses_per_semester = 4
        elif contract_type == "Part-time":
            self._max_courses_per_semester = 2
        else:  # Adjunct
            self._max_courses_per_semester = 1
    
    @property
    def contract_type(self):
        """Get contract type."""
        return self._contract_type
    
    @property
    def teaching_load(self):
        """Get teaching load."""
        return self._teaching_load
    
    def _validate_contract_type(self, contract_type):
        """Validate contract type."""
        valid_types = ["Full-time", "Part-time", "Adjunct"]
        if contract_type not in valid_types:
            raise ValueError(f"Contract type must be one of: {valid_types}")
        return contract_type
    
    def add_professional_experience(self, company: str, position: str, years: int):
        """Add professional experience."""
        experience = {
            'company': company,
            'position': position,
            'years': years,
            'date_added': datetime.now()
        }
        self._professional_experience.append(experience)
    
    def add_student_evaluation(self, course_code: str, rating: float, comments: str = ""):
        """Add student evaluation."""
        if not 1.0 <= rating <= 5.0:
            raise ValueError("Rating must be between 1.0 and 5.0")
        
        evaluation = {
            'course_code': course_code,
            'rating': rating,
            'comments': comments,
            'semester': self._get_current_semester(),
            'date': datetime.now()
        }
        self._student_evaluations.append(evaluation)
    
    def get_average_evaluation(self) -> float:
        """Get average student evaluation rating."""
        if not self._student_evaluations:
            return 0.0
        
        total_rating = sum(eval['rating'] for eval in self._student_evaluations)
        return round(total_rating / len(self._student_evaluations), 2)
    
    def calculate_workload(self) -> Dict:
        """Calculate lecturer workload focused on teaching."""
        base_workload = super().calculate_workload()
        
        # Lecturers have heavier teaching loads
        teaching_intensity = sum(len(course.enrolled_students) for course in self._courses_taught)
        
        return {
            **base_workload,
            'contract_type': self._contract_type,
            'teaching_load': self._teaching_load,
            'teaching_intensity': teaching_intensity,
            'average_evaluation': self.get_average_evaluation(),
            'total_evaluations': len(self._student_evaluations),
            'workload_type': 'Lecturer'
        }
    
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
    
    def get_responsibilities(self):
        """Get lecturer-specific responsibilities."""
        base_responsibilities = super().get_responsibilities()
        lecturer_responsibilities = [
            "Focus primarily on teaching excellence",
            "Develop and update course materials",
            "Provide extensive student support and tutoring",
            "Participate in curriculum development",
            "Maintain industry connections and practical knowledge"
        ]
        return base_responsibilities + lecturer_responsibilities
    
    def get_role(self):
        """Get role type."""
        return f"Lecturer ({self._contract_type})"


class TA(Faculty):
    """
    Teaching Assistant - typically graduate students with teaching duties.
    
    Additional Attributes:
        student_status (bool): Whether TA is also a student
        supervising_professor (str): Professor they work under
        ta_level (str): Undergraduate, Masters, or PhD level TA
        courses_assisting (list): Courses they assist with
    """
    
    def __init__(self, name, email, phone, department, ta_level="Masters", salary=20000.0, **kwargs):
        """Initialize Teaching Assistant."""
        super().__init__(name, email, phone, department, salary, **kwargs)
        self._faculty_id = f"TA{self.person_id}"
        self._student_status = True
        self._supervising_professor = None
        self._ta_level = self._validate_ta_level(ta_level)
        self._courses_assisting = []  # Different from courses_taught
        self._grading_duties = []
        self._lab_sessions = []
        self._max_courses_per_semester = 2
    
    @property
    def ta_level(self):
        """Get TA level."""
        return self._ta_level
    
    @property
    def supervising_professor(self):
        """Get supervising professor."""
        return self._supervising_professor
    
    @supervising_professor.setter
    def supervising_professor(self, professor):
        """Set supervising professor."""
        self._supervising_professor = professor
    
    def _validate_ta_level(self, level):
        """Validate TA level."""
        valid_levels = ["Undergraduate", "Masters", "PhD"]
        if level not in valid_levels:
            raise ValueError(f"TA level must be one of: {valid_levels}")
        return level
    
    def assist_course(self, course, duties: List[str] = None):
        """
        Assist with a course (different from teaching).
        
        Args:
            course: Course object to assist with
            duties (list, optional): List of specific duties
        """
        if course.course_code not in [c.course_code for c in self._courses_assisting]:
            assistance = {
                'course': course,
                'duties': duties or ['Grading', 'Lab supervision', 'Office hours'],
                'start_date': datetime.now()
            }
            self._courses_assisting.append(assistance)
            print(f"Now assisting with {course.course_code}")
    
    def add_grading_duty(self, course_code: str, assignment_type: str):
        """Add grading responsibility."""
        duty = {
            'course_code': course_code,
            'assignment_type': assignment_type,
            'date_assigned': datetime.now()
        }
        self._grading_duties.append(duty)
    
    def schedule_lab_session(self, course_code: str, day: str, time: str, location: str):
        """Schedule a lab session."""
        lab_session = {
            'course_code': course_code,
            'day': day,
            'time': time,
            'location': location,
            'capacity': 25
        }
        self._lab_sessions.append(lab_session)
    
    def calculate_workload(self) -> Dict:
        """Calculate TA workload including assistance and grading."""
        base_workload = super().calculate_workload()
        
        # TAs have different workload calculations
        assistance_load = len(self._courses_assisting) * 10
        grading_load = len(self._grading_duties) * 5
        lab_load = len(self._lab_sessions) * 3
        
        return {
            **base_workload,
            'ta_level': self._ta_level,
            'courses_assisting': len(self._courses_assisting),
            'grading_duties': len(self._grading_duties),
            'lab_sessions': len(self._lab_sessions),
            'assistance_load_points': assistance_load,
            'grading_load_points': grading_load,
            'lab_load_points': lab_load,
            'total_load_points': assistance_load + grading_load + lab_load,
            'workload_type': 'Teaching Assistant'
        }
    
    def get_responsibilities(self):
        """Get TA-specific responsibilities."""
        base_responsibilities = super().get_responsibilities()
        ta_responsibilities = [
            "Assist professors with course delivery",
            "Grade assignments and exams",
            "Conduct lab sessions and tutorials",
            "Hold office hours for student support",
            f"Balance TA duties with {self._ta_level} studies",
            "Work under supervision of assigned professor"
        ]
        return base_responsibilities + ta_responsibilities
    
    def get_role(self):
        """Get role type."""
        return f"Teaching Assistant ({self._ta_level})"
    
    def get_ta_info(self) -> Dict:
        """Get TA-specific information."""
        base_info = self.get_faculty_info()
        ta_specific = {
            'ta_level': self._ta_level,
            'supervising_professor': self._supervising_professor,
            'courses_assisting': [
                {
                    'course_code': assist['course'].course_code,
                    'duties': assist['duties']
                }
                for assist in self._courses_assisting
            ],
            'lab_sessions': self._lab_sessions,
            'grading_duties_count': len(self._grading_duties)
        }
        
        return {**base_info, **ta_specific}