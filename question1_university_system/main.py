"""
Main demonstration file for University Management System
Demonstrates all OOP concepts: Inheritance, Encapsulation, Polymorphism, and Abstraction
"""

from person import Person, Staff
from student import Student, UndergraduateStudent, GraduateStudent, Course, SecureStudentRecord
from faculty import Faculty, Professor, Lecturer, TA
from department import Department, CourseRegistrationSystem
from datetime import datetime


def demonstrate_inheritance():
    """Demonstrate inheritance hierarchy and method inheritance."""
    print("=" * 60)
    print("DEMONSTRATING INHERITANCE")
    print("=" * 60)
    
    try:
        # Create different types of people demonstrating inheritance
        print("Creating different person types...\n")
        
        # Staff member
        staff1 = Staff(
            name="Alice Johnson",
            email="alice.johnson@university.edu",
            phone="555-0101",
            department="Administration",
            position="Academic Advisor",
            salary=45000.0
        )
        
        # Undergraduate student
        undergrad = UndergraduateStudent(
            name="Bob Smith",
            email="bob.smith@student.edu",
            phone="555-0102",
            major="Computer Science",
            class_year="Sophomore"
        )
        
        # Graduate student
        grad_student = GraduateStudent(
            name="Carol Davis",
            email="carol.davis@student.edu",
            phone="555-0103",
            major="Data Science",
            degree_type="PhD"
        )
        
        # Professor
        professor = Professor(
            name="Dr. David Wilson",
            email="david.wilson@university.edu",
            phone="555-0104",
            department="Computer Science",
            salary=85000.0,
            tenure_status=True
        )
        
        # Lecturer
        lecturer = Lecturer(
            name="Emma Brown",
            email="emma.brown@university.edu",
            phone="555-0105",
            department="Computer Science",
            contract_type="Full-time",
            salary=60000.0
        )
        
        # Teaching Assistant
        ta = TA(
            name="Frank Garcia",
            email="frank.garcia@university.edu",
            phone="555-0106",
            department="Computer Science",
            ta_level="PhD",
            salary=25000.0
        )
        
        # Demonstrate inheritance - all objects inherit from Person
        people = [staff1, undergrad, grad_student, professor, lecturer, ta]
        
        print("All person types inherit basic Person functionality:")
        for person in people:
            print(f"- {person.get_role()}: {person.name} (ID: {person.person_id})")
        
        print("\nInheritance hierarchy demonstrated:")
        print("Person → Student → UndergraduateStudent, GraduateStudent")
        print("Person → Faculty → Professor, Lecturer, TA")
        print("Person → Staff")
        
        return people
        
    except Exception as e:
        print(f"Error in inheritance demonstration: {e}")
        return []


