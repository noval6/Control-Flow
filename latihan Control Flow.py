jarak=int(input("Input Jarak :"))
if jarak <=5:
    total = jarak * 1000
    print("total yang harus dibayar : ",total)
elif jarak <=10:
    total = jarak * 900
    print("total yang harus dibayar : ",total)
else:
    total = jarak * 800
    print("total yang harus dibayar : ",total)