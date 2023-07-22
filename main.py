class FitnessTracker:
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

     def get_calories_intake(self):
        return self.calories_consumed - self.calories_burned   

     def get_water_intake(self):
       return self.water_intake_ml
                
def main():
     print("Welcome to the Dream Fitness Tracker!")

     tracker = FitnessTracker()

     while True:
          print("\nChoose an option:")
          print("1. Track Excerise")
          print("2. Track Meal")
          print("3. Track Water Intake")
          print("4. View Calories Balance")
          print("5. View Water Intake")
          print("6. Exit")

          
          choice = input("Enter your choice (1/2/3/4/5/6):")

          if choice == "1":
               try:
                    calories_burned = float(input("Enter the calories burned during exercise: "))
                    tracker.track_exerices(calories_burned)
                    print("Exercise tracked successfully!")
               except ValueError:
                print("Invalid input. Please enter a valid number.")


          elif choice =="2":
               try:
                    calories_consumed =float(input("Enter the calories consumed during the meal:"))
                    tracker.track_meal(calories_consumed)
                    print("Meal tracked sucessfully!")
               except ValueError:
                     print("Invalid input. Please enter a valid number.")

          elif choice =="3":
                try:
                    water_intake_ml=float(input("Enter the water intake in milliliters:"))  
                    tracker.track_water_intake(water_intake_ml)
                    print("Water intake Tracked!")
                except ValueError:
                     print("Invalid input. Please enter a valid number.")
      
          elif choice =="4":
               calories_Balance = tracker.get_calories_Balance()
               print(f"Calories intake for the day: {calories_Balance}") 

          elif choice =="5":
               water_intake = tracker.get_water_intake()
               print(f"water intake for the day: {water_intake} ml")

          elif choice =="6":
               print("Exiting the Dream Fitness Tracker. Goodbye!")
               break 
          else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()                     



  
  
  
