for i in range(4):
  class = str(input("Name of class: "))
  building = str(input("Building class is in: "))
  time = str(input("Start time of class: "))
  place_1 = str(input("Place you are coming from: "))

coords_library = (50,10)
coords_lecture = (300, 10)
coords_cwing = (50, 100)
coords_sci_lib = (300, 100)
coords_union = (30, 50)


if building == Library:
  return coords_library
  print(coords_library)

if building == Lecture Hall:
  return coords_lecture
  print(coords_lecture)

if building == Classroom Wing:
  return coords_cwing
  print(coords_cwing)

if building == Science Library:
  return coords_sci_lib
  print(coords_sci_lib)

if building == Union:
  return coords_union
  print(coords_union)


