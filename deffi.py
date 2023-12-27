q=int(input("enter prime number"))
alpha=int(input("enter primitive root"))
Xa=int(input("alice secret key"))
Xb=int(input("bob secret key"))

#alice count there private key using alpha
Ya=pow(alpha,Xa,q)
print("Ya is ",Ya)
#bob count there private key using alpha
Yb=pow(alpha,Xb,q)
print("Yb is ",Yb)


#they share each othere private keys Xa and Xb
#now they count there keys 

#alice key
Key1=pow(Yb,Xa,q)
print("Key1 is ",Key1)

#alice key
Key2=pow(Ya,Xb,q)
print("Key2 is ",Key2)


#if both K1 and K2 are same then Diffi-Hellman is successfull

if Key1==Key2:
    print("key successfully tranfer")
else:
    print("key mismatch")    

    