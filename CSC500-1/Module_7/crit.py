# Course and room number dictionary
course_room = {
            "CSC101":3004,
            "CSC102":4501,
            "CSC103":6755,
            "NET110":1244,
            "COM241":1411}

# Course and instructor dictionary
course_instructor = {
            "CSC101":"Haynes",
            "CSC102":"Alvarado",
            "CSC103":"Rich",
            "NET110":"Burke",
            "COM241":"Lee"}

# Course and meeting time dictionary
course_time = {
            "CSC101":"8:00 a.m.",
            "CSC102":"9:00 a.m.",
            "CSC103":"10:00 a.m.",
            "NET110":"11:00 a.m.",
            "COM241":"1:00 p.m."}

# user defined function to get course number
def get_course():
    # input validation
    try:
        print("Course Catalog: CSC101, CSC102, CSC103, NET110, COM241")
        course = input("Please enter the course number you are looking up: ")
        
        # Raise error if input is not one of the courses
        if course not in ["CSC101","CSC102","CSC103","NET110","COM241"]:
            raise ValueError(print("Please enter a valid course number."))
        else:
            return course

    except ValueError:
        return get_course()

# Print course information
course = get_course()
print("\nCourse Information: ", course)
print(  "-----------------------------")
print(  "Room number  :", course_room[course])
print(  "Instructor   :", course_instructor[course])
print(  "Meeting Time :", course_time[course])
print()
