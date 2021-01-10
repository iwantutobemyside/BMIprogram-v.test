weight = int(input("Enter ur weight(kg): "))
height = int(input("Enter ur height(cm): ")) / 100 #cm -> m.
BMI = (weight/(height ** 2))
print("BMI = %.2f" %(BMI))

if BMI < 18.50:
    print("คุณอยู่ในเกณฑ์น้ำหนักน้อยหรือผอม")
elif BMI >= 18.50 and BMI <= 22.90:
    print("คุณอยู่ในเกณฑ์ปกติ")
elif BMI >= 23.00 and BMI <= 24.90:
    print("คุณอยู่ในเกณฑ์ที่น้ำหนักเกิน")
elif BMI >= 25.00 and BMI <= 29.90:
    print("คุณอยู่ในเกณฑ์โรคอ้วนระดับที่ 1")
else:
    print("คุณอยู่ในเกณฑ์โรคอ้วนระดับที่ 2")




