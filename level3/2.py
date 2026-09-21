#  Access Nested Dictionary
student = {
    "marks": {
        "python" : 88,
        "math"   : 75,
        "english": 90
    },
    "address" : {
        "street" : "mg road",
        "pincode": "380001" 
    }
}

print(student["marks"]["python"])
print(student["marks"]["math"])                   #student["marks"]["python"] 
print(student["marks"]["english"])
print(student["address"]["street"])
print(student["address"]["pincode"])
# Python  : 88
# Math    : 75
# English : 90

# Street  : MG Road
# Pincode : 380001
