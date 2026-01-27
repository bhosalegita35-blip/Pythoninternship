# Mobile Recharge Validation System
def mobile_recharge():
    try:
        
        mobile_number = input("Enter your 10-digit mobile number: ")
        recharge_amount = float(input("Enter recharge amount (₹): "))

        
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            raise ValueError("Invalid mobile number! Must be exactly 10 digits.")

        
        if recharge_amount <= 10:
            raise ValueError("Invalid recharge amount! Must be greater than ₹10.")

        
        print(f"Recharge successful! ₹{recharge_amount} has been added to {mobile_number}.")

    except ValueError as ve:
        print(f"Recharge failed: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


mobile_recharge()

# Online Movie Ticket Booking
def book_movie_tickets():
    try:
        
        tickets = input("Enter number of tickets: ")

        
        if not tickets.isdigit():
            print(" Invalid input! Please enter a numeric value.")
            return

        tickets = int(tickets)

        
        if tickets > 6:
            print(" You can book a maximum of 6 tickets only.")
            return

    
        ticket_price = 250
        total_price = tickets * ticket_price

        print(f" Booking successful! Total price: ₹{total_price}")

    except Exception as e:
        print(" An error occurred:", e)



book_movie_tickets()


#Electricity Bill Calculator
def calculate_electricity_bill():
    try:
        
        units = input("Enter electricity units consumed: ")

        
        if not units.isdigit():
            print(" Invalid input! Please enter a positive numeric value.")
            return

        units = int(units)

        if units <= 0:
            print(" Units must be a positive number.")
            return

        
        if units <= 100:
            bill = units * 5
        elif units <= 300:
            bill = (100 * 5) + ((units - 100) * 7)
        else:
            bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

        print(f" Your electricity bill is: ₹{bill}")

    except Exception as e:
        print(" An error occurred:", e)



calculate_electricity_bill()

