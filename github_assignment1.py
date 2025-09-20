# PERSONAL INFORMATION STORAGE (STRINGS)
full_name = "James McNeil"
student_email = "jamcneil1@ncat.edu"
hometown = "Fayetteville, NC"
grad_semester = "Spring 2029"
major = "Computer Science"

# ACADEMIC DATA ORGANIZATION (LISTS)
current_courses = ["COMP 163", "MATH 101", "ENG 100", "HIS 106"]
completed_courses = []
credit_hours = [3 , 3 , 3 , 3]
gpa_history = [3.2 , 3.6 , 3.4 , 3.7]

# CONTACT INFORMATION STORAGE (TUPLES)
emergency_contact = ("Mom", "Carol McNeil", "910-238-6236")
home_address = ("830 Sandy Street", "Fayetteville", "NC", "28391")
insta_info = ("Instagram", "@james.wrldd", "1481")
twitter_info = ("Twitter", "@james.wrldd", "500")
birthday_info = ("Birthday", "12", "12", "2006")

# INTEREST TRACKING (SETS)
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interest = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Weightlifting", "Music"}
enterainment_backlog = {"Vinland Saga", "Naruto", "Fortnite", "Dragon Ball", "HunterxHunter"}

# ORGANIZATIONAL MAPPING (DICTIONARY)
course_credits = {
    "COMP 163": 3,
    "MATH 101": 3,
    "ENG 100": 3,
    "HIS 106": 3
    }
course_professors = {
     "COMP 163": "Prof. Rhodes",
     "MATH 101": "Dr. Black",
     "ENG 100": "Dr. Jefferson",
     "HIS 106": "Dr. Devoe"
}
course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Frye 310",
    "ENG 101": "Crosby 132",
    "HIS 105": "Crosby 205"
}
monthly_budget = {
     "Food": 500,
     "Entertainment": 250,
     "Books": 125,
     "Transportation": 100
}
subject_study_hours = {
     "Programming": 10,
     "Math": 8,
     "English": 4,
     "History": 3
}
contact_directory = {
    "Mom": "910-238-6236",
    "Roommate": "336-432-9943",
    "Academic Advisor": "201-334-4544"
}

# REQUIRED CALCULATIONS
all_credits = 12
all_courses = 4
cumulative_gpa = 3.48
completed_courses_count = 0
weekly_study_hours = 25
academic_load = all_credits + weekly_study_hours
monthly_budget_total = 900
daily_food_budget = 16.7
annual_budget = monthly_budget_total * 12
study_cost = 5

# ANALYTICS CALCULATIONS
social_media_followers = 1981
comparison = len(current_skills)
learning = len(skills_to_learn)
size_analysis = len(contact_directory)
enterainment_backlog_count = len(enterainment_backlog)




print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {grad_semester}")
print(f"Major: {major}")
print()
print(f"=== ACADEMIC PROFILE ===")
print(f"Current Semester: {all_credits} credits across {all_courses} courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost:.1f} per study hour")
print()
print("Current Courses:")
print(f"{current_courses[0]} - {credit_hours[0]} credits - {course_professors["COMP 163"]} - {course_rooms["COMP 163"]}")
print(f"{current_courses[1]} - {credit_hours[1]} credits - {course_professors["MATH 101"]} - {course_rooms["MATH 101"]}")
print(f"{current_courses[2]} - {credit_hours[2]} credits - {course_professors["ENG 100"]} - {course_rooms["ENG 100"]}")
print(f"{current_courses[3]} - {credit_hours[3]} credits - {course_professors["HIS 106"]} - {course_rooms["HIS 106"]}")
print()
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_interest}")
print(f"Skills Currently Have: {comparison}")
print(f"Skills Want to Learn: {learning}")
print()
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget["Food"]} (${daily_food_budget:.1f}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")
print()
print(f"=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {size_analysis} people in directory")
print()
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {enterainment_backlog_count} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("================================================================")c