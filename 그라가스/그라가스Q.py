스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))

최소피해량 = 40 + (스킬레벨 * 40) + (주문력 *0.7)
최대피해량 = 최소피해량*1.5

print("최소피해량은 : " + str(최소피해량) +  " 입니다." )
print("최대피해량은 : " + str(최대피해량) +  " 입니다." )
