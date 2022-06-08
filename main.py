# Now You Know Luhn
#
# You found receipt form Credit Card Transaction.
#
# Card Number: 543210******1234
#
# You need to find the whole Credit Card Number.
#
# 1) Card Number must be valid by the Luhn digit check algorithm
# 2) Card Number must be multiple of 123457.
#
# Tips: Flag format: "flag{16digit_card_number}"

number = "543210******1234";
numberPre = "543210";
numberMid = "000000";
numberPost = "1234";
num = "";
for i in range(1,1000000):
    if(i<10):
        num = "00000"+ str(i)
    elif (i < 100):
        num = "0000" +str(i)
    elif (i < 1000):
        num = "000" + str(i)
    elif (i < 10000):
        num = "00" + str(i)
    elif (i < 100000):
        num = "0" + str(i)
    elif (i < 1000000):
        num = str(i)
    card = numberPre + num + numberPost
    #print(card)
    if int(card) % 123457 == 0:
        print(card)

    #print(num)
