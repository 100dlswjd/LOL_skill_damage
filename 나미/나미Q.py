스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
# 공격력 = int(input("공격력을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
# 최대체력 = int(input("최대 체력을 입력해주세요 : "))

기본공격력 = 20+(스킬레벨 * 55)
스킬데미지 = 기본공격력+(주문력 * 0.5)

print("나미 Q스킬 데미지는 " + str(스킬데미지) + "입니다.")
