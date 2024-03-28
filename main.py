# Built-in imports
import math
# Your code below
GRADE = dict()
for i in range(101):
  if 40 > i:
    grade = "U"
  elif 45 > i:
    grade = "S"
  elif 50 > i:
    grade = "E"
  elif 55 > i:
    grade = "D"
  elif 60 > i:
    grade = "C"
  elif 70 > i:
    grade = "B"
  else:
    grade = "A"
  GRADE[i] = grade

def read_testscores(filename):
  studentdata = []
  data_file = open(filename,'r')
  for x in data_file:
    x = x.strip().split(",")
    if x[3].isdigit():
      overall = math.ceil(int(x[2])/30 * 15 + (int(x[3])/40 * 30) + (int(x[4])/80 * 35) + (int(x[5])/30 * 20))
      temp = {"class":x[0],"name":x[1],"overall":overall,"grade":GRADE[overall]}
      studentdata.append(temp)
  return studentdata

def analyze_grades(studentdata):
  class_grades = dict()
  dynclass = ""
  for i in range(len(studentdata)):
    if dynclass != studentdata[i]["class"]:
      dynclass = studentdata[i]["class"]
      class_grades[dynclass] = {"A":0,"B":0,"C":0,"D":0,"E":0,"S":0,"U":0}
    
    if studentdata[i]["grade"] == "A":
      class_grades[dynclass]["A"] += 1
    elif studentdata[i]["grade"] == "B":
      class_grades[dynclass]["B"] += 1
    elif studentdata[i]["grade"] == "C":
      class_grades[dynclass]["C"] += 1
    elif studentdata[i]["grade"] == "D":
      class_grades[dynclass]["D"] += 1
    elif studentdata[i]["grade"] == "E":
      class_grades[dynclass]["E"] += 1
    elif studentdata[i]["grade"] == "S":
      class_grades[dynclass]["S"] += 1
    else:
      class_grades[dynclass]["U"] += 1
  return class_grades