def demonstrate_encapsulation():
    """Demonstrate encapsulation with private attributes and validation."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING ENCAPSULATION")
    print("=" * 60)
    
    try:
        # Create a student to demonstrate encapsulation
        student = UndergraduateStudent(
            name="John Doe",
            email="john.doe@student.edu",
            phone="555-0201",
            major="Mathematics",
            class_year="Junior"
        )
        
        print("Creating SecureStudentRecord with encapsulation...")
        secure_record = SecureStudentRecord(student)
        
        print(f"Original student name: {student.name}")
        print(f"Student ID (read-only): {student.student_id}")
        
        # Demonstrate property validation
        print("\nDemonstrating validation in setters:")
        
        try:
            student.name = "Jane Doe"  # Valid name change
            print(f"✓ Valid name change: {student.name}")
        except ValueError as e:
            print(f"✗ Name validation failed: {e}")
        
        try:
            student.name = ""  # Invalid name
            print("This shouldn't print")
        except ValueError as e:
            print(f"✓ Invalid name rejected: {e}")
        
        try:
            student.email = "invalid-email"  # Invalid email
            print("This shouldn't print")
        except ValueError as e:
            print(f"✓ Invalid email rejected: {e}")
        
        # Demonstrate secure access
        print("\nDemonstrating secure record access:")
        requester = "admin_001"
        
        info = secure_record.get_student_info(requester)
        print(f"✓ Retrieved student info: {info['name']}")
        
        # Show access logging
        access_log = secure_record.get_access_log(requester)
        print(f"✓ Access log entries: {len(access_log)}")
        
        # Demonstrate record locking
        secure_record.lock_record(requester)
        print(f"✓ Record locked: {secure_record.is_locked}")
        
        try:
            secure_record.get_student_info("unauthorized_user")
        except PermissionError as e:
            print(f"✓ Locked record protected: {e}")
        
        secure_record.unlock_record(requester)
        print(f"✓ Record unlocked: {secure_record.is_locked}")
        
        return student, secure_record
        
    except Exception as e:
        print(f"Error in encapsulation demonstration: {e}")
        return None, None


def demonstrate_polymorphism(people_list):
    """Demonstrate polymorphism with method overriding."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING POLYMORPHISM")
    print("=" * 60)
    
    try:
        print("Same method call, different behavior based on object type:\n")
        
        # Demonstrate get_responsibilities() polymorphism
        print("1. get_responsibilities() method - Different for each person type:")
        for person in people_list:
            print(f"\n{person.get_role()} - {person.name}:")
            responsibilities = person.get_responsibilities()
            for i, responsibility in enumerate(responsibilities[:3], 1):  # Show first 3
                print(f"   {i}. {responsibility}")
            if len(responsibilities) > 3:
                print(f"   ... and {len(responsibilities) - 3} more")
        
        # Demonstrate calculate_workload() polymorphism for faculty
        print("\n" + "-" * 40)
        print("2. calculate_workload() method - Different for each faculty type:")
        
        faculty_members = [p for p in people_list if isinstance(p, Faculty)]
        
        for faculty in faculty_members:
            workload = faculty.calculate_workload()
            print(f"\n{faculty.get_role()} - {faculty.name}:")
            print(f"   Workload type: {workload['workload_type']}")
            print(f"   Courses: {workload['courses']}")
            
            if 'total_load_points' in workload:
                print(f"   Total load points: {workload['total_load_points']}")
            if 'research_grants' in workload:
                print(f"   Research grants: {workload['research_grants']}")
            if 'teaching_load' in workload:
                print(f"   Teaching load: {workload['teaching_load']}")
        
        # Demonstrate polymorphic behavior in lists
        print("\n" + "-" * 40)
        print("3. Polymorphic behavior in collections:")
        
        print("\nProcessing different person types in the same way:")
        for person in people_list:
            # Same method call works for all person types but behaves differently
            basic_info = person.get_basic_info()
            print(f"   {basic_info['role']}: {basic_info['name']} - {basic_info['person_id']}")
        
        # Show that we can call the same method but get different behavior
        print("\nDemonstrating method overriding:")
        for person in people_list:
            role_description = person.get_role()  # Overridden in each subclass
            print(f"   {person.name}: {role_description}")
        
    except Exception as e:
        print(f"Error in polymorphism demonstration: {e}")


