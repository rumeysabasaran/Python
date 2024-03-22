
#Girilen sayının asal olup olmadığını söyleyen kod
n=int(input("Bir sayi giriniz\n"))
asal=1
if(n==0 or n==1):
    print("Girdiğiniz sayi asal sayi değildir")
elif(n==2):
    print("Girdiğiniz sayi asal sayidir")
elif(n%2==0):
    print("Girdiğiniz sayi asal değildir")
else:
    i=3
    while(i*i<=n):
        if(n%i==0):
            asal=0
        i=i+2
    if(asal==0):
        print("Girdiğiniz sayi asal değildir")
    else:
        print("Girdiğiniz sayi asaldir")




