스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
공격력 = int(input("공격력을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
최대체력 = int(input("최대 체력을 입력해주세요 : "))

기본피해량 = 50 + (스킬레벨 * 100)
피해량 = 기본피해량 + (주문력 * 0.6)

print("피해량은" + str(피해량) + "입니다.")
