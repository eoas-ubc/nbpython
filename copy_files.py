import shutil
import os

#/mnt/c/Users/paust/Nextcloud/e340_coursework/e340_2018_spring
#/mnt/c/Users/paust/Dropbox/e340 FILES FOR CONNECT

course_dir=os.environ['course_dir']
student_visible_dir=os.environ['student_visible_dir']
#
#  Assignments
#
file_new=f'{course_dir}/Assignments/Assignment1/Assignment01_17wT2.pdf'
file_old=f"{student_visible_dir}/Assignments/Assignment01.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Assignments/Assignment1/Assignment01Solutions_2017wT1.pdf'
file_old=f'{student_visible_dir}/Assignments/Assignment01Solutions.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Assignments/Assignment2/Assignment02_17wT2.pdf'
file_old=f"{student_visible_dir}/Assignments/Assignment02.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')              
file_new=f'{course_dir}/Assignments/Assignment2/Assignment02_17wT2_Solutions.pdf'
file_old=f'{student_visible_dir}/Assignments/Assignment02Solutions.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Assignments/Assignment3/Assignment03_17wT2.pdf'
file_old=f'{student_visible_dir}/Assignments/Assignment03.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Assignments/Assignment3/Assignment03_17wT2_sol.pdf'
file_old=f'{student_visible_dir}/Assignments/Assignment03Solutions.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')              
file_new=f'{course_dir}/Assignments/Assignment4/Assignment04_2017wT2.pdf'
file_old=f'{student_visible_dir}/Assignments/Assignment04.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Assignments/Assignment 5/New assignment 5 - transfer functions/Assignment 5-2_transfer functions_v4.pdf'
file_old=f'{student_visible_dir}/Assignments/Assignment05.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')

#
# day 1
#
file_new=f'{course_dir}/practice_questions/equation_sheet_2017.pdf'
file_old=f"{student_visible_dir}/Admin files/EOSC340EquationSheet.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Admin - no student info/EOSC340LearningGoals.pdf'
file_old=f"{student_visible_dir}/Admin files/EOSC340LearningGoals.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Admin - no student info/EOSC340Schedule.pdf'
file_old=f"{student_visible_dir}/Admin files/EOSC340Schedule.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Admin - no student info/EOSC340_Syllabus_Spring2018.pdf'
file_old=f"{student_visible_dir}/Admin files/EOSC340_Syllabus.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Admin - no student info/STUDYADVICEforEOSC340.pdf'
file_old=f"{student_visible_dir}/Admin files/STUDYADVICEforEOSC340.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day 01 Intro/Worksheet-Day 1/Day01_Worksheet_ClimateData_v3.pdf'
file_old=f"{student_visible_dir}/Worksheets/Day01Worksheet1.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day 01 Intro/Slides/Day01_IntroClass_Spring18.pdf'
file_old=f"{student_visible_dir}/Post Class Slides/Day01PostClassSlides.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
#
# day 2
#
file_old=f'{student_visible_dir}/Worksheets/Day02WorksheetSolutions.pdf'
file_new=f'{course_dir}/Classes/Day 02 stock and flow/worksheet/day2_worksheet_sol.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day02Reading.pdf'
file_new=f'{course_dir}/Classes/Day 02 stock and flow/Reading/BasicSystems_StockFlowFeedback.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day02PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day 02 stock and flow/Slides/Day02_Systems_Spring18_preclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(out)
file_old=f'{student_visible_dir}/Pre Class Slides/Day02PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day 02 stock and flow/Slides/Day02_Systems_Spring18_postclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(out)
#
#  day 3
#
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day03Reading.pdf'
file_new=f'{course_dir}/Classes/Day_03_Blackbody_I/Reading/Day03Reading_17wT1.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_03_Blackbody_I/quiz/Day03Quiz_2017t1.pdf'
file_old=f"{student_visible_dir}/Pre Class Assignments/Day03PreClassAssignment.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_03_Blackbody_I/quiz/Day03Quiz_2016wT2_Solutions.pdf'
file_old=f"{student_visible_dir}/Quiz Solutions/Day03QuizSolutions.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Worksheets/Day03Worksheet.pdf'
file_new=f'{course_dir}/Classes/Day_03_Blackbody_I/Worksheet/Day03Worksheet.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Worksheets/Day03WorksheetSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_03_Blackbody_I/Worksheet/Day03Worksheet_soln.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day03PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_03_Blackbody_I/Slides/Day03Slides_17wT2_preclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_03_Blackbody_I/Slides/Day03Slides_17wT2_postclass.pdf'
file_old=f'{student_visible_dir}/Post Class Slides/Day03PostClassSlides.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# # day 4
# #
file_new=f'{course_dir}/Classes/Day_04_Earth_energy_budget/pre_class_quiz/day04_quiz_2018.pdf'
file_old=f"{student_visible_dir}/Pre Class Assignments/Day04PreClassAssignment.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day04PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_04_Earth_energy_budget/Slides/Day04_17wT2_preclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Worksheets/Day04Worksheet.pdf'
file_new=f'{course_dir}/Classes/Day_04_Earth_energy_budget/worksheet/day4_worksheet_2017_jan.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Worksheets/Day04WorksheetSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_04_Earth_energy_budget/worksheet/Day04Worksheet_v6_soln.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')

