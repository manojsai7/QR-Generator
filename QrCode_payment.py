import qrcode
import random,time
'''
purpose?
To generate Secrets using qr, instead of displaying regular texts to everyone publicly aka TEXT TO QR
also:
to make upi payments.
UPI payments in two ways:
1. direct payment to your upi id using any upi app's id (ex: karthik@ybl ,(or), Anuj@okaxis ) 
2. Using Upi limit:
 it is useful when you need exact amount you want to receive (especially used to skip bargaining? 😂)
 So Lets dive in!
NB: This Project was made considering only indian UPI usage, so default currency is INR only
 '''
wishes = [
    "Hey, stranger 👀",  "Long time no see, mate!","Well hello there 😏","Sup??", "Yo, looking fresh today 💅",
    "Ready to make someone's day?","Hey baddie 😉", "Feeling lucky? 🤑", "Welcome back, Rockstar 🤘",
    "Hey hey hey! Let's roll 🎉"]
i=1
print("WelCome to Qr generator! ",random.choice(wishes))
time.sleep(1)
while True:
    purpose=int(input("\n Whats The Purpose? \n 1.Qr Secrets [Text to QR]\n2.Upi payment Qr Generator? \n\n"))
    time.sleep(0.7)
    print("Press 'x' to Exit the Menu \n")
    if purpose==1:
        qr_txt=input("Hey !, enter secret (TEXT) \n")
        qr=qrcode.make(qr_txt)
        #print(qr)
        qr.show()
        ask=input("Want to Download Qr? (y/n)")
        if ask=="y":
            qr.save(f'Secret_Text_{i}.png')
            i+=1
    elif purpose==2:
        upi_id=input("Enter upi id: \n")
        ask=input("Want to generate custom amount limit QR? (y/n) \n")
        if ask=="y":
            limit=int(input("Enter Amount limit in rs (ex: 93.00) \n"))
            upi_url_1 = f'upi://pay?pa={upi_id}&pn=Your Name&am={limit}&cu=INR&tn=tn=Thanks%20for%20Using%20me%20%E2%9D%A4'
            upi_qr=qrcode.make(upi_url_1)
            upi_qr.show()
            ask=input("Want to Download Qr? (y/n)")
            if ask=="y":
                upi_qr.save(f'upi_qr_{i}.png')
                i+=1  
        else:
            upi_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&tn=Thanks%20for%20Using%20me%20%E2%9D%A4&cu=INR"
            upi_qr=qrcode.make(upi_url)
            upi_qr.show()
            ask=input("Want to Download Qr? (y/n)")
            if ask=="y":
                upi_qr.save(f'upi_qr_{i}.png')
                i+=1   
    if (str(purpose)=='x'):
        break;
print("Happy Scannning!")
