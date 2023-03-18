
def find_item(students_dict, key, value):
  h = []
  for i in students_dict:
    if i[key].lower() == value.lower():
      h.append(i)
  return h

def find_everyone(students_dict, value):
  h = []
  for i in students_dict:
    for key in i:
      if i[key].lower() == value.lower():
        h.append(i)
  return h

def find_all(students_dict):
  return {"data": students_dict}

def find_project(student_dict, uuid):
    for i in student_dict:
        if i["uuid"] == uuid:
            return i