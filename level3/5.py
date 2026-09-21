#  Loop + Condition
student = {
    "marks":{
        "python":88,
        "math":75,
        "english":90
    }
}
for key, value in student["marks"].items():
    if value > 80:
      print(key,"->",value)