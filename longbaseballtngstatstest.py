import random
import time
from source import*
from test import*
from tabulate import tabulate
import pandas as pd
import os
cwd = os.getcwd()
print(cwd)
out=0
hometeamruns = 0
awayteamruns = 0
Safe = ("")
Team = ("")
def atbat():
    global out, atbats, walks, Ks, walksallowed, so
    from source import ba
    from source import pa
    #pa = input ("pitcher's accuracy?")
    #ba = input ("batter's accuracy?")
    bp = 33
    ps = 26
    #so = ("Strike Out")
    #nso = ("Not a Strike Out")
    result1 = int(ba) - int(pa)
    result2 = int(pa) - int(ba)
    die1 = random.randrange(1,7)
    die1ba = random.randrange(1,7)
    die2 = random.randrange(1,13)
    die2ba = random.randrange(1,13)
    pareach = die1 + int(pa)
    pareach2 = die2 + int(pa)
    bareach = die1ba + int(ba)
    bareach2 = die2ba + int(ba)
    if (int(ba)>int(pa)):
        if (result1>=12):
            if (die2==12):
                print ("Strike out")
                atbats += 1
                out += 1
                Ks += 1
                so += 1
            if (die2!=12):
                print("not strike out")
                atbats += 1
                caught()
        if (result1<12):
            if (result1==6):
                if (pareach!=int(ba)):
                    print("not strike out")
                    atbats += 1
                    caught()
                if (pareach==int(ba)):
                    print("strike out")
                    atbats += 1
                    out += 1
                    Ks += 1
                    so +=1 
            if (result1>6):
                if (pareach2==int(ba)):
                    print ("walk")
                    walks += 1
                    walksallowed += 1
                    walk()
                if (pareach2<int(ba)):
                    print ("not strike out")
                    atbats += 1
                    caught()
                if (pareach2>int(ba)):
                    print ("strike out")
                    atbats += 1
                    out += 1
                    Ks += 1
                    so += 1
            if (result1<6):
                if (result1>=4):
                    if (pareach==int(ba)):
                        print ("walk")
                        walks += 1
                        walksallowed += 1
                        walk()
                    if (pareach<int(ba)):
                        print("not strike out")
                        atbats += 1
                        caught()
                    if (pareach>int(ba)):
                        print("strike out")
                        atbats += 1
                        out += 1
                        Ks += 1
                        so += 1
                if (result1<4):
                    if (pareach==bareach):
                        print ("walk")
                        walks += 1
                        walksallowed += 1
                        walk()
                    if (pareach>bareach):
                        print ("strike out")
                        atbats += 1
                        out += 1
                        Ks += 1
                        so += 1
                    if (pareach<bareach):
                        print ("not strike out")
                        atbats += 1
                        caught()
    if (int(ba)<int(pa)):
        if (result2>=12):
            if (die2==12):
                print ("not strike out")
                atbats += 1
                caught()
            if (die2!=12):
                print ("strike out")
                atbats += 1
                out += 1
                Ks += 1
                so += 1
        if (result2<12):
            if (result2==6):
                if (bareach2==6):
                    print("not strike out")
                    atbats += 1
                    caught()
                if (bareach!=6):
                    print("strike out")
                    atbats += 1
                    out += 1
                    Ks += 1
                    so += 1
            if (result2>6):
                if (bareach2<int(pa)):
                    print ("strike out")
                    atbats += 1
                    out += 1
                    Ks += 1
                    so += 1
                if (bareach2>int(pa)):
                    print ("not strike out")
                    atbats += 1
                    caught()
                if (bareach2==int(pa)):
                    print ("walk")
                    walks += 1
                    walksallowed += 1
                    walk()
            if (result2<6):
                if (result2>=4):
                    if (bareach==int(pa)):
                        print("walk")
                        walks += 1
                        walksallowed += 1
                        walk()
                    if (bareach<int(pa)):
                        print("strike out")
                        atbats += 1
                        out += 1
                        Ks += 1
                        so += 1
                    if (bareach>int(pa)):
                        print("not strike out")
                        atbats += 1
                        caught()
                if (result2<4):
                    if (bareach==pareach):
                        print ("walk")
                        walks += 1
                        walksallowed += 1
                        walk()
                    if (bareach>pareach):
                        print ("not strike out")
                        atbats += 1
                        caught()
                    if (bareach<pareach):
                        print ("strike out")
                        atbats += 1
                        out += 1
                        Ks += 1
                        so += 1
    if (int(pa)==int(ba)):
        if (pareach<bareach):
            print ("not strike out")
            atbats += 1
            caught()
        if (pareach>bareach):
            print ("strike out")
            atbats += 1
            out += 1
            Ks += 1
            so += 1
        if (pareach==bareach):
            print ("walk")
            walks += 1
            walksallowed += 1
            walk()
            
    print ("outs:",out)
    #if (out==3):
        #out = 0
        #import awaylineup
def caught():
    time.sleep(5)
    from source import bp
    from source import ps
    #bp = input ("batter's power?")
    #ps = input ("pitcher's stuff?")
    result3 = int(bp) - int(ps)
    result4 = int(ps) - int(bp)
    die3 = random.randrange(1,7)
    die3bp = random.randrange(1,7)
    die4 = random.randrange(1,13)
    die4bp = random.randrange(1,13)
    psreach = die3 + int(ps)
    psreach2 = die4 + int(ps)
    bpreach = die3bp + int(bp)
    bpreach2 = die4bp + int(bp)
    minordie = random.randrange(1,7)
    hitdie = random.randrange(1,7)
    fielddie = random.randrange (1,13)
    caughtdieL = random.randrange (1,3)
    caughtdieC = random.randrange (1,3)
    caughtdieR = random.randrange (1,3)
    if (int(bp)>int(ps)):
        if (result3>=12):
            if (die3==12):
                print ("minor")
                majorminor()
            if (die3!=12):
                print ("major")
                whereM()
        if (result3<12):
            if (result3==6):
                if (psreach2==6):
                    print("minor")
                    majorminor()
                if (psreach!=6):
                    print("major")
                    whereM()
            if (result3>6):
                if (psreach2<int(bp)):
                    print ("major")
                    whereM()
                if (psreach2>int(bp)):
                    print ("minor")
                    majorminor()
                if (psreach2==int(bp)):
                    print ("major")
                    whereM()
            if (result3<6):
                if (result3>=4):
                    if (psreach==int(bp)):
                        print("major")
                        whereM()
                    if (psreach<int(bp)):
                        print("major")
                        whereM()
                    if (psreach>int(bp)):
                        print("minor")
                        majorminor()
                if (result3<4):
                    if (psreach==psreach):
                        print ("major")
                        whereM()
                    if (psreach>psreach):
                        print ("minor")
                        majorminor()
                    if (psreach<psreach):
                        print ("major")
                        whereM()
    if (int(bp)<int(ps)):
        if (result4>=12):
            if (die4==12):
                print ("major")
                whereM()
            if (die4!=12):
                print ("minor")
                majorminor()
        if (result4<12):
            if (result4==6):
                if (bpreach2==6):
                    print("major")
                    whereM()
                if (bpreach!=6):
                    print("minor")
                    majorminor()
            if (result4>6):
                if (bpreach2<int(ps)):
                    print ("minor")
                    majorminor()
                if (bpreach2>int(ps)):
                    print ("major")
                    whereM()
                if (bpreach2==int(ps)):
                    print ("minor")
                    majorminor()
            if (result4<6):
                if (result4>=4):
                    if (bpreach==int(ps)):
                        print("minor")
                        majorminor()
                    if (bpreach<int(ps)):
                        print("minor")
                        majorminor()
                    if (bpreach>int(ps)):
                        print("major")
                        whereM()
                if (result4<4):
                    if (bpreach==psreach):
                        print ("minor")
                        majorminor()
                    if (bpreach>psreach):
                        print ("major")
                        whereM()
                    if (bpreach<psreach):
                        print ("minor")
                        majorminor()
    if (int(ps)==int(bp)):
        if (psreach<bpreach):
            print ("major")
            whereM()
        if (psreach>bpreach):
            print ("minor")
            majorminor()
        if (psreach==bpreach):
            print ("minor")
            majorminor()
def majorminor():
    time.sleep(5)
    diew = random.randrange(1,3)
    if (diew==1):
        print ("infield")
        whereI()
    else:
        print ("outfield")
        wherem()
def whereM():
    time.sleep(5)
    global diem
    diem = random.randrange(1,13)
    if (diem <=5):
        print ("Left Field")
        LF()
        catchM()
    if (diem == 6 or diem == 7 or diem == 8 or diem ==9):
        print ("Center Field")
        CF()
        catchM()
    if (diem >=10):
        print ("Right Field")
        RF()
        catchM()
def whereI():
    global singles, diei
    time.sleep(5)
    diei = random.randrange(1,4)
    if (diei==1):
        print ("Short Stop")
        SS()
        speed()
        infieldstats()
        if (Safe==("Safe!")):
            singles = 1
            single()
    if (diei ==2):
        print ("2nd Base")
        secondbase()
        speed()
        infieldstats()
        if (Safe==("Safe!")):
            singles = 1
            single()
    if (diei ==3):
        print ("3rd Base")
        thirdbase()
        speed()
        infieldstats()
        if (Safe==("Safe!")):
            singles = 1
            single()
def wherem():
    time.sleep(5)
    global diem
    diem = random.randrange(1,13)
    if (diem <=5):
        print ("Left Field")
        LF()
        catchm()
    if (diem == 6 or diem == 7 or diem == 8 or diem ==9):
        print ("Center Field")
        CF()
        catchm()
    if (diem >=10):
        print ("Right Field")
        RF()
        catchm()
def catchM():
    time.sleep(5)
    global out
    catchdie = random.randrange(1,3)
    if (catchdie==1):
        print ("Caught")
        out += 1
    else:
        print ("Not Caught")
        Major()
        #outfieldstats()
def catchm():
    time.sleep(5)
    global out
    catchdie = random.randrange(1,3)
    if (catchdie==1):
        print ("Caught")
        out += 1
    else:
        print ("Not Caught")
        Minor()
        #outfieldstats()
def speed(): 
    time.sleep(5)
    global out, hits, hitsallowed, fs
    #from source import fs
    from source import bs
    #fs = input ("fielder's speed?")
    #bs = input ("batter's speed?")
    die3 = random.randrange(1,7)
    die4 = random.randrange(1,13)
    result5 = int(fs) - int(bs)
    result6 = int(bs) - int(fs)
    die5 = random.randrange(1,7)
    die5fs = random.randrange(1,7)
    die6 = random.randrange(1,13)
    die6fs = random.randrange(1,13)
    bsreach = die3 + int(bs)
    bsreach2 = die4 + int(bs)
    fsreach = die5fs + int(fs)
    fsreach2 = die6fs + int(fs)
    global Safe
    if (int(fs)>int(bs)):
        if (result5>=12):
            if (die6==12):
                print ("Safe!")
                hits = 1
                hitsallowed += 1
                Safe = ("Safe!")
            if (die6!=12):
                print ("Out!")
                out += 1
        if (result5<12):
            if (result5==6):
                if (bsreach!=int(fs)):
                    print("Out!")
                    out += 1
                if (bsreach==int(fs)):
                    print("Safe!")
                    hits = 1
                    hitsallowed += 1
                    Safe = ("Safe!")
            if (result5>6):
                if (bsreach2==int(fs)):
                    print ("Safe!")
                    hits = 1
                    hitsallowed += 1
                    Safe = ("Safe!")
                if (bsreach2<int(fs)):
                    print ("Out!")
                    out += 1
                if (bsreach2>int(fs)):
                    print ("Safe!")
                    hits = 1
                    hitsallowed += 1
                    Safe = ("Safe!")
            if (result5<6):
                if (result5>=4):
                    if (bsreach==int(fs)):
                        print ("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
                    if (bsreach<int(fs)):
                        print("Out!")
                        out += 1
                    if (bsreach>int(fs)):
                        print("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
                if (result5<4):
                    if (bsreach==fsreach):
                        print ("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
                    if (bsreach>fsreach):
                        print ("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
                    if (bsreach<fsreach):
                        print ("Out!")
                        out += 1
    if (int(fs)<int(bs)):
        if (result6>=12):
            if (die6==12):
                print ("Out!")
                out += 1
            if (die6!=12):
                print ("Safe!")
                hits = 1
                hitsallowed += 1
                Safe = ("Safe!")
        if (result6<12):
            if (result6==6):
                if (fsreach==6):
                    print("Out!")
                    out += 1
                if (fsreach!=6):
                    print("Safe!")
                    hits = 1
                    hitsallowed += 1
                    Safe = ("Safe!")
            if (result6>6):
                if (fsreach2<int(bs)):
                    print ("Safe!")
                    hits = 1
                    hitsallowed += 1
                    Safe = ("Safe!")
                if (fsreach2>int(bs)):
                    print ("Out!")
                    out += 1
                if (fsreach2==int(bs)):
                    print ("Safe!")
                    hits = 1
                    hitsallowed += 1
                    Safe = ("Safe!")
            if (result6<6):
                if (result6>=4):
                    if (fsreach==int(bs)):
                        print("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
                    if (fsreach<int(bs)):
                        print("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
                    if (fsreach>int(bs)):
                        print("Out!")
                        out += 1
                if (result6<4):
                    if (fsreach==bsreach):
                        print ("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
                    if (fsreach>bsreach):
                        print ("not Safe!")
                        out += 1
                    if (fsreach<bsreach):
                        print ("Safe!")
                        hits = 1
                        hitsallowed += 1
                        Safe = ("Safe!")
    if (int(bs)==int(fs)):
        if (bsreach<fsreach):
            print ("Out!")
            out += 1
        if (bsreach>fsreach):
            print ("Safe!")
            Safe = ("Safe!")
            hits = 1
            hitsallowed += 1
        if (bsreach==fsreach):
            print ("Safe!")
            Safe = ("Safe!")
            hits = 1
            hitsallowed += 1
def Major():
    global hr, hits, Safe, singles, doubles, triples, hitsallowed, hrallowed
    time.sleep(5)
    majordie= random.randrange(1,7)
    confirmeddie= random.randrange(1,3)
    if (majordie==1):
        print ("single?")
        speed()
        outfieldstats()
        if Safe == "Safe!":
            singles = 1
            single()
    elif (majordie==2 or majordie==3):
        print ("double?")
        speed()
        outfieldstats()
        if Safe=="Safe!":
            doubles = 1
            double()
    elif (majordie==4):
        print ("triple?")
        speed()
        outfieldstats()
        if (Safe==("Safe!")):
            triples = 1
            triple()
    elif (majordie==5 or majordie==6):
        if (confirmeddie==2):
            print ("Homerun")
            hitsallowed += 1
            hits = 1
            hr += 1
            hrallowed += 1
            homerun()
        else:
            print ("unconfirmed HR, Double?")
            speed()
            outfieldstats()
            if (Safe==("Safe!")):
                doubles = 1
                double()
def Minor():
    global hr, hits, Safe, singles, doubles, triples, hitsallowed, hrallowed
    time.sleep(5)
    minordie = random.randrange(1,7)
    confirmeddie = random.randrange(1,3)
    if (minordie==1 or minordie==2):
        print ("single?")
        speed()
        outfieldstats()
        if (Safe==("Safe!")):
            singles = 1
            single()
    elif (minordie==3 or minordie==4):
        print ("double?")
        speed()
        outfieldstats()
        if (Safe==("Safe!")):
            doubles = 1
            double()
    elif (minordie==5):
        print ("triple?")
        speed()
        outfieldstats()
        if (Safe==("Safe!")):
            triples = 1
            triple()
    elif (minordie==6):
        if (confirmeddie==2):
            print ("Homerun")
            hitsallowed += 1
            hits = 1
            hr += 1
            hrallowed += 1
            homerun()
        else:
            print ("unconfirmed HR, Double?")
            speed()
            outfieldstats()
            if (Safe==("Safe!")):
                doubles = 1
                double()

#this is where it transfers from the mechanics of the game to the actual baseball game
current_batter = 1
def lineup():
    awaypitcher()
    global out, current_batter, Htable, Safe, Team
    Team = ("Away")
    for i in range(100):
        if (current_batter==1):
            batter1()
            print (batter1name,"",batter1hits,"-",batter1atbats)
            atbat()
            batter1stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==2):
            batter2()
            print (batter2name,"",batter2hits,"-",batter2atbats)
            atbat()
            batter2stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==3):
            batter3()
            print (batter3name,"",batter3hits,"-",batter3atbats)
            atbat()
            batter3stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==4):
            batter4()
            print (batter4name,"",batter4hits,"-",batter4atbats)
            atbat()
            batter4stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==5):
            batter5()
            print (batter5name,"",batter5hits,"-",batter5atbats)
            atbat()
            batter5stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==6):
            batter6()
            print (batter6name,"",batter6hits,"-",batter6atbats)
            atbat()
            batter6stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==7):
            batter7()
            print (batter7name,"",batter7hits,"-",batter7atbats)
            atbat()
            batter7stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==8):
            batter8()
            print (batter8name,"",batter8hits,"-",batter8atbats)
            atbat()
            batter8stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outs()
            time.sleep(5)
        elif (current_batter==9):
            batter9()
            print (batter9name,"",batter9hits,"-",batter9atbats)
            atbat()
            batter9stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter = 1
            walkoff()
            outs()
            time.sleep(5)
