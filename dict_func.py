# Write your code here!
def employee_print(employee_info):
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    otros = employee_info.copy()
    otros.pop("Name", None)
    otros.pop("Salary", None)
    otros.pop("Role", None)

    if len(otros) == 0:
        print("No other info!")
    else:
        for k, v in otros.items():
            print(f"{k}: {v}")