file_old=f'{student_visible_dir}/Post Class Slides/Day04PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_04_Earth_energy_budget/Slides/day04_17wT2_postclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Quiz Solutions/Day04QuizSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_04_Earth_energy_budget/pre_class_quiz/Day04PreClassAssn_RadBalance_Spring2018_answers.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# # day 5
# #
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day05Reading.pdf'
file_new=f'{course_dir}/Classes/Day 05 Greenhouse 1/Reading/Day05Reading_2017.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day 05 Greenhouse 1/Pre-class quiz/Day05PreClassAssn_GHE1_Spring2018.pdf'
file_old=f"{student_visible_dir}/Pre Class Assignments/Day05PreClassAssignment.pdf"
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Quiz Solutions/Day05QuizSolutions.pdf'
file_new=f'{course_dir}/Classes/Day 05 Greenhouse 1/Pre-class quiz/Day05PreClassAssn_GHE1_Spring2018_sols.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day05PeClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day 05 Greenhouse 1/Slides/Day05_Greenhouse1_Spring18_preclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day 05 Greenhouse 1/day05_questions.pdf'
file_old=f'{student_visible_dir}/Student Questions & Comments on Pre Class Quiz/Day05StudentCommentsPreClassQuiz.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Post Class Slides/Day05PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day 05 Greenhouse 1/Slides/Day05_Greenhouse1_Spring18_postclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Worksheets/Day05WorksheetSolutions.pdf'
file_new=f'{course_dir}/Classes/Day 05 Greenhouse 1/Worksheet/AbsorptionSpectraActivity_v6_studentversionofanswers.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# #  day 6
# #
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day06Reading.pdf'
file_new=f'{course_dir}/Classes/Day_06_greenhouse2/Reading/Day06Reading18T2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Quiz Solutions/Day06QuizSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_06_greenhouse2/quiz/Day06Quiz_17wT2_sol.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Assignments/Day06PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day_06_greenhouse2/quiz/Day06Quiz_17wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment2/Assignment02_17wT1.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment02.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment2/Assignment02_17wT1_Solutions.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment02Solutions.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day06PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_06_greenhouse2/Slides/Day06Slides_17wT2_preclass.pdf' 
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Post Class Slides/Day06PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_06_greenhouse2/Slides/Day06Slides_17wT2_postclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# # day 7
# #
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day07Reading.pdf'
file_new=f'{course_dir}/Classes/Day_07_greenhouse3/reading/Day07Reading_17wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Assignments/Day07PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day_07_greenhouse3/quiz/Day07Quiz_17wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment3/Assignment03_17wT1.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment03.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_07_greenhouse3/slides/Day07Slides_17wT2.pdf'
file_old=f'{student_visible_dir}/Pre Class Slides/Day07PreClassSlides.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_07_greenhouse3/slides/Day07Slides_17wT2_postclass.pdf'
file_old=f'{student_visible_dir}/Pre Class Slides/Day07PostClassSlides.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Quiz Solutions/Day07QuizSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_07_greenhouse3/quiz/Day07quiz_17wT2_sol.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n{file_old}\n---\n')
# #
# # day 8
# #
file_new=f'{course_dir}/Classes/Day_08_greenhouse4/slides/Day08Slides_preclass.pdf'
file_old=f'{student_visible_dir}/Pre Class Slides/Day08PreClassSlides.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_08_greenhouse4/quiz/day8_student_questions.pdf'
file_old=f'{student_visible_dir}/Student Questions & Comments on Pre Class Quiz/Day08StudentCommentsPreClassQuiz.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Assignments/Day08PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day_08_greenhouse4/quiz/Day08Quiz_2018wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
file_old=f'{student_visible_dir}/Quiz Solutions/Day08QuizSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_08_greenhouse4/quiz/Day08Quiz_2018wT2_solution.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day08Reading.pdf'
file_new=f'{course_dir}/Classes/Day_08_greenhouse4/reading/Day08Reading_17wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Worksheets/Day08WorksheetSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_08_greenhouse4/Worksheet/Day08Worksheet_2017wT2_sol.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Post Class Slides/Day08PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_08_greenhouse4/slides/day_08_postclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# #  day 9
# #
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day09Reading.pdf'
file_new=f'{course_dir}/Classes/Day_09_temperature/reading/Day09Reading_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Assignments/Day09PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day_09_temperature/quiz/Day09Quiz_2018T2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_09_temperature/quiz/Day_09_quiz_sols_2017wT2.pdf'
file_old=f'{student_visible_dir}/Quiz Solutions/Day09QuizSolutions.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Post Class Slides/Day09PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_09_temperature/slides/day09_postclass_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(out)
file_old=f'{student_visible_dir}/Post Class Slides/Day09PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_09_temperature/slides/Day09Slides2017wT2_preclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day10Reading.pdf'
# file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/Reading/Day10reading_2017.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# #
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/practice_questions/equation_sheet_2017.pdf'
# # file_old=f'{student_visible_dir}/Admin files/EOSC340EquationSheet.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
#
# midterm 1
#
file_new=f'{course_dir}/practice_questions/Practice_Mid1_2017wT2.pdf'
file_old=f'{student_visible_dir}/Practice Questions/Practice_Mid1_set1.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/practice_questions/Practice_Mid1_set2_sols.pdf'
file_old=f'{student_visible_dir}/Practice Questions/Practice_Mid1_set2_solutions.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/practice_questions/Practice_Mid1_2017wT2_set2.pdf'
file_old=f'{student_visible_dir}/Practice Questions/Practice_Mid1_set2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/practice_questions/mid1_equation_sheet_2017wT2.pdf'
file_old=f'{student_visible_dir}/Practice Questions/mid1_equation_sheet.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/practice_questions/Practice_Mid1_2017wT2_sols.pdf'
file_old=f'{student_visible_dir}/Practice Questions/Practice_Mid1_set1_sols.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# #  day 10
# #
file_old=f'{student_visible_dir}/Pre Class Assignments/Day10PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/quiz/Day10Quiz_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day10Reading.pdf'
file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/Reading/Day10Reading_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/quiz/Day10Quiz_2017_wT2_sol.pdf'
file_old=f'{student_visible_dir}/Quiz Solutions/Day10QuizSolutions.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment3/Assignment03_17wT1_sol.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment03Solutions.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day10PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/slides/Day10Slides2017_wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Post Class Slides/Day10PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/slides/Day10Slides2017_wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Quiz Solutions/Day10QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/quiz/Day10Quiz_2017_wT1_sol.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Post Class Slides/Day10PostClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day_10_climate_sensitivity/Slides/Day10Slides2017_wT1.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# #
# # day 12
# #
file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day12Reading.pdf'
file_new=f'{course_dir}/Classes/Day_13_feedbacks/reading/Day12Reading_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Assignments/Day12PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day_13_feedbacks/quiz/day12quiz_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day12PreClassAssignment.pdf'
# file_new=f'{course_dir}/Classes/Day_13_feedbacks/quiz/day13quiz_2017.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Quiz Solutions/Day12QuizSolutions.pdf'
file_new=f'{course_dir}/Classes/Day_13_feedbacks/quiz/day12quiz_sol_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day12PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_13_feedbacks/Slides/Day12Slides_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Post Class Slides/Day12PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day_13_feedbacks/Slides/Day12Slides_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_new=f'{course_dir}/Classes/Day_13_feedbacks/Worksheet/day12_2017wT2_worksheet_solutions.pdf'
file_old=f'{student_visible_dir}/Worksheets/Day12WorksheetSols.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# # day 13
# #
file_old=f'{student_visible_dir}/Post Class Slides/Day13PostClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day 14 Paleotemp 1/Slides/Day13_EstimatingPaleoTemp1_2017wT2_postclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Slides/Day13PreClassSlides.pdf'
file_new=f'{course_dir}/Classes/Day 14 Paleotemp 1/Slides/Day13_EstimatingPaleoTemp1_2017wT2_preclass.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Quiz Solutions/Day13QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day 14 Paleotemp 1/Quiz/Day14PreClassAssn_PaleoT1_Fall2017_answers.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
file_old=f'{student_visible_dir}/Pre Class Assignments/Day13PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day 14 Paleotemp 1/Quiz/Day13PreClassAssn_PaleoT1_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# #
# # day 14
# #
file_old=f'{student_visible_dir}/Pre Class Assignments/Day14PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day 15 Paleotemp 2/Quiz/Day14PreClassAssn_PaleoT2_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Quiz Solutions/Day14QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day 15 Paleotemp 2/Quiz/Day14PreClassAssn_PaleoT1_Fall2017_answers.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Slides/Day14PreClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 15 Paleotemp 2/Slides/Day14_EstimatingPaleoTemp2_Fall17_preclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Slides/Day14PostClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 15 Paleotemp 2/Slides/Day14_EstimatingPaleoTemp2_Fall17_postclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# #
# # day 15
# #
file_old=f'{student_visible_dir}/Pre Class Assignments/Day15PreClassAssignment.pdf'
file_new=f'{course_dir}/Classes/Day 16 Milankovitch/Quiz/Day15PreClassAssn_Milank_2017wT2.pdf'
out=shutil.copyfile(str(file_new),str(file_old))
print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Worksheets/Day15WorksheetSols.pdf'
# file_new=f'{course_dir}/Classes/Day 16 Milankovitch/Worksheet/Milank_worksheet_v1_instructor.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Slides/Day15PreClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 16 Milankovitch/Slides/Day15_Milankovitch_Fall17_preclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Post Class Slides/Day15PostClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 16 Milankovitch/Slides/Day15_Milankovitch_Fall17_postclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Quiz Solutions/Day15QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day 16 Milankovitch/Quiz/Day15PreClassAssn_Milank_Fall2017_answers.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# #
# # day 16
# #
# file_old=f'{student_visible_dir}/Post Class Slides/Day16PostClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 17 GH My/Slides/Day17_GHvariabilityMy_Fall2017_postclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Slides/Day16PreClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 17 GH My/Slides/Day16_GHvariabilityMy_Fall2017_preclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Quiz Solutions/Day16QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day 17 GH My/Quiz/Day16PreClassAssn_GH_My_Fall2017_answers.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# #
# # day 17
# #
# file_old=f'{student_visible_dir}/Pre Class Slides/Day17PreClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 18 GH Ky/Slides/Day17_GHvariabilityKy_Fall17_preclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Post Class Slides/Day17PostClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 18 GH Ky/Slides/Day17_GHvariabilityKy_Fall17_postclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day17PreClassAssignment.pdf'
# file_new=f'{course_dir}/Classes/Day 18 GH Ky/Quiz/Day17PreClassAssn_GH_ky_Fall2017.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day17QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day 18 GH Ky/Quiz/Day17PreClassAssn_GH_ky_Fall2017_answers.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment4/Assignment04_2017wT1.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment04.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment4/Assignment04_2017wT1_solutions.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment04Solutions.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# #
# # day 18
# #
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day18PreClassAssignment.pdf'
# file_new=f'{course_dir}/Classes/Day 19 GH Y/Quiz/Day18PreClassAssn_GH_centtoseas_Fall2017.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day18PreClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 19 GH Y/Slides/Day18_GHvariabilityCentToSeason_Fall2017_preclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Post Class Slides/Day18PostlassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 19 GH Y/Slides/Day18_GHvariabilityCentToSeason_Fall2017_postclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment 6/Assn6_Geocarb_Fall2017.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment06.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day18QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day 19 GH Y/Quiz/Day18PreClassAssn_GH_centtoseas_Fall2017_answers.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# #
# #  Day 19
# #
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day19PreClassSlides.pdf'
# file_new=f'{course_dir}/Classes/Day 20 Paleo Analogues/Slides/Day19_PETM_Fall17_preclass.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_new=f'{course_dir}/Assignments/Assignment 7/Assn7_CarbonAccounting_Fall2017.pdf'
# file_old=f'{student_visible_dir}/Assignments/Assignment07.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print(f'{out}\n{file_new}\n---\n')
# file_old=f'{student_visible_dir}/Pre Class Assignments/Day19QuizSolutions.pdf'
# file_new=f'{course_dir}/Classes/Day 20 Paleo Analogues/Quiz/Day19PreClassAssn_PETM_Fall2017_answers.pdf'
# out=shutil.copyfile(str(file_new),str(file_old))
# print('finished')
# # # newfile=f'/Users/phil/ownCloud/e340review/posts/day2_headheight/_build/day2_headheight.pdf'
# # # oldfile=f'{student_visible_dir}/Miscellaneous Files/feedback_math.pdf'
# # # out=shutil.copyfile(str(newfile),str(oldfile))
# # # print(f'{out}\n{file_new}\n---\n')
# # # file_old=f'{student_visible_dir}/Quiz Solutions/Day13QuizSolutions.pdf'
# # # file_new=f'{course_dir}/Classes/Day_13_feedbacks/quiz/Day13QuizSoln.pdf'
# # # out=shutil.copyfile(str(file_new),str(file_old))
# # # print(f'{out}\n{file_new}\n---\n')
# # # file_new=f'{course_dir}/Assignments/Assignment4/Assignment04_2017_solutions.pdf'
# # # file_old=f'{student_visible_dir}/Assignments/Assignment04Solutions.pdf'
# # # out=shutil.copyfile(str(file_new),str(file_old))
# # # file_old=f'{student_visible_dir}/Post Class Slides/Day13PostClassSlides.pdf'
# # # file_new=f'{course_dir}/Classes/Day_13_feedbacks/Slides/Day13Slides.pdf'
# # # out=shutil.copyfile(str(file_new),str(file_old))
# # # print(f'{out}\n{file_new}\n---\n')
# # # file_new=f'{course_dir}/Classes/Day_13_feedbacks/Worksheet/day13_worksheet_sols.pdf'
# # # file_old=f'{student_visible_dir}/Worksheets/Day13WorksheetSol.pdf'
# # # out=shutil.copyfile(str(file_new),str(file_old))
# # # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Readings - non-textbook, non-journal article/Day23Reading.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/reading/Day23Reading.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Readings_text/dessler_ch8.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/reading/dessler_ch8.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Readings_text/dessler_ch9.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/reading/dessler_ch9.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Pre Class Assignments/Day23PreClassAssignment.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/quiz/Day23PreClassAssignment.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Pre Class Assignments/Day24PreClassAssignment.pdf'
# # file_new=f'{course_dir}/Classes/Day_24_forecasts/quiz/day24quiz.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Pre Class Slides/Day23PreClassSlides.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/Slides/Day23_2017.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Worksheets/Day23Worksheet.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/worksheet/kaya_worksheet.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Quiz Solutions/Day23QuizSolutions.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/quiz/Day-23-Quiz_2017_answers.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Quiz Solutions/Day23QuizSolutions.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/quiz/Day-23-Quiz_2017_answers.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Worksheets/Day23WorksheetSolutions.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/worksheet/kaya_worksheet_sol.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Quiz Solutions/Day24QuizSolutions.pdf'
# # file_new=f'{course_dir}/Classes/Day_24_forecasts/quiz/day24reading_solutions.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Pre Class Slides/Day24PreClassSlides.pdf'
# # file_new=f'{course_dir}/Classes/Day_24_forecasts/slides/Day24_2017.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/practice_questions/equation_sheet_2017.pdf'
# # file_old=f'{student_visible_dir}/Admin files/EOSC340EquationSheet.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/practice_questions/Practice_Physics_2017A.pdf'
# # file_old=f'{student_visible_dir}/Practice Questions/Practice_Physics_Final_2017A.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Post Class Slides/Day23PostClassSlides.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/Slides/Day23_2017.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Post Class Slides/Day24PostClassSlides.pdf'
# # file_new=f'{course_dir}/Classes/Day_24_forecasts/slides/Day24_2017.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/practice_questions/Practice_Physics_solutions.pdf'
# # file_old=f'{student_visible_dir}/Practice Questions/Practice_Physics_solutions.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/Assignments/Assignment8/_build/Assignment8_sol.pdf'
# # file_old=f'{student_visible_dir}/Assignments/Assigment08Solutions.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/Classes/Day 26 Review/Slides/day26_review_last.pdf'
# # file_old=f'{student_visible_dir}/Pre Class Slides/Day26PreClassSlides.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')

# # file_old=f'{student_visible_dir}/Post Class Slides/Day23PostClassSlides.pdf'
# # file_new=f'{course_dir}/Classes/Day_23_modeling/Slides/Day23_2017.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=f'{student_visible_dir}/Post Class Slides/Day24PostClassSlides.pdf'
# # file_new=f'{course_dir}/Classes/Day_24_forecasts/slides/Day24_2017.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/practice_questions/Practice_Physics_solutions.pdf'
# # file_old=f'{student_visible_dir}/Practice Questions/Practice_Physics_solutions.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/Assignments/Assignment8/_build/Assignment8_sol.pdf'
# # file_old=f'{student_visible_dir}/Assignments/Assigment08Solutions.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=f'{course_dir}/Classes/Day 26 Review/Slides/day26_review_last.pdf'
# # file_old=f'{student_visible_dir}/Pre Class Slides/Day26PreClassSlides.pdf'
# # out=shutil.copyfile(str(file_new),str(file_old))
# # print(f'{out}\n{file_new}\n---\n')
