스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
공격력 = int(input("공격력을 입력해주세요 : "))

피해량 = 5 + (스킬레벨 * 40) + (공격력 * 1.15)

print("피해량은 " + str(피해량) + "입니다. " )
