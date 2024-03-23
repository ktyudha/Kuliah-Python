class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_salary(self, hours_worked):
        # Fungsi ini akan di-overridden oleh subclass
        pass


class RegularEmployee(Employee):
    def __init__(self, name, employee_id, basic_salary, hourly_rate):
        super().__init__(name, employee_id, basic_salary)
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked):
        return self.basic_salary + (hours_worked * self.hourly_rate)


class Contractor(Employee):
    def __init__(self, name, employee_id, basic_salary, monthly_rate):
        super().__init__(name, employee_id, basic_salary)
        self.monthly_rate = monthly_rate

    def calculate_salary(self, hours_worked):
        return self.basic_salary + self.monthly_rate


class Intern(Employee):
    def __init__(self, name, employee_id, basic_salary):
        super().__init__(name, employee_id, basic_salary)

    def calculate_salary(self, hours_worked):
        return self.basic_salary



name = input("Masukkan nama karyawan: ")
employee_id = input("Masukkan ID karyawan: ")
basic_salary = float(input("Masukkan gaji pokok: "))
employee_type = input("Masukkan jenis karyawan (Regular/Contractor/Intern): ")

if employee_type.lower() == "regular":
    hourly_rate = float(input("Masukkan tarif lembur per jam: "))
    employee = RegularEmployee(name, employee_id, basic_salary, hourly_rate)
elif employee_type.lower() == "contractor":
    monthly_rate = float(input("Masukkan upah bulanan: "))
    employee = Contractor(name, employee_id, basic_salary, monthly_rate)
elif employee_type.lower() == "intern":
    employee = Intern(name, employee_id, basic_salary)
else:
    print("Jenis karyawan tidak valid.")
    exit()

hours_worked = float(input("Masukkan jumlah jam kerja: "))


print("Gaji", employee.name, ":", employee.calculate_salary(hours_worked))
