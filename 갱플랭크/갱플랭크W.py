스킬레벨 = int(input("스킬 레벨을 입력해주세요 : "))
주문력 = int(input("주문력을 입력해주세요 : "))
잃은체력 = int(input("잃은체력을 입력해주세요 : "))

회복량 = 25 + (스킬레벨 * 25) + (주문력 * 0.9) + (잃은체력 * 0.15)

print("회복량은 " + str(회복량) + " 입니다.")

