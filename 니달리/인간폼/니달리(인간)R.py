스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
#공격력 = int(input("공격력을 입력해주세요 : "))
#추가공격력 = int(input("추가공격력을 입력해주세요 : "))
#주문력 = int(input("주문력을 입력해주세요 : "))
#최대체력 = int(input("최대 체력을 입력해주세요 : "))
#자신의최대체력 = int(input("자신의최대체력을 입력해주세요 : "))
#자신의현재체력 = int(input("자신의현재체력을 입력해주세요 : "))

Q증가량 = -20 + (스킬레벨 * 25)
Q추가피해량 = 0.75 + (스킬레벨 * 0.25)
W피해량 = 10 + (스킬레벨 * 50)
E피해량 = 20 + (스킬레벨 * 60)

print("Q증가량은 " + str(Q증가량) + "입니다.")
print("Q추가피해량은 " + str(Q추가피해량) + "입니다")
print("W피해량은 " + str(W피해량) + "입니다")
print("E피해량은 " + str(E피해량) + "입니다")
