print("Script started")

from database import get_department_complaints

print("Function imported")

data = get_department_complaints(1)

print("Data returned:", data)

print("Script finished")