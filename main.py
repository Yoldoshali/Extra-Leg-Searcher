from flight_search import FlightSearch

departure_airport = input("Enter departure: ")
destination_airport = input("Enter destination: ")
departure_date = input("Enter departure date: ")
return_date = input("Enter return date: ")
print(f"\n[+] Processing ...\n")

flight_search = FlightSearch(departure_airport, destination_airport, departure_date, return_date)