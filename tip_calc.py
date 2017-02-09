bill = float(raw_input("Total bill amount?: "))
service = raw_input("Level of service? (good, fair, or bad): ")
tip = 0.00

if service == "good":
    tip = bill * 0.20
elif service == "fair":
    tip = bill * .15
elif service == "bad":
    tip = bill * .10

total = bill + tip

print "Tip amount: $%.2f"  % tip
print "Total amount: $%.2f" % total
