스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
추가체력 = int(input("추가 체력을 입력해주세요 : "))

궁극기보호막 = 55 + (스킬레벨 * 10) + (추가체력 * 0.3) + (주문력 * 1.5)

print(궁극기보호막)
