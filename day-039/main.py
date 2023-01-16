import time
from data_manager import DataManager
from flight_search import FlightSearch


def main():
    data_manager = DataManager()
    sheet_data = data_manager.get_the_data()
    flight_search = FlightSearch()

    for item in sheet_data:         # If IATA code missing, search with searching_for_flights
        if item["iataCode"] == "":
            item["iataCode"] = flight_search.searching_for_flights(item["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_iata_codes()

    for item in sheet_data:
        print(f"{item['city']}: {flight_search.cost_from_london(item['iataCode'])}")


if __name__ == '__main__':
    main()
