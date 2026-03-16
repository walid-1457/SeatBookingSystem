import random
import string


# class to store passenger information
class Passenger:

    def __init__(self, first_name, last_name, passenger_number, booking_reference):
        self.first_name = first_name
        self.last_name = last_name
        self.passenger_number = passenger_number
        self.booking_reference = booking_reference


# class for the seat booking system
class SeatBookingSystem:
    
    def __init__(self):
        # create the list that will store all seats
        self.seats = []
        
        # create 80 rows of seats and add storage in first and last row
        for i in range(80):

            # add storage in first and last row
            if i == 0 or i == 79:
                row = ["S","F","F","X","F","F","S"]
            else:
                row = ["F","F","F","X","F","F","F"]

            self.seats.append(row)
        # dictionary to store booking details    
        self.bookings = {}
        
        # counter to give each passenger a different number
        self.passenger_counter = 1
            
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
        
        # get the row number from the input
        row = int(seat[:-1])

        # check if the row number is within the plane
        if row < 1 or row > 80:
            print("Invalid seat number")
            return None, None
        
        # get the seat letter and convert it to uppercase
        letter = seat[-1].upper()

        # dictionary to convert seat letters to column numbers
        columns = {"A":0,"B":1,"C":2,"D":4,"E":5,"F":6}
        column = columns[letter]

        return row, column
            
    
    # function to check if a seat is available
    def check_seat(self):
        
        # get seat position from the helper function
        row, column = self.get_seat_position()

        # stop the function if the seat input is invalid
        if row is None:
            return

        # get the current seat status from the seats list
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
            # ask the user for passenger details
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            
            # generate booking reference number
            booking_reference = self.generate_reference_number()
            
            # give the passenger a unique passenger number from passenger counter
            passenger_number = self.passenger_counter

            # create passenger object
            passenger = Passenger(first_name, last_name, passenger_number, booking_reference)
            
            self.bookings[booking_reference] = {
                "passenger": passenger,
                "seat_row": row,
                "seat_column": column
                }
            
            # increase passenger number for the next booking
            self.passenger_counter += 1
            
            # change seat status from free to reserved
            self.seats[row-1][column] = "R"
            
            # show booking confirmation
            print("Seat booked successfully")
            print("Booking Reference:", booking_reference)
            print("Passenger number:", passenger_number)

        elif status == "X":
            print("This is aisle")
        elif status == "S":
             print("This is storage")
        else:
            print("Seat is already reserved")
            
            
    # function to free a reserved seat
    def free_seat(self):
        
        # get seat position from the helper function
        row, column = self.get_seat_position()

        # stop the function if the seat input is invalid
        if row is None:
            return

        # get current seat status
        status = self.seats[row-1][column]
       
        if status == "R":
            # make the seat free again
            self.seats[row-1][column] = "F"
            
            # remove the related booking from the dictionary
            for reference in list(self.bookings):
                booking = self.bookings[reference]
                
                if booking["seat_row"] == row and booking["seat_column"] == column:
                    del self.bookings[reference]
                    break
                
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
            
            
    # function to generate a random booking reference number
    def generate_reference_number(self):
        
       # use letters and numbers for the booking reference
        characters = string.ascii_uppercase + string.digits
        reference = ""
        
        # create an 8-character random reference
        for i in range(8):
            reference += random.choice(characters)
         
        return reference    


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
        
               
        
        
           
            
            
                