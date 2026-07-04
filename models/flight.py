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
        print(f"Airline : {self.airline}\n")
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
    def to_dictionary(self) -> dict[str, object]:
        # df = pd.DataFrame([flight.to_dictionary()])
        return {
            "Airline": self.airline,
            "Source": self.source,
            "Destination": self.destination,
            "Journey_Date": self.journey_date,
            "Departure_Time": self.departure_time,
            "Arrival_Time": self.arrival_time,
            "Duration": self.duration,
            "Total_Stops": self.total_stops,
            "Additional_Information": self.additional_information,
            "Fare": self.fare,
        }

# Possible helper method: to_dictionary()