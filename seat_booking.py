# class for the seat booking system
class SeatBookingSystem:
    
    def __init__(self):
        # create the list that will store all seats
        self.seats = []
        
        # create 80 rows of seats
        for i in range(80):
            row = ["F","F","F","X","F","F","F"]
            self.seats.append(row)
            
            
    # function to show all seats in the plane
    def show_booking_status(self):
        for row in self.seats:
            print(row)
            
            
    # function to get the seat position and check if it is valid
    def get_seat_position(self):
        seat = input("Enter seat number: ")

        # check if the input format is correct
        if not seat[:-1].isdigit() or seat[-1].upper() not in ["A","B","C","D","E","F"]:
            print("Invalid seat number")
            return None, None

        row = int(seat[:-1])

        # check if the row number is within the plane
        if row < 1 or row > 80:
            print("Invalid seat number")
            return None, None

        letter = seat[-1].upper()

        # dictionary to convert seat letters to column numbers
        columns = {"A":0,"B":1,"C":2,"D":4,"E":5,"F":6}
        column = columns[letter]

        return row, column
            
    
    # function to check if a seat is available
    def check_seat(self):

        row, column = self.get_seat_position()

        if row is None:
            return

        status = self.seats[row-1][column]
       
        if status == "F":
           print("Seat is available")
        elif status == "X":
           print("This is aisle")
        elif status == "S":
            print("This is storage")
        else:
            print("Seat is booked")
        
           
    # function to reserve a seat
    def book_seat(self):

        row, column = self.get_seat_position()

        if row is None:
            return

        status = self.seats[row-1][column]
       
        if status == "F":
            self.seats[row-1][column] = "R"
            print("Seat booked successfully")
        elif status == "X":
            print("This is aisle")
        elif status == "S":
             print("This is storage")
        else:
            print("Seat is already reserved")
            
            
    # function to free a reserved seat
    def free_seat(self):

        row, column = self.get_seat_position()

        if row is None:
            return

        status = self.seats[row-1][column]
       
        if status == "R":
            self.seats[row-1][column] = "F"
            print("Seat is now free")
        elif status == "X":
            print("This is aisle")
        elif status == "S":
             print("This is storage")
        else:
            print("Seat is already free")
            
            
    # additional function to count and show the number of free seats
    def show_available_seats(self):
        count = 0

        # loop through all rows and seats
        for row in self.seats:
            for seat in row:
                if seat == "F":
                    count += 1

        print("Available seats:", count)
            
            
# create object from the class
main_menu = SeatBookingSystem()


# main menu function
def main():

    while True:

        print("Welcome to Apache Airlines")
        print("1. Check seat availability")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking status")
        print("5. Show number of available seats")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            main_menu.check_seat()

        elif choice == "2":
            main_menu.book_seat()

        elif choice == "3":
            main_menu.free_seat()

        elif choice == "4":
            main_menu.show_booking_status()

        elif choice == "5":
            main_menu.show_available_seats()

        elif choice == "6":
            break

        else:
            print("Invalid option")


# run the program
main()  
            
        
        
        
                
            
            
       
            
        
        
               
        
        
           
            
            
                