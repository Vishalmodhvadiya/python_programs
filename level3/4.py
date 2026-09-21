# Loop Through Keys and Values
 
student = {
    "marks":{
        "python":88,
        "math":75,
        "english":90
    }
}
for key, value in student["marks"].items():
    print(key,"->",value)

# python  → 88
# math    → 75
# english → 90