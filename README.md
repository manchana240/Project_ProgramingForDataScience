# University Management System - OOP Implementation

A comprehensive University Management System demonstrating advanced Object-Oriented Programming concepts including Inheritance, Encapsulation, Polymorphism, and Abstraction.

## Project Overview

This project implements a complete university management system with multiple person types, course enrollment, department management, and cross-departmental registration capabilities. It demonstrates all major OOP principles through a real-world application.

##  Architecture & Design

### Class Hierarchy

```
Person (Abstract Base Class)
├── Student
│   ├── UndergraduateStudent
│   └── GraduateStudent
├── Faculty
│   ├── Professor
│   ├── Lecturer
│   └── TA (Teaching Assistant)
└── Staff

Supporting Classes:
├── Course
├── Department
├── CourseRegistrationSystem
└── SecureStudentRecord
```

### Key Features

- **Inheritance**: Multi-level inheritance hierarchy with proper `__init__` method chaining
- **Encapsulation**: Private attributes, property decorators, and data validation
- **Polymorphism**: Method overriding with different behaviors for each person type
- **Abstraction**: Abstract base classes and interfaces

##  Project Structure

```
question1_university_system/
├── main.py                 # Main demonstration file
├── person.py              # Base Person class and Staff
├── student.py             # Student hierarchy and Course class
├── faculty.py             # Faculty hierarchy (Professor, Lecturer, TA)
├── department.py          # Department and registration system

```

## How to Run

### Prerequisites
- Python 3.8 or higher
- No external dependencies required (uses only standard library)

### Installation & Execution

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd question1_university_system
   ```

2. **Install dependencies (optional)**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main demonstration**
   ```bash
   python main.py
   ```

### Expected Output

The main.py file will demonstrate:
-  Inheritance hierarchy creation
-  Encapsulation with validation
-  Polymorphic behavior
-  Advanced student management
-  Department operations
-  Cross-registration system

##  Testing Individual Components

### Test Person Hierarchy
```python
from person import Staff
from student import UndergraduateStudent
from faculty import Professor

# Create different person types
staff = Staff("Lily Cooper", "lily@admin.university.edu", "555-0101", "Administration", "Registrar")
student = UndergraduateStudent("Alex Smith", "alex@student.edu", "555-0102", "Computer Science")
professor = Professor("Professor Samuel Bennett", "bennett@university.edu", "555-0103", "Computer Science", 85000.0)

print(f"Staff: {staff.get_role()}")
print(f"Student: {student.get_role()}")
print(f"Professor: {professor.get_role()}")
```

### Test Course Enrollment
```python
from student import UndergraduateStudent, Course

student = UndergraduateStudent("Maya Thompson", "maya@student.edu", "555-0201", "Statistics")
course = Course("Inference I", "Operational Research", 4, [])

success = student.enroll_course(course)
print(f"Enrollment success: {success}")

student.add_grade("Inference I", 3.7)
gpa = student.calculate_gpa()
print(f"Current GPA: {gpa}")
```

### Test Department Management
```python
from department import Department
from faculty import Professor

prof = Professor("Proffesor. Mira Chen", "chen@university.edu", "555-0301", "Computer Science")
dept = Department("CS", "Computer Science", prof)

print(f"Department: {dept.dept_name}")
print(f"Head: {dept.head_of_department.name}")
```

##  Features Demonstrated

### A. Inheritance with Multiple Classes 
- **Base class**: `Person` with common attributes and abstract methods
- **Student hierarchy**: `Student` → `UndergraduateStudent`, `GraduateStudent`
- **Faculty hierarchy**: `Faculty` → `Professor`, `Lecturer`, `TA`
- **Staff class**: Direct inheritance from `Person`
- **Method inheritance**: All subclasses inherit and extend parent methods

### B. Advanced Student Management 
- **Course enrollment system**: Students can enroll in multiple courses
- **GPA calculation**: Across multiple semesters with history tracking
- **Academic status tracking**: Good Standing, Probation, Dean's List
- **Methods implemented**: `enroll_course()`, `drop_course()`, `calculate_gpa()`, `get_academic_status()`

### C. Encapsulation with Validation 
- **Private attributes**: Using underscore convention and property decorators
- **Input validation**: GPA (0.0-4.0), email format, name requirements
- **Data integrity checks**: Enrollment limits, prerequisite validation
- **SecureStudentRecord class**: Controlled access with logging and locking

### D. Polymorphism with Method Overriding 
- **get_responsibilities()**: Different behavior for each person type
- **calculate_workload()**: Specialized for Professor, Lecturer, TA
- **get_role()**: Returns specific role information for each class
- **Polymorphic collections**: Same interface, different implementations

### E. Department and Course Management 
- **Department class**: Manages faculty, courses, and students
- **Course class**: Handles enrollment limits and prerequisites
- **Faculty assignment**: Assign instructors to courses
- **Registration system**: Complete course registration with prerequisite checking
- **Cross-departmental registration**: Students can take courses from other departments

##  OOP Principles Demonstrated

### 1. **Inheritance**
- Multi-level inheritance chains
- Method inheritance and overriding
- Super() calls for proper initialization
- Abstract base classes

### 2. **Encapsulation**
- Private attributes with property decorators
- Input validation in setters
- Controlled access through methods
- Data hiding and protection

### 3. **Polymorphism**
- Method overriding in subclasses
- Same interface, different implementations
- Duck typing with common methods
- Polymorphic behavior in collections

### 4. **Abstraction**
- Abstract base classes with abstract methods
- Common interfaces across different classes
- Hide implementation details
- Focus on what objects do, not how

##  Code Quality Features

- **Error Handling**: Comprehensive try-catch blocks
- **Input Validation**: Data type and range checking
- **Documentation**: Detailed docstrings for all classes and methods
- **Naming Conventions**: Clear, meaningful variable and method names
- **Modular Design**: Separate files for logical grouping
- **Type Hints**: Enhanced code readability and IDE support

##  Advanced Features

- **Prerequisites System**: Automatic checking of course prerequisites
- **GPA Calculation**: Weighted by credit hours with history tracking
- **Academic Status**: Automatic determination based on GPA
- **Cross-Registration**: Students can take courses from multiple departments
- **Analytics**: Department statistics and enrollment reports
- **Access Control**: Secure student records with logging

##  Error Handling

The system includes comprehensive error handling for:
- Invalid input data (names, emails, GPAs)
- Enrollment conflicts (prerequisites, capacity limits)
- Permission errors (locked records, unauthorized access)
- Data integrity violations

##  Design Patterns Used

- **Abstract Factory**: Person type creation
- **Strategy**: Different workload calculation methods
- **Observer**: Access logging in SecureStudentRecord
- **Composite**: Department containing multiple entity types
- **Template Method**: Common enrollment process with customization

##  Usage Examples

See `main.py` for comprehensive examples of all features. The demonstration covers:

1. Creating different person types
2. Student course enrollment and GPA tracking
3. Faculty workload management
4. Department operations
5. Cross-departmental course registration
6. System analytics and reporting

# E-commerce Data Analysis - Web Scraping & Statistical Analysis

A comprehensive data analysis project demonstrating web scraping, data preprocessing, statistical analysis, and predictive modeling on e-commerce data from website.

##  Project Overview

This project implements a complete data science pipeline for e-commerce analysis, scraping book data from website, performing comprehensive statistical analysis, and building predictive models. It demonstrates professional data science practices including ethical web scraping, robust data cleaning, advanced statistics, and interactive visualizations.

##  Architecture & Design

### Data Pipeline Flow

```
Data Collection → Data Cleaning → Statistical Analysis → Visualization → Predictive Modeling
```

### Key Data Sources

- **Books.toscrape.com**: Primary book data (title, price, rating, availability)

##  Project Structure

```
question2_ecommerce_analysis/

