
# Q2 - OTP Verification using for loop

correct_otp = "1234"

for i in range(3):
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry. Try again.")
        continue

    if otp == correct_otp:
        print("OTP verified successfully")
        break
    else:
        print("Wrong OTP")

else:
    print("Account locked for 30 minutes")
