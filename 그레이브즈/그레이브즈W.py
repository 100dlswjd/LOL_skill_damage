스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))

피해량 = 10 + (스킬레벨 * 50) + (주문력 * 0.6)

print("피해량은 : " + str(피해량) + " 입니다." )
