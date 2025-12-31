header="""BOOKSTORE
 RECEIPT"""
item1="\n\tBOOK:{}\n\tPRICE:Rs{}".format("Python Basics",450)
item2="\n\tBOOK:{}\n\tPRICE:Rs{}".format("Data Science Intro",600)
total_price=450+600
total_line="\n\tTOTAL AMOUNT:\t₹{}".format(total_price)
thank_you="\n\tTHANK YOU FOR SHOPPING WITH US!"
receipt=(header+"\n"+item1+"\n"+item2+"\n"+total_line+"\n"+thank_you)
print(receipt.upper())