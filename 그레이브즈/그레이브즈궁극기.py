스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
추가공격력 = int(input("추가공격력을 입력해주세요 : "))

처음피해량 = 100 + (스킬레벨 * 150) + (추가공격력 * 1.5)
폭발피해량 =  100 + (스킬레벨 * 120) + (추가공격력 * 1.2)

print("처음피해량은 : " + str(처음피해량) + " 입니다." )
print("폭발피해량은 : " + str(폭발피해량) + " 입니다." )

