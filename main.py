from tracker import add_session, view_summary, view_all_session

def add_screen_time_sessons():
    add_session()



def main_loop():

    #greeting
    x = input("Welcome to screen time tracker! \n1. Add Screen Time Session\n2. View Summary \n3. View All Sessions\n4. Exit \nEnter choice:  ")
    #pathhing: use the match statment to asign the correct function for the users choise
    match x:
        case "1":
            add_screen_time_sessons()
        case "2":
            view_summary()
        case "3":
            view_all_session()
        case "4":
            print("exiting program \nGoodbye.")
            return
        case _:
            print("⚠ ⚠ ⚠\t invalid input \t\t⚠ ⚠ ⚠ \n⚠ ⚠ ⚠\t error[400]Badrequest,\t⚠ ⚠ ⚠\n⚠ ⚠ ⚠\t please try again using\t⚠ ⚠ ⚠\n⚠ ⚠ ⚠\t the options given\t⚠ ⚠ ⚠")
    return

main_loop()