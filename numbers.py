#6xxx xxxx - Public Switched Telephone Network (PSTN) and Residential IP Telephony Services

#8zxx xxxx - Mobile, Data Services, New Numbers and Prepaid Numbers

#9yxx xxxx - Mobile, Data Services and Pager (until May 2012)

#x denotes 0 to 9
#y denotes 0 to 8 only
#z denotes 1 to 9 only

with open("six.txt", "w") as f:
        for i in range(6000000,6999999):
                number = str(i)
                f.write(number)
                f.write("\n")




with open("eight.txt", "w") as f:
        for i in range(81000000,89999999):
                number = str(i)
                f.write(number)
                f.write("\n")

with open("nine.txt", "w") as f:
        for i in range(90000000,98999999):
                number = str(i)
                f.write(number)
                f.write("\n")


