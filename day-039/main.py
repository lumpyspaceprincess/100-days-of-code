from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


def main():
    data_manager = DataManager()
    sheet_data = data_manager.get_the_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    for item in sheet_data:         # If IATA code missing, search with searching_for_flights
        if item["iataCode"] == "":
            item["iataCode"] = flight_search.searching_for_flights(item["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_iata_codes()

    for item in sheet_data:
        flight = flight_search.cost_from_london(item['iataCode'])

        if flight.price < item["lowest Price"]:
            notification_manager.send_sms_message(message_body=f"Low price alert! only {flight.price} to fly from "
                                                  f"{flight.departure_city}-{flight.departure_iata_code} to "
                                                  f"{flight.destination_city}-{flight.destination_iata_code}, from "
                                                  f"{flight.departure_date} to {flight.return_date}.")

    # TODO 3:
    # If the price is lower than the lowest price listed in the Google Sheet then send
    # an SMS to your own number with the Twilio API.


if __name__ == '__main__':
    main()
