import pyotp
totp = pyotp.TOTP("OAIFU5BHA7OS7EDMIZARTK233QTFCRCS") #Don't make it public like this
print("Current OTP:", totp.now())