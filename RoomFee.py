

size_rate = 0.43
floor_rate = 0.02
beds_rate = 0.3
people_rate = 0.15
condition_rate = 0.1
bedroom = []
floor = {}

class Bedroom:
    def __init__(self,size,bad_condition,people,beds,floor):
        self.size = size
        self.bad_condition = bad_condition
        self.people = people
        self.beds = beds
        self.floor = floor
        self.size_fee = 0
        self.bad_condition_fee = 0
        self.people_fee = 0
        self.beds_fee = 0
        self.floor_fee = 0


def getSizeFee():
    total_size = 0
    for e in bedroom:
        total_size += e.size
    unit_size_fee = cost * size_rate / total_size
    for e in bedroom:
        e.size_fee = unit_size_fee * e.size

def getFloorFee():
    total_floor = 0
    for e in bedroom:
        total_floor += e.floor
    unit_floor_fee = cost * floor_rate / total_floor
    for e in bedroom:
        e.floor_fee = unit_floor_fee * e.floor

def getBedsFee():
    total_beds = 0
    for e in bedroom:
        total_beds += e.beds
    unit_beds_fee = cost * beds_rate / total_beds
    for e in bedroom:
        e.beds_fee = unit_beds_fee * e.beds

def getPeopleFee():
    total_people = 0
    for e in bedroom:
        total_people += e.people
    unit_people_fee = cost * people_rate / total_people
    for e in bedroom:
        e.people_fee = unit_people_fee * e.people

def getConditionFee():
    total_good_condition = 0
    for e in bedroom:
        if e.bad_condition == 0:
            total_good_condition += 1
    if total_good_condition == 0:
        total_good_condition = len(bedroom)
    unit_bad_condition_fee = cost * condition_rate / total_good_condition
    for e in bedroom:
        if e.bad_condition == 0:
            e.bad_condition_fee = unit_bad_condition_fee

if __name__ == "__main__":
    print("Total cost:")
    cost = float(input())
    print("Floors:")
    n_floor = int(input())
    for i in range(1,n_floor+1):
        print("How many bedrooms in {0}st floor:".format(i))
        n_room = int(input())
        floor[i]=n_room
        for j in range(1,n_room+1):
            print("Room size:")
            size = float(input())
            print("Bad condition[0/1]:")
            bad_condition = int(input())
            print("How many people live in:")
            n_people = int(input())
            print("How many beds:")
            n_beds = int(input())
            bedroom.append(Bedroom(size,bad_condition,n_people,n_beds,i))
            print("Room {0} completed.".format(j))

    getSizeFee()
    print("\nSize Fee: {0}".format(cost*size_rate))
    index = 0
    for e in floor:
        for i in range(1,floor[e]+1):
            print("Bedroom {0} : {1}".format(i,bedroom[index].size_fee))
            index += 1

    getFloorFee()
    print("\nFloor Fee: {0}".format(cost * floor_rate))
    index = 0
    for e in floor:
        for i in range(1,floor[e]+1):
            print("Bedroom {0} : {1}".format(index+1, bedroom[index].floor_fee))
            index += 1

    getBedsFee()
    print("\nBeds Fee: {0}".format(cost * beds_rate))
    index = 0
    for e in floor:
        for i in range(1,floor[e]+1):
            print("Bedroom {0} : {1}".format(index+1, bedroom[index].beds_fee))
            index += 1

    getPeopleFee()
    print("\nPeople Fee: {0}".format(cost * people_rate))
    index = 0
    for e in floor:
        for i in range(1,floor[e]+1):
            print("Bedroom {0} : {1}".format(index+1, bedroom[index].people_fee))
            index += 1

    getConditionFee()
    print("\nBad Condition Fee: {0}".format(cost * condition_rate))
    index = 0
    for e in floor:
        for i in range(1,floor[e]+1):
            print("Bedroom {0} : {1}".format(index+1, bedroom[index].bad_condition_fee))
            index += 1

    print("\nTotal Price For Every Room: ")
    for i in range(0,len(bedroom)):
        room_price = bedroom[i].size_fee+bedroom[i].bad_condition_fee+bedroom[i].people_fee+bedroom[i].floor_fee+bedroom[i].beds_fee
        print("Bedroom {0} : {1}. For single person : {2}".format(i,round(room_price,2),round(room_price/bedroom[i].people,2)))