current_batter2 = 1
def lineup2():
    homepitcher()
    global current_batter2, Atable, Safe, Team
    Team = ("Home")
    for i in range(100):
        if (current_batter2==1):
            batter10()
            print (batter10name,"",batter10hits,"-",batter10atbats)
            atbat()
            batter10stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==2):
            batter11()
            print (batter11name,"",batter11hits,"-",batter11atbats)
            atbat()
            batter11stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==3):
            batter12()
            print (batter12name,"",batter12hits,"-",batter12atbats)
            atbat()
            batter12stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==4):
            batter13()
            print (batter13name,"",batter13hits,"-",batter13atbats)
            atbat()
            batter13stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==5):
            batter14()
            print (batter14name,"",batter14hits,"-",batter14atbats)
            atbat()
            batter14stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==6):
            batter15()
            print (batter15name,"",batter15hits,"-",batter15atbats)
            atbat()
            batter15stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==7):
            batter16()
            print (batter16name,"",batter16hits,"-",batter16atbats)
            atbat()
            batter16stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==8):
            batter17()
            print (batter17name,"",batter17hits,"-",batter17atbats)
            atbat()
            batter17stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2()
            time.sleep(5)
        if (current_batter2==9):
            batter18()
            print (batter18name,"",batter18hits,"-",batter18atbats)
            atbat()
            batter18stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 = 1
            outs2()
            time.sleep(5)
innings = 1
def inning():
    global innings, homepa, homeps, awaypa, awayps, Htable, Atable, Hpitcher, Apitcher, homestarterposition, awaystarterposition, homereliefposition1, homereliefposition2,awayreliefposition1, awayreliefposition2
    if (innings==1):
        print ("top of the first")
        print ("")
        time.sleep(5)
        lineup2()
    elif (innings==1.5):
        print ("bottom of the first")
        print ("")
        time.sleep(5)
        lineup()
    elif (innings==2):
        print ("top of the second")
        print ("")
        time.sleep(5)
        lineup2()
    elif (innings==2.5):
        print ("bottom of the second")
        print ("")
        time.sleep(5)
        lineup()
    elif (innings==3):
        print ("top of the third")
        print ("")
        time.sleep(5)
        lineup2()
    elif (innings==3.5):
        print ("bottom of the third")
        print ("")
        time.sleep(5)
        lineup()
    elif (innings==4):
        print ("top of the fourth")
        print ("")
        time.sleep(5)
        lineup2()
    elif (innings==4.5):
        print ("bottom of the fourth")
        print ("")
        time.sleep(5)
        lineup()
    elif (innings==5):
        print ("top of the fifth")
        print ("")
        time.sleep(5)
        lineup2()
    elif (innings==5.5):
        print ("bottom of the fifth")
        print ("")
        time.sleep(5)
        lineup()
    elif (innings==6):
        print ("top of the sixth")
        print ("")
        time.sleep(5)
        homepitcherrequest()
        homereliefposition1 = input("Home pitcher position?")
        lineup2()
    elif (innings==6.5):
        print ("bottom of the sixth")
        print ("")
        time.sleep(5)
        awaypitcherrequest()
        awayreliefposition1 = input("Away pitcher position?")
        lineup()
    elif (innings==7):
        print ("top of the seventh")
        print ("")
        time.sleep(5)
        lineup2()
    elif (innings==7.5):
        print ("bottom of the seventh")
        print ("")
        time.sleep(5)
        lineup()
    elif (innings==8):
        print ("top of the eighth")
        print ("")
        time.sleep(5)
        homepitcherrequest()
        homereliefposition2 = input("Home pitcher position?")
        lineup2()
    elif (innings==8.5):
        print ("bottom of the eighth")
        print ("")
        time.sleep(5)
        awaypitcherrequest()
        awayreliefposition2 = input("Away pitcher position?")
        lineup()
    elif (innings==9):
        print ("top of the ninth")
        print ("")
        time.sleep(5)
        lineup2()
    elif hometeamruns>awayteamruns:
        print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
        Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
        Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
        Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks]]
        Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks]]
        Boxscore = input("Boxscore?")
        if (Boxscore=="n"):
            print (awaycenteropps)
            print (awaycenterthrowouts)
            print ("")
            print (away2Bopps)
            print (away2Bthrowouts)
            test()
            test2()
            exit()
        else:
            print (" ")
            print ("Home team:")
            print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
            print (" ")
            print (" ")
            print ("Home team:")
            print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
            print (" ")
            print (" ")
            print ("Away team:")
            print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
            print (" ")
            print (" ")
            print ("Away team:")
            print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
            test()
            test2()
            exit()
        exit()
    elif (innings==9.5):
        print ("bottom of the ninth")
        print ("")

        lineup()
    elif (innings==10):
        if hometeamruns==awayteamruns:
            extrainning()
        print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
        Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
        Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
        Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks]]
        Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks]]
        Boxscore = input("Boxscore?")
        if (Boxscore=="n"):
            print (awaycenteropps)
            print (awaycenterthrowouts)
            print ("")
            print (away2Bopps)
            print (away2Bthrowouts)
            test()
            test2()
            exit()
        else:
            print (" ")
            print ("Home team:")
            print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
            print (" ")
            print (" ")
            print ("Home team:")
            print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
            print (" ")
            print (" ")
            print ("Away team:")
            print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
            print (" ")
            print (" ")
            print ("Away team:")
            print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
            test()
            test2()
            exit()
def outs():
    global out, on_base, innings, extrainnings, ip
    if (out==3):
        ip = 1
        home()
        awaystarterstats()
        awayreliefstats()
        awayrelief2stats()
        print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
        print ("")
        time.sleep(5)
        out = 0
        on_base = [-1, -1, -1, -1]
        innings += 0.5
        if innings>=10:
            if hometeamruns==awayteamruns:
                extrainnings = 10
                extrainning()
        inning()
def outs2():
    global out, on_base, innings, extrainnings, ip
    if (out==3):
        ip = 1
        away()
        homestarterstats()
        homereliefstats()
        homerelief2stats()
        print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
        print ("")
        time.sleep(5)
        out = 0
        on_base = [-1, -1, -1, -1]
        innings +=0.5
        if innings>=10:
            if hometeamruns==awayteamruns:
                extrainnings = 10
                extrainning()
        inning()
runs = 0
on_base = [-1, -1, -1, -1]
def walk():
    outs()
    outs2()
    global runs, runsallowed, rbi
    if (on_base[1] == -1 and on_base[2] == -1 and on_base[3] == -1):
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] == -1):
        on_base[2] = on_base[1]
        on_base[1] = 1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] == -1):
        on_base[1] = 1
    elif (on_base[1] == -1 and on_base[2] == -1 and on_base[3] > -1):
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] == -1):
        on_base[3] = on_base[2]
        on_base[2] = on_base[1]
        on_base[1] = 1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] > -1):
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] > -1):
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = on_base[2]
        on_base[2] = on_base[1]
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] > -1):
        on_base[2] = on_base[1]
        on_base[1] = 1
def single():
    outs()
    outs2()
    global hit, pos, runs, on_first, on_second, on_third, home, on_base, runsallowed, rbi
    if (on_base[1] == -1 and on_base[2] == -1 and on_base[3] == -1):
        #bases empty
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] == -1):
        #runner on first
        on_base[2] = on_base [1]
        on_base[1] = 1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] == -1):
        on_base[3] = on_base[2]
        on_base[2] = -1
        on_base[1] = 1
		# Runner on second
    elif (on_base[1] == -1 and on_base[2] == -1 and on_base[3] > -1):
        # Runner on third
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = -1
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] == -1):
        # Runners on first and second
        on_base[3] = on_base[2]
        on_base[2] = on_base[1]
        on_base[1] = 1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] > -1):
        # Runners on second and third
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = on_base[2]
        on_base[2] = -1
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] > -1):
        # bases loaded
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = on_base[2]
        on_base[2] = on_base[1]
        on_base[1] = 1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] > -1):
        # Runner on first and third
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = -1
        on_base[2] = on_base[1]
        on_base[1] = 1
def double():
    outs()
    outs2()
    global runs, runsallowed, rbi
    if (on_base[1] == -1 and on_base[2] == -1 and on_base[3] == -1):
        # Bases empty
        on_base[2] = 1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] == -1):
        # Runner on first
        on_base[3] = on_base[1]
        on_base[2] = 1
        on_base[1] = -1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] == -1):
        # Runner on second
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[2] = 1
    elif (on_base[1] == -1 and on_base[2] == -1 and on_base[3] > -1):
        # Runner on third
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = -1
        on_base[2] = 1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] == -1):
        # Runner on first and second
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = 1
        on_base[2] = 1
        on_base[1] = -1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] > -1):
        # Runner on second and third
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[2] = 1
        on_base[3] = -1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] > -1):
        # Bases loaded
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[3] = on_base[1]
        on_base[2] = 1
        on_base[1] = -1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] > -1):
        # Runners on first and third
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = on_base[1]
        on_base[2] = 1
        on_base[1] = -1
def triple():
    outs()
    outs2()
    global hit, pos, runs, runsallowed, rbi
    if (on_base[1] == -1 and on_base[2] == -1 and on_base[3] == -1):
        # Bases empty
        on_base[3] = 1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] == -1):
        # Runner on first
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = 1
        on_base[1] = -1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] == -1):
        # Runner on second
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = 1
        on_base[2] = -1
    elif (on_base[1] == -1 and on_base[2] == -1 and on_base[3] > -1):
        # Runner on third
        runs += 1
        rbi += 1
        runsallowed += 1
        on_base[3] = 1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] == -1):
        # Runners on first and second
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[3] = 1
        on_base[2] = -1
        on_base[1] = -1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] > -1):
        # Runners on second and third
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[3] = 1
        on_base[2] = -1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] > -1):
        # Bases loaded
        runs += 3
        rbi += 3
        runsallowed += 3
        on_base[3] = 1
        on_base[2] = -1
        on_base[1] = -1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] > -1):
        # Runners on first and third
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[3] = 1
        on_base[1] = -1
def homerun():
    outs()
    outs2()
    global hit, pos, runs, runsallowed, rbi
    if (on_base[1] == -1 and on_base[2] == -1 and on_base[3] == -1):
        # Bases empty 
        runs += 1
        rbi += 1
        runsallowed += 1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] == -1):
        # Runner on first
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[1] = -1
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] == -1):
        # Runner on second
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[2] = -1
    elif (on_base[1] == -1 and on_base[2] == -1 and on_base[3] > -1):
        # Runner on third
        runs += 2
        rbi += 2
        runsallowed += 2
        on_base[3] = -1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] == -1):
        runs += 3
        rbi += 3
        runsallowed += 3
        on_base[1] = -1
        on_base[2] = -1
		# Runners on first and second
    elif (on_base[1] == -1 and on_base[2] > -1 and on_base[3] > -1):
		# Runners on second and third
        runs += 3
        rbi += 3
        runsallowed += 3
        on_base[2] = -1
        on_base[3] = -1
    elif (on_base[1] > -1 and on_base[2] > -1 and on_base[3] > -1):
		# Bases loaded
        runs += 4
        rbi += 4
        runsallowed += 4
        on_base[1] = -1
        on_base[2] = -1
        on_base[3] = -1
    elif (on_base[1] > -1 and on_base[2] == -1 and on_base[3] > -1):
		# Runners on first and third
        runs += 3
        rbi += 4
        runsallowed += 3
        on_base[1] = -1
        on_base[3] = -1
def home():
    global runs
    global hometeamruns
    hometeamruns += runs
    runs = 0
def away():
    global runs, awayteamruns
    awayteamruns += runs
    runs = 0
def batter1stats():
    global batter1atbats, batter1hits, batter1hr, batter1walks, atbats, hits, hr, walks, batter1singles, singles, batter1doubles, doubles, batter1triples, triples, batter1so, so, batter1rbi, rbi
    batter1atbats += atbats
    atbats = 0
    batter1hits += hits
    hits = 0
    batter1hr += hr
    hr = 0
    batter1walks += walks
    walks = 0
    batter1singles += singles
    singles = 0
    batter1doubles += doubles
    doubles = 0
    batter1triples += triples
    triples = 0
    batter1so += so
    so = 0
    batter1rbi += rbi
    rbi = 0
def batter2stats():
    global batter2atbats, batter2hits, batter2hr, batter2walks, atbats, hits, hr, walks, batter2singles, singles, batter2doubles, doubles, batter2triples, triples, batter2so, so, batter2rbi, rbi
    batter2atbats += atbats
    atbats = 0
    batter2hits += hits
    hits = 0
    batter2hr += hr
    hr = 0
    batter2walks += walks
    walks = 0
    batter2singles += singles
    singles = 0
    batter2doubles += doubles
    doubles = 0
    batter2triples += triples
    triples = 0
    batter2so += so
    so = 0
    batter2rbi += rbi
    rbi = 0
def batter3stats():
    global batter3atbats, batter3hits, batter3hr, batter3walks, atbats, hits, hr, walks, batter3singles, singles, batter3doubles, doubles, batter3triples, triples, batter3so, so, batter3rbi, rbi
    batter3atbats += atbats
    atbats = 0
    batter3hits += hits
    hits = 0
    batter3hr += hr
    hr = 0
    batter3walks += walks
    walks = 0
    batter3singles += singles
    singles = 0
    batter3doubles += doubles
    doubles = 0
    batter3triples += triples
    triples = 0
    batter3so += so
    so = 0
    batter3rbi += rbi
    rbi = 0
