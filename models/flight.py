from dataclasses import dataclass

@dataclass
class Flight:
    flight_id: int | None = None
    airline: str = ""
    source: str = ""
    destination: str = ""
    journey_date: str = ""
    departure_time: str = ""
    arrival_time: str = ""
    duration: str = ""
    total_stops: str = ""
    additional_information: str = ""
    fare: float | None = None

    def display_details(self):
        print(f"Airline : {self.airline}")
        print(f"Source : {self.source}")
        print(f"Destination : {self.destination}")
        print(f"Journey Date : {self.journey_date}")
        print(f"Departure Time : {self.departure_time}")
        print(f"Arrival Time : {self.arrival_time}")
        print(f"Duration : {self.duration}")
        print(f"Stops : {self.total_stops}")

        if self.fare is not None:
            print(f"Fare : ₹{self.fare}")

    # When the ML pipeline is implemented, a pandas DataFrame from Flight objects is to be created
    def to_dictionary(self) -> dict:
        # df = pd.DataFrame([flight.to_dictionary()])
        ...

# Possible helper method: to_dictionary()