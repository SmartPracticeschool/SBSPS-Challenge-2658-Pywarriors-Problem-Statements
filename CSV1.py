# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:09:59 2020

@author: Praveen
"""

def bill_count(Usermoney,Billsavailable):     
    if(Usermoney>1):
        a=Usermoney/max(Billsavailable)
        b=(Usermoney%max(Billsavailable))/Billsavailable[-2]
        c=((Usermoney%max(Billsavailable))%Billsavailable[-2])/Billsavailable[-3]
        d=(((Usermoney%max(Billsavailable))%Billsavailable[-2])%Billsavailable[-3])/Billsavailable[-4]
        e=((((Usermoney%max(Billsavailable))%Billsavailable[-2])%Billsavailable[-3])%Billsavailable[-4])/Billsavailable[-5]
        f=(((((Usermoney%max(Billsavailable))%Billsavailable[-2])%Billsavailable[-3])%Billsavailable[-4])%Billsavailable[-5])/Billsavailable[-6]
        g=((((((Usermoney%max(Billsavailable))%Billsavailable[-2])%Billsavailable[-3])%Billsavailable[-4])%Billsavailable[-5])%Billsavailable[-6])/Billsavailable[-7]
        h=(((((((Usermoney%max(Billsavailable))%Billsavailable[-2])%Billsavailable[-3])%Billsavailable[-4])%Billsavailable[-5])%Billsavailable[-6])%Billsavailable[-7])/Billsavailable[-8]
        i=((((((((Usermoney%max(Billsavailable))%Billsavailable[-2])%Billsavailable[-3])%Billsavailable[-4])%Billsavailable[-5])%Billsavailable[-6])%Billsavailable[-7])%Billsavailable[-8])/Billsavailable[-9]
        print('Number of notes in RS 2000:',int(a))
        print('Number of notes in RS 500:',int(b))
        print('Number of notes in RS 200:',int(c))
        print('Number of notes in RS 100:',int(d))
        print('Number of notes in RS 50:',int(e))
        print('Number of notes in RS 20:',int(f))
        print('Number of notes in RS 10:',int(g))
        print('Number of notes in RS 5:',int(h))
        print('Number of notes in RS 1:',int(i))
    else:
        print('Input error, Please enter the value above RS 1.')

    return;
bill_count(Usermoney=int(input("Enter the amount of money the user has:")), Billsavailable=[1,5,10,20,50,100,200,500,2000])      
   
    
    
    