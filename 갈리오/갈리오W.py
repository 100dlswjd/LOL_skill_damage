스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
최대체력 = int(input("최대체력을 입력해주세요 : "))
추가방어력 = int(input("추가 방어력을 입력해주세요 : "))

최대데미지 = 15 + (스킬레벨 * 45)
기본지속효과마법보호막 = 최대체력 * 0.08
충전시작시마법피해감소량 = 20 + (주문력 * 0.0005) + (추가방어력 * 0.0008)
충전시작시물리피해감소량 = 10 + (주문력 * 0.0025) + (추가방어력 * 0.0004)

print("최대 데미지는 " + str(최대데미지) + " 입니다.")
print("기본지속효과의 보호막량은 " + str(기본지속효과마법보호막) +" 입니다.")
print("충전시작시 마법피해 감소량은 " + str(충전시작시마법피해감소량) + " 입니다.")
print("충전시작시 물리피해 감소량은 " + str(충전시작시물리피해감소량) + " 입니다.")
