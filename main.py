
class fitnesstracker:
     def __init__(self):
          self.calories_burned = 0
          self.calories_consumed = 0
          self.water_intake_ml = 0

def track_exerices(self,calories):
     self.calories_burned += calories 

def track_meal(self,calories):
     self.calories_consumed += calories

def track_water_intake(self, ml):
     self.water_intake_ml += ml 

def get_calories_balance(self):
     return self.calories_consumed - self.calories_burned   

def get_water_intake(self):
     return self.water_intake_ml
                
def main():
     print("Welcome to the dream fitness tracker!")

     tracker = fitnesstracker()

     while True:
          print("\nChoose an option:")
          print("1. Track Excercise")
          print("2. Track meal")
          print("3. Track Water Intake")
          print("4. view Calories Balance")
          print("5. View Water Intake")
          print("6. Exit")
          
          choice = input("Enter your choice (1/2/3/4/5/6):")

          if choice == "1":



  
  
  
