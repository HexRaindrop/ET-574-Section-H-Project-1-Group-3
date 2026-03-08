import data
from data import apps, screentime, type_app

def add_session():
    print("\n--- Add a new screen time session ---")
    
    # 1. App / site name (cannot be empty)
    name = input("Efacetime,text,intstgram: ").strip()
    while not name:
        print("Error: Name cannot be empty!")
        name = input("Enter app/site name: ").strip()
    
    while True:
        try:
            minutes = int(input("60,15,45: ").strip())
            if minutes > 0:
                break
            print("Error: Please enter a number bigger than 0.")
        except ValueError:
            print("Error: That's not a valid number. Try again.")

    category = input("(Social/School/Entertainment/Other): ").strip()
    apps.append(name)
    type_app.append(category)
    screentime.append(minutes)  
    save_data()
    print("\nSession added successfully!")

def save_data():
    with open("data.py", "w") as f:
        f.write(f"apps = {apps} \nscreentime = {screentime} \ntype_app = {type_app}")
        
save_data()
