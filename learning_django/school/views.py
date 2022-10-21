from django.shortcuts import render
import json

from django.http import HttpResponse
 



def insert_student(request):
  with open('./school/data.json') as f:
    file_data = json.load(f)
  request_data = json.loads(request.body)
  students_data = file_data['students']
  for student in students_data:
    if student['id'] == request_data['id']:
      return HttpResponse(json.dumps({"message": "student already exists"}))

  students_data.append(request_data)
  file_data['students'] = students_data
  
  with open('./school/data.json',"w+") as of:
    json.dump(file_data, of)
  return HttpResponse(json.dumps({"message": "student inserted successfully"}))

def get_student(request , id):
  with open('./school/data.json') as f:
    file_data = json.load(f)
  students_data = file_data['students']
  for student in students_data:
    if student['id'] == id:
      return HttpResponse(json.dumps(student))
  return HttpResponse(json.dumps({"message": "student not found"}))

def delete_or_update_student(request , id):
  with open('./school/data.json') as f:
    file_data = json.load(f)
  students_data = file_data['students']
  for student in students_data:
    if student['id'] == id:
      if request.method == "DELETE":
        students_data.remove(student)
        file_data['students'] = students_data
        with open('./school/data.json',"w+") as of:
          json.dump(file_data, of)
        return HttpResponse(json.dumps({"message": "student deleted successfully"}))
      elif request.method == "PUT":
        request_data = json.loads(request.body)
        student['id'] = request_data['id']
        student['age'] = request_data['age']
        student['name'] = request_data['name']
        file_data['students'] = students_data
        with open('./school/data.json',"w+") as of:
          json.dump(file_data, of)
        return HttpResponse(json.dumps({"message": "student updated successfully"}))
  return HttpResponse(json.dumps({"message": "student not found"}))
  