from dataclasses import dataclass, InitVar
from typing import Optional
from enum import Enum


class TransportType(Enum):
    BUS = 1
    TAXI_BUS = 2
    TROLLEYBUS = 3
    TRAM = 4
    RIVER_BUS = 5
    METRO = 6
    HELICOPTER = 7
    RICKSHAW = 8


# заморозили следовательно сделали константным
@dataclass(frozen=True)
class Route:
    transport_type: TransportType
    route_id: str
    start_point: str
    end_point: str


@dataclass  # декоратор
class PublicVehicle:
    transport_type: TransportType
    vehicle_id: str
    owner_company: str
    capacity: InitVar[int] = 100
    is_benefit_available: bool = True
    current_route: Optional[Route] = None
    license_plate: Optional[str] = None

    def assign_route(self, new_route: Route):
        if self.transport_type == new_route.transport_type:
            self.current_route = new_route

    def __post_init__(self, *args):
        if self.transport_type == TransportType.TAXI_BUS:
            self.is_benefit_available = False
        # self.is_benefit_available = False if self.transport_type == TransportType.TAXI_BUS else self.is_benefit_available


#при наслдеовании в дате классе нельзя добалвтья в конец занчения по умолчанию(проблема)
# @dataclass
# class Bus(PublicVehicle):
#     # transport_type = TransportType.BUS
#     fuel_tye: str


# new_veh = PublicVehicle(1, 'bus', True, '33', 'YarBus')
public_veh1 = PublicVehicle(TransportType.BUS, '123', 'SuperTrans Ltd', capacity=50, license_plate='AOOO1AA76')
# public_veh2 = PublicVehicle(50, TransportType.BUS, '123', 'SuperTrans Ltd', license_plate='AOOO1AA76')
public_veh1.capacity = 100
# public_veh3 = Bus(50, vehicle_id='123', owner_company='SuperTrans Ltd', license_plate='AOOO1AA76')

# new_r = Route('bus', '2013', 'Bragino', 'Suzdalka')
# new_veh.assign_route(new_r)

# print(public_veh1, public_veh2)
# print(repr(public_veh1), repr(public_veh2))
# print(public_veh1 == public_veh2)
# print(TransportType.TRAM.name, TransportType.TRAM.value)
# print('IDENTICAL' if public_veh1 == public_veh3 else 'NO')
print(public_veh1.capacity)
public_veh1.capacity = 200
print(public_veh1.capacity)
print(public_veh1)