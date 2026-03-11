import data
from data import apps, screentime, type_app

def add_session():
    print("\n--- Add a new screen time session ---")
    
    # 1. App / site name (cannot be empty)
    name = input("what app did you use? \nex:facetime,text,intstgram: ").strip()
    while not name:
        print("Error: Name cannot be empty!")
        name = input("Enter app/site name: ").strip()
    
    while True:
        try:
            minutes = int(input("how much time did you use the app? \nex:60,15,45: ").strip())
            if minutes > 0:
                break
            print("Error: Please enter a number bigger than 0.")
        except ValueError:
            print("Error: That's not a valid number. Try again.")

    category = input("(what was the reasson for the screen time? \nex:Social/School/Entertainment/Other): ").strip()
    apps.append(name)
    type_app.append(category)
    screentime.append(minutes)  
    #save_data()
    print("\nSession added successfully!")

def view_summary():
    total_sessions = len(screentime)
    total_minutes = sum(screentime)
    average_minutes = total_minutes / total_sessions
    max_minutes = max(screentime)
    min_minutes = min(screentime)

    print("Total sessions:", total_sessions)
    print("Total minutes:", total_minutes)
    print("Average minutes:", average_minutes)
    print("Max minutes:", max_minutes)
    print("Min minutes:", min_minutes)

def view_all_session():

    print("\nAll Screen Time Sessions")

    for i in range(len(apps)):
        print(f"{apps[i]} - {screentime[i]} minutes - {type_app[i]}")  

#def save_data():
    #with open("data.py", "w") as f:
        #f.write(f"apps = {apps} \nscreentime = {screentime} \ntype_app = {type_app}")
        
#save_data()
