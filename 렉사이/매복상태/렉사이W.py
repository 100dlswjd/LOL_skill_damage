스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
#공격력 = int(input("공격력을 입력해주세요 : "))
추가공격력 = int(input("추가공격력을 입력해주세요 : "))
#주문력 = int(input("주문력을 입력해주세요 : "))
#상대의최대체력 = int(input("상대의최대 체력을 입력해주세요 : "))
#상대가잃은체력 = int(input("상대가잃은 체력을 입력해주세요 : "))
#자신의최대체력 = int(input("자신의최대체력을 입력해주세요 : "))
#자신의현재체력 = int(input("자신의현재체력을 입력해주세요 : "))

기본피해량 = 40 + (스킬레벨 * 15)
피해량 = 기본피해량 + (추가공격력 * 0.8)

print("피해량은 " + str(피해량) + " 입니다.")
