from prac_08.taxi import Taxi

vehicle = Taxi("Prius 1", 100)
vehicle.drive(40)
print("Taxi Details: {}".format(vehicle))
print("Total Fare: ${:.2f}".format(vehicle.get_fare()))
vehicle.start_fare()
vehicle.drive(100)
print("Taxi Details: {}".format(vehicle))
print("Total Fare: ${:.2f}".format(vehicle.get_fare()))

