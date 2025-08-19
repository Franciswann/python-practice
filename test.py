print("---------------------------")
# Python 2D Array
print("Python 2D Array\n")
martrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(martrix)
print(martrix[1][2])

print("---------------------------")
# Python Encapsulation -> class (Python沒有struct關鍵字)
print("Python Encapsulation\n")

class user:
    def __init__(self, name, user_id, user_grades):
        self.name = name
        self.user_id = user_id
        self.user_grades = user_grades
    
    def average(self):
        return (sum(self.user_grades)/len(self.user_grades))

Jennie = user("Jennie", 40, [10, 7, 8])

print("attribute")
print("def __init__(self, name, user_id, user_grades):\n")
print("Jennie = user(\"Jennie\", 40, [10, 7, 8])\n")
print(Jennie.name)
print(Jennie.user_id)
print(Jennie.user_grades)

print("\nmethod")
print("def average(self):\n")
print("Jennie.average\n")
print(Jennie.average())
        
print("---------------------------")
