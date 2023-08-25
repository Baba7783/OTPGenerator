import random

def generate_otp(length=6):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

if __name__ == "__main__":
    otp_length = 6  # You can change the length of the OTP as per your requirement
    otp = generate_otp(otp_length)
    print(f"Your OTP is: {otp}")
