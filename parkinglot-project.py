from datetime import datetime as dt
# import json

parking_tower = [ # 주차 타워 현재 상태
    [0, 0, 0, 1111, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

current = { # 현재 주차된 차량 리스트
    "1111": {
        "parkinglot": "1F 4",
        "enter": "01:01:00:00"
    }
}

registered = { # 정기차량 리스트
    "1234": {
        "discount": 50
    }
}

enter_parkinglot = True

reserved = True

while enter_parkinglot :
    for floor in parking_tower:
        for i in floor:
            if i == 0:
                print("[ ]", end=" ")
            else:
                print("[X]", end=" ")
        print("")
    # print(json.dumps(current, indent=2))
    status = input("입차:1, 출차:2, 종료:3 ")
    match status:
        case "1":
            license_plate = input("차량번호 (0000)를 입력해주세요. ")
            enter_time = input("입차시각 (MM:DD:hh:mm)을 입력해주세요. ")
            while reserved: # 입력한 자리가 비어 있을때까지 다시 물어보기 
                parking_lot = input("원하는 주차 위치 (0F 00)를 입력해주세요. ")
                location = parking_lot.split("F ") # 층과 자리로 나누기 
                if parking_tower[int(location[0])-1][int(location[1])-1] == 0:
                    parking_tower[int(location[0])-1][int(location[1])-1] = license_plate
                    current[license_plate] = {} # 현재 주차된 차량 리스트에 정보 추가
                    current[license_plate]["parkinglot"] = parking_lot
                    current[license_plate]["enter"] = enter_time
                    print("주차가 완료되었습니다")
                    reserved = False # 입력한 자리가 비어있고 주차까지 완료시 루프에서 탈출
                else:
                    print("해당 자리에 이미 차량이 주차 되어 있습니다.")
        case "2":
            license_plate = input("차량번호 (0000)를 입력해주세요. ")
            exit_time = input("출차시각 (MM:DD:hh:mm)을 입력해주세요. ")
            time1 = dt.strptime(current[license_plate]["enter"], "%m:%d:%H:%M")
            time2 = dt.strptime(exit_time, "%m:%d:%H:%M")
            time_difference = (time2 - time1).total_seconds() / 60
            fee = time_difference * 100
            if license_plate in registered: #정기차량인지 확인
                fee *= registered[license_plate]["discount"] /100
            print(f"총 {int(time_difference)}분 주차 하였고 요금은 {int(fee)}원 입니다.")
            parking_tower[int(location[0])-1][int(location[1])-1] = 0 # 빈자리로 돌려짐
        case "3":
            enter_parkinglot = False
        case _:
            print("Invalid number")