def batter4stats():
    global batter4atbats, batter4hits, batter4hr, batter4walks, atbats, hits, hr, walks, batter4singles, singles, batter4doubles, doubles, batter4triples, triples, batter4so, so, batter4rbi, rbi
    batter4atbats += atbats
    atbats = 0
    batter4hits += hits
    hits = 0
    batter4hr += hr
    hr = 0
    batter4walks += walks
    walks = 0
    batter4singles += singles
    singles = 0
    batter4doubles += doubles
    doubles = 0
    batter4triples += triples
    triples = 0
    batter4so += so
    so = 0
    batter4rbi += rbi
    rbi = 0
def batter5stats():
    global batter5atbats, batter5hits, batter5hr, batter5walks, atbats, hits, hr, walks, batter5singles, singles, batter5doubles, doubles, batter5triples, triples, batter5so, so, batter5rbi, rbi
    batter5atbats += atbats
    atbats = 0
    batter5hits += hits
    hits = 0
    batter5hr += hr
    hr = 0
    batter5walks += walks
    walks = 0
    batter5singles += singles
    singles = 0
    batter5doubles += doubles
    doubles = 0
    batter5triples += triples
    triples = 0
    batter5so += so
    so = 0
    batter5rbi += rbi
    rbi = 0
def batter6stats():
    global batter6atbats, batter6hits, batter6hr, batter6walks, atbats, hits, hr, walks, batter6singles, singles, batter6doubles, doubles, batter6triples, triples, batter6so, so, batter6rbi, rbi
    batter6atbats += atbats
    atbats = 0
    batter6hits += hits
    hits = 0
    batter6hr += hr
    hr = 0
    batter6walks += walks
    walks = 0
    batter6singles += singles
    singles = 0
    batter6doubles += doubles
    doubles = 0
    batter6triples += triples
    triples = 0
    batter6so += so
    so = 0
    batter6rbi += rbi
    rbi = 0
def batter7stats():
    global batter7atbats, batter7hits, batter7hr, batter7walks, atbats, hits, hr, walks, batter7singles, singles, batter7doubles, doubles, batter7triples, triples, batter7so, so, batter7rbi, rbi
    batter7atbats += atbats
    atbats = 0
    batter7hits += hits
    hits = 0
    batter7hr += hr
    hr = 0
    batter7walks += walks
    walks = 0
    batter7singles += singles
    singles = 0
    batter7doubles += doubles
    doubles = 0
    batter7triples += triples
    triples = 0
    batter7so += so
    so = 0
    batter7rbi += rbi
    rbi = 0
def batter8stats():
    global batter8atbats, batter8hits, batter8hr, batter8walks, atbats, hits, hr, walks, batter8singles, singles, batter8doubles, doubles, batter8triples, triples, batter8so, so, batter8rbi, rbi
    batter8atbats += atbats
    atbats = 0
    batter8hits += hits
    hits = 0
    batter8hr += hr
    hr = 0
    batter8walks += walks
    walks = 0
    batter8singles += singles
    singles = 0
    batter8doubles += doubles
    doubles = 0
    batter8triples += triples
    triples = 0
    batter8so += so
    so = 0
    batter8rbi += rbi
    rbi = 0
def batter9stats():
    global batter9atbats, batter9hits, batter9hr, batter9walks, atbats, hits, hr, walks, batter9singles, singles, batter9doubles, doubles, batter9triples, triples, batter9so, so, batter9rbi, rbi
    batter9atbats += atbats
    atbats = 0
    batter9hits += hits
    hits = 0
    batter9hr += hr
    hr = 0
    batter9walks += walks
    walks = 0
    batter9singles += singles
    singles = 0
    batter9doubles += doubles
    doubles = 0
    batter9triples += triples
    triples = 0
    batter9so += so
    so = 0
    batter9rbi += rbi
    rbi = 0
def batter10stats():
    global batter10atbats, batter10hits, batter10hr, batter10walks, atbats, hits, hr, walks, batter10singles, singles, batter10doubles, doubles, batter10triples, triples, batter10so, so, batter10rbi, rbi
    batter10atbats += atbats
    atbats = 0
    batter10hits += hits
    hits = 0
    batter10hr += hr
    hr = 0
    batter10walks += walks
    walks = 0
    batter10singles += singles
    singles = 0
    batter10doubles += doubles
    doubles = 0
    batter10triples += triples
    triples = 0
    batter10so += so
    so = 0
    batter10rbi += rbi
    rbi = 0
def batter11stats():
    global batter11atbats, batter11hits, batter11hr, batter11walks, atbats, hits, hr, walks, batter11singles, singles, batter11doubles, doubles, batter11triples, triples, batter11so, so, batter11rbi, rbi
    batter11atbats += atbats
    atbats = 0
    batter11hits += hits
    hits = 0
    batter11hr += hr
    hr = 0
    batter11walks += walks
    walks = 0
    batter11singles += singles
    singles = 0
    batter11doubles+= doubles
    doubles = 0
    batter11triples += triples
    triples = 0
    batter11so += so
    so = 0
    batter11rbi += rbi
    rbi = 0
def batter12stats():
    global batter12atbats, batter12hits, batter12hr, batter12walks, atbats, hits, hr, walks, batter12singles, singles, batter12doubles, doubles, batter12triples, triples, batter12so, so, batter12rbi, rbi
    batter12atbats += atbats
    atbats = 0
    batter12hits += hits
    hits = 0
    batter12hr += hr
    hr = 0
    batter12walks += walks
    walks = 0
    batter12singles += singles
    singles = 0
    batter12doubles += doubles
    doubles = 0
    batter12triples += triples
    triples = 0
    batter12so += so
    so = 0
    batter12rbi += rbi
    rbi = 0
def batter13stats():
    global batter13atbats, batter13hits, batter13hr, batter13walks, atbats, hits, hr, walks, batter13singles, singles, batter13doubles, doubles, batter13triples, triples, batter13so, so, batter13rbi, rbi
    batter13atbats += atbats
    atbats = 0
    batter13hits += hits
    hits = 0
    batter13hr += hr
    hr = 0
    batter13walks += walks
    walks = 0
    batter13singles += singles
    singles = 0
    batter13doubles += doubles
    doubles = 0
    batter13triples += triples
    triples = 0
    batter13so += so
    so = 0
    batter13rbi += rbi
    rbi = 0
def batter14stats():
    global batter14atbats, batter14hits, batter14hr, batter14walks, atbats, hits, hr, walks, batter14singles, singles, batter14doubles, doubles, batter14triples, triples, batter14so, so, batter14rbi, rbi
    batter14atbats += atbats
    atbats = 0
    batter14hits += hits
    hits = 0
    batter14hr += hr
    hr = 0
    batter14walks += walks
    walks = 0
    batter14singles += singles
    singles = 0
    batter14doubles += doubles
    doubles = 0
    batter14triples += triples
    triples = 0
    batter14so += so
    so = 0
    batter14rbi += rbi
    rbi = 0
def batter15stats():
    global batter15atbats, batter15hits, batter15hr, batter15walks, atbats, hits, hr, walks, batter15singles, singles, batter15doubles, doubles, batter15triples, triples, batter15so, so, batter15rbi, rbi
    batter15atbats += atbats
    atbats = 0
    batter15hits += hits
    hits = 0
    batter15hr += hr
    hr = 0
    batter15walks += walks
    walks = 0
    batter15singles += singles
    singles = 0
    batter15doubles += doubles
    doubles = 0
    batter15triples += triples
    triples = 0
    batter15so += so
    so = 0
    batter15rbi += rbi
    rbi = 0
def batter16stats():
    global batter16atbats, batter16hits, batter16hr, batter16walks, atbats, hits, hr, walks, batter16singles, singles, batter16doubles, doubles, batter16triples, triples, batter16so, so, batter16rbi, rbi
    batter16atbats += atbats
    atbats = 0
    batter16hits += hits
    hits = 0
    batter16hr += hr
    hr = 0
    batter16walks += walks
    walks = 0
    batter16singles += singles
    singles = 0
    batter16doubles += doubles
    doubles = 0
    batter16triples += triples
    triples = 0
    batter16so += so
    so = 0
    batter16rbi += rbi
    rbi = 0
def batter17stats():
    global batter17atbats, batter17hits, batter17hr, batter17walks, atbats, hits, hr, walks, batter17singles, singles, batter17doubles, doubles, batter17triples, triples, batter17so, so, batter17rbi, rbi
    batter17atbats += atbats
    atbats = 0
    batter17hits += hits
    hits = 0
    batter17hr += hr
    hr = 0
    batter17walks += walks
    walks = 0
    batter17singles += singles
    singles = 0
    batter17doubles += doubles
    doubles = 0
    batter17triples += triples
    triples = 0
    batter17so += so
    so = 0
    batter17rbi += rbi
    rbi = 0
def batter18stats():
    global batter18atbats, batter18hits, batter18hr, batter18walks, atbats, hits, hr, walks, batter18singles, singles, batter18doubles, doubles, batter18triples, triples, batter18so, so, batter18rbi, rbi
    batter18atbats += atbats
    atbats = 0
    batter18hits += hits
    hits = 0
    batter18hr += hr
    hr = 0
    batter18walks += walks
    walks = 0
    batter18singles += singles
    singles = 0
    batter18doubles += doubles
    doubles = 0
    batter18triples += triples
    triples = 0
    batter18so += so
    so = 0
    batter18rbi += rbi
    rbi = 0
def homestarterstats():
    global hitsallowed, homestarterhitsallowed, Ks, homestarterks, innings, walksallowed, homestarterwalks, runsallowed, homestarterrunsallowed, homestarterhrallowed, hrallowed
    if innings < 6:
        homestarterhitsallowed += hitsallowed
        hitsallowed = 0
        homestarterks += Ks
        Ks = 0
        homestarterwalks += walksallowed
        walksallowed = 0
        homestarterrunsallowed += runsallowed
        runsallowed = 0
        homestarterhrallowed += hrallowed
        hrallowed = 0
def awaystarterstats():
    global hitsallowed, awaystarterhitsallowed, Ks, awaystarterks, innings, awaystarterwalks, walksallowed, runsallowed, awaystarterrunsallowed, awaystarterhrallowed, hrallowed
    if innings < 6:
        awaystarterhitsallowed += hitsallowed
        hitsallowed = 0
        awaystarterks += Ks
        Ks = 0
        awaystarterwalks += walksallowed
        walksallowed = 0
        awaystarterrunsallowed += runsallowed
        runsallowed = 0
        awaystarterhrallowed += hrallowed
        hrallowed = 0
def homereliefstats():
    global hitsallowed, homereliefhitsallowed, Ks, homereliefks, innings, homereliefwalks, walksallowed, runsallowed, homereliefrunsallowed, ip, homereliefip, homereliefhrallowed, hrallowed
    if (innings == 6 or innings == 7):
        homereliefhitsallowed += hitsallowed
        hitsallowed = 0
        homereliefks += Ks
        Ks = 0
        homereliefwalks += walksallowed
        walksallowed = 0
        homereliefrunsallowed += runsallowed
        runsallowed = 0
        homereliefip += ip
        ip = 0
        homereliefhrallowed += hrallowed
        hrallowed = 0
def awayreliefstats():
    global hitsallowed, awayreliefhitsallowed, Ks, awayreliefks, innings, awayreliefwalks, walksallowed, runsallowed, awayreliefrunsallowed, ip, awayreliefip, awayreliefhrallowed, hrallowed
    if (innings == 6.5 or innings == 7.5):
        awayreliefhitsallowed += hitsallowed
        hitsallowed = 0
        awayreliefks += Ks
        Ks = 0
        awayreliefwalks += walksallowed
        walksallowed = 0
        awayreliefrunsallowed += runsallowed
        runsallowed = 0
        awayreliefip += ip
        ip = 0
        awayreliefhrallowed += hrallowed
        hrallowed = 0
def homerelief2stats():
    global hitsallowed, homerelief2hitsallowed, Ks, homerelief2ks, innings, homerelief2walks, walksallowed, runsallowed, homerelief2runsallowed, ip, homerelief2ip, homerelief2hrallowed, hrallowed
    if (innings == 8 or innings == 9):
        homerelief2hitsallowed += hitsallowed
        hitsallowed = 0
        homerelief2ks += Ks
        Ks = 0
        homerelief2walks += walksallowed
        walksallowed = 0
        homerelief2runsallowed += runsallowed
        runsallowed = 0
        homerelief2ip += ip
        ip = 0
        homerelief2hrallowed += hrallowed
        hrallowed = 0
def awayrelief2stats():
    global hitsallowed, awayrelief2hitsallowed, Ks, awayrelief2ks, innings, awayrelief2walks, walksallowed, runsallowed, awayrelief2runsallowed, awayrelief2ip, ip, awayrelief2hrallowed, hrallowed
    if (innings == 8.5 or innings == 9.5):
        awayrelief2hitsallowed += hitsallowed
        hitsallowed = 0
        awayrelief2ks += Ks
        Ks = 0
        awayrelief2walks += walksallowed
        walksallowed = 0
        awayrelief2runsallowed += runsallowed
        runsallowed = 0
        awayrelief2ip += ip
        ip = 0
        awayrelief2hrallowed += hrallowed
        hrallowed = 0
def outfieldstats():
    global homeleftopps, homeleftthrowouts, homecenteropps, homecenterthrowouts, homerightopps, homerightthrowouts, awayleftopps, awayleftthrowouts, awaycenteropps, awaycenterthrowouts, awayrightopps, awayrightthrowouts
    if Team == ("Home"):
            if (diem <=5):
                if Safe == ("Safe!"):
                    homeleftopps += 1
                else:
                    homeleftopps += 1
                    homeleftthrowouts += 1
            if (diem == 6 or diem == 7 or diem == 8 or diem ==9):
                if Safe == ("Safe!"):
                    homecenteropps += 1
                else:
                    homecenteropps += 1
                    homecenterthrowouts += 1
            if (diem >=10):
                if Safe == ("Safe!"):
                    homerightopps += 1
                else:
                    homerightopps += 1
                    homerightthrowouts += 1
    elif Team == ("Away"):
            if (diem <=5):
                if Safe == ("Safe!"):
                    awayleftopps += 1
                else:
                    awayleftopps += 1
                    awayleftthrowouts += 1
            if (diem == 6 or diem == 7 or diem == 8 or diem ==9):
                if Safe == ("Safe!"):
                    awaycenteropps += 1
                else:
                    awaycenteropps += 1
                    awaycenterthrowouts += 1
            if (diem >=10):
                if Safe == ("Safe!"):
                    awayrightopps += 1
                else:
                    awayrightopps += 1
                    awayrightthrowouts += 1
def infieldstats():
    global homeSSopps, homeSSthrowouts, home2Bopps, home2Bthrowouts, home3Bopps, home3Bthrowouts, awaySSopps, awaySSthrowouts, away2Bopps, away2Bthrowouts, away3Bopps, away3Bthrowouts
    if Team == ("Home"):
        if (diei==1):
            if Safe == ("Safe!"):
                homeSSopps += 1
            else:
                homeSSopps += 1
                homeSSthrowouts += 1
        if (diei ==2):
            if Safe == ("Safe!"):
                home2Bopps += 1
            else:
                home2Bopps += 1
                home2Bthrowouts += 1
        if (diei ==3):
            if Safe == ("Safe!"):
                home3Bopps += 1
            else:
                home3Bopps += 1
                home3Bthrowouts += 1
    if Team == ("Away"):
        if (diei==1):
            if Safe == ("Safe!"):
                awaySSopps += 1
            else:
                awaySSopps += 1
                awaySSthrowouts += 1
        if (diei ==2):
            if Safe == ("Safe!"):
                away2Bopps += 1
            else:
                away2Bopps += 1
                away2Bthrowouts += 1
        if (diei ==3):
            if Safe == ("Safe!"):
                away3Bopps += 1
            else:
                away3Bopps += 1
                away3Bthrowouts += 1

Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
def boxscore():
    Boxscore = input("Boxscore?")
    if (Boxscore=="n"):
        test()
        test2()
        exit()
    else:
        print (" ")
        print ("Home team:")
        print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
        print (" ")
        print (" ")
        print ("Away team:")
        print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