├── data_collection/
│   ├── data_collection.py         # Primary web scraping functionality
├── data_processing/
│   ├── data_processing.ipynb      # Comprehensive data cleaning pipeline 
├── analysis/
│   ├── analysis.ipynb             # Descriptive statistics and analysis
├── visualizations/
│   ├── visualizations.ipynb       # Matplotlib/Seaborn visualizations
├── predictions/
│   ├── predicive_analysis.ipynb    # predictive Analysis


```

##  How to Run

### Prerequisites
- Python 3.8 or higher
- Internet connection for web scraping
- 1-2 GB free disk space for data storage

### Installation & Execution

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd question2_ecommerce_analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **run individual components**
   ```bash
   # Data collection only
   python data_collection.py
   
   # Data cleaning pipeline
   python data_processing.ipynb
   
   # Statistical analysis
   python analysis.ipynb
   
   # Generate visualizations
   python visualizations.ipynb

   # Predictive Analysis
   python predictive_analysis.ipynb
   ```

### Expected Output

-  Multi-source data collection (50+ pages)
-  Comprehensive data cleaning and validation
-  Advanced statistical analysis with hypothesis testing
-  Interactive and static visualizations
-  Predictive modeling and recommendations


##  Features Demonstrated

### A.  Data Collection 
- **Primary Scraping**: Books.toscrape.com with full pagination (50+ pages)
- **Error Handling**: Robust retry logic, connection timeouts, rate limiting
- **Ethical Practices**: 2-second delays, robots.txt compliance, user-agent rotation
- **Data Export**: Structured CSV with metadata tracking
- **Pagination Handling**: Automatic next-page detection and processing

### B. Data Cleaning and Preprocessing  
- **Text Preprocessing**: Special character removal, text normalization, encoding fixes
- **Validation Pipeline**: Data type verification

### C. Advanced Statistical Analysis 
- **Descriptive Statistics**: Mean, median, mode, std dev 
- **Outlier Detection**: IQR method
- **Correlation Analysis**
- **Hypothesis Testing**: T-tests for price differences

### D. Visualizations 
- **Price Distributions**: Histograms by category, box plots for comparisons
- **Correlation Heatmaps**: Multi-variable relationship visualization
- **Rating Analysis**: Scatter plots with trend lines, regression analysis
- **Interactive Dashboards**: Plotly-based filtering and exploration

### E. Predictive Analysis
- **Price Prediction**: Linear regression based on rating, category, availability

##  Data Analysis Insights

### Key Findings Demonstrated

#### Price Analysis
- **Average Book Price**: 35.07 across all categories
- **Price Range**: 10.00 - 59.99 with standard deviation of 14.44n
- **Rating Correlation**: Weak positive correlation between price and rating

#### Statistical Significance
- **Fiction vs Non-fiction**: No significant price difference (p>0.05, t-test)

### Predictive Model Performance
- **Price Prediction**: Price = 34.24 + 0.28 × Rating

## Technical Implementation Details

### Web Scraping Ethics & Best Practices
- **Rate Limiting**: 1-3 second delays between requests
- **Error Handling**: Exponential backoff, maximum retry limits

### Statistical Rigor
- **Hypothesis Testing**: t- testing comparing fiction vs non-fictionmean pricing
- **Confidence Intervals**: 95% CI for all point estimates


##  Learning Outcomes Demonstrated

### Data Science Skills
- **Web Scraping Mastery**: Ethical, robust, scalable scraping implementation
- **Data Wrangling**: Professional-grade cleaning and preprocessing
- **Statistical Analysis**: Advanced statistical methods with proper interpretation
- **Visualization Design**: Effective communication through charts and plots
- **Predictive Modeling**: End-to-end ML pipeline with validation

### Software Engineering
- **Code Organization**: Modular, maintainable, well-documented codebase
- **Error Handling**: Comprehensive exception handling and logging
- **Testing**: Unit tests for critical functionality
- **Documentation**: Professional README, docstrings, inline comments
- **Version Control**: Git best practices with meaningful commits

### Business Intelligence
- **Insight Generation**: Actionable business insights from data analysis
- **Reporting**: Professional presentation of findings
- **Recommendation Systems**: Practical ML applications
- **Performance Metrics**: ROI calculations and business impact assessment
