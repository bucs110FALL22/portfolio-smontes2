from time import strftime

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.id = strftime("%d%m%M%S")
        self.arrived = strftime("%A, %D %B %Y")
        self.adopted = None
        
    def set_adopted(self):
          self.adopted = strftime("%d%m%M%S")

    def __str__(self):
         result_str = f"{self.name}[{self.type}]"
         result_str += f"\narrived: {self.arrived}"
         result_str += f"\nadopted: {self.adopted}"
         return result_str

    
def main():
      fido = Animal("fido", "cat")
      print(fido.set_adopted())
      print(fido)

      

main()



        