#Extra innings code------------------------------------------------------------------------------------------------------------------

extrainnings = 0
def extrainning():
    global extrainnings, homereliefposition3, homereliefposition4, homereliefposition5, homereliefposition6, awayreliefposition3, awayreliefposition4, awayreliefposition5, awayreliefposition6
    if extrainnings==10:
        if hometeamruns==awayteamruns:
            print ("tenth")
            print ("")
            homepitcherrequest()
            homereliefposition3 = input("Home pitcher position?")
            awaypitcherrequest()
            awayreliefposition3 = input("Away pitcher position?")
            lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==11:
        if hometeamruns==awayteamruns:
            print ("eleventh")
            print ("")
            time.sleep(5)
            lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==12:
        if hometeamruns==awayteamruns:
                print ("twelveths")
                print ("")
                time.sleep(5)
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==13:
        if hometeamruns==awayteamruns:
                print ("thirteenths")
                print ("")
                time.sleep(5)
                homepitcherrequest()
                homereliefposition4 = input("Home pitcher position?")
                awaypitcherrequest()
                awayreliefposition4 = input("Away pitcher position?")
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==14:
        if hometeamruns==awayteamruns:
                print ("fourteenths")
                print ("")
                time.sleep(5)
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==15:
        if hometeamruns==awayteamruns:
                print ("fifteenths")
                print ("")
                time.sleep(5)
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==16:
        if hometeamruns==awayteamruns:
                print ("sixteenths")
                print ("")
                time.sleep(5)
                homepitcherrequest()
                homereliefposition5 = input("Home pitcher position?")
                awaypitcherrequest()
                awayreliefposition5 = input("Away pitcher position?")
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==17:
        if hometeamruns==awayteamruns:
                print ("seventeenths")
                print ("")
                time.sleep(5)
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==18:
        if hometeamruns==awayteamruns:
                print ("eighteenths")
                print ("")
                time.sleep(5)
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==19:
        if hometeamruns==awayteamruns:
                print ("nineteenths")
                print ("")
                time.sleep(5)
                homepitcherrequest()
                homereliefposition6 = input("Home pitcher position?")
                awaypitcherrequest()
                awayreliefposition6 = input("Away pitcher position?")
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks], ['Relief 6', homerelief6ip, homerelief6runsallowed, homerelief6ks, homerelief6hitsallowed, homerelief6walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks], ['Relief 6', awayrelief6ip, awayrelief6runsallowed, awayrelief6ks, awayrelief6hitsallowed, awayrelief6walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==20:
        if hometeamruns==awayteamruns:
                print ("twentieths")
                print ("")
                time.sleep(5)
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks], ['Relief 6', homerelief6ip, homerelief6runsallowed, homerelief6ks, homerelief6hitsallowed, homerelief6walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks], ['Relief 6', awayrelief6ip, awayrelief6runsallowed, awayrelief6ks, awayrelief6hitsallowed, awayrelief6walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
    elif extrainnings==21:
        if hometeamruns==awayteamruns:
                print ("twentyfirst")
                print ("")
                time.sleep(5)
                lineup2extra()
        else:
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks], ['Relief 6', homerelief6ip, homerelief6runsallowed, homerelief6ks, homerelief6hitsallowed, homerelief6walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks], ['Relief 6', awayrelief6ip, awayrelief6runsallowed, awayrelief6ks, awayrelief6hitsallowed, awayrelief6walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
def walkoff():
    global ip
    if innings>9:
        home()
        away()
        if hometeamruns>awayteamruns:
            ip = 1
            awayrelief2stats()
            awayrelief3stats()
            awayrelief4stats()
            awayrelief5stats()
            awayrelief6stats()
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks], ['Relief 6', homerelief6ip, homerelief6runsallowed, homerelief6ks, homerelief6hitsallowed, homerelief6walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks], ['Relief 6', awayrelief6ip, awayrelief6runsallowed, awayrelief6ks, awayrelief6hitsallowed, awayrelief6walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                print (awaycenteropps)
                print (awaycenterthrowouts)
                print ("")
                print (away2Bopps)
                print (away2Bthrowouts)
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit() 
    elif extrainnings>9:
        ip = 1
        home()
        away()
        if hometeamruns>awayteamruns:
            ip = 1
            awayrelief3stats()
            awayrelief4stats()
            awayrelief5stats()
            awayrelief6stats()
            print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
            Htable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter1name, batter1hits, batter1atbats, batter1hr, batter1walks, batter1singles, batter1doubles, batter1triples], [batter2name, batter2hits, batter2atbats, batter2hr, batter2walks, batter2singles, batter2doubles, batter2triples], [batter3name, batter3hits, batter3atbats, batter3hr, batter3walks, batter3singles, batter3doubles, batter3triples], [batter4name, batter4hits, batter4atbats, batter4hr, batter4walks, batter4singles, batter4doubles, batter4triples], [batter5name, batter5hits, batter5atbats, batter5hr, batter5walks, batter5singles, batter5doubles, batter5triples], [batter6name, batter6hits, batter6atbats, batter6hr, batter6walks, batter6singles, batter6doubles, batter6triples], [batter7name, batter7hits, batter7atbats, batter7hr, batter7walks, batter7singles, batter7doubles, batter7triples], [batter8name, batter8hits, batter8atbats, batter8hr, batter8walks, batter8singles, batter8doubles, batter8triples], [batter9name, batter9hits, batter9atbats, batter9hr, batter9walks, batter9singles, batter9doubles, batter9triples]]
            Atable = [['Name', 'Hits', 'Atbats', 'HRs', 'Walks', '1bs', '2bs', '3bs'], [batter10name, batter10hits, batter10atbats, batter10hr, batter10walks, batter10singles, batter10doubles, batter10triples], [batter11name, batter11hits, batter11atbats, batter11hr, batter11walks, batter11singles, batter11doubles, batter11triples], [batter12name, batter12hits, batter12atbats, batter12hr, batter12walks, batter12singles, batter12doubles, batter12triples], [batter13name, batter13hits, batter13atbats, batter13hr, batter13walks, batter13singles, batter13doubles, batter13triples], [batter14name, batter14hits, batter14atbats, batter14hr, batter14walks, batter14singles, batter14doubles, batter14triples], [batter15name, batter15hits, batter15atbats, batter15hr, batter15walks, batter15singles, batter15doubles, batter15triples], [batter16name, batter16hits, batter16atbats, batter16hr, batter16walks, batter16singles, batter16doubles, batter16triples], [batter17name, batter17hits, batter17atbats, batter17hr, batter17walks, batter17singles, batter17doubles, batter17triples], [batter18name, batter18hits, batter18atbats, batter18hr, batter18walks, batter18singles, batter18doubles, batter18triples]]
            Hpitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Home Starter', '5', homestarterrunsallowed, homestarterks, homestarterhitsallowed, homestarterwalks],['Relief', homereliefip, homereliefrunsallowed, homereliefks, homereliefhitsallowed, homereliefwalks], ['Relief 2', homerelief2ip, homerelief2runsallowed, homerelief2ks, homerelief2hitsallowed, homerelief2walks], ['Relief 3', homerelief3ip, homerelief3runsallowed, homerelief3ks, homerelief3hitsallowed, homerelief3walks], ['Relief 4', homerelief4ip, homerelief4runsallowed, homerelief4ks, homerelief4hitsallowed, homerelief4walks], ['Relief 5', homerelief5ip, homerelief5runsallowed, homerelief5ks, homerelief5hitsallowed, homerelief5walks], ['Relief 6', homerelief6ip, homerelief6runsallowed, homerelief6ks, homerelief6hitsallowed, homerelief6walks]]
            Apitcher = [['Name', 'innings', 'runs', 'Ks', 'hits', 'walks'], ['Away Starter', '5', awaystarterrunsallowed, awaystarterks, awaystarterhitsallowed, awaystarterwalks],['Relief', awayreliefip, awayreliefrunsallowed, awayreliefks, awayreliefhitsallowed, awayreliefwalks], ['Relief 2', awayrelief2ip, awayrelief2runsallowed, awayrelief2ks, awayrelief2hitsallowed, awayrelief2walks], ['Relief 3', awayrelief3ip, awayrelief3runsallowed, awayrelief3ks, awayrelief3hitsallowed, awayrelief3walks], ['Relief 4', awayrelief4ip, awayrelief4runsallowed, awayrelief4ks, awayrelief4hitsallowed, awayrelief4walks], ['Relief 5', awayrelief5ip, awayrelief5runsallowed, awayrelief5ks, awayrelief5hitsallowed, awayrelief5walks], ['Relief 6', awayrelief6ip, awayrelief6runsallowed, awayrelief6ks, awayrelief6hitsallowed, awayrelief6walks]]
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Home team:")
                print (tabulate(Hpitcher, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Apitcher, headers='firstrow', tablefmt='fancy_grid'))
                test()
                test2()
                exit()
def extrahome():
    if innings >= 9.5:
        if awayteamruns>hometeamruns:
            Boxscore = input("Boxscore?")
            if (Boxscore=="n"):
                test()
                test2()
                exit()
            else:
                print (" ")
                print ("Home team:")
                print (tabulate(Htable, headers='firstrow', tablefmt='fancy_grid'))
                print (" ")
                print (" ")
                print ("Away team:")
                print (tabulate(Atable, headers='firstrow', tablefmt='fancy_grid'))
def lineupextra():
    awaypitcher()
    global out, current_batter, Htable, Safe, Team
    Team = ("Away")
    for i in range(100):
        if (current_batter==1):
            batter1()
            print (batter1name,"",batter1hits,"-",batter1atbats)
            atbat()
            batter1stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==2):
            batter2()
            print (batter2name,"",batter2hits,"-",batter2atbats)
            atbat()
            batter2stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==3):
            batter3()
            print (batter3name,"",batter3hits,"-",batter3atbats)
            atbat()
            batter3stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==4):
            batter4()
            print (batter4name,"",batter4hits,"-",batter4atbats)
            atbat()
            batter4stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==5):
            batter5()
            print (batter5name,"",batter5hits,"-",batter5atbats)
            atbat()
            batter5stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==6):
            batter6()
            print (batter6name,"",batter6hits,"-",batter6atbats)
            atbat()
            batter6stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==7):
            batter7()
            print (batter7name,"",batter7hits,"-",batter7atbats)
            atbat()
            batter7stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==8):
            batter8()
            print (batter8name,"",batter8hits,"-",batter8atbats)
            atbat()
            batter8stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter += 1
            walkoff()
            outsextra()
            time.sleep(5)
        elif (current_batter==9):
            batter9()
            print (batter9name,"",batter9hits,"-",batter9atbats)
            atbat()
            batter9stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter = 1
            walkoff()
            outsextra()
            time.sleep(5)
def lineup2extra():
    homepitcher()
    global current_batter2, Atable, Safe, Team
    Team = ("Home")
    for i in range(100):
        if (current_batter2==1):
            batter10()
            print (batter10name,"",batter10hits,"-",batter10atbats)
            atbat()
            batter10stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==2):
            batter11()
            print (batter11name,"",batter11hits,"-",batter11atbats)
            atbat()
            batter11stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==3):
            batter12()
            print (batter12name,"",batter12hits,"-",batter12atbats)
            atbat()
            batter12stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==4):
            batter13()
            print (batter13name,"",batter13hits,"-",batter13atbats)
            atbat()
            batter13stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==5):
            batter14()
            print (batter14name,"",batter14hits,"-",batter14atbats)
            atbat()
            batter14stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==6):
            batter15()
            print (batter15name,"",batter15hits,"-",batter15atbats)
            atbat()
            batter15stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==7):
            batter16()
            print (batter16name,"",batter16hits,"-",batter16atbats)
            atbat()
            batter16stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==8):
            batter17()
            print (batter17name,"",batter17hits,"-",batter17atbats)
            atbat()
            batter17stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 += 1
            outs2extra()
            time.sleep(5)
        if (current_batter2==9):
            batter18()
            print (batter18name,"",batter18hits,"-",batter18atbats)
            atbat()
            batter18stats()
            print (" ")
            print (on_base[1])
            print (on_base[2])
            print (on_base[3])
            Safe = ("")
            current_batter2 = 1
            outs2extra()
            time.sleep(5)
def outsextra():
    global out, on_base, innings, extrainnings, ip
    if (out==3):
        ip = 1
        home()
        awayrelief3stats()
        awayrelief4stats()
        awayrelief5stats()
        awayrelief6stats()
        print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
        print ("")
        time.sleep(5)
        out = 0
        on_base = [-1, -1, -1, -1]
        extrainnings+=0.5
        extrainning()
def outs2extra():
    global out, on_base, innings, extrainnings, ip
    if (out==3):
        ip = 1
        away()
        homerelief3stats()
        homerelief4stats()
        homerelief5stats()
        homerelief6stats()
        print (Ateam,":",awayteamruns,Hteam,":", hometeamruns)
        print ("")
        time.sleep(5)
        out = 0
        on_base = [-1, -1, -1, -1]
        print ("Next Team")
        print ("")
        extrainnings+=0.5
        lineupextra()
#Some extra inning stats
def homerelief3stats():
    global hitsallowed, homerelief3hitsallowed, Ks, homerelief3ks, extrainnings, homerelief3walks, walksallowed, runsallowed, homerelief3runsallowed, homerelief3ip, ip, homerelief3hrallowed, hrallowed
    if (extrainnings == 10 or extrainnings == 11 or extrainnings == 12):
            homerelief3hitsallowed += hitsallowed
            hitsallowed = 0
            homerelief3ks += Ks
            Ks = 0
            homerelief3walks += walksallowed
            walksallowed = 0
            homerelief3runsallowed += runsallowed
            runsallowed = 0
            homerelief3ip += ip
            ip = 0
            homerelief3hrallowed += hrallowed
            hrallowed = 0
def homerelief4stats():
    global hitsallowed, homerelief4hitsallowed, Ks, homerelief4ks, extrainnings, homerelief4walks, walksallowed, runsallowed, homerelief4runsallowed, homerelief4ip, ip, homerelief4hrallowed, hrallowed
    if (extrainnings == 13 or extrainnings == 14 or extrainnings == 15):
            homerelief4hitsallowed += hitsallowed
            hitsallowed = 0
            homerelief4ks += Ks
            Ks = 0
            homerelief4walks += walksallowed
            walksallowed = 0
            homerelief4runsallowed += runsallowed
            runsallowed = 0
            homerelief4ip += ip
            ip = 0
            homerelief4hrallowed += hrallowed
            hrallowed = 0
