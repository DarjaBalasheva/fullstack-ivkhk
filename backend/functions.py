
def find_item(students_dict, key, value):
  h = []
  for i in students_dict:
    if value.lower() in i[key].lower():
      h.append(i)
  return h

def find_better(students_dict, value):
  h = []
  for i in students_dict:
    for key in i:
      if type(i[key]) == str:
        if i["top"]==True and i[key].lower() == value.lower():
          h.append(i)
  return h

def find_all_better(students_dict):
  h = []
  for i in students_dict:
    if i["top"]==True:
      h.append(i)
  return h
      

def find_everyone(students_dict, value):
  h = []
  for i in students_dict:
    for key in i:
      if type(i[key]) == str:
        if i[key].lower() == value.lower():
          h.append(i)
  return h

def find_all(students_dict):
  return {"data": students_dict}

def find_project(student_dict, uuid):
    for i in student_dict:
        if i["uuid"] == uuid:
          return i