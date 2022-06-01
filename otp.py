import pyotp
def generate(token):
    totp = pyotp.TOTP(token) #Don't make it public like this
    otpp = totp.now()
    print("Current OTP:", otpp)
    return otpp 
