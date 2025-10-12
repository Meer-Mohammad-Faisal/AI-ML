marks = {
    "Faisal": 100,
    "badal": 56,
    "Rohan":23,
    0:"badal"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Faisal":99, "Renu": 56})
print(marks)
print(marks.get("Faisal"))
print(marks.get("Faisal2")) # prints NONE
#print(marks["Faisal2"]) # Return an error