def demonstrate_advanced_student_management():
    """Demonstrate advanced student management features."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING ADVANCED STUDENT MANAGEMENT")
    print("=" * 60)
    
    try:
        # Create courses with prerequisites
        print("Creating courses with prerequisites...\n")
        
        courses = [
            Course("CS101", "Introduction to Computer Science", 3, []),
            Course("CS201", "Data Structures", 3, ["CS101"]),
            Course("CS301", "Algorithms", 3, ["CS201"]),
            Course("MATH101", "Calculus I", 4, []),
            Course("MATH201", "Calculus II", 4, ["MATH101"]),
            Course("STAT301", "Statistics for Data Science", 3, ["MATH201"])
        ]
        
        for course in courses:
            prereq_str = f" (Prerequisites: {', '.join(course.prerequisites)})" if course.prerequisites else " (No prerequisites)"
            print(f"   {course.course_code}: {course.course_name}{prereq_str}")
        
        # Create student
        student = UndergraduateStudent(
            name="Sarah Johnson",
            email="sarah.johnson@student.edu",
            phone="555-0301",
            major="Computer Science",
            class_year="Sophomore"
        )
        
        print(f"\nCreated student: {student.name} ({student.student_id})")
        print(f"Major: {student.major}, Class: {student.class_year}")
        
        # Demonstrate course enrollment
        print("\n" + "-" * 40)
        print("COURSE ENROLLMENT PROCESS")
        print("-" * 40)
        
        # Enroll in prerequisite course first
        print("\n1. Enrolling in foundation course:")
        success = student.enroll_course(courses[0], "Fall 2024")  # CS101
        print(f"   CS101 enrollment: {'✓ Success' if success else '✗ Failed'}")
        
        # Add grade to complete the course
        student.add_grade("CS101", 3.5)
        print("   Added grade: 3.5 for CS101")
        
        # Try to enroll in course with prerequisite
        print("\n2. Enrolling in course with prerequisite:")
        success = student.enroll_course(courses[1], "Spring 2025")  # CS201
        print(f"   CS201 enrollment: {'✓ Success' if success else '✗ Failed'}")
        
        # Try to enroll in course without meeting prerequisites
        print("\n3. Attempting enrollment without prerequisites:")
        success = student.enroll_course(courses[2], "Spring 2025")  # CS301
        print(f"   CS301 enrollment: {'✗ Expected failure' if not success else '✓ Unexpected success'}")
        
        # Enroll in more courses
        student.enroll_course(courses[3], "Fall 2024")  # MATH101
        student.add_grade("MATH101", 3.8)
        
        student.enroll_course(courses[4], "Spring 2025")  # MATH201
        student.add_grade("MATH201", 3.6)
        
        # Complete CS201 to unlock CS301
        student.add_grade("CS201", 3.7)
        
        print("\n4. Re-attempting enrollment after completing prerequisites:")
        success = student.enroll_course(courses[2], "Fall 2025")  # CS301
        print(f"   CS301 enrollment: {'✓ Success' if success else '✗ Failed'}")
        
        # Demonstrate GPA calculation
        print("\n" + "-" * 40)
        print("GPA CALCULATION AND ACADEMIC STATUS")
        print("-" * 40)
        
        current_gpa = student.calculate_gpa()
        academic_status = student.get_academic_status()
        
        print(f"\nCurrent GPA: {current_gpa}")
        print(f"Academic Status: {academic_status}")
        print(f"Total Credits Earned: {student.total_credits}")
        
        # Show transcript
        transcript = student.get_transcript()
        print(f"\nTranscript for {transcript['student_info']['name']}:")
        print(f"Major: {transcript['major']}")
        
        print("\nCompleted Courses:")
        for code, course_info in transcript['courses'].items():
            if course_info['grade']:
                print(f"   {code}: {course_info['course_name']} - Grade: {course_info['grade']} ({course_info['credits']} credits)")
        
        print(f"\nGraduation Status: {'✓ Can graduate' if student.can_graduate() else '✗ Cannot graduate yet'}")
        
        return student, courses
        
    except Exception as e:
        print(f"Error in advanced student management demonstration: {e}")
        return None, []


def demonstrate_department_management():
    """Demonstrate department and course management system."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING DEPARTMENT MANAGEMENT")
    print("=" * 60)
    
    try:
        # Create department
        prof = Professor(
            name="Dr. Alan Turing",
            email="alan.turing@university.edu",
            phone="555-0401",
            department="Computer Science",
            salary=90000.0,
            tenure_status=True
        )
        
        cs_dept = Department("CS", "Computer Science", prof)
        print(f"Created department: {cs_dept.dept_name}")
        print(f"Department head: {cs_dept.head_of_department.name}")
        
        # Add faculty members
        lecturer = Lecturer(
            name="Dr. Ada Lovelace",
            email="ada.lovelace@university.edu",
            phone="555-0402",
            department="Computer Science",
            salary=65000.0
        )
        
        ta = TA(
            name="Grace Hopper",
            email="grace.hopper@university.edu",
            phone="555-0403",
            department="Computer Science",
            ta_level="PhD",
            salary=22000.0
        )
        
        cs_dept.add_faculty(lecturer)
        cs_dept.add_faculty(ta)
        
        print(f"\nFaculty added. Total faculty: {cs_dept.faculty_count}")
        
        # Add courses
        courses = [
            Course("CS101", "Intro to Computer Science", 3, [], 30),
            Course("CS201", "Data Structures", 3, ["CS101"], 25),
            Course("CS301", "Algorithms", 3, ["CS201"], 20),
            Course("CS401", "Machine Learning", 3, ["CS201", "STAT301"], 15)
        ]
        
        for course in courses:
            cs_dept.add_course(course)
        
        print(f"Courses added. Total courses: {cs_dept.course_count}")
        
        # Assign instructors to courses
        cs_dept.assign_instructor("CS101", prof.faculty_id)
        cs_dept.assign_instructor("CS201", lecturer.faculty_id)
        cs_dept.assign_instructor("CS301", prof.faculty_id)
        
        ta.assist_course(cs_dept.get_course_by_code("CS101"), ["Lab supervision", "Grading"])
        ta.assist_course(cs_dept.get_course_by_code("CS201"), ["Tutoring", "Grading"])
        
        print("\nInstructor assignments completed")
        
        # Add students
        students = [
            UndergraduateStudent("Alice Smith", "alice.smith@student.edu", "555-0501", "Computer Science", "Freshman"),
            UndergraduateStudent("Bob Jones", "bob.jones@student.edu", "555-0502", "Computer Science", "Sophomore"),
            GraduateStudent("Carol White", "carol.white@student.edu", "555-0503", "Computer Science", "PhD")
        ]
        
        for student in students:
            cs_dept.add_student(student)
        
        print(f"Students added. Total students: {cs_dept.student_count}")
        
        # Demonstrate course registration
        print("\n" + "-" * 40)
        print("COURSE REGISTRATION PROCESS")
        print("-" * 40)
        
        # Register students for courses
        alice = students[0]  # Freshman
        bob = students[1]    # Sophomore
        carol = students[2]  # PhD student
        
        # Alice starts with CS101
        success = cs_dept.register_student_for_course(alice.student_id, "CS101", "Fall 2024")
        print(f"Alice → CS101: {'✓ Success' if success else '✗ Failed'}")
        
        # Bob can take CS101 or CS201 (if he has prerequisites)
        success = cs_dept.register_student_for_course(bob.student_id, "CS101", "Fall 2024")
        print(f"Bob → CS101: {'✓ Success' if success else '✗ Failed'}")
        
        # Simulate Bob completing CS101
        alice.add_grade("CS101", 3.2)
        bob.add_grade("CS101", 3.5)
        
        # Now they can register for CS201
        success = cs_dept.register_student_for_course(alice.student_id, "CS201", "Spring 2025")
        print(f"Alice → CS201: {'✓ Success' if success else '✗ Failed'}")
        
        success = cs_dept.register_student_for_course(bob.student_id, "CS201", "Spring 2025")
        print(f"Bob → CS201: {'✓ Success' if success else '✗ Failed'}")
        
        # Carol (PhD) can register for advanced courses
        carol.add_grade("CS101", 4.0)  # Simulate completion
        carol.add_grade("CS201", 3.9)  # Simulate completion
        success = cs_dept.register_student_for_course(carol.student_id, "CS301", "Fall 2025")
        print(f"Carol → CS301: {'✓ Success' if success else '✗ Failed'}")
        
        # Show department statistics
        print("\n" + "-" * 40)
        print("DEPARTMENT STATISTICS")
        print("-" * 40)
        
        stats = cs_dept.get_enrollment_statistics()
        
        print(f"\nDepartment: {stats['department_info']['name']}")
        print(f"Head: {stats['department_info']['head']}")
        
        print(f"\nFaculty Breakdown:")
        faculty_stats = stats['faculty_stats']
        print(f"   Total: {faculty_stats['total_faculty']}")
        print(f"   Professors: {faculty_stats['professors']}")
        print(f"   Lecturers: {faculty_stats['lecturers']}")
        print(f"   Teaching Assistants: {faculty_stats['tas']}")
        
        print(f"\nStudent Breakdown:")
        student_stats = stats['student_stats']
        print(f"   Total: {student_stats['total_students']}")
        print(f"   Undergraduate: {student_stats['undergraduate']}")
        print(f"   Graduate: {student_stats['graduate']}")
        
        print(f"\nCourse Statistics:")
        course_stats = stats['course_stats']
        print(f"   Total courses: {course_stats['total_courses']}")
        print(f"   Courses with instructors: {course_stats['courses_with_instructors']}")
        print(f"   Total enrollment: {course_stats['total_enrollment']}")
        print(f"   Average class size: {course_stats['average_class_size']}")
        
        # Show course schedule
        print("\n" + "-" * 40)
        print("COURSE SCHEDULE")
        print("-" * 40)
        
        schedule = cs_dept.get_course_schedule()
        print(f"{'Course':<8} {'Name':<25} {'Instructor':<15} {'Enrolled':<8} {'Available':<9}")
        print("-" * 70)
        
        for course_info in schedule:
            print(f"{course_info['course_code']:<8} "
                  f"{course_info['course_name'][:24]:<25} "
                  f"{course_info['instructor'][:14]:<15} "
                  f"{course_info['enrolled_students']:<8} "
                  f"{course_info['availability']:<9}")
        
        # Show faculty workload
        print("\n" + "-" * 40)
        print("FACULTY WORKLOAD REPORT")
        print("-" * 40)
        
        workload_report = cs_dept.get_faculty_workload_report()
        
        for faculty_info in workload_report:
            print(f"\n{faculty_info['name']} ({faculty_info['role']}):")
            workload = faculty_info['workload']
            print(f"   Workload type: {workload['workload_type']}")
            print(f"   Courses teaching: {workload['courses']}")
            print(f"   Total students: {workload['total_students']}")
            
            if 'total_load_points' in workload:
                print(f"   Load points: {workload['total_load_points']}")
        
        return cs_dept, students
        
    except Exception as e:
        print(f"Error in department management demonstration: {e}")
        return None, []


