from dataclasses import dataclass
from datetime import date, time

@dataclass
class Flight:
    flight_id: int | None = None
    airline: str = ""
    source: str = ""
    destination: str = ""
    journey_date: date = ""
    departure_time: time = ""
    arrival_time: time = ""
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

# df = pd.DataFrame([flight.to_dictionary()])

# Data_train.csv        Model
# Airline               ✔ airline
# Date_of_Journey       ✔ journey_date
# Source                ✔ source
# Destination           ✔ destination
# Route                 ✔ 
# Dep_Time              ✔ departure_time
# Arrival_Time          ✔ arrival_time
# Duration              ✔ duration
# Total_Stops           ✔ total_stops
# Additional_Info       ✔ additional_information
# Price                 ✔ fare

# Test_set.csv
# Airline
# Date_of_Journey
# Source
# Destination
# Route
# Dep_Time
# Arrival_Time
# Duration
# Total_Stops
# Additional_Info