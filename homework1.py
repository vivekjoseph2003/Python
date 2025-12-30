import random
rice=45
sugar=40
oil=130
tot_a=float(3*rice)
tot_b=2.5*sugar
tot_c=1.8*oil
print("Rice total =",tot_a)
print("Sugar total =",tot_b)
print("Oil total =",tot_c)
final_tot=tot_a+tot_b+tot_c
print("total bill as integer=",int(final_tot))
print("total bill as string=",str(final_tot))
del_charge=random.randint(5,10)
final_bill=final_tot+del_charge
print("Final Bill=",final_bill)