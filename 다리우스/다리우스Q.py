스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
공격력 = int(input("공격력을 입력해주세요 : "))
#추가공격력 = int(input("추가공격력을 입력해주세요 : "))
#주문력 = int(input("주문력을 입력해주세요 : "))
#상대의최대체력 = int(input("상대의최대 체력을 입력해주세요 : "))
#상대가잃은체력 = int(input("상대가잃은 체력을 입력해주세요 : "))
자신의최대체력 = int(input("자신의최대체력을 입력해주세요 : "))
자신의현재체력 = int(input("자신의현재체력을 입력해주세요 : "))
도끼날에맞은적 = int(input("도끼날에 맞은 상대를 입력해주세요 : "))

if(도끼날에맞은적 > 3):
    도끼날에맞은적 = 3

자신이잃은체력 = 자신의최대체력 - 자신의현재체력

기본피해량 = 20 + (스킬레벨 * 30)
총공격력_퍼센트 = 0.9 + (스킬레벨 * 0.1)
회복량 = 자신이잃은체력 * (도끼날에맞은적 * 0.15)

피해량 = 기본피해량 + (공격력 * 총공격력_퍼센트)

print("피해량은 " + str(피해량) + "입니다.")
print("회복량은 " + str(회복량) + "입니다.")
