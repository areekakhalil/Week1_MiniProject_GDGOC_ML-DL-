# week1_project.py

# Question 1: User Data Collector
print("----- Question 1: User Data Collector -----")
data = {}
data["name"] = input("Enter your name: ")
data["age"] = input("Enter your age: ")
data["email"] = input("Enter your email: ")

# Check email
if "@" in data["email"] and "." in data["email"]:
    print("Email is valid.")
else:
    print("Email is not valid.")

data["fav_num"] = input("Enter your favorite number: ")
print(f"\nInfo:\nName: {data['name']}\nAge: {data['age']}\nEmail: {data['email']}\nFav Number: {data['fav_num']}")

# Question 2: Even or Odd?
print("\n----- Question 2: Even or Odd -----")
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if is_even(n):
    print(f"{n} is Even.")
else:
    print(f"{n} is Odd.")

# Question 3: Temperature Converter
print("\n----- Question 3: Temperature Converter -----")
def convert_temp(t, s):
    if s == "C":
        return (t * 9/5) + 32
    elif s == "F":
        return (t - 32) * 5/9
    else:
        return None

t = float(input("Enter temperature: "))
s = input("Enter scale (C/F): ").upper()
res = convert_temp(t, s)
if res is not None:
    if s == "C":
        print(f"{t}°C = {res:.2f}°F")
    else:
        print(f"{t}°F = {res:.2f}°C")
else:
    print("Wrong scale entered.")

# Question 4: Finding Min & Max
print("\n----- Question 4: Finding Min & Max -----")
def find_min_max(lst):
    return max(lst), min(lst)

nums = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)

mx, mn = find_min_max(nums)
print(f"Max: {mx}")
print(f"Min: {mn}")

# Question 5: Student Data Manager
print("\n----- Question 5: Student Data Manager -----")
std_list = []
for i in range(3):
    n = input(f"Enter name of student {i+1}: ")
    a = input("Enter age: ")
    g = input("Enter grade: ")
    std_list.append((n, a, g))

std_dict = {}
for s in std_list:
    std_dict[s[0]] = (s[1], s[2])

print("Student Info:")
print(std_dict)

# Question 6: Inventory Management System
print("\n----- Question 6: Inventory Management System -----")
def update_inv(inv, item, qty):
    if item in inv:
        inv[item] = max(0, inv[item] + qty)
    else:
        inv[item] = max(0, qty)
    return inv

inv = {
    "pen": 10,
    "book": 5,
    "eraser": 7,
    "marker": 3,
    "scissor": 4
}

for i in range(3):
    it = input("Enter item to update: ").lower()
    q = int(input("Enter quantity (+ to add, - to remove): "))
    update_inv(inv, it, q)

print("Updated Inventory:")
print(inv)
