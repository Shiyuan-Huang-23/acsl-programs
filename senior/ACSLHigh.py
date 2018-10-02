def main():
    calDays = int(input("Enter number of calendar days since school started: "))
    buildCal(calDays)

def buildCal(calDays):
    curriculumDays = 0
    vacationDays = 0
    schoolDays = 0
    programDayHolder = 0
    programDay = None
    dayOfWeek = "Mon"
    daysWeek = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    onVacation = False
    vacationComplete = False
    for i in range(1, calDays + 1):
        dayOfWeek = daysWeek[(daysWeek.index(dayOfWeek) + 1) % 7]
        if dayOfWeek != "Sat" and dayOfWeek != "Sun":
            if onVacation == False:
                schoolDays += 1
                if schoolDays % 30 == 0:
                    curriculumDays += 1
                    programDayHolder = programDay
                    programDay = "CURRICULUM"
                elif schoolDays % 40 == 1 and schoolDays > 40 and vacationComplete == False:
                    schoolDays -= 1
                    onVacation = True
                    vacationDays += 1
                    programDayHolder = programDay
                    programDay = "VACATION"
                else:
                    if programDay == "CURRICULUM" or programDay == "VACATION":
                        programDay = programDayHolder + 1
                    elif programDay == "SUMMER":
                        continue
                    elif programDay == None:
                        programDay = 1
                    else:
                        programDay = (programDay + 1) % 8
                        if programDay == 0:
                            programDay = 1
                vacationComplete = False
            else:
                vacationDays += 1
                if vacationDays % 5 == 0:
                    onVacation = False
                    vacationComplete = True
    print("Weekdays: " + str(schoolDays + vacationDays))
    print("Curriculum days: " + str(curriculumDays))
    print("Vacation days: " + str(vacationDays))
    print("School days: " + str(schoolDays))
    print("Program day: " + str(programDay))
    # print("Day of week: " + dayOfWeek)

main()
