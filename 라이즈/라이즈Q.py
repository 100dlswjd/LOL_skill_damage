스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
#공격력 = int(input("공격력을 입력해주세요 : "))
추가마나 = int(input("추가마나를 입력해주세요 : "))
궁극기레벨 = int(input("궁극기 레벨을 입력해주세요 : "))
#추가공격력 = int(input("추가공격력을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
#상대의최대체력 = int(input("상대의최대 체력을 입력해주세요 : "))
#상대가잃은체력 = int(input("상대가잃은 체력을 입력해주세요 : "))
#자신의최대체력 = int(input("자신의최대체력을 입력해주세요 : "))
#자신의현재체력 = int(input("자신의현재체력을 입력해주세요 : "))

기본피해량 = 50 + (스킬레벨 * 25)
피해량 = 기본피해량 + (주문력 * 0.4) + (추가마나 * 0.03)
과부하_퍼센트 = -0.2 + (스킬레벨 * 0.3)
과부하피해량 = 피해량 + (피해량 * 과부하_퍼센트)
이동속도증가량 = 24 + (스킬레벨 * 4)

print("피해량은 " + str(피해량) + " 입니다.")
print("과부하피해량은 " + str(과부하피해량) + " 입니다.")
print("이동속도증가량은 " + str(이동속도증가량) + " 입니다.")
