#PESO DENOMINATOR
# MONEY = 3573
# 1000, 500, 200, 100, 50, 20, 10, 5, 1

#what operator / symbol did you use to solve the problem ?
# floor division, % modulus

money = 3573

libo = money // 1000 #3.6 --> 3
libo_sukli = money % 1000 # 573
#libo_sukli = (libo * 1000)

payb_h = libo_sukli // 500
payb_sukli = libo_sukli % 500 # 73

two_h = payb_sukli // 200
two_sukli = payb_sukli % 200

wan_h = two_sukli // 100
wan_sukli = two_sukli % 100

pipti = wan_sukli // 50
pipti_sukli = wan_sukli % 50

bente = pipti_sukli // 20
bente_sukli = pipti_sukli % 20

sampo = bente_sukli // 10
sampo_sukli = bente_sukli % 10

payb = sampo_sukli // 5
payb_sukli = sampo_sukli % 5

piso = payb_sukli // 1
piso_sukli = payb_sukli % 1

print("1000 - ", libo)
print("500 - ", payb_h)
print("200 - ", two_h)
print("100 -", wan_h)
print("50 -", pipti)
print("20 -", bente)
print("10 -", sampo)
print("5 -", payb)
print("1 -", piso)