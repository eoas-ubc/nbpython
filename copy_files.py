import shutil
import sys
from pathlib import Path
import os

root_e340_fall = os.environ["E340root"]
root_dropbox = os.environ["E340dropbox"]

the_file = Path(__file__).resolve()
e340_fall = the_file.parent.parent
print("pha")
course_dir = root_e340_fall / Path("e340_2019_fall")
student_visible_dir = root_dropbox / Path("e340 FILES FOR CONNECT")
print(f"debug")
print(f"student_visible_dir is: {student_visible_dir}")

#
#  Assignments
#
file_new = course_dir / Path("Assignments/Assignment1/Assignment01_2019t1.pdf")
file_old = student_visible_dir / Path("Assignments/Assignment01.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# file_new= course_dir / Path('Assignments/Assignment1/lowe_gregory.pdf')
# file_old= student_visible_dir / Path('Assignments/lowe_gregory.pdf')
# out=shutil.copyfile(file_new,file_old)
file_new = course_dir / Path(
    "Assignments/Assignment1/Assignment01Solutions_2018wT2.pdf"
)
file_old = student_visible_dir / Path("Assignments/Assignment01Solutions.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# file_new=course_dir / Path('Assignments/Assignment2/Assignment02_2018t2.pdf')
# file_old= student_visible_dir/ Path('Assignments/Assignment02.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Assignments/Assignment2/Assignment02_2018t2_sln.pdf')
# file_old=student_visible_dir / Path('Assignments/Assignment02Solutions.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
file_new = course_dir / Path("Assignments/Assignment3/assignment3_2019t1_student.pdf")
file_old = student_visible_dir / Path("Assignments/Assignment03.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Assignments/Assignment3/assignment3_2019t1_solution.pdf")
file_old = student_visible_dir / Path("Assignments/Assignment03Solutions.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_new=course_dir / Path('Assignments/Assignment3/Assignment03_18t2_sln.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment03Solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment4/Assignment04_2018t2.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment04.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment4/Assignment04_2018t2_sln.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment04Solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment_5/Assignment_5_ProxyTemps_2018wT2.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment05.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment_5/Assignment_5_ProxyTemps_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment05Solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment_6/Assn6_GeocarbPlus_2018wT2.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment06.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment_6/Assn6_GeocarbPlus_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment06Solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment_7/Assignment7_CarbonReview_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment07Solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
file_new=course_dir / Path('Assignments/Assignment4/assign04_2019t1_students.pdf')
file_old=student_visible_dir / Path('Assignments/Assignment07.pdf')
out=shutil.copyfile(file_new,file_old)
print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment_7/Reading.Dessler.CH14.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment07.Reading.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment_7/Reading_Dessler_8.3-8.6.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment07.Reading2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # day 1
# # #
file_new = course_dir / Path(
    "Admin_-_no_student_info/EOSC340LearningGoals_Fall2019.pdf"
)
file_old = student_visible_dir / Path("Admin files/EOSC340LearningGoals.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Admin_-_no_student_info/EOSC340_Syllabus_Fall2019.pdf")
file_old = student_visible_dir / Path("Admin files/EOSC340_Syllabus.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Admin_-_no_student_info/python/2019_fall.pdf")
file_old = student_visible_dir / Path("Admin files/EOSC340Schedule.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # # file_new=course_dir / Path('Admin_-_no_student_info/EOSC340Schedule.pdf') used schedule_spring2019 in e340_2018t2
# # # file_old=student_visible_dir / Path('Admin files/EOSC340Schedule.pdf')
# # # out=shutil.copyfile(file_new,file_old)
# # # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('EXAMS/midterm1_2018t2/mid1_equation_sheet_2018t2.pdf')
# # file_old=student_visible_dir / Path('Admin files/mid1_equation_sheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('EXAMS/final_2018t2/Final_equations_2018t2.pdf')
# # file_old=student_visible_dir / Path('Admin files/EOSC340EquationSheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Admin_-_no_student_info/STUDYADVICEforEOSC340.pdf')
# # file_old=student_visible_dir / Path('Admin files/STUDYADVICEforEOSC340.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_01_Intro/Worksheet-Day_1/Day01_Worksheet_ClimateData_v3.pdf')
# file_old=student_visible_dir / Path('Worksheets/Day01Worksheet1.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_01_Intro/Slides/Day01_IntroClass_Fall2019.pdf')
# file_old=student_visible_dir / Path('Post Class Slides/Day01PostClassSlides.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # #
# # # day 2
# # #
# file_new=course_dir / Path('Classes/Day_02_stock_and_flow/Pre-class_quiz/Day02PreClassAssn_Systems_2019T1.pdf')
# file_old=student_visible_dir / Path('Pre Class Assignments/Day02PreClassAssignment.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_02_stock_and_flow/Reading/BasicSystems_StockFlowFeedback.pdf')
# # file_old=student_visible_dir / Path('Readings - non-textbook, non-journal article/Day02Reading.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_02_stock_and_flow/worksheet/Stock&FlowWorksheet_EOSC340_Spring18_use.pdf')
# file_old=student_visible_dir / Path('Worksheets/Day02Worksheet.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_02_stock_and_flow/worksheet/day2_worksheet_sol.pdf')
# file_old=student_visible_dir / Path('Worksheets/Day02WorksheetSolutions.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_02_stock_and_flow/Pre-class_quiz/Day02PreClassAssn_Systems_2019t1_sln.pdf')
# file_old=student_visible_dir / Path('Quiz Solutions/Day02QuizSolutions.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Pre Class Slides/Day02PreClassSlides.pdf')
# file_new=course_dir / Path('Classes/Day_02_stock_and_flow/Slides/Day02_Systems_Fall19_preclass.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Pre Class Slides/Day02PostClassSlides.pdf')
# file_new=course_dir / Path('Classes/Day_02_stock_and_flow/Slides/Day02_Systems_2019t1_postclass.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # #
# # ## Day 3
# # #
# file_old=student_visible_dir / Path('Readings - non-textbook, non-journal article/Day03Reading.pdf')
# file_new=course_dir / Path('Classes/Day_03_Blackbody_I/Reading/Day03Reading_19wT1.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_03_Blackbody_I/quiz/Day03Quiz_2019t1.pdf')
# file_old=student_visible_dir / Path('Pre Class Assignments/Day03PreClassAssignment.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_03_Blackbody_I/quiz/Day03Quiz_2019t1_sln.pdf')
# file_old=student_visible_dir / Path('Quiz Solutions/Day03QuizSolutions.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Worksheets/Day03Worksheet.pdf')
# file_new=course_dir / Path('Classes/Day_03_Blackbody_I/Worksheet/Day03Worksheet.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Worksheets/Day03WorksheetSolutions.pdf')
# file_new=course_dir / Path('Classes/Day_03_Blackbody_I/Worksheet/Day03Worksheet_19t1_sln.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Pre Class Slides/Day03PreClassSlides.pdf')
# file_new=course_dir / Path('Classes/Day_03_Blackbody_I/Slides/Day03Slides_19wt1_preclass.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_03_Blackbody_I/Slides/Day03Slides_19t1_postclass.pdf')
# file_old=student_visible_dir / Path('Post Class Slides/Day03PostClassSlides.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # # #
# # # # day 4
# # # #
# file_new=course_dir / Path("Classes/Day_04_Earth_energy_budget/pre_class_quiz/Day04PreClassAssn_RadBalance_2019t1.pdf")
# file_old=student_visible_dir / Path('Pre Class Assignments/Day04PreClassAssignment.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_04_Earth_energy_budget/pre_class_quiz/Day04PreClassAssn_RadBalance_2018t2_sln.pdf')
# file_old=student_visible_dir / Path('Quiz Solutions/Day04QuizSolutions.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_04_Earth_energy_budget/Slides/Day04_19wt1_preclass.pdf')
# file_old=student_visible_dir / Path('Pre Class Slides/Day04PreClassSlides.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_04_Earth_energy_budget/worksheet/Day04Worksheet_v6.pdf')
# file_old=student_visible_dir / Path('Worksheets/Day04Worksheet.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Worksheets/Day04WorksheetSolutions.pdf')
# file_new=course_dir / Path('Classes/Day_04_Earth_energy_budget/worksheet/Day04Worksheet_v6_soln.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Post Class Slides/Day04PostClassSlides.pdf')
# file_new=course_dir / Path('Classes/Day_04_Earth_energy_budget/Slides/Day04_19wt1_postclass.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')

# # # #
# # # # day 5
# # # #
# file_old=student_visible_dir / Path('Readings - non-textbook, non-journal article/Day05Reading.pdf')
# file_new=course_dir / Path('Classes/Day_05_Greenhouse_1/Reading/Day05Reading_2019t1.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_new=course_dir / Path('Classes/Day_05_Greenhouse_1/Pre-class_quiz/Day05PreClassAssn_GHE1_2019t1.pdf')
# file_old=student_visible_dir / Path('Pre Class Assignments/Day05PreClassAssignment.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Quiz Solutions/Day05QuizSolutions.pdf')
# file_new=course_dir / Path('Classes/Day_05_Greenhouse_1/Pre-class_quiz/Day05PreClassAssn_GHE1_2019t1_sln.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Pre Class Slides/Day05PeClassSlides.pdf')
# file_new=course_dir / Path('Classes/Day_05_Greenhouse_1/Slides/Day05_Greenhouse1_2018t2_preclass.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # # file_new=course_dir / Path('Classes/Day_05_Greenhouse_1/day05_questions.pdf')
# # # file_old=student_visible_dir / Path('Student Questions & Comments on Pre Class Quiz/Day05StudentCommentsPreClassQuiz.pdf')
# # # out=shutil.copyfile(file_new,file_old)
# # #print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Post Class Slides/Day05PostClassSlides.pdf')
# file_new=course_dir / Path('Classes/Day_05_Greenhouse_1/Slides/Day05_Greenhouse1_2019t1_postclass.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # #
# # # 2018 fall and 2019 spring: skip day 5 spectral worksheet
# # # #  day 6
# # # #
# file_old=student_visible_dir / Path('Readings - non-textbook, non-journal article/Day06Reading.pdf')
# file_new=course_dir / Path('Classes/Day_06_greenhouse2/Reading/Day6reading.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day06QuizSolutions.pdf')
# # file_new=course_dir / Path('Classes/Day_06_greenhouse2/quiz/Day06Quiz_18wt2_sol.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# file_old=student_visible_dir / Path('Pre Class Assignments/Day06PreClassAssignment.pdf')
# file_new=course_dir / Path('Classes/Day_06_greenhouse2/quiz/Day06Quiz_19t1.pdf')
# out=shutil.copyfile(file_new,file_old)
# print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment2/Assignment02_18t2.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment02.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Assignments/Assignment2/Assignment02_18t2_sln.pdf')
# # file_old=student_visible_dir / Path('Assignments/Assignment02Solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # # file_old=student_visible_dir / Path('Pre Class Slides/Day06PreClassSlides.pdf')
# # # file_new=course_dir / Path('Classes/Day_06_greenhouse2/Slides/Day06Slides_18wt_preclass.pdf')
# # # out=shutil.copyfile(file_new,file_old)
# # # print(f'{out}\n{file_new}\n---\n')
file_old = student_visible_dir / Path("Post Class Slides/Day06PostClassSlides.pdf")
file_new = course_dir / Path(
    "Classes/Day_06_greenhouse2/Slides/day06Slides_19t1_postclass.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # # #
# # # # day 7
# # # #
# # file_old=student_visible_dir / Path('Readings - non-textbook, non-journal article/Day07Reading.pdf')
# # file_new=course_dir / Path('Classes/Day_07_greenhouse3/reading/Day07Reading_18wt1.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day07PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_07_greenhouse3/quiz/Day07Quiz_18wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
file_new = course_dir / Path(
    "Classes/Day_07_greenhouse3/slides/Day07Slides_19t1_preclass.pdf"
)
file_old = student_visible_dir / Path("Pre Class Slides/Day07PreClassSlides.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Classes/Day_07_greenhouse3/slides/Day_07_layers.pdf")
file_old = student_visible_dir / Path("Post Class Slides/Day_07_layers.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path(
    "Classes/Day_07_greenhouse3/slides/Day07Slides_19t1_postclass.pdf"
)
file_old = student_visible_dir / Path("Post Class Slides/Day07PostClassSlides.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_new=course_dir / Path('Classes/Day_07_greenhouse3/slides/Day07Slides_18wt2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day07PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day07QuizSolutions.pdf')
# # file_new=course_dir / Path('Classes/Day_07_greenhouse3/quiz/Day07quiz_18wT2_sln.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n{file_old}\n---\n')
# # # #
# # # # day 8
# # # #
file_new = course_dir / Path(
    "Classes/Day_08_greenhouse4/slides/Day08Slides_19t1_preclass.pdf"
)
file_old = student_visible_dir / Path("Pre Class Slides/Day08PreClassSlides.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # # file_new=course_dir / Path('Classes/Day_08_greenhouse4/quiz/day8_student_questions.pdf')
# # # file_old=student_visible_dir / Path('Student Questions & Comments on Pre Class Quiz/Day08StudentCommentsPreClassQuiz.pdf')
# # # out=shutil.copyfile(file_new,file_old)
# # # print(f'{out}\n{file_new}\n---\n')
file_old = student_visible_dir / Path(
    "Pre Class Assignments/Day08PreClassAssignment.pdf"
)
file_new = course_dir / Path("Classes/Day_08_greenhouse4/quiz/Day08Quiz_2019t1.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_old=student_visible_dir / Path('Quiz Solutions/Day08QuizSolutions.pdf')
# # file_new=course_dir / Path('Classes/Day_08_greenhouse4/quiz/Day08Quiz_2018wT2_sln.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
file_old = student_visible_dir / Path(
    "Readings - non-textbook, non-journal article/Day08Reading.pdf"
)
file_new = course_dir / Path("Classes/Day_08_greenhouse4/reading/Day08Reading_19t1.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_old=student_visible_dir / Path('Worksheets/Day08Worksheet.pdf')
# # file_new=course_dir / Path('Classes/Day_08_greenhouse4/Worksheet/Day08Worksheet_2018wt2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Worksheets/Day08WorksheetSolutions.pdf')
# # file_new=course_dir / Path('Classes/Day_08_greenhouse4/Worksheet/Day08Worksheet_2018wt2_sln.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Post Class Slides/Day08PostClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_08_greenhouse4/slides/Day08Slides_18wt2_postclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # # #
# # # #  day 9
# # # #
file_old = student_visible_dir / Path(
    "Readings - non-textbook, non-journal article/Day09Reading.pdf"
)
file_new = course_dir / Path("Classes/Day_09_temperature/reading/Day09Reading.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path(
    "Pre Class Assignments/Day09PreClassAssignment.pdf"
)
file_new = course_dir / Path("Classes/Day_09_temperature/quiz/Day_09_quiz_2019t1.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path(
    "Classes/Day_09_temperature/quiz/Day_09_quiz_2019t1_sln.pdf"
)
file_old = student_visible_dir / Path("Quiz Solutions/Day09QuizSolutions.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path("Pre Class Slides/Day09PreClassSlides.pdf")
file_new = course_dir / Path(
    "Classes/Day_09_temperature/slides/Day09Slides2019t1_preclass.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path("Post Class Slides/Day09PostClassSlides.pdf")
file_new = course_dir / Path(
    "Classes/Day_09_temperature/slides/Day09Slides2019t1_preclass.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # # #
# # #
# # #
# # # quiz 1
# # #
file_new = course_dir / Path("practice_questions/quiz1/Practice_quiz1_2019t1.pdf")
file_old = student_visible_dir / Path("Practice Questions/Practice_Mid1_set1.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("practice_questions/quiz1/quiz1_equation_sheet_2019t1.pdf")
file_old = student_visible_dir / Path("Practice Questions/quiz1_equation_sheet.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Exams/quiz2_2019t1/e340_quiz2_2019t1_equations.pdf")
file_old = student_visible_dir / Path("Practice Questions/quiz2_equation_sheet.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Exams/quiz1_2019t1/quiz1_vera_answers.pdf")
file_old = student_visible_dir / Path("Practice Questions/quiz1_vera_answers.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_new=course_dir / Path('practice_questions/Practice_Mid1_set2_2018t2.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/Practice_Mid1_set2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('practice_questions/Review_LayerWorksheet.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/Review_LayerWorksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
##  quiz 1 set 1
file_new = course_dir / Path("practice_questions/quiz1/Practice_quiz1_2019t1.pdf")
file_old = student_visible_dir / Path("Practice Questions/Practice_Mid1_set1.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("practice_questions/quiz1/Practice_quiz1_2019t1_sln.pdf")
file_old = student_visible_dir / Path("Practice Questions/Practice_Mid1_set1_sols.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
##  quiz 1 set 2
file_new = course_dir / Path("practice_questions/quiz1/Practice_quiz1_set2_2019t1.pdf")
file_old = student_visible_dir / Path("Practice Questions/Practice_Mid1_set2.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("practice_questions/quiz1/Practice_Mid1_set2_sols.pdf")
file_old = student_visible_dir / Path("Practice Questions/Practice_Mid1_set2_sols.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
## quiz 2 set 1
file_new = course_dir / Path(
    "practice_questions/quiz2/practice_quiz2_set1_students.pdf"
)
file_old = student_visible_dir / Path("Practice Questions/practice_quiz2_set1.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("practice_questions/quiz2/practice_quiz2_set1.pdf")
file_old = student_visible_dir / Path(
    "Practice Questions/practice_quiz2_set1_solutions.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
## quiz 2 set 2
file_new = course_dir / Path(
    "practice_questions/quiz2/practice_quiz2_set2_students.pdf"
)
file_old = student_visible_dir / Path("Practice Questions/practice_quiz2_set2.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("practice_questions/quiz2/practice_quiz2_set2.pdf")
file_old = student_visible_dir / Path(
    "Practice Questions/practice_quiz2_set2_solutions.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
#
# layers
#
file_new = course_dir / Path("practice_questions/Review_LayerWorksheet.pdf")
file_old = student_visible_dir / Path("Practice Questions/Review_LayerWorksheet.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("practice_questions/Review_LayerWorksheet_sln.pdf")
file_old = student_visible_dir / Path(
    "Practice Questions/Review_LayerWorksheet_Solution.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # # #
# # # # Day 10
# # # #
# # # Day 10 covered part 2 of air temperature/moist atmosphere
file_old = student_visible_dir / Path(
    "Pre Class Assignments/Day10PreClassAssignment.pdf"
)
file_new = course_dir / Path(
    "Classes/Day_10_climate_sensitivity/quiz/Day_10_quiz_2019t1.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path(
    "Classes/Day_10_climate_sensitivity/quiz/day_10_quiz_2019t1_solutions.pdf"
)
file_old = student_visible_dir / Path("Quiz Solutions/Day10QuizSolutions.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path("Post Class Slides/Day10PostClassSlides.pdf")
file_new = course_dir / Path(
    "Classes/Day_10_climate_sensitivity/slides/Day10Slides_2019t1_preclass.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # #
# # # # Day 11 -- climate sensitivity I
# # # #
# # # Day 11 wrapped up air temperature/moist atmosphere; review for midterm 1
file_old = student_visible_dir / Path("Quiz Solutions/Day11QuizSolutions.pdf")
file_new = course_dir / Path(
    "Classes/Day_10_climate_sensitivity/quiz/Day11Quiz_2019t1_solutions.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path(
    "Pre Class Assignments/Day11PreClassAssignment.pdf"
)
file_new = course_dir / Path("Classes/Day_10_climate_sensitivity/quiz/day10_posted.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path(
    "Readings - non-textbook, non-journal article/Day11Reading.pdf"
)
file_new = course_dir / Path(
    "Classes/Day_10_climate_sensitivity/Reading/Day10reading_2019t1.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path("Pre Class Slides/Day11PreClassSlides.pdf")
file_new = course_dir / Path(
    "Classes/Day_12_feedbacks/Slides/Day11_2019t1_postclass.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path("Worksheets/Day11Worksheet.pdf")
file_new = course_dir / Path(
    "Classes/Day_12_feedbacks/Worksheet/Day11-Worksheet-ice-feedback-2019t1.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path("Worksheets/Day11WorksheetSolutions.pdf")
file_new = course_dir / Path(
    "Classes/Day_12_feedbacks/Worksheet/day11_2019t1_worksheet_solutions.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_old=student_visible_dir / Path('Post Class Slides/Day11PostClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_11_sytems_review/Day11Slides2018_wT2_postclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# Day 12 --- feedback
file_old = student_visible_dir / Path(
    "Readings - non-textbook, non-journal article/Day12Reading.pdf"
)
file_new = course_dir / Path("Classes/Day_12_feedbacks/reading/Day12Reading_2019t1.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_old = student_visible_dir / Path("Pre Class Slides/Day12PreClassSlides.pdf")
file_new = course_dir / Path(
    "Classes/Day_12_feedbacks/Slides/Day12_2019t1_postclass.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# #
#
# # Day 13 --- quiz 2
# #
file_new = course_dir / Path("Exams/quiz2_2019t1/quiz2_2019t1_answers.pdf")
file_old = student_visible_dir / Path("Practice Questions/quiz2_answers.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # #
# # # # Day 14 --- Climate Sensitivity
# # # #
# # #
# # file_old=student_visible_dir / Path('Readings - non-textbook, non-journal article/Day14Reading.pdf')
# # file_new=course_dir / Path('Classes/Day_10_climate_sensitivity/Reading/Day14reading_2018wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day14PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_10_climate_sensitivity/quiz/Day14Quiz_2018_wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_10_climate_sensitivity/quiz/Day14Quiz_2018_wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day14QuizSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Worksheets/Day14Worksheet.pdf')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/Worksheet/FeedbackLoop_SimpleWorksheet-2018t2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day14PreClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_10_climate_sensitivity/slides/Day14_ClimateSensitivity_18t2_preclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Post Class Slides/Day14PostClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_10_climate_sensitivity/slides/Day14_ClimateSensitivity_18t2_postclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 15 --- Feedbacks
# # # #
# # #
# # file_old=student_visible_dir / Path('Readings - non-textbook, non-journal article/Day15Reading.pdf')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/reading/Day12Reading_2018t1.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day15PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/quiz/Day15Quiz_2018_wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/quiz/Day15Quiz_2018_wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day15QuizSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Worksheets/Day15Worksheet.pdf')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/Worksheet/Day15-Worksheet-ice-feedback-2018t2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Worksheets/Day15WorksheetSolutions.pdf')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/Worksheet/day22_2018t1_worksheet_solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day15PreClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/slides/Day15_Feedbacks_18t2_preclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Post Class Slides/Day15PostClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_13_feedbacks/slides/Day15_Feedbacks_18t2_postclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 16 --- Paleotemperatures I
# # # #
# # #
file_new = course_dir / Path(
    "Classes/Day_14_Paleotemp_1/Quiz/Day14PreClassAssn_PaleoT1_2019wT1.pdf"
)
file_old = student_visible_dir / Path(
    "Pre Class Assignments/Day14PreClassAssignment.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path(
    "Classes/Day_14_Paleotemp_1/Quiz/Day14PreClassAssn_PaleoT1_2019wT1_sln.pdf"
)
file_old = student_visible_dir / Path("Quiz Solutions/Day14QuizSolutions.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_new=course_dir / Path('Classes/Day_14_Paleotemp_1/Worksheet/Day16Worksheet_all_2018wT2.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day16Worksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_14_Paleotemp_1/Worksheet/Day16Worksheet_all_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day16WorksheetSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
file_new = course_dir / Path(
    "Classes/Day_14_Paleotemp_1/Slides/Day14_EstimatingPaleoTemp1_2019wT1_preclass.pdf"
)
file_old = student_visible_dir / Path("Pre Class Slides/Day14PreClassSlides.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # file_old=student_visible_dir / Path('Post Class Slides/Day16PostClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_14_Paleotemp_1/Slides/Day16_EstimatingPaleoTemp1_2018wT2_postclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 17 --- Paleotemperatures II
# # # #
# # #
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day17PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_15_Paleotemp_2/Quiz/Day17PreClassAssn_PaleoT2_2018wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_15_Paleotemp_2/Quiz/Day17PreClassAssn_PaleoT2_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day17QuizSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_15_Paleotemp_2/Worksheet/Glacial-Interglacial18O_simplified.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day17Worksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_15_Paleotemp_2/Worksheet/Glacial-Interglacial18O_simplified_sln.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day17WorksheetSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day17PreClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_15_Paleotemp_2/Slides/Day17_EstimatingPaleoTemp2_2018wT2_preclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Post Class Slides/Day17PostClassSlides.pdf')
# # file_new=course_dir / Path('Classes/Day_15_Paleotemp_2/Slides/Day17_EstimatingPaleoTemp2_2018wT2_postclass.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # Day 17 --- quiz 3
# #
file_new = course_dir / Path("Exams/quiz3_2019t1/quiz3_2019t1_answers.pdf")
file_old = student_visible_dir / Path("Practice Questions/quiz3_answers.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Exams/quiz4_2019t1/e340_quiz4_2019t1_equations.pdf")
file_old = student_visible_dir / Path("Practice Questions/quiz4_equations.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Exams/quiz4_2019t1/quiz4_2019t1.pdf")
file_old = student_visible_dir / Path("Practice Questions/quiz4_answers.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # #
# # # #
# # # # Day 18 --- Milankovitch
# # # #
# # #
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day18PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_16_Milankovitch/Quiz/Day18PreClassAssn_Milank_2018wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_16_Milankovitch/Quiz/Day18PreClassAssn_Milank_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day18QuizSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_16_Milankovitch/Worksheet/Milank_worksheet_v2.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day18Worksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_16_Milankovitch/Slides/Day18_Milankovitch_2018wT2_preclass.pdf')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day18PreClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_16_Milankovitch/Slides/Day18_Milankovitch_2018wT2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day18PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_16_Milankovitch/Worksheet/Milank_worksheet_v1_instructor.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day18WorksheetSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 19 --- GH My
# # # #
# # #
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day19PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_17_GH_My/Quiz/Day19PreClassAssn_GH_My_2018wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_17_GH_My/Quiz/Day19PreClassAssn_GH_My_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day19QuizSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_17_GH_My/Slides/Day19_GHvariabilityMy_2018wT2_preclass.pdf')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day19PreClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_17_GH_My/worksheet/SilicateWeatheringFeedbacks_v1nn.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day19Worksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_17_GH_My/worksheet/SilicateWeatheringFeedbacks_Instructor_v1.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day19WorksheetSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_17_GH_My/Slides/Day19_GHvariabilityMy_2018wT2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day19PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 20 --- GH Ky
# # # #
# # #
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day20PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_18_GH_Ky/Quiz/Day20PreClassAssn_GH_ky_2018wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day20QuizSolutions.pdf')
# # file_new=course_dir / Path('Classes/Day_18_GH_Ky/Quiz/Day20PreClassAssn_GH_ky_2018wT2_sln.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_18_GH_Ky/Slides/Day20_GHvariabilityKy_2018wT2_preclass.pdf')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day20PreClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_18_GH_Ky/Slides/Day20_GHvariabilityKy_2018wT2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day20PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 21 --- GH Y
# # # #
# # #
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day21PreClassAssignment.pdf')
# # file_new=course_dir / Path('Classes/Day_19_GH_Y/Quiz/Day21PreClassAssn_GH_centtoseas_2018wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day21QuizSolutions.pdf`w')
# # file_new=course_dir / Path('Classes/Day_19_GH_Y/Quiz/Day21PreClassAssn_GH_centtoseas_2018wT2_sln.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_19_GH_Y/Worksheet/SeasonalToCenturyCO2Worksheet_2018wT2.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day21Worksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_19_GH_Y/Worksheet/SeasonalToCenturyCO2Worksheet_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day21WorksheetSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_19_GH_Y/Slides/Day21_GHvariabilityCentToSeason_2018wT2_preclass.pdf')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day21PreClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_19_GH_Y/Slides/Day21_GHvariabilityCentToSeason_2018wT2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day21PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 22 ---
# # # #
# # #
# # file_old=student_visible_dir / Path('Practice Questions/M2_practiceQs_paleo.pdf')
# # file_new=course_dir / Path('Exams/midterm2_2018t1/Practice_Qs/M2_PracticeQs_2018wT2.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_old=student_visible_dir / Path('Practice Questions/M2_practiceQs_paleo_sln.pdf')
# # file_new=course_dir / Path('Exams/midterm2_2018t1/Practice_Qs/M2_PracticeQs_2018wT2_sln.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 23 --- How do we know its us?
# # # #
# # #
# # file_new=course_dir / Path('Classes/Day_22_How_do_we_know/Quiz/Day23PreClass_reading.pdf')
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day23PreClassAssignment.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_22_How_do_we_know/Worksheet/Day21_worksheet.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day23Worksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_22_How_do_we_know/Slides/Day23_HowDoWeKnowItsUs_2018t2_preclass.pdf')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day23PreClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_22_How_do_we_know/Slides/Day23_HowDoWeKnowItsUs_2018t2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day23PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # #
# # # #
# # # # Day 22 --- Climate models
# # # #
file_new = course_dir / Path("Classes/Day_23_modeling/reading/dessler_ch8.pdf")
file_old = student_visible_dir / Path("Pre Class Assignments/dessler_chapter8.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Classes/Day_23_modeling/quiz/day23quiz.pdf")
file_old = student_visible_dir / Path(
    "Pre Class Assignments/Day22PreClassAssignment.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Classes/Day_23_modeling/quiz/day23quiz_solutions.pdf")
file_old = student_visible_dir / Path("Quiz Solutions/Day23QuizSolutions.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Classes/Day_23_modeling/slides/Day22_2019t1.pdf")
file_old = student_visible_dir / Path("Pre Class Slides/Day22PreClassSlides.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Classes/Day_23_modeling/slides/Day22_2019t1.pdf")
file_old = student_visible_dir / Path("Post Class Slides/Day22PostClassSlides.pdf")
out = shutil.copyfile(file_new, file_old)
file_new = course_dir / Path(
    "Classes/Day_23_modeling/worksheet/kaya_worksheet_students.pdf"
)
file_old = student_visible_dir / Path("Worksheets/Day22Worksheet.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
#
#
## # # Day 23 --- Climate forecasts
# # # #
file_new = course_dir / Path("Classes/Day_23_modeling/reading/day22_md.pdf")
file_old = student_visible_dir / Path(
    "Readings - non-textbook, non-journal article/Day23Reading.pdf"
)
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
file_new = course_dir / Path("Classes/Day_24_forecasts/slides/Day23Slides_2019t1.pdf")
file_old = student_visible_dir / Path("Pre Class Slides/Day23PreClassSlides.pdf")
out = shutil.copyfile(file_new, file_old)
print(f"{out}\n{file_new}\n---\n")
# # #
# # file_new=course_dir / Path('Classes/Day_25_Future_Decisions/PreClassQuiz/Day24PreClassAssn_FutureDecisions_2018wT2.pdf# # # #
# # # # Day 24 --- Future Decisions
# # # #
# # #
# # file_new=course_dir / Path('Classes/Day_25_Future_Decisions/PreClassQuiz/Day24PreClassAssn_FutureDecisions_2018wT2.pdf')
# # file_old=student_visible_dir / Path('Pre Class Assignments/Day24PreClassAssignment.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_25_Future_Decisions/PreClassQuiz/Day24PreClassAssn_FutureDecisions_2018wT2_sln.pdf')
# # file_old=student_visible_dir / Path('Quiz Solutions/Day24QuizSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_25_Future_Decisions/Slides/Day24_FutureDecisions_2018wT2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day24PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_25_Future_Decisions/Worksheet/FutureDecisionsWorksheet_v4.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day24Worksheet.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_25_Future_Decisions/Worksheet/FutureDecisionsWorksheet_v4_sln.pdf')
# # file_old=student_visible_dir / Path('Worksheets/Day24WorksheetSolutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # # file_new=course_dir / Path('Assignments/Assignment_7/Reading_Dessler_8.3-8.6.pdf')
# # # file_old=student_visible_dir / Path('Assignments/Assignment07.Reading2.pdf')
# # # out=shutil.copyfile(file_new,file_old)
# # # print(f'{out}\n{file_new}\n---\n')
# # # the reading above was assigned but was substantially different from the first edition
# # #
# # # #
# # # # Day 25 --- Review
# # # #
# # #
# # file_new=course_dir / Path('Classes/Day_26_Review/Slides/day25_review_final_2018wT2_preclass.pdf')
# # file_old=student_visible_dir / Path('Pre Class Slides/Day25PreClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('Classes/Day_26_Review/Slides/day25_review_final_2018wT2_postclass.pdf')
# # file_old=student_visible_dir / Path('Post Class Slides/Day25PostClassSlides.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('practice_questions/FinalExamPractice/pha_practiceII.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/final/pha_practiceII.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('practice_questions/FinalExamPractice/pha_practiceII_solutions.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/final/pha_practiceII_solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('practice_questions/FinalExamPractice/greenhouse_questions.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/final/greenhouse_questions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('practice_questions/FinalExamPractice/greenhouse_questions_solutions.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/final/greenhouse_questions_solutions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('practice_questions/FinalExamPractice/paleo_questions.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/final/paleo_questions.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
# # file_new=course_dir / Path('practice_questions/FinalExamPractice/paleo_questions_sln.pdf')
# # file_old=student_visible_dir / Path('Practice Questions/final/paleo_questions_sln.pdf')
# # out=shutil.copyfile(file_new,file_old)
# # print(f'{out}\n{file_new}\n---\n')
