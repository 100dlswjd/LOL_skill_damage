스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
#공격력 = int(input("공격력을 입력해주세요 : "))
#추가공격력 = int(input("추가공격력을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
#최대체력 = int(input("최대 체력을 입력해주세요 : "))
#자신의최대체력 = int(input("자신의최대체력을 입력해주세요 : "))
#자신의현재체력 = int(input("자신의현재체력을 입력해주세요 : "))

기본회복량 = 15 + (스킬레벨 * 20)
회복량 = 기본회복량 + (주문력 * 0.325)

print("회복량은 " + str(회복량) + "입니다.")