def homerelief5stats():
    global hitsallowed, homerelief5hitsallowed, Ks, homerelief5ks, extrainnings, homerelief5walks, walksallowed, runsallowed, homerelief5runsallowed, homerelief5ip, ip, homerelief5hrallowed, hrallowed
    if (extrainnings == 16 or extrainnings == 17 or extrainnings == 18):
            homerelief5hitsallowed += hitsallowed
            hitsallowed = 0
            homerelief5ks += Ks
            Ks = 0
            homerelief5walks += walksallowed
            walksallowed = 0
            homerelief5runsallowed += runsallowed
            runsallowed = 0
            homerelief5ip += ip
            ip = 0
            homerelief5hrallowed += hrallowed
            hrallowed = 0
def homerelief6stats():
    global hitsallowed, homerelief6hitsallowed, Ks, homerelief6ks, extrainnings, homerelief6walks, walksallowed, runsallowed, homerelief6runsallowed, homerelief6ip, ip, homerelief6hrallowed, hrallowed
    if (extrainnings == 19 or extrainnings == 20 or extrainnings == 21):
            homerelief6hitsallowed += hitsallowed
            hitsallowed = 0
            homerelief6ks += Ks
            Ks = 0
            homerelief6walks += walksallowed
            walksallowed = 0
            homerelief6runsallowed += runsallowed
            runsallowed = 0
            homerelief6ip += ip
            ip = 0
            homerelief6hrallowed += hrallowed
            hrallowed = 0
def awayrelief3stats():
    global hitsallowed, awayrelief3hitsallowed, Ks, awayrelief3ks, extrainnings, awayrelief3walks, walksallowed, runsallowed, awayrelief3runsallowed, awayrelief3ip, ip, awayrelief3hrallowed, hrallowed
    if (extrainnings == 10.5 or extrainnings == 11.5 or extrainnings == 12.5):
            awayrelief3hitsallowed += hitsallowed
            hitsallowed = 0
            awayrelief3ks += Ks
            Ks = 0
            awayrelief3walks += walksallowed
            walksallowed = 0
            awayrelief3runsallowed += runsallowed
            runsallowed = 0
            awayrelief3ip += ip
            ip = 0
            awayrelief3hrallowed += hrallowed
            hrallowed = 0
def awayrelief4stats():
    global hitsallowed, awayrelief4hitsallowed, Ks, awayrelief4ks, extrainnings, awayrelief4walks, walksallowed, runsallowed, awayrelief4runsallowed, awayrelief4ip, ip, awayrelief4hrallowed, hrallowed
    if (extrainnings == 13.5 or extrainnings == 14.5 or extrainnings == 15.5):
            awayrelief4hitsallowed += hitsallowed
            hitsallowed = 0
            awayrelief4ks += Ks
            Ks = 0
            awayrelief4walks += walksallowed
            walksallowed = 0
            awayrelief4runsallowed += runsallowed
            runsallowed = 0
            awayrelief4ip += ip
            ip = 0
            awayrelief4hrallowed += hrallowed
            hrallowed = 0
def awayrelief5stats():
    global hitsallowed, awayrelief5hitsallowed, Ks, awayrelief5ks, extrainnings, awayrelief5walks, walksallowed, runsallowed, awayrelief5runsallowed, awayrelief5ip, ip, awayrelief5hrallowed, hrallowed
    if (extrainnings == 16.5 or extrainnings == 17.5 or extrainnings == 18.5):
            awayrelief5hitsallowed += hitsallowed
            hitsallowed = 0
            awayrelief5ks += Ks
            Ks = 0
            awayrelief5walks += walksallowed
            walksallowed = 0
            awayrelief5runsallowed += runsallowed
            runsallowed = 0
            awayrelief5ip += ip
            ip = 0
            awayrelief5hrallowed += hrallowed
            hrallowed = 0
def awayrelief6stats():
    global hitsallowed, awayrelief6hitsallowed, Ks, awayrelief6ks, extrainnings, awayrelief6walks, walksallowed, runsallowed, awayrelief6runsallowed, awayrelief6ip, ip, awayrelief6hrallowed, hrallowed
    if (extrainnings == 19.5 or extrainnings == 20.5 or extrainnings == 21.5):
            awayrelief6hitsallowed += hitsallowed
            hitsallowed = 0
            awayrelief6ks += Ks
            Ks = 0
            awayrelief6walks += walksallowed
            walksallowed = 0
            awayrelief6runsallowed += runsallowed
            runsallowed = 0
            awayrelief6ip += ip
            ip = 0
            awayrelief6hrallowed += hrallowed
            hrallowed = 0
#indivisual defense type beat
def secondbase():
    global fs, away2b, home2b
    if Team == ("Away"):
        fs = away2b
    elif Team == ("Home"):
        fs = home2b
def thirdbase():
    global fs, away3b, home3b
    if Team == ("Away"):
        fs = away3b
    elif Team == ("Home"):
        fs = home3b
def SS():
    global fs, awayss, homess
    if Team == ("Away"):
        fs = awayss
    elif Team == ("Home"):
        fs = homess
def LF():
    global fs, awaylf, homelf
    if Team == ("Away"):
        fs = awaylf
    elif Team == ("Home"):
        fs = homelf
def CF():
    global fs, awaycf, homecf
    if Team == ("Away"):
        fs = awaycf
    elif Team == ("Home"):
        fs = homecf
def RF():
    global fs, awayrf, homerf
    if Team == ("Away"):
        fs = awayrf
    elif Team == ("Home"):
        fs = homerf
