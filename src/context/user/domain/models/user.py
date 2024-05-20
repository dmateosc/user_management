from datetime import datetime


class Name:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DNI:
    def __init__(self, dni: str):
        self.dni = dni

    def __str__(self):
        return f"{self.dni}"

class Phone:
    def __init__(self, number: int):
        if not self.validate(number):
            raise ValueError("Invalid phone number")
        self.number = number

    def __str__(self):
        return str(self.number)

    @staticmethod
    def validate(number: int) -> bool:
        # Implementar una lógica de validación de número de teléfono aquí
        # Esto es solo un ejemplo simple
        return len(str(number)) == 9  # Ejemplo de longitud de número de teléfono

class LastDate:
    def __init__(self, last_date_str: str):
        self.last_date = datetime.strptime(last_date_str, "%Y-%m-%d")

    def __str__(self):
        return self.last_date.strftime("%Y-%m-%d")

class Active:
    def __init__(self, active: bool):
        self.active = active

    def __str__(self):
        return "Active" if self.active else "Inactive"
      
class User():
  def __init__(self,dni: DNI, name: Name, phone: Phone, active: Active, last_date: LastDate):
    self.dni = dni
    self.name = name
    self.phone = phone
    self.active = active
    self.last_date = last_date
  def __str__(self):
    return f"Name: {self.name}, Phone: {self.phone}, Active: {self.active}, Last Date: {self.last_date}, DNI: {self.dni}"

