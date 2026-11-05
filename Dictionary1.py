
prd1 = {"name": "laptop1", "price":90000}

print(prd1)

prd1["price"] = 90000

print(prd1)

prd1["price"] = 100000

print(prd1)

students={"name":"Ravi","age":19}
students["ERP"]="343434"
students["age"]="20"
print(students)

# Nested Dictionary

students = {
    "st1":{"name":"Ravi","ERP":909, "branch":"CSE CORE"},
    "st2":{"name":"Kishan","ERP":919, "branch":"CSE AIML"},
    "st3":{"name":"Rishabh","ERP":929, "branch":"CSE CYBER SECURITY"},
    "st4":{"name":"Rahul","ERP":939, "branch":"CSE DATA SCIENCE"},
    "st5":{"name":"Kundan","ERP":949, "branch":"CSE IT"},
}
print(students["st4"]["branch"])
students["st2"]["name"]="Virat Kohli"
for i in students.values():
    print(i)