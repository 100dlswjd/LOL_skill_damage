스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
#공격력 = float(input("공격력을 입력해주세요 : "))
#추가공격력 = int(input("추가공격력을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
#상대의최대체력 = int(input("상대의최대 체력을 입력해주세요 : "))
#상대가잃은체력 = int(input("상대가잃은 체력을 입력해주세요 : "))
#자신의최대체력 = int(input("자신의최대체력을 입력해주세요 : "))
#자신의현재체력 = int(input("자신의현재체력을 입력해주세요 : "))

기본피해량 = 스킬레벨 * 40
피해량 = (기본피해량 + (주문력 * 0.1)) * 15
추가체력 = 100 + (스킬레벨 * 150)

print("피해량 " + str(피해량) + " 입니다.")
print("추가체력 " + str(추가체력) + " 입니다.")
