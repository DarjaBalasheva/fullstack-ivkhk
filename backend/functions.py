def dict_create(tuple_):
  dict_lict = []
  for row in tuple_:
    row = dict(row)
    dict_lict.append(row)
  return dict_lict
def create_media_list(file_dict):
  file_list = []
  for i in range(2,26):
    if file_dict[f'app_{i}'] is not None:
      file_list.append(file_dict[f'app_{i}'])
  return file_list


