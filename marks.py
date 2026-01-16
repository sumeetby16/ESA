import sys

if len(sys.argv) > 3:
    script_name = sys.argv[0]
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
else:
    script_name = sys.argv[0]
    n1=90
    n2=92
    n3=94

avg = (n1 + n2 + n3) / 3 

if avg >= 90:
    print(f"Average marks is : {avg}  S grade")
elif 75 <= avg < 90:
    print(f"Average marks is : {avg}  A grade")
elif 60 <= avg < 75:
    print(f"Average marks is : {avg}  B grade")
elif 45 <= avg < 60:
    print(f"Average marks is : {avg}  C grade")
elif 30 <= avg < 45:
    print(f"Average marks is : {avg}  D grade")
else:
    print(f"Average marks is : {avg}  Fail")