import pyotp
totp = pyotp.TOTP("N4HF6H5YKGSQIUCVACFHWDC2Y5OWCE5M") #Don't make it public like this
print("Current OTP:", totp.now())