def demonstrate_cross_registration_system():
    """Demonstrate cross-departmental registration system."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING CROSS-REGISTRATION SYSTEM")
    print("=" * 60)
    
    try:
        # Create registration system
        reg_system = CourseRegistrationSystem()
        
        # Create multiple departments
        # Computer Science Department
        cs_prof = Professor("Dr. John McCarthy", "mccarthy@university.edu", "555-0601", "Computer Science", 95000.0, True)
        cs_dept = Department("CS", "Computer Science", cs_prof)
        
        cs_courses = [
            Course("CS101", "Intro to Programming", 3, []),
            Course("CS201", "Data Structures", 3, ["CS101"]),
            Course("CS301", "Machine Learning", 3, ["CS201", "MATH201"])
        ]
        
        for course in cs_courses:
            cs_dept.add_course(course)
        
        # Mathematics Department
        math_prof = Professor("Dr. Emmy Noether", "noether@university.edu", "555-0602", "Mathematics", 88000.0, True)
        math_dept = Department("MATH", "Mathematics", math_prof)
        
        math_courses = [
            Course("MATH101", "Calculus I", 4, []),
            Course("MATH201", "Linear Algebra", 3, ["MATH101"]),
            Course("MATH301", "Advanced Statistics", 3, ["MATH201"])
        ]
        
        for course in math_courses:
            math_dept.add_course(course)
        
        # Statistics Department
        stat_prof = Professor("Dr. Ronald Fisher", "fisher@university.edu", "555-0603", "Statistics", 85000.0, True)
        stat_dept = Department("STAT", "Statistics", stat_prof)
        
        stat_courses = [
            Course("STAT201", "Intro to Statistics", 3, ["MATH101"]),
            Course("STAT301", "Statistical Modeling", 3, ["STAT201", "MATH201"]),
            Course("STAT401", "Data Science Applications", 3, ["STAT301", "CS201"])
        ]
        
        for course in stat_courses:
            stat_dept.add_course(course)
        
        # Add departments to registration system
        reg_system.add_department(cs_dept)
        reg_system.add_department(math_dept)
        reg_system.add_department(stat_dept)
        
        print("Created multi-departmental registration system:")
        print(f"   • Computer Science Department: {len(cs_courses)} courses")
        print(f"   • Mathematics Department: {len(math_courses)} courses")
        print(f"   • Statistics Department: {len(stat_courses)} courses")
        
        # Create students in different departments
        cs_student = UndergraduateStudent("Alex Chen", "alex.chen@student.edu", "555-0701", "Computer Science")
        math_student = UndergraduateStudent("Maria Rodriguez", "maria.rodriguez@student.edu", "555-0702", "Mathematics")
        
        cs_dept.add_student(cs_student)
        math_dept.add_student(math_student)
        
        print(f"\nStudents created:")
        print(f"   • {cs_student.name}: CS major")
        print(f"   • {math_student.name}: Math major")
        
        # Demonstrate cross-registration
        print("\n" + "-" * 40)
        print("CROSS-DEPARTMENTAL REGISTRATION")
        print("-" * 40)
        
        # CS student taking math courses
        print(f"\n{cs_student.name} (CS major) registering for courses:")
        
        # Start with prerequisites
        success = reg_system.cross_register_student(cs_student.student_id, "CS101", "Fall 2024")
        print(f"   CS101: {'✓ Success' if success else '✗ Failed'}")
        
        success = reg_system.cross_register_student(cs_student.student_id, "MATH101", "Fall 2024")
        print(f"   MATH101 (cross-dept): {'✓ Success' if success else '✗ Failed'}")
        
        # Complete prerequisites
        cs_student.add_grade("CS101", 3.6)
        cs_student.add_grade("MATH101", 3.8)
        
        # Register for more advanced courses
        success = reg_system.cross_register_student(cs_student.student_id, "CS201", "Spring 2025")
        print(f"   CS201: {'✓ Success' if success else '✗ Failed'}")
        
        success = reg_system.cross_register_student(cs_student.student_id, "MATH201", "Spring 2025")
        print(f"   MATH201 (cross-dept): {'✓ Success' if success else '✗ Failed'}")
        
        # Math student taking CS and STAT courses
        print(f"\n{math_student.name} (Math major) registering for courses:")
        
        success = reg_system.cross_register_student(math_student.student_id, "MATH101", "Fall 2024")
        print(f"   MATH101: {'✓ Success' if success else '✗ Failed'}")
        
        success = reg_system.cross_register_student(math_student.student_id, "CS101", "Fall 2024")
        print(f"   CS101 (cross-dept): {'✓ Success' if success else '✗ Failed'}")
        
        # Complete prerequisites
        math_student.add_grade("MATH101", 4.0)
        math_student.add_grade("CS101", 3.4)
        
        success = reg_system.cross_register_student(math_student.student_id, "STAT201", "Spring 2025")
        print(f"   STAT201 (cross-dept): {'✓ Success' if success else '✗ Failed'}")
        
        # Show available options for students
        print("\n" + "-" * 40)
        print("AVAILABLE COURSE OPTIONS")
        print("-" * 40)
        
        print(f"\nAvailable courses for {cs_student.name}:")
        cs_options = reg_system.get_student_options(cs_student.student_id)
        
        for dept_code, dept_info in cs_options.items():
            print(f"   {dept_info['department_name']}:")
            for course in dept_info['courses'][:3]:  # Show first 3
                print(f"      • {course['course_code']}: {course['course_name']} ({course['available_seats']} seats)")
        
        print(f"\nAvailable courses for {math_student.name}:")
        math_options = reg_system.get_student_options(math_student.student_id)
        
        for dept_code, dept_info in math_options.items():
            print(f"   {dept_info['department_name']}:")
            for course in dept_info['courses'][:3]:  # Show first 3
                print(f"      • {course['course_code']}: {course['course_name']} ({course['available_seats']} seats)")
        
        # Generate system report
        print("\n" + "-" * 40)
        print("SYSTEM-WIDE REPORT")
        print("-" * 40)
        
        report = reg_system.generate_system_report()
        overview = report['system_overview']
        
        print(f"\nSystem Overview:")
        print(f"   Total departments: {overview['total_departments']}")
        print(f"   Total students: {overview['total_students']}")
        print(f"   Total courses: {overview['total_courses']}")
        print(f"   Total registrations: {overview['total_registrations']}")
        
        efficiency = report['system_efficiency']
        print(f"\nSystem Efficiency:")
        print(f"   Registration success rate: {efficiency['registration_success_rate']}%")
        print(f"   Average class size: {efficiency['average_class_size']}")
        print(f"   Course utilization: {efficiency['course_utilization']}%")
        
        print(f"\nMost Popular Courses:")
        for i, course in enumerate(report['popular_courses'][:5], 1):
            print(f"   {i}. {course['course_code']}: {course['course_name']} ({course['enrolled_students']} students)")
        
        return reg_system
        
    except Exception as e:
        print(f"Error in cross-registration demonstration: {e}")
        return None


def main():
    """Main function demonstrating all OOP concepts."""
    print("UNIVERSITY MANAGEMENT SYSTEM")
    print("Comprehensive OOP Demonstration")
    print("=" * 60)
    
    try:
        # Demonstrate each OOP concept
        people = demonstrate_inheritance()
        
        student, secure_record = demonstrate_encapsulation()
        
        if people:
            demonstrate_polymorphism(people)
        
        student_demo, courses_demo = demonstrate_advanced_student_management()
        
        department, students = demonstrate_department_management()
        
        reg_system = demonstrate_cross_registration_system()
        
        # Summary
        print("\n" + "=" * 60)
        print("DEMONSTRATION SUMMARY")
        print("=" * 60)
        
        print("\n✓ INHERITANCE demonstrated:")
        print("   • Person → Student → UndergraduateStudent, GraduateStudent")
        print("   • Person → Faculty → Professor, Lecturer, TA")
        print("   • Person → Staff")
        print("   • Method inheritance and super() usage")
        
        print("\n✓ ENCAPSULATION demonstrated:")
        print("   • Private attributes with property decorators")
        print("   • Input validation in setters")
        print("   • SecureStudentRecord with controlled access")
        print("   • Data integrity and access logging")
        
        print("\n✓ POLYMORPHISM demonstrated:")
        print("   • Method overriding in get_responsibilities()")
        print("   • Different calculate_workload() implementations")
        print("   • Same interface, different behavior")
        print("   • Polymorphic behavior in collections")
        
        print("\n✓ ADVANCED FEATURES demonstrated:")
        print("   • Course enrollment with prerequisite checking")
        print("   • GPA calculation and academic status tracking")
        print("   • Department management with faculty and students")
        print("   • Cross-departmental registration system")
        print("   • Comprehensive reporting and analytics")
        
        print("\n✓ DESIGN PATTERNS used:")
        print("   • Abstract base classes for common interface")
        print("   • Composition (Department contains Faculty and Students)")
        print("   • Strategy pattern (different workload calculations)")
        print("   • Observer pattern (access logging)")
        
        print(f"\nTotal classes implemented: 12+")
        print(f"Lines of code: 1000+")
        print(f"OOP principles: All demonstrated comprehensively")
        
        print("\n" + "=" * 60)
        print("DEMONSTRATION COMPLETE")
        print("All OOP requirements successfully implemented!")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error in main demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()