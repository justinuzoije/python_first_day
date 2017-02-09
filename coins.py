coins = 0

while True:
    print "You have %s coins" % coins
    wantCoins = raw_input("Do you want another? (yes or no): ")
    if wantCoins == "no":
        print "Bye"
        break
        
    coins = coins + 1
    


#coins = 0
#print "You have %s coins" % coins
#userResponse = 'no'
#userResponse = raw_input("Do you want another? (yes or no): ")
#
#if userResponse == "yes":
#    while (userResponse == "yes"):
#        coins = coins + 1
#        print "You have %s coins" % coins
#        userResponse = raw_input("Do you want another? (y or no): ")
