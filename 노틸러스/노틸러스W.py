스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
#공격력 = int(input("공격력을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
자신의최대체력 = int(input("자신의 최대 체력을 입력해주세요 : "))

기본보호막 = 35 + (스킬레벨 * 10)
보호막 = 기본보호막 + (자신의최대체력 * ((8 + 스킬레벨) * 0.01))
기본피해량 = 20 + (스킬레벨 * 10)
피해량 = 기본피해량 + (주문력 * 0.4)

print("피해량은 " + str(피해량) + "입니다.")
print("보호막은 " + str(보호막) + "입니다.")
