# Day 10 ( Functions)

#  1: Student Marks Management (Assignment 1)

## 1️1 Store Student Data


def store_students():
    students = [
        {"roll": 1, "name": "Ajay", "marks": 450, "total": 500},
        {"roll": 2, "name": "Bhanu", "marks": 420, "total": 500},
        {"roll": 3, "name": "Pandu", "marks": 390, "total": 500},
        {"roll": 4, "name": "Hamza", "marks": 470, "total": 500},
    ]
    return students



## 2️ Sort Students by Name


def sort_by_name(students):
    return sorted(students, key=lambda s: s["name"])


## 3️ Calculate Percentage


def calculate_percentage(students):
    for student in students:
        student["percentage"] = (student["marks"] / student["total"]) * 100
    return students


## 4️ Print Student Data


def print_students(students):
    for s in students:
        print(
            f"Roll: {s['roll']}, "
            f"Name: {s['name']}, "
            f"Marks: {s['marks']}/{s['total']}, "
            f"Percentage: {s['percentage']:.2f}%"
        )

students = store_students()
students = sort_by_name(students)
students = calculate_percentage(students)
print_students(students)



#  PART 2: Readability Example (E-Commerce Billing)

### Calculation Function


def calculate_total(price, quantity):
    return price * quantity


### Display Function


def print_bill(item, price, quantity, total):
    print("Item:", item)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Amount:", total)


### Main Flow


item = "T-Shirt"
price = 500
quantity = 3

total = calculate_total(price, quantity)
print_bill(item, price, quantity, total)



#  PART 3: Car Service Center (Traceability Assignment)

### Calculation Function


def calculate_service_bill(car_code, service_charge):
    return {
        "car_code": car_code,
        "service_charge": service_charge
    }


### Display Function


def print_service_bill(bill):
    print("Car Code:", bill["car_code"])
    print("Service Charge:", bill["service_charge"])


### Main Flow


car_code = "SUV123"
service_charge = 3500

bill = calculate_service_bill(car_code, service_charge)
print_service_bill(bill)