def test():
    consent()
    import pandas as pd
    if Hteam == ("brawlers"):
        df = pd.read_csv("brawlers.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
        # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        #Second starter
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("six")
            or homereliefposition1 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[5, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homereliefks
            # Saving hits
            df.loc[5, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[5, 'Hr'] += homereliefhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("six")
            or homereliefposition2 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[5, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[5, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[5, 'Hr'] += homerelief2hrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("brawlers.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("six")
            or homereliefposition3 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief3hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("six")
            or homereliefposition4 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief4hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("six")
            or homereliefposition5 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief5hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("six")
            or homereliefposition6 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief6hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("brawlers.csv", index=False)
                #print(df)
    elif Hteam == ("wardogs"):
        import pandas as pd
        df = pd.read_csv("wardogs.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
        # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        #Second starter
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("six")
            or homereliefposition1 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[5, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homereliefks
            # Saving hits
            df.loc[5, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[5, 'Hr'] += homereliefhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("six")
            or homereliefposition2 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[5, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[5, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[5, 'Hr'] += homerelief2hrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("wardogs.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("six")
            or homereliefposition3 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief3hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("six")
            or homereliefposition4 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief4hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("six")
            or homereliefposition5 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief5hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("six")
            or homereliefposition6 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief6hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("wardogs.csv", index=False)
                #print(df)
        import test
    elif Hteam == ("manitees"):
        import pandas as pd
        df = pd.read_csv("manitees.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
        # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        elif (homestarterposition == ("six")
              or homestarterposition == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += 5
            # Saving Runs
            df.loc[5, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homestarterks
            # Saving hits
            df.loc[5, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homestarterwalks
            df.loc[5, 'Hr'] += homestarterhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("eleven")
            or homereliefposition1 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[10, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homereliefks
            # Saving hits
            df.loc[10, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homereliefwalks
            df.loc[10, 'Hr'] += homereliefhrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("eleven")
            or homereliefposition2 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[10, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[10, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homerelief2walks
            df.loc[10, 'Hr'] += homerelief2hrallowed
            df.to_csv("manitees.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("eleven")
            or homereliefposition3 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief3walks
                df.loc[10, 'Hr'] += homerelief3hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Third relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("eleven")
            or homereliefposition4 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief4walks
                df.loc[10, 'Hr'] += homerelief4hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("eleven")
            or homereliefposition5 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief5walks
                df.loc[10, 'Hr'] += homerelief5hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("manitees.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("eleven")
            or homereliefposition6 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief6walks
                df.loc[10, 'Hr'] += homerelief6hrallowed
                df.to_csv("manitees.csv", index=False)
        manitees1baa()
        manitees2baa()
        manitees3baa()
        manitees4baa()
        manitees5baa()
        manitees6baa()
        manitees7baa()
        manitees8baa()
        manitees9baa()
        manitees1obp()
        manitees2obp()
        manitees3obp()
        manitees4obp()
        manitees5obp()
        manitees6obp()
        manitees7obp()
        manitees8obp()
        manitees9obp()
        manitees1slg()
        manitees2slg()
        manitees3slg()
        manitees4slg()
        manitees5slg()
        manitees6slg()
        manitees7slg()
        manitees8slg()
        manitees9slg()
        manitees1ops()
        manitees2ops()
        manitees3ops()
        manitees4ops()
        manitees5ops()
        manitees6ops()
        manitees7ops()
        manitees8ops()
        manitees9ops()
    elif Hteam == ("liberty"):
        import pandas as pd
        df = pd.read_csv("liberty.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
                # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        elif (homestarterposition == ("six")
              or homestarterposition == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += 5
            # Saving Runs
            df.loc[5, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homestarterks
            # Saving hits
            df.loc[5, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homestarterwalks
            df.loc[5, 'Hr'] += homestarterhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("eleven")
            or homereliefposition1 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[10, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homereliefks
            # Saving hits
            df.loc[10, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homereliefwalks
            df.loc[10, 'Hr'] += homereliefhrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("eleven")
            or homereliefposition2 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[10, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[10, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homerelief2walks
            df.loc[10, 'Hr'] += homerelief2hrallowed
            df.to_csv("liberty.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("eleven")
            or homereliefposition3 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief3walks
                df.loc[10, 'Hr'] += homerelief3hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Third relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("eleven")
            or homereliefposition4 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief4walks
                df.loc[10, 'Hr'] += homerelief4hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("eleven")
            or homereliefposition5 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief5walks
                df.loc[10, 'Hr'] += homerelief5hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("liberty.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("eleven")
            or homereliefposition6 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief6walks
                df.loc[10, 'Hr'] += homerelief6hrallowed
                df.to_csv("liberty.csv", index=False)
        liberty1baa()
        liberty2baa()
        liberty3baa()
        liberty4baa()
        liberty5baa()
        liberty6baa()
        liberty7baa()
        liberty8baa()
        liberty9baa()
        liberty1obp()
        liberty2obp()
        liberty3obp()
        liberty4obp()
        liberty5obp()
        liberty6obp()
        liberty7obp()
        liberty8obp()
        liberty9obp()
        liberty1slg()
        liberty2slg()
        liberty3slg()
        liberty4slg()
        liberty5slg()
        liberty6slg()
        liberty7slg()
        liberty8slg()
        liberty9slg()
        liberty1ops()
        liberty2ops()
        liberty3ops()
        liberty4ops()
        liberty5ops()
        liberty6ops()
        liberty7ops()
        liberty8ops()
        liberty9ops()
    elif Hteam == ("knights"):
        import pandas as pd
        df = pd.read_csv("knights.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
                # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        #Second starter
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("six")
            or homereliefposition1 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[5, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homereliefks
            # Saving hits
            df.loc[5, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[5, 'Hr'] += homereliefhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("six")
            or homereliefposition2 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[5, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[5, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[5, 'Hr'] += homerelief2hrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("knights.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("six")
            or homereliefposition3 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief3hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("six")
            or homereliefposition4 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief4hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("six")
            or homereliefposition5 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief5hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("six")
            or homereliefposition6 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief6hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("knights.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("knights.csv", index=False)
        knights1baa()
        knights2baa()
        knights3baa()
        knights4baa()
        knights5baa()
        knights6baa()
        knights7baa()
        knights8baa()
        knights9baa()
        knights1obp()
        knights2obp()
        knights3obp()
        knights4obp()
        knights5obp()
        knights6obp()
        knights7obp()
        knights8obp()
        knights9obp()
        knights1slg()
        knights2slg()
        knights3slg()
        knights4slg()
        knights5slg()
        knights6slg()
        knights7slg()
        knights8slg()
        knights9slg()
        knights1ops()
        knights2ops()
        knights3ops()
        knights4ops()
        knights5ops()
        knights6ops()
        knights7ops()
        knights8ops()
        knights9ops()
    elif Hteam == ("arches"):
        import pandas as pd
        df = pd.read_csv("arches.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
                # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        #Second starter
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("six")
            or homereliefposition1 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[5, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homereliefks
            # Saving hits
            df.loc[5, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[5, 'Hr'] += homereliefhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("six")
            or homereliefposition2 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[5, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[5, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[5, 'Hr'] += homerelief2hrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("arches.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("six")
            or homereliefposition3 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief3hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("six")
            or homereliefposition4 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief4hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("six")
            or homereliefposition5 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief5hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("six")
            or homereliefposition6 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief6hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("arches.csv", index=False)
                #print(df)
        arches1baa()
        arches2baa()
        arches3baa()
        arches4baa()
        arches5baa()
        arches6baa()
        arches7baa()
        arches8baa()
        arches9baa()
        arches1obp()
        arches2obp()
        arches3obp()
        arches4obp()
        arches5obp()
        arches6obp()
        arches7obp()
        arches8obp()
        arches9obp()
        arches1slg()
        arches2slg()
        arches3slg()
        arches4slg()
        arches5slg()
        arches6slg()
        arches7slg()
        arches8slg()
        arches9slg()
        arches1ops()
        arches2ops()
        arches3ops()
        arches4ops()
        arches5ops()
        arches6ops()
        arches7ops()
        arches8ops()
        arches9ops()
    elif Hteam == ("blondes"):
        import pandas as pd
        df = pd.read_csv("blondes.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
                # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        #Second starter
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("six")
            or homereliefposition1 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[5, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homereliefks
            # Saving hits
            df.loc[5, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[5, 'Hr'] += homereliefhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("six")
            or homereliefposition2 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[5, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[5, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[5, 'Hr'] += homerelief2hrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("blondes.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("six")
            or homereliefposition3 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief3hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("six")
            or homereliefposition4 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief4hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("six")
            or homereliefposition5 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief5hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("six")
            or homereliefposition6 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief6hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("blondes.csv", index=False)
                #print(df)
        blondes1baa()
        blondes2baa()
        blondes3baa()
        blondes4baa()
        blondes5baa()
        blondes6baa()
        blondes7baa()
        blondes8baa()
        blondes9baa()
        blondes1obp()
        blondes2obp()
        blondes3obp()
        blondes4obp()
        blondes5obp()
        blondes6obp()
        blondes7obp()
        blondes8obp()
        blondes9obp()
        blondes1slg()
        blondes2slg()
        blondes3slg()
        blondes4slg()
        blondes5slg()
        blondes6slg()
        blondes7slg()
        blondes8slg()
        blondes9slg()
        blondes1ops()
        blondes2ops()
        blondes3ops()
        blondes4ops()
        blondes5ops()
        blondes6ops()
        blondes7ops()
        blondes8ops()
        blondes9ops()
    elif Hteam == ("cheesestakes"):
        import pandas as pd
        df = pd.read_csv("cheesestakes.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
                # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        #Second starter
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            # Saving Hrs
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("six")
            or homereliefposition1 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[5, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homereliefks
            # Saving hits
            df.loc[5, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[5, 'Hr'] += homereliefhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            # Saving Hrs
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("six")
            or homereliefposition2 == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[5, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[5, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[5, 'Hr'] += homerelief2hrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            # Saving Hrs
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("cheesestakes.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("six")
            or homereliefposition3 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief3hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("six")
            or homereliefposition4 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief4hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("six")
            or homereliefposition5 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief5hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("six")
            or homereliefposition6 == "6"):
                #Saving innings
                df.loc[5, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[5, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[5, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[5, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[5, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[5, 'Hr'] += homerelief6hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                # Saving Hrs
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("cheesestakes.csv", index=False)
                #print(df)
        cheesestakes1baa()
        cheesestakes2baa()
        cheesestakes3baa()
        cheesestakes4baa()
        cheesestakes5baa()
        cheesestakes6baa()
        cheesestakes7baa()
        cheesestakes8baa()
        cheesestakes9baa()
        cheesestakes1obp()
        cheesestakes2obp()
        cheesestakes3obp()
        cheesestakes4obp()
        cheesestakes5obp()
        cheesestakes6obp()
        cheesestakes7obp()
        cheesestakes8obp()
        cheesestakes9obp()
        cheesestakes1slg()
        cheesestakes2slg()
        cheesestakes3slg()
        cheesestakes4slg()
        cheesestakes5slg()
        cheesestakes6slg()
        cheesestakes7slg()
        cheesestakes8slg()
        cheesestakes9slg()
        cheesestakes1ops()
        cheesestakes2ops()
        cheesestakes3ops()
        cheesestakes4ops()
        cheesestakes5ops()
        cheesestakes6ops()
        cheesestakes7ops()
        cheesestakes8ops()
        cheesestakes9ops()
    elif Hteam == ("sheet 5"):
        import pandas as pd
        df = pd.read_csv("sheet5.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
                # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        elif (homestarterposition == ("six")
              or homestarterposition == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += 5
            # Saving Runs
            df.loc[5, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homestarterks
            # Saving hits
            df.loc[5, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homestarterwalks
            df.loc[5, 'Hr'] += homestarterhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("eleven")
            or homereliefposition1 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[10, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homereliefks
            # Saving hits
            df.loc[10, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homereliefwalks
            df.loc[10, 'Hr'] += homereliefhrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("eleven")
            or homereliefposition2 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[10, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[10, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homerelief2walks
            df.loc[10, 'Hr'] += homerelief2hrallowed
            df.to_csv("sheet5.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("eleven")
            or homereliefposition3 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief3walks
                df.loc[10, 'Hr'] += homerelief3hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Third relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("eleven")
            or homereliefposition4 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief4walks
                df.loc[10, 'Hr'] += homerelief4hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("eleven")
            or homereliefposition5 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief5walks
                df.loc[10, 'Hr'] += homerelief5hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("sheet5.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("eleven")
            or homereliefposition6 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief6walks
                df.loc[10, 'Hr'] += homerelief6hrallowed
                df.to_csv("sheet5.csv", index=False)
        sheet51baa()
        sheet52baa()
        sheet53baa()
        sheet54baa()
        sheet55baa()
        sheet56baa()
        sheet57baa()
        sheet58baa()
        sheet59baa()
        sheet51obp()
        sheet52obp()
        sheet53obp()
        sheet54obp()
        sheet55obp()
        sheet56obp()
        sheet57obp()
        sheet58obp()
        sheet59obp()
        sheet51slg()
        sheet52slg()
        sheet53slg()
        sheet54slg()
        sheet55slg()
        sheet56slg()
        sheet57slg()
        sheet58slg()
        sheet59slg()
        sheet51ops()
        sheet52ops()
        sheet53ops()
        sheet54ops()
        sheet55ops()
        sheet56ops()
        sheet57ops()
        sheet58ops()
        sheet59ops()
    elif Hteam == ("monkeys"):
        import pandas as pd
        df = pd.read_csv("monkeys.csv")
        # Saving Names
        df.loc[0, 'Name'] = batter1name
        df.loc[1, 'Name'] = batter2name
        df.loc[2, 'Name'] = batter3name
        df.loc[3, 'Name'] = batter4name
        df.loc[4, 'Name'] = batter5name
        df.loc[5, 'Name'] = batter6name
        df.loc[6, 'Name'] = batter7name
        df.loc[7, 'Name'] = batter8name
        df.loc[8, 'Name'] = batter9name
        # Saving Hits
        df.loc[0, 'Hits'] += batter1hits
        df.loc[1, 'Hits'] += batter2hits
        df.loc[2, 'Hits'] += batter3hits
        df.loc[3, 'Hits'] += batter4hits
        df.loc[4, 'Hits'] += batter5hits
        df.loc[5, 'Hits'] += batter6hits
        df.loc[6, 'Hits'] += batter7hits
        df.loc[7, 'Hits'] += batter8hits
        df.loc[8, 'Hits'] += batter9hits
        # Saving Atbats
        df.loc[0, 'Atbats'] += batter1atbats
        df.loc[1, 'Atbats'] += batter2atbats
        df.loc[2, 'Atbats'] += batter3atbats
        df.loc[3, 'Atbats'] += batter4atbats
        df.loc[4, 'Atbats'] += batter5atbats
        df.loc[5, 'Atbats'] += batter6atbats
        df.loc[6, 'Atbats'] += batter7atbats
        df.loc[7, 'Atbats'] += batter8atbats
        df.loc[8, 'Atbats'] += batter9atbats
        # Saving Hrs
        df.loc[0, 'Hrs'] += batter1hr
        df.loc[1, 'Hrs'] += batter2hr
        df.loc[2, 'Hrs'] += batter3hr
        df.loc[3, 'Hrs'] += batter4hr
        df.loc[4, 'Hrs'] += batter5hr
        df.loc[5, 'Hrs'] += batter6hr
        df.loc[6, 'Hrs'] += batter7hr
        df.loc[7, 'Hrs'] += batter8hr
        df.loc[8, 'Hrs'] += batter9hr
        # Saving walks
        df.loc[0, 'Walks'] += batter1walks
        df.loc[1, 'Walks'] += batter2walks
        df.loc[2, 'Walks'] += batter3walks
        df.loc[3, 'Walks'] += batter4walks
        df.loc[4, 'Walks'] += batter5walks
        df.loc[5, 'Walks'] += batter6walks
        df.loc[6, 'Walks'] += batter7walks
        df.loc[7, 'Walks'] += batter8walks
        df.loc[8, 'Walks'] += batter9walks
        # Saving singles
        df.loc[0, '1bs'] += batter1singles
        df.loc[1, '1bs'] += batter2singles
        df.loc[2, '1bs'] += batter3singles
        df.loc[3, '1bs'] += batter4singles
        df.loc[4, '1bs'] += batter5singles
        df.loc[5, '1bs'] += batter6singles
        df.loc[6, '1bs'] += batter7singles
        df.loc[7, '1bs'] += batter8singles
        df.loc[8, '1bs'] += batter9singles
        # Saving doubles
        df.loc[0, '2bs'] += batter1doubles
        df.loc[1, '2bs'] += batter2doubles
        df.loc[2, '2bs'] += batter3doubles
        df.loc[3, '2bs'] += batter4doubles
        df.loc[4, '2bs'] += batter5doubles
        df.loc[5, '2bs'] += batter6doubles
        df.loc[6, '2bs'] += batter7doubles
        df.loc[7, '2bs'] += batter8doubles
        df.loc[8, '2bs'] += batter9doubles
        # Saving Triples
        df.loc[0, '3bs'] += batter1triples
        df.loc[1, '3bs'] += batter2triples
        df.loc[2, '3bs'] += batter3triples
        df.loc[3, '3bs'] += batter4triples
        df.loc[4, '3bs'] += batter5triples
        df.loc[5, '3bs'] += batter6triples
        df.loc[6, '3bs'] += batter7triples
        df.loc[7, '3bs'] += batter8triples
        df.loc[8, '3bs'] += batter9triples
        # Saving Strike Outs
        df.loc[0, 'So'] += batter1so
        df.loc[1, 'So'] += batter2so
        df.loc[2, 'So'] += batter3so
        df.loc[3, 'So'] += batter4so
        df.loc[4, 'So'] += batter5so
        df.loc[5, 'So'] += batter6so
        df.loc[6, 'So'] += batter7so
        df.loc[7, 'So'] += batter8so
        df.loc[8, 'So'] += batter9so
        # Saving RBI's
        df.loc[0, 'RBI'] += batter1rbi
        df.loc[1, 'RBI'] += batter2rbi
        df.loc[2, 'RBI'] += batter3rbi
        df.loc[3, 'RBI'] += batter4rbi
        df.loc[4, 'RBI'] += batter5rbi
        df.loc[5, 'RBI'] += batter6rbi
        df.loc[6, 'RBI'] += batter7rbi
        df.loc[7, 'RBI'] += batter8rbi
        df.loc[8, 'RBI'] += batter9rbi
        # Fielding stats
        df.loc[0, 'Opps'] += home2Bopps
        df.loc[0, 'Throwouts'] += home2Bthrowouts
        df.loc[1, 'Opps'] += home3Bopps
        df.loc[1, 'Throwouts'] += home3Bthrowouts
        df.loc[2, 'Opps'] += homeSSopps
        df.loc[2, 'Throwouts'] += homeSSthrowouts
        df.loc[3, 'Opps'] += homeleftopps
        df.loc[3, 'Throwouts'] += homeleftthrowouts
        df.loc[4, 'Opps'] += homecenteropps
        df.loc[4, 'Throwouts'] += homecenterthrowouts
        df.loc[5, 'Opps'] += homerightopps
        df.loc[5, 'Throwouts'] += homerightthrowouts
        # First Pitcher
        if (homestarterposition == ("one")
            or homestarterposition == "1"):
            #Saving innings
            df.loc[0, 'Innings'] += 5
            # Saving Runs
            df.loc[0, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[0, 'Ks'] += homestarterks
            # Saving hits
            df.loc[0, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[0, 'pWalks'] += homestarterwalks
            df.loc[0, 'Hr'] += homestarterhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        elif (homestarterposition == ("two")
              or homestarterposition == "2"):
            #Saving innings
            df.loc[1, 'Innings'] += 5
            # Saving Runs
            df.loc[1, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[1, 'Ks'] += homestarterks
            # Saving hits
            df.loc[1, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[1, 'pWalks'] += homestarterwalks
            df.loc[1, 'Hr'] += homestarterhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        #Third starter
        elif (homestarterposition == ("three")
              or homestarterposition == "3"):
            #Saving innings
            df.loc[2, 'Innings'] += 5
            # Saving Runs
            df.loc[2, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[2, 'Ks'] += homestarterks
            # Saving hits
            df.loc[2, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[2, 'pWalks'] += homestarterwalks
            df.loc[2, 'Hr'] += homestarterhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        #Fourth starter
        elif (homestarterposition == ("four")
              or homestarterposition == "4"):
            #Saving innings
            df.loc[3, 'Innings'] += 5
            # Saving Runs
            df.loc[3, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[3, 'Ks'] += homestarterks
            # Saving hits
            df.loc[3, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[3, 'pWalks'] += homestarterwalks
            df.loc[3, 'Hr'] += homestarterhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        #Fifth starter
        elif (homestarterposition == ("five")
              or homestarterposition == "5"):
            #Saving innings
            df.loc[4, 'Innings'] += 5
            # Saving Runs
            df.loc[4, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[4, 'Ks'] += homestarterks
            # Saving hits
            df.loc[4, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[4, 'pWalks'] += homestarterwalks
            df.loc[4, 'Hr'] += homestarterhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        elif (homestarterposition == ("six")
              or homestarterposition == "6"):
            #Saving innings
            df.loc[5, 'Innings'] += 5
            # Saving Runs
            df.loc[5, 'Runs'] += homestarterrunsallowed
            # Saving Ks
            df.loc[5, 'Ks'] += homestarterks
            # Saving hits
            df.loc[5, 'pHits'] += homestarterhitsallowed
            # Saving walks
            df.loc[5, 'pWalks'] += homestarterwalks
            df.loc[5, 'Hr'] += homestarterhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # First relief pitcher
        if (homereliefposition1 == ("seven")
            or homereliefposition1 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[6, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homereliefks
            # Saving hits
            df.loc[6, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homereliefwalks
            df.loc[6, 'Hr'] += homereliefhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition1 == ("eight")
            or homereliefposition1 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[7, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homereliefks
            # Saving hits
            df.loc[7, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homereliefwalks
            df.loc[7, 'Hr'] += homereliefhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition1 == ("nine")
            or homereliefposition1 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[8, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homereliefks
            # Saving hits
            df.loc[8, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homereliefwalks
            df.loc[8, 'Hr'] += homereliefhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition1 == ("ten")
            or homereliefposition1 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[9, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homereliefks
            # Saving hits
            df.loc[9, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homereliefwalks
            df.loc[9, 'Hr'] += homereliefhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition1 == ("eleven")
            or homereliefposition1 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homereliefip
            # Saving Runs
            df.loc[10, 'Runs'] += homereliefrunsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homereliefks
            # Saving hits
            df.loc[10, 'pHits'] += homereliefhitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homereliefwalks
            df.loc[10, 'Hr'] += homereliefhrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (homereliefposition2 == ("seven")
            or homereliefposition2 == "7"):
            #Saving innings
            df.loc[6, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[6, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[6, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[6, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[6, 'pWalks'] += homerelief2walks
            df.loc[6, 'Hr'] += homerelief2hrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Second relief pitcher
        if (homereliefposition2 == ("eight")
            or homereliefposition2 == "8"):
            #Saving innings
            df.loc[7, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[7, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[7, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[7, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[7, 'pWalks'] += homerelief2walks
            df.loc[7, 'Hr'] += homerelief2hrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Third relief pitcher
        if (homereliefposition2 == ("nine")
            or homereliefposition2 == "9"):
            #Saving innings
            df.loc[8, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[8, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[8, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[8, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[8, 'pWalks'] += homerelief2walks
            df.loc[8, 'Hr'] += homerelief2hrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Fourth relief pitcher
        if (homereliefposition2 == ("ten")
            or homereliefposition2 == "10"):
            #Saving innings
            df.loc[9, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[9, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[9, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[9, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[9, 'pWalks'] += homerelief2walks
            df.loc[9, 'Hr'] += homerelief2hrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Fifth relief pitcher
        if (homereliefposition2 == ("eleven")
            or homereliefposition2 == "11"):
            #Saving innings
            df.loc[10, 'Innings'] += homerelief2ip
            # Saving Runs
            df.loc[10, 'Runs'] += homerelief2runsallowed
            # Saving Ks
            df.loc[10, 'Ks'] += homerelief2ks
            # Saving hits
            df.loc[10, 'pHits'] += homerelief2hitsallowed
            # Saving walks
            df.loc[10, 'pWalks'] += homerelief2walks
            df.loc[10, 'Hr'] += homerelief2hrallowed
            df.to_csv("monkeys.csv", index=False)
            #print(df)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (homereliefposition3 == ("seven")
            or homereliefposition3 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief3walks
                df.loc[6, 'Hr'] += homerelief3hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition3 == ("eight")
            or homereliefposition3 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief3walks
                df.loc[7, 'Hr'] += homerelief3hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition3 == ("nine")
            or homereliefposition3 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief3walks
                df.loc[8, 'Hr'] += homerelief3hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition3 == ("ten")
            or homereliefposition3 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief3walks
                df.loc[9, 'Hr'] += homerelief3hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition3 == ("eleven")
            or homereliefposition3 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief3ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief3runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief3ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief3hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief3walks
                df.loc[10, 'Hr'] += homerelief3hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (homereliefposition4 == ("seven")
            or homereliefposition4 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief4walks
                df.loc[6, 'Hr'] += homerelief4hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition4 == ("eight")
            or homereliefposition4 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief4walks
                df.loc[7, 'Hr'] += homerelief4hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Third relief pitcher
            if homereliefposition4 == ("nine"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief4walks
                df.loc[8, 'Hr'] += homerelief4hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition4 == ("ten")
            or homereliefposition4 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief4walks
                df.loc[9, 'Hr'] += homerelief4hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition4 == ("eleven")
            or homereliefposition4 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief4ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief4runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief4ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief4hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief4walks
                df.loc[10, 'Hr'] += homerelief4hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (homereliefposition5 == ("seven")
            or homereliefposition5 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief5walks
                df.loc[6, 'Hr'] += homerelief5hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition5 == ("eight")
            or homereliefposition5 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief5walks
                df.loc[7, 'Hr'] += homerelief5hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition5 == ("nine")
            or homereliefposition5 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief5walks
                df.loc[8, 'Hr'] += homerelief5hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition5 == ("ten")
            or homereliefposition5 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief5walks
                df.loc[9, 'Hr'] += homerelief5hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition5 == ("eleven")
            or homereliefposition5 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief5ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief5runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief5ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief5hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief5walks
                df.loc[10, 'Hr'] += homerelief5hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (homereliefposition6 == ("seven")
            or homereliefposition6 == "7"):
                #Saving innings
                df.loc[6, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[6, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[6, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[6, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[6, 'pWalks'] += homerelief6walks
                df.loc[6, 'Hr'] += homerelief6hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Second relief pitcher
            if (homereliefposition6 == ("eight")
            or homereliefposition6 == "8"):
                #Saving innings
                df.loc[7, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[7, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[7, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[7, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[7, 'pWalks'] += homerelief6walks
                df.loc[7, 'Hr'] += homerelief6hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Third relief pitcher
            if (homereliefposition6 == ("nine")
            or homereliefposition6 == "9"):
                #Saving innings
                df.loc[8, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[8, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[8, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[8, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[8, 'pWalks'] += homerelief6walks
                df.loc[8, 'Hr'] += homerelief6hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fourth relief pitcher
            if (homereliefposition6 == ("ten")
            or homereliefposition6 == "10"):
                #Saving innings
                df.loc[9, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[9, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[9, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[9, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[9, 'pWalks'] += homerelief6walks
                df.loc[9, 'Hr'] += homerelief6hrallowed
                df.to_csv("monkeys.csv", index=False)
                #print(df)
            # Fifth relief pitcher
            if (homereliefposition6 == ("eleven")
            or homereliefposition6 == "11"):
                #Saving innings
                df.loc[10, 'Innings'] += homerelief6ip
                # Saving Runs
                df.loc[10, 'Runs'] += homerelief6runsallowed
                # Saving Ks
                df.loc[10, 'Ks'] += homerelief6ks
                # Saving hits
                df.loc[10, 'pHits'] += homerelief6hitsallowed
                # Saving walks
                df.loc[10, 'pWalks'] += homerelief6walks
                df.loc[10, 'Hr'] += homerelief6hrallowed
                df.to_csv("monkeys.csv", index=False)
        monkeys1baa()
        monkeys2baa()
        monkeys3baa()
        monkeys4baa()
        monkeys5baa()
        monkeys6baa()
        monkeys7baa()
        monkeys8baa()
        monkeys9baa()
        monkeys1obp()
        monkeys2obp()
        monkeys3obp()
        monkeys4obp()
        monkeys5obp()
        monkeys6obp()
        monkeys7obp()
        monkeys8obp()
        monkeys9obp()
        monkeys1slg()
        monkeys2slg()
        monkeys3slg()
        monkeys4slg()
        monkeys5slg()
        monkeys6slg()
        monkeys7slg()
        monkeys8slg()
        monkeys9slg()
        monkeys1ops()
        monkeys2ops()
        monkeys3ops()
        monkeys4ops()
        monkeys5ops()
        monkeys6ops()
        monkeys7ops()
        monkeys8ops()
        monkeys9ops()
    #print(df)
def test2():
    consent2()
    if Ateam == ("brawlers"):
        import pandas as pd
        dfa = pd.read_csv("brawlers.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        #Second starter
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("six")
            or awayreliefposition1 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("six")
            or awayreliefposition2 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("brawlers.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("six")
            or awayreliefposition3 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("six")
            or awayreliefposition4 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("six")
            or awayreliefposition5 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("six")
            or awayreliefposition6 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("brawlers.csv", index=False)
                #print(dfa)
    elif Ateam == ("wardogs"):
        import pandas as pd
        dfa = pd.read_csv("wardogs.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        #Second starter
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("six")
            or awayreliefposition1 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("six")
            or awayreliefposition2 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("wardogs.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("six")
            or awayreliefposition3 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("six")
            or awayreliefposition4 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("six")
            or awayreliefposition5 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("six")
            or awayreliefposition6 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("wardogs.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("wardogs.csv", index=False)
    elif Ateam == ("manitees"):
        import pandas as pd
        dfa = pd.read_csv("manitees.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("six")
              or awaystarterposition == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += 5
            # Saving Runs
            dfa.loc[5, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[5, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awaystarterwalks
            dfa.loc[5, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("eleven")
            or awayreliefposition1 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayreliefwalks
            dfa.loc[10, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("eleven")
            or awayreliefposition2 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayrelief2walks
            dfa.loc[10, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("manitees.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("eleven")
            or awayreliefposition3 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief3walks
                dfa.loc[10, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("eleven")
            or awayreliefposition4 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief4walks
                dfa.loc[10, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("eleven")
            or awayreliefposition5 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief5walks
                dfa.loc[10, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("manitees.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("eleven")
            or awayreliefposition6 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief6walks
                dfa.loc[10, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("manitees.csv", index=False)
        manitees1baa()
        manitees2baa()
        manitees3baa()
        manitees4baa()
        manitees5baa()
        manitees6baa()
        manitees7baa()
        manitees8baa()
        manitees9baa()
        manitees1obp()
        manitees2obp()
        manitees3obp()
        manitees4obp()
        manitees5obp()
        manitees6obp()
        manitees7obp()
        manitees8obp()
        manitees9obp()
        manitees1slg()
        manitees2slg()
        manitees3slg()
        manitees4slg()
        manitees5slg()
        manitees6slg()
        manitees7slg()
        manitees8slg()
        manitees9slg()
        manitees1ops()
        manitees2ops()
        manitees3ops()
        manitees4ops()
        manitees5ops()
        manitees6ops()
        manitees7ops()
        manitees8ops()
        manitees9ops()
    elif Ateam == ("knights"):
        import pandas as pd
        dfa = pd.read_csv("knights.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        #Second starter
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("six")
            or awayreliefposition1 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("six")
            or awayreliefposition2 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("knights.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("six")
            or awayreliefposition3 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("six")
            or awayreliefposition4 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("six")
            or awayreliefposition5 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("six")
            or awayreliefposition6 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("knights.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("knights.csv", index=False)
        knights1baa()
        knights2baa()
        knights3baa()
        knights4baa()
        knights5baa()
        knights6baa()
        knights7baa()
        knights8baa()
        knights9baa()
        knights1obp()
        knights2obp()
        knights3obp()
        knights4obp()
        knights5obp()
        knights6obp()
        knights7obp()
        knights8obp()
        knights9obp()
        knights1slg()
        knights2slg()
        knights3slg()
        knights4slg()
        knights5slg()
        knights6slg()
        knights7slg()
        knights8slg()
        knights9slg()
        knights1ops()
        knights2ops()
        knights3ops()
        knights4ops()
        knights5ops()
        knights6ops()
        knights7ops()
        knights8ops()
        knights9ops()
    elif Ateam == ("arches"):
        import pandas as pd
        dfa = pd.read_csv("arches.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        #Second starter
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("six")
            or awayreliefposition1 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("six")
            or awayreliefposition2 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("arches.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("six")
            or awayreliefposition3 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("six")
            or awayreliefposition4 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("six")
            or awayreliefposition5 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("six")
            or awayreliefposition6 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("arches.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("arches.csv", index=False)
        arches1baa()
        arches2baa()
        arches3baa()
        arches4baa()
        arches5baa()
        arches6baa()
        arches7baa()
        arches8baa()
        arches9baa()
        arches1obp()
        arches2obp()
        arches3obp()
        arches4obp()
        arches5obp()
        arches6obp()
        arches7obp()
        arches8obp()
        arches9obp()
        arches1slg()
        arches2slg()
        arches3slg()
        arches4slg()
        arches5slg()
        arches6slg()
        arches7slg()
        arches8slg()
        arches9slg()
        arches1ops()
        arches2ops()
        arches3ops()
        arches4ops()
        arches5ops()
        arches6ops()
        arches7ops()
        arches8ops()
        arches9ops()
    elif Ateam == ("liberty"):
        import pandas as pd
        dfa = pd.read_csv("liberty.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("six")
              or awaystarterposition == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += 5
            # Saving Runs
            dfa.loc[5, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[5, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awaystarterwalks
            dfa.loc[5, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("eleven")
            or awayreliefposition1 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayreliefwalks
            dfa.loc[10, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("eleven")
            or awayreliefposition2 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayrelief2walks
            dfa.loc[10, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("liberty.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("eleven")
            or awayreliefposition3 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief3walks
                dfa.loc[10, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("eleven")
            or awayreliefposition4 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief4walks
                dfa.loc[10, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("eleven")
            or awayreliefposition5 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief5walks
                dfa.loc[10, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("liberty.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("eleven")
            or awayreliefposition6 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief6walks
                dfa.loc[10, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("liberty.csv", index=False)
        liberty1baa()
        liberty2baa()
        liberty3baa()
        liberty4baa()
        liberty5baa()
        liberty6baa()
        liberty7baa()
        liberty8baa()
        liberty9baa()
        liberty1obp()
        liberty2obp()
        liberty3obp()
        liberty4obp()
        liberty5obp()
        liberty6obp()
        liberty7obp()
        liberty8obp()
        liberty9obp()
        liberty1slg()
        liberty2slg()
        liberty3slg()
        liberty4slg()
        liberty5slg()
        liberty6slg()
        liberty7slg()
        liberty8slg()
        liberty9slg()
        liberty1ops()
        liberty2ops()
        liberty3ops()
        liberty4ops()
        liberty5ops()
        liberty6ops()
        liberty7ops()
        liberty8ops()
        liberty9ops()
    elif Ateam == ("blondes"):
        import pandas as pd
        dfa = pd.read_csv("blondes.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        #Second starter
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("six")
            or awayreliefposition1 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("six")
            or awayreliefposition2 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("blondes.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("six")
            or awayreliefposition3 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("six")
            or awayreliefposition4 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("six")
            or awayreliefposition5 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("six")
            or awayreliefposition6 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("blondes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("blondes.csv", index=False)
        blondes1baa()
        blondes2baa()
        blondes3baa()
        blondes4baa()
        blondes5baa()
        blondes6baa()
        blondes7baa()
        blondes8baa()
        blondes9baa()
        blondes1obp()
        blondes2obp()
        blondes3obp()
        blondes4obp()
        blondes5obp()
        blondes6obp()
        blondes7obp()
        blondes8obp()
        blondes9obp()
        blondes1slg()
        blondes2slg()
        blondes3slg()
        blondes4slg()
        blondes5slg()
        blondes6slg()
        blondes7slg()
        blondes8slg()
        blondes9slg()
        blondes1ops()
        blondes2ops()
        blondes3ops()
        blondes4ops()
        blondes5ops()
        blondes6ops()
        blondes7ops()
        blondes8ops()
        blondes9ops()
    elif Ateam == ("cheesestakes"):
        import pandas as pd
        dfa = pd.read_csv("cheesestakes.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        #Second starter
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            # Saving Hrs
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("six")
            or awayreliefposition1 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("six")
            or awayreliefposition2 == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[5, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[5, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[5, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            # Saving Hrs
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("cheesestakes.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("six")
            or awayreliefposition3 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("six")
            or awayreliefposition4 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("six")
            or awayreliefposition5 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("six")
            or awayreliefposition6 == "6"):
                #Saving innings
                dfa.loc[5, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[5, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[5, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[5, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[5, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[5, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                # Saving Hrs
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("cheesestakes.csv", index=False)
        cheesestakes1baa()
        cheesestakes2baa()
        cheesestakes3baa()
        cheesestakes4baa()
        cheesestakes5baa()
        cheesestakes6baa()
        cheesestakes7baa()
        cheesestakes8baa()
        cheesestakes9baa()
        cheesestakes1obp()
        cheesestakes2obp()
        cheesestakes3obp()
        cheesestakes4obp()
        cheesestakes5obp()
        cheesestakes6obp()
        cheesestakes7obp()
        cheesestakes8obp()
        cheesestakes9obp()
        cheesestakes1slg()
        cheesestakes2slg()
        cheesestakes3slg()
        cheesestakes4slg()
        cheesestakes5slg()
        cheesestakes6slg()
        cheesestakes7slg()
        cheesestakes8slg()
        cheesestakes9slg()
        cheesestakes1ops()
        cheesestakes2ops()
        cheesestakes3ops()
        cheesestakes4ops()
        cheesestakes5ops()
        cheesestakes6ops()
        cheesestakes7ops()
        cheesestakes8ops()
        cheesestakes9ops()
    elif Ateam == ("sheet 5"):
        import pandas as pd
        dfa = pd.read_csv("sheet5.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("six")
              or awaystarterposition == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += 5
            # Saving Runs
            dfa.loc[5, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[5, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awaystarterwalks
            dfa.loc[5, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("eleven")
            or awayreliefposition1 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayreliefwalks
            dfa.loc[10, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("eleven")
            or awayreliefposition2 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayrelief2walks
            dfa.loc[10, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("sheet5.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("eleven")
            or awayreliefposition3 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief3walks
                dfa.loc[10, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("eleven")
            or awayreliefposition4 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief4walks
                dfa.loc[10, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("eleven")
            or awayreliefposition5 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief5walks
                dfa.loc[10, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("sheet5.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("eleven")
            or awayreliefposition6 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief6walks
                dfa.loc[10, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("sheet5.csv", index=False)
        sheet51baa()
        sheet52baa()
        sheet53baa()
        sheet54baa()
        sheet55baa()
        sheet56baa()
        sheet57baa()
        sheet58baa()
        sheet59baa()
        sheet51obp()
        sheet52obp()
        sheet53obp()
        sheet54obp()
        sheet55obp()
        sheet56obp()
        sheet57obp()
        sheet58obp()
        sheet59obp()
        sheet51slg()
        sheet52slg()
        sheet53slg()
        sheet54slg()
        sheet55slg()
        sheet56slg()
        sheet57slg()
        sheet58slg()
        sheet59slg()
        sheet51ops()
        sheet52ops()
        sheet53ops()
        sheet54ops()
        sheet55ops()
        sheet56ops()
        sheet57ops()
        sheet58ops()
        sheet59ops()
    elif Ateam == ("monkeys"):
        import pandas as pd
        dfa = pd.read_csv("monkeys.csv")
        dfa.loc[0, 'Name'] = batter10name
        dfa.loc[1, 'Name'] = batter11name
        dfa.loc[2, 'Name'] = batter12name
        dfa.loc[3, 'Name'] = batter13name
        dfa.loc[4, 'Name'] = batter14name
        dfa.loc[5, 'Name'] = batter15name
        dfa.loc[6, 'Name'] = batter16name
        dfa.loc[7, 'Name'] = batter17name
        dfa.loc[8, 'Name'] = batter18name
        # Saving Hits
        dfa.loc[0, 'Hits'] += batter10hits
        dfa.loc[1, 'Hits'] += batter11hits
        dfa.loc[2, 'Hits'] += batter12hits
        dfa.loc[3, 'Hits'] += batter13hits
        dfa.loc[4, 'Hits'] += batter14hits
        dfa.loc[5, 'Hits'] += batter15hits
        dfa.loc[6, 'Hits'] += batter16hits
        dfa.loc[7, 'Hits'] += batter17hits
        dfa.loc[8, 'Hits'] += batter18hits
        # Saving Atbats
        dfa.loc[0, 'Atbats'] += batter10atbats
        dfa.loc[1, 'Atbats'] += batter11atbats
        dfa.loc[2, 'Atbats'] += batter12atbats
        dfa.loc[3, 'Atbats'] += batter13atbats
        dfa.loc[4, 'Atbats'] += batter14atbats
        dfa.loc[5, 'Atbats'] += batter15atbats
        dfa.loc[6, 'Atbats'] += batter16atbats
        dfa.loc[7, 'Atbats'] += batter17atbats
        dfa.loc[8, 'Atbats'] += batter18atbats
        # Saving Hrs
        dfa.loc[0, 'Hrs'] += batter10hr
        dfa.loc[1, 'Hrs'] += batter11hr
        dfa.loc[2, 'Hrs'] += batter12hr
        dfa.loc[3, 'Hrs'] += batter13hr
        dfa.loc[4, 'Hrs'] += batter14hr
        dfa.loc[5, 'Hrs'] += batter15hr
        dfa.loc[6, 'Hrs'] += batter16hr
        dfa.loc[7, 'Hrs'] += batter17hr
        dfa.loc[8, 'Hrs'] += batter18hr
        # Saving walks
        dfa.loc[0, 'Walks'] += batter10walks
        dfa.loc[1, 'Walks'] += batter11walks
        dfa.loc[2, 'Walks'] += batter12walks
        dfa.loc[3, 'Walks'] += batter13walks
        dfa.loc[4, 'Walks'] += batter14walks
        dfa.loc[5, 'Walks'] += batter15walks
        dfa.loc[6, 'Walks'] += batter16walks
        dfa.loc[7, 'Walks'] += batter17walks
        dfa.loc[8, 'Walks'] += batter18walks
        # Saving singles
        dfa.loc[0, '1bs'] += batter10singles
        dfa.loc[1, '1bs'] += batter11singles
        dfa.loc[2, '1bs'] += batter12singles
        dfa.loc[3, '1bs'] += batter13singles
        dfa.loc[4, '1bs'] += batter14singles
        dfa.loc[5, '1bs'] += batter15singles
        dfa.loc[6, '1bs'] += batter16singles
        dfa.loc[7, '1bs'] += batter17singles
        dfa.loc[8, '1bs'] += batter18singles
        # Saving doubles
        dfa.loc[0, '2bs'] += batter10doubles
        dfa.loc[1, '2bs'] += batter11doubles
        dfa.loc[2, '2bs'] += batter12doubles
        dfa.loc[3, '2bs'] += batter13doubles
        dfa.loc[4, '2bs'] += batter14doubles
        dfa.loc[5, '2bs'] += batter15doubles
        dfa.loc[6, '2bs'] += batter16doubles
        dfa.loc[7, '2bs'] += batter17doubles
        dfa.loc[8, '2bs'] += batter18doubles
        # Saving Triples
        dfa.loc[0, '3bs'] += batter10triples
        dfa.loc[1, '3bs'] += batter11triples
        dfa.loc[2, '3bs'] += batter12triples
        dfa.loc[3, '3bs'] += batter13triples
        dfa.loc[4, '3bs'] += batter14triples
        dfa.loc[5, '3bs'] += batter15triples
        dfa.loc[6, '3bs'] += batter16triples
        dfa.loc[7, '3bs'] += batter17triples
        dfa.loc[8, '3bs'] += batter18triples
        # Saving Strike Outs
        dfa.loc[0, 'So'] += batter10so
        dfa.loc[1, 'So'] += batter11so
        dfa.loc[2, 'So'] += batter12so
        dfa.loc[3, 'So'] += batter13so
        dfa.loc[4, 'So'] += batter14so
        dfa.loc[5, 'So'] += batter15so
        dfa.loc[6, 'So'] += batter16so
        dfa.loc[7, 'So'] += batter17so
        dfa.loc[8, 'So'] += batter18so
        # Saving RBI's
        dfa.loc[0, 'RBI'] += batter10rbi
        dfa.loc[1, 'RBI'] += batter11rbi
        dfa.loc[2, 'RBI'] += batter12rbi
        dfa.loc[3, 'RBI'] += batter13rbi
        dfa.loc[4, 'RBI'] += batter14rbi
        dfa.loc[5, 'RBI'] += batter15rbi
        dfa.loc[6, 'RBI'] += batter16rbi
        dfa.loc[7, 'RBI'] += batter17rbi
        dfa.loc[8, 'RBI'] += batter18rbi
        # Fielding stats
        dfa.loc[0, 'Opps'] += away2Bopps
        dfa.loc[0, 'Throwouts'] += away2Bthrowouts
        dfa.loc[1, 'Opps'] += away3Bopps
        dfa.loc[1, 'Throwouts'] += away3Bthrowouts
        dfa.loc[2, 'Opps'] += awaySSopps
        dfa.loc[2, 'Throwouts'] += awaySSthrowouts
        dfa.loc[3, 'Opps'] += awayleftopps
        dfa.loc[3, 'Throwouts'] += awayleftthrowouts
        dfa.loc[4, 'Opps'] += awaycenteropps
        dfa.loc[4, 'Throwouts'] += awaycenterthrowouts
        dfa.loc[5, 'Opps'] += awayrightopps
        dfa.loc[5, 'Throwouts'] += awayrightthrowouts
                # First Pitcher
        if (awaystarterposition == ("one")
            or awaystarterposition == "1"):
            #Saving innings
            dfa.loc[0, 'Innings'] += 5
            # Saving Runs
            dfa.loc[0, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[0, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[0, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[0, 'pWalks'] += awaystarterwalks
            dfa.loc[0, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("two")
              or awaystarterposition == "2"):
            #Saving innings
            dfa.loc[1, 'Innings'] += 5
            # Saving Runs
            dfa.loc[1, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[1, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[1, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[1, 'pWalks'] += awaystarterwalks
            dfa.loc[1, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        #Third starter
        elif (awaystarterposition == ("three")
              or awaystarterposition == "3"):
            #Saving innings
            dfa.loc[2, 'Innings'] += 5
            # Saving Runs
            dfa.loc[2, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[2, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[2, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[2, 'pWalks'] += awaystarterwalks
            dfa.loc[2, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        #Fourth starter
        elif (awaystarterposition == ("four")
              or awaystarterposition == "4"):
            #Saving innings
            dfa.loc[3, 'Innings'] += 5
            # Saving Runs
            dfa.loc[3, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[3, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[3, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[3, 'pWalks'] += awaystarterwalks
            dfa.loc[3, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        #Fifth starter
        elif (awaystarterposition == ("five")
              or awaystarterposition == "5"):
            #Saving innings
            dfa.loc[4, 'Innings'] += 5
            # Saving Runs
            dfa.loc[4, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[4, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[4, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[4, 'pWalks'] += awaystarterwalks
            dfa.loc[4, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        elif (awaystarterposition == ("six")
              or awaystarterposition == "6"):
            #Saving innings
            dfa.loc[5, 'Innings'] += 5
            # Saving Runs
            dfa.loc[5, 'Runs'] += awaystarterrunsallowed
            # Saving Ks
            dfa.loc[5, 'Ks'] += awaystarterks
            # Saving hits
            dfa.loc[5, 'pHits'] += awaystarterhitsallowed
            # Saving walks
            dfa.loc[5, 'pWalks'] += awaystarterwalks
            dfa.loc[5, 'Hr'] += awaystarterhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # First relief pitcher
        if (awayreliefposition1 == ("seven")
            or awayreliefposition1 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayreliefwalks
            dfa.loc[6, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition1 == ("eight")
            or awayreliefposition1 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayreliefwalks
            dfa.loc[7, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition1 == ("nine")
            or awayreliefposition1 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayreliefwalks
            dfa.loc[8, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition1 == ("ten")
            or awayreliefposition1 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayreliefwalks
            dfa.loc[9, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition1 == ("eleven")
            or awayreliefposition1 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayreliefip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayreliefrunsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayreliefks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayreliefhitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayreliefwalks
            dfa.loc[10, 'Hr'] += awayreliefhrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Second reliever to enter the game
        #
        # First relief pitcher
        if (awayreliefposition2 == ("seven")
            or awayreliefposition2 == "7"):
            #Saving innings
            dfa.loc[6, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[6, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[6, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[6, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[6, 'pWalks'] += awayrelief2walks
            dfa.loc[6, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Second relief pitcher
        if (awayreliefposition2 == ("eight")
            or awayreliefposition2 == "8"):
            #Saving innings
            dfa.loc[7, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[7, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[7, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[7, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[7, 'pWalks'] += awayrelief2walks
            dfa.loc[7, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Third relief pitcher
        if (awayreliefposition2 == ("nine")
            or awayreliefposition2 == "9"):
            #Saving innings
            dfa.loc[8, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[8, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[8, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[8, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[8, 'pWalks'] += awayrelief2walks
            dfa.loc[8, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Fourth relief pitcher
        if (awayreliefposition2 == ("ten")
            or awayreliefposition2 == "10"):
            #Saving innings
            dfa.loc[9, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[9, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[9, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[9, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[9, 'pWalks'] += awayrelief2walks
            dfa.loc[9, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Fifth relief pitcher
        if (awayreliefposition2 == ("eleven")
            or awayreliefposition2 == "11"):
            #Saving innings
            dfa.loc[10, 'Innings'] += awayrelief2ip
            # Saving Runs
            dfa.loc[10, 'Runs'] += awayrelief2runsallowed
            # Saving Ks
            dfa.loc[10, 'Ks'] += awayrelief2ks
            # Saving hits
            dfa.loc[10, 'pHits'] += awayrelief2hitsallowed
            # Saving walks
            dfa.loc[10, 'pWalks'] += awayrelief2walks
            dfa.loc[10, 'Hr'] += awayrelief2hrallowed
            dfa.to_csv("monkeys.csv", index=False)
            #print(dfa)
        # Third reliever to enter the game
        #
        # First relief pitcher
        if (extrainnings >= 10.5):
            if (awayreliefposition3 == ("seven")
            or awayreliefposition3 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief3walks
                dfa.loc[6, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition3 == ("eight")
            or awayreliefposition3 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief3walks
                dfa.loc[7, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition3 == ("nine")
            or awayreliefposition3 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief3walks
                dfa.loc[8, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition3 == ("ten")
            or awayreliefposition3 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief3walks
                dfa.loc[9, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition3 == ("eleven")
            or awayreliefposition3 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief3ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief3runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief3ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief3hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief3walks
                dfa.loc[10, 'Hr'] += awayrelief3hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fourth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 13.5):
            if (awayreliefposition4 == ("seven")
            or awayreliefposition4 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief4walks
                dfa.loc[6, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition4 == ("eight")
            or awayreliefposition4 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief4walks
                dfa.loc[7, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition4 == ("nine")
            or awayreliefposition4 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief4walks
                dfa.loc[8, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition4 == ("ten")
            or awayreliefposition4 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief4walks
                dfa.loc[9, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition4 == ("eleven")
            or awayreliefposition4 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief4ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief4runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief4ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief4hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief4walks
                dfa.loc[10, 'Hr'] += awayrelief4hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fifth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 16.5):
            if (awayreliefposition5 == ("seven")
            or awayreliefposition5 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief5walks
                dfa.loc[6, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition5 == ("eight")
            or awayreliefposition5 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief5walks
                dfa.loc[7, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition5 == ("nine")
            or awayreliefposition5 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief5walks
                dfa.loc[8, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition5 == ("ten")
            or awayreliefposition5 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief5walks
                dfa.loc[9, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition5 == ("eleven")
            or awayreliefposition5 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief5ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief5runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief5ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief5hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief5walks
                dfa.loc[10, 'Hr'] += awayrelief5hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Sixth reliever to enter the game
            #
            # First relief pitcher
        if (extrainnings >= 19.5):
            if (awayreliefposition6 == ("seven")
            or awayreliefposition6 == "7"):
                #Saving innings
                dfa.loc[6, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[6, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[6, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[6, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[6, 'pWalks'] += awayrelief6walks
                dfa.loc[6, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Second relief pitcher
            if (awayreliefposition6 == ("eight")
            or awayreliefposition6 == "8"):
                #Saving innings
                dfa.loc[7, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[7, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[7, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[7, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[7, 'pWalks'] += awayrelief6walks
                dfa.loc[7, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Third relief pitcher
            if (awayreliefposition6 == ("nine")
            or awayreliefposition6 == "9"):
                #Saving innings
                dfa.loc[8, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[8, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[8, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[8, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[8, 'pWalks'] += awayrelief6walks
                dfa.loc[8, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fourth relief pitcher
            if (awayreliefposition6 == ("ten")
            or awayreliefposition6 == "10"):
                #Saving innings
                dfa.loc[9, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[9, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[9, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[9, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[9, 'pWalks'] += awayrelief6walks
                dfa.loc[9, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("monkeys.csv", index=False)
                #print(dfa)
            # Fifth relief pitcher
            if (awayreliefposition6 == ("eleven")
            or awayreliefposition6 == "11"):
                #Saving innings
                dfa.loc[10, 'Innings'] += awayrelief6ip
                # Saving Runs
                dfa.loc[10, 'Runs'] += awayrelief6runsallowed
                # Saving Ks
                dfa.loc[10, 'Ks'] += awayrelief6ks
                # Saving hits
                dfa.loc[10, 'pHits'] += awayrelief6hitsallowed
                # Saving walks
                dfa.loc[10, 'pWalks'] += awayrelief6walks
                dfa.loc[10, 'Hr'] += awayrelief6hrallowed
                dfa.to_csv("monkeys.csv", index=False)
        monkeys1baa()
        monkeys2baa()
        monkeys3baa()
        monkeys4baa()
        monkeys5baa()
        monkeys6baa()
        monkeys7baa()
        monkeys8baa()
        monkeys9baa()
        monkeys1obp()
        monkeys2obp()
        monkeys3obp()
        monkeys4obp()
        monkeys5obp()
        monkeys6obp()
        monkeys7obp()
        monkeys8obp()
        monkeys9obp()
        monkeys1slg()
        monkeys2slg()
        monkeys3slg()
        monkeys4slg()
        monkeys5slg()
        monkeys6slg()
        monkeys7slg()
        monkeys8slg()
        monkeys9slg()
        monkeys1ops()
        monkeys2ops()
        monkeys3ops()
        monkeys4ops()
        monkeys5ops()
        monkeys6ops()
        monkeys7ops()
        monkeys8ops()
        monkeys9ops()
    #print(dfa)
def consent():
    global consenting
    consenting = input("Export?")
    if consenting == ("n"):
        exit()
    else:
        pass
def consent2():
    if consenting == ("n"):
        exit()
    else:
        pass
inning()
