
class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, price, departure_city, departure_iata_code, destination_city, destination_iata_code,
                 departure_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.departure_city = departure_city
        self.departure_iata_code = departure_iata_code
        self.destination_city = destination_city
        self.destination_iata_code = destination_iata_code
        self.departure_date = departure_date
        self.return_date = return_date
        # Optional:
        self.stop_overs = stop_overs
        self.via_city = via_city
