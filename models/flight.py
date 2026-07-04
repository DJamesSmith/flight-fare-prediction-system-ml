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

# fare: float | None = None
# because:
# During training: Fare exists.
# During prediction: Fare is unknown.

# Possible helper methods
# display()
# to_dictionary()
# useful for pandas

# Dataclass fields
# Constructor
# Types