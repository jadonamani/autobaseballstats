ba = 0
bp = 0
bs = 0
pa = 0
ps = 0
fs = 0
ip = 0
atbats = 0
hits = 0
hr = 0
walks = 0
singles = 0
doubles = 0
triples = 0
hitsallowed = 0
walksallowed = 0
runsallowed = 0
Ks = 0
opps = 0
throwouts = 0
hrallowed = 0
rbi = 0
so = 0
homeleftopps = 0
homeleftthrowouts = 0
homecenteropps = 0
homecenterthrowouts = 0
homerightopps = 0
homerightthrowouts = 0
homeSSopps = 0
homeSSthrowouts = 0
home2Bopps = 0
home2Bthrowouts = 0
home3Bopps = 0
home3Bthrowouts = 0
awayleftopps = 0
awayleftthrowouts = 0
awaycenteropps = 0
awaycenterthrowouts = 0
awayrightopps = 0
awayrightthrowouts = 0
awaySSopps = 0
awaySSthrowouts = 0
away2Bopps = 0
away2Bthrowouts = 0
away3Bopps = 0
away3Bthrowouts = 0
Ateam = input("Away team?")
Hteam = input("Home team?")
def homepitcherrequest():
    global homepa, homeps, homeposition
    homepa = input("Home pitcher's accuracy?")
    homeps = input("Home pitcher's stuff")
def awaypitcherrequest():
    global awaypa, awayps, awayposition
    awaypa = input("Away pitcher's accuracy?")
    awayps = input("Away pitcher's stuff")
homepitcherrequest()
homestarterposition = input("Home pitcher position?")
awaypitcherrequest()
awaystarterposition = input("Away pitcher position?")
#consenting = input("Export?")
def homepitcher():
    global pa, ps, fs, homepa, homeps, homefs
    pa = homepa
    ps = homeps
def awaypitcher():
    global pa, ps, fs, awaypa, awayps, awayfs
    pa = awaypa
    ps = awayps
batter1atbats = 0
batter1hits = 0
batter1hr = 0
batter1walks = 0
batter1singles = 0
batter1doubles = 0
batter1triples = 0
batter1rbi = 0
batter1so = 0
batter2atbats = 0
batter2hits = 0
batter2hr = 0
batter2walks = 0
batter2singles = 0
batter2doubles = 0
batter2rbi = 0
batter2triples = 0
batter2so = 0
batter3atbats = 0
batter3hits = 0
batter3hr = 0
batter3walks = 0
batter3singles = 0
batter3doubles = 0
batter3triples = 0
batter3rbi = 0
batter3so = 0
batter4atbats = 0
batter4hits = 0
batter4hr = 0
batter4walks = 0
batter4singles = 0
batter4doubles = 0
batter4triples = 0
batter4rbi = 0
batter4so = 0
batter5atbats = 0
batter5hits = 0
batter5hr = 0
batter5walks = 0
batter5singles = 0
batter5doubles = 0
batter5triples = 0
batter5rbi = 0
batter5so = 0
batter6atbats = 0
batter6hits = 0
batter6hr = 0
batter6walks = 0
batter6singles = 0
batter6doubles = 0
batter6triples = 0
batter6rbi = 0
batter6so = 0
batter7atbats = 0
batter7hits = 0
batter7hr = 0
batter7walks = 0
batter7singles = 0
batter7doubles = 0
batter7triples = 0
batter7rbi = 0
batter7so = 0
batter8atbats = 0
batter8hits = 0
batter8hr = 0
batter8walks = 0
batter8singles = 0
batter8doubles = 0
batter8triples = 0
batter8rbi = 0
batter8so = 0
batter9atbats = 0
batter9hits = 0
batter9hr = 0
batter9walks = 0
batter9singles = 0
batter9doubles = 0
batter9triples = 0
batter9rbi = 0
batter9so = 0
batter10atbats = 0
batter10hits = 0
batter10hr = 0
batter10walks = 0
batter10singles = 0
batter10doubles = 0
batter10triples = 0
batter10rbi = 0
batter10so = 0
batter11atbats = 0
batter11hits = 0
batter11hr = 0
batter11walks = 0
batter11singles = 0
batter11doubles = 0
batter11triples = 0
batter11rbi = 0
batter11so = 0
batter12atbats = 0
batter12hits = 0
batter12hr = 0
batter12walks = 0
batter12singles = 0
batter12doubles = 0
batter12triples = 0
batter12rbi = 0
batter12so = 0
batter13atbats = 0
batter13hits = 0
batter13hr = 0
batter13walks = 0
batter13singles = 0
batter13doubles = 0
batter13triples = 0
batter13rbi = 0
batter13so = 0
batter14atbats = 0
batter14hits = 0
batter14hr = 0
batter14walks = 0
batter14singles = 0
batter14doubles = 0
batter14triples = 0
batter14rbi = 0
batter14so = 0
batter15atbats = 0
batter15hits = 0
batter15hr = 0
batter15walks = 0
batter15singles = 0
batter15doubles = 0
batter15triples = 0
batter15rbi = 0
batter15so = 0
batter16atbats = 0
batter16hits = 0
batter16hr = 0
batter16walks = 0
batter16singles = 0
batter16doubles = 0
batter16triples = 0
batter16rbi = 0
batter16so = 0
batter17atbats = 0
batter17hits = 0
batter17hr = 0
batter17walks = 0
batter17singles = 0
batter17doubles = 0
batter17triples = 0
batter17rbi = 0
batter17so = 0
batter18atbats = 0
batter18hits = 0
batter18hr = 0
batter18walks = 0
batter18singles = 0
batter18doubles = 0
batter18triples = 0
batter18rbi = 0
batter18so = 0
homestarterhitsallowed = 0
homestarterks = 0
homestarterwalks = 0
awaystarterhitsallowed = 0
awaystarterks = 0
awaystarterwalks = 0
homereliefhitsallowed = 0
homereliefks = 0
homereliefwalks = 0
awayreliefhitsallowed = 0
awayreliefks = 0
awayreliefwalks = 0
homerelief2hitsallowed = 0
homerelief2ks = 0
homerelief2walks = 0
awayrelief2hitsallowed = 0
awayrelief2ks = 0
awayrelief2walks = 0
homerelief3hitsallowed = 0
homerelief3ks = 0
homerelief3walks = 0
awayrelief3hitsallowed = 0
awayrelief3ks = 0
awayrelief3walks = 0
homerelief4hitsallowed = 0
homerelief4ks = 0
homerelief4walks = 0
awayrelief4hitsallowed = 0
awayrelief4ks = 0
awayrelief4walks = 0
homerelief5hitsallowed = 0
homerelief5ks = 0
homerelief5walks = 0
awayrelief5hitsallowed = 0
awayrelief5ks = 0
awayrelief5walks = 0
homerelief6hitsallowed = 0
homerelief6ks = 0
homerelief6walks = 0
awayrelief6hitsallowed = 0
awayrelief6ks = 0
awayrelief6walks = 0
homestarterrunsallowed = 0
awaystarterrunsallowed = 0
homereliefrunsallowed = 0
awayreliefrunsallowed = 0
homerelief2runsallowed = 0
awayrelief2runsallowed = 0
homerelief3runsallowed = 0
awayrelief3runsallowed = 0
homerelief4runsallowed = 0
awayrelief4runsallowed = 0
homerelief5runsallowed = 0
awayrelief5runsallowed = 0
homerelief6runsallowed = 0
awayrelief6runsallowed = 0
homereliefip = 0
homerelief2ip = 0
homerelief3ip = 0
homerelief4ip = 0
homerelief5ip = 0
homerelief6ip = 0
awayreliefip = 0
awayrelief2ip = 0
awayrelief3ip = 0
awayrelief4ip = 0
awayrelief5ip = 0
awayrelief6ip = 0
homestarterhrallowed = 0
awaystarterhrallowed = 0
homereliefhrallowed = 0
awayreliefhrallowed = 0
homerelief2hrallowed = 0
awayrelief2hrallowed = 0
homerelief3hrallowed = 0
awayrelief3hrallowed = 0
homerelief4hrallowed = 0
awayrelief4hrallowed = 0
homerelief5hrallowed = 0
awayrelief5hrallowed = 0
homerelief6hrallowed = 0
awayrelief6hrallowed = 0
battername = ("")
if Hteam ==("vulcans"):
    batter1name = ("Spock")
    batter1ba = 108
    batter1bp = 49
    batter1bs = 11

    batter2name = ("Horea")
    batter2ba = 72
    batter2bp = 43
    batter2bs = 12

    batter3name = ("Magdy")
    batter3ba = 81
    batter3bp = 52
    batter3bs = 12

    batter4name = ("Perce")
    batter4ba = 95
    batter4bp = 51
    batter4bs = 6

    batter5name = ("Rafiq")
    batter5ba = 104
    batter5bp = 30
    batter5bs = 8

    batter6name = ("Kirill")
    batter6ba = 84
    batter6bp = 37
    batter6bs = 7

    batter7name = ("Irune")
    batter7ba = 91
    batter7bp = 40
    batter7bs = 13

    batter8name = ("Satan")
    batter8ba = 98
    batter8bp = 36
    batter8bs = 14

    batter9name = ("Tawny")
    batter9ba = 82
    batter9bp = 51
    batter9bs = 9
elif Hteam==("brawlers"):
    batter1name = ("Logan")
    batter1ba = 109
    batter1bp = 37
    batter1bs = 5

    batter2name = ("Haley")
    batter2ba = 110
    batter2bp = 41
    batter2bs = 7

    batter3name = ("Katheryn")
    batter3ba = 109
    batter3bp = 39
    batter3bs = 13

    batter4name = ("Suzanna")
    batter4ba = 103
    batter4bp = 40
    batter4bs = 1

    batter5name = ("Haywood")
    batter5ba = 91
    batter5bp = 30
    batter5bs = 13

    batter6name = ("Shiori")
    batter6ba = 101
    batter6bp = 32
    batter6bs = 13

    batter7name = ("Sabella")
    batter7ba = 118
    batter7bp = 33
    batter7bs = 58

    batter8name = ("Duncan")
    batter8ba = 99
    batter8bp = 47
    batter8bs = 12

    batter9name = ("Luana")
    batter9ba = 105
    batter9bp = 42
    batter9bs = 3

    home2b = 13
    home3b = 10
    homess = 0
    homelf = 12
    homecf = 13
    homerf = 13
elif Hteam==("americans"):
    batter1name = ("Rowan")
    batter1ba = 110
    batter1bp = 30
    batter1bs = 5

    batter2name = ("Tino")
    batter2ba = 98
    batter2bp = 30
    batter2bs = 8

    batter3name = ("Tirto")
    batter3ba = 97
    batter3bp = 44
    batter3bs = 8

    batter4name = ("Aldith")
    batter4ba = 95
    batter4bp = 48
    batter4bs = 10

    batter5name = ("Arbore")
    batter5ba = 94
    batter5bp = 34
    batter5bs = 9

    batter6name = ("Ughi")
    batter6ba = 89
    batter6bp = 29
    batter6bs = 14

    batter7name = ("Robinson")
    batter7ba = 86
    batter7bp = 28
    batter7bs = 6

    batter8name = ("Leonardi")
    batter8ba = 71
    batter8bp = 38
    batter8bs = 5

    batter9name = ("Porcher")
    batter9ba = 65
    batter9bp = 60
    batter9bs = 19
elif Hteam ==("wardogs"):
    batter1name = ("Boffy")
    batter1ba = 120
    batter1bp = 50
    batter1bs = 15

    batter2name = ("Romi")
    batter2ba = 111
    batter2bp = 20
    batter2bs = 9

    batter3name = ("Roxana")
    batter3ba = 114
    batter3bp = 45
    batter3bs = 11

    batter4name = ("Anthony")
    batter4ba = 116
    batter4bp = 47
    batter4bs = 14

    batter5name = ("Nevada")
    batter5ba = 110
    batter5bp = 15
    batter5bs = 8

    batter6name = ("Jase")
    batter6ba = 96
    batter6bp = 37
    batter6bs = 11

    batter7name = ("Ainara")
    batter7ba = 92
    batter7bp = 43
    batter7bs = 4

    batter8name = ("Marina")
    batter8ba = 92
    batter8bp = 29
    batter8bs = 11

    batter9name = ("Reina")
    batter9ba = 69
    batter9bp = 19
    batter9bs = 14

    home2b = 11
    home3b = 9
    homess = 15
    homelf = 14
    homecf = 8
    homerf = 11
elif Hteam == ("empire state university"):
    batter1name = ("River")
    batter1ba = 69
    batter1bp = 26
    batter1bs = 3

    batter2name = ("Jenae")
    batter2ba = 86
    batter2bp = 35
    batter2bs = 5

    batter3name = ("Addie")
    batter3ba = 64
    batter3bp = 16
    batter3bs = 11

    batter4name = ("Tawnya")
    batter4ba = 85
    batter4bp = 35
    batter4bs = 10

    batter5name = ("Arleen")
    batter5ba = 71
    batter5bp = 20
    batter5bs = 6

    batter6name = ("Kyler")
    batter6ba = 64
    batter6bp = 16
    batter6bs = 11

    batter7name = ("Deacon")
    batter7ba = 84
    batter7bp = 16
    batter7bs = 8

    batter8name = ("Valeria")
    batter8ba = 85
    batter8bp = 20
    batter8bs = 1

    batter9name = ("Grover")
    batter9ba = 73
    batter9bp = 19
    batter9bs = 11
elif Hteam == ("bumblyburg college"):
    batter1name = ("Pikachu")
    batter1ba = 76
    batter1bp = 22
    batter1bs = 4

    batter2name = ("Beavis")
    batter2ba = 83
    batter2bp = 29
    batter2bs = 7

    batter3name = ("Leia")
    batter3ba = 80
    batter3bp = 15
    batter3bs = 11

    batter4name = ("Goku")
    batter4ba = 81
    batter4bp = 34
    batter4bs = 11

    batter5name = ("Castiel")
    batter5ba = 86
    batter5bp = 16
    batter5bs = 6

    batter6name = ("Elora")
    batter6ba = 81
    batter6bp = 25
    batter6bs = 10

    batter7name = ("Aang")
    batter7ba = 74
    batter7bp = 27
    batter7bs = 5

    batter8name = ("Anakin")
    batter8ba = 88
    batter8bp = 17
    batter8bs = 8

    batter9name = ("Django")
    batter9ba = 90
    batter9bp = 25
    batter9bs = 9

elif Hteam == ("tokyo academy"):
    batter1name = ("Sang-Hun")
    batter1ba = 74
    batter1bp = 22
    batter1bs = 9

    batter2name = ("Dae-Jung")
    batter2ba = 61
    batter2bp = 24
    batter2bs = 1

    batter3name = ("Shin'ichi")
    batter3ba = 67
    batter3bp = 17
    batter3bs = 4

    batter4name = ("Ryuu")
    batter4ba = 65
    batter4bp = 28
    batter4bs = 1

    batter5name = ("Kota")
    batter5ba = 83
    batter5bp = 21
    batter5bs = 5

    batter6name = ("Joo-Won")
    batter6ba = 88
    batter6bp = 22
    batter6bs = 7

    batter7name = ("Young")
    batter7ba = 70
    batter7bp = 24
    batter7bs = 1

    batter8name = ("Hyeon")
    batter8ba = 62
    batter8bp = 21
    batter8bs = 8

    batter9name = ("Masao")
    batter9ba = 89
    batter9bp = 32
    batter9bs = 6

elif Hteam ==("jerusalem college"):
    batter1name = ("Amit")
    batter1ba = 75
    batter1bp = 34
    batter1bs = 9

    batter2name = ("Ohad")
    batter2ba = 71
    batter2bp = 21
    batter2bs = 0

    batter3name = ("Debbora")
    batter3ba = 89
    batter3bp = 22
    batter3bs = 9

    batter4name = ("Ophir")
    batter4ba = 60
    batter4bp = 33
    batter4bs = 2

    batter5name = ("Gera")
    batter5ba = 74
    batter5bp = 23
    batter5bs = 3

    batter6name = ("Talia")
    batter6ba = 77
    batter6bp = 24
    batter6bs = 4

    batter7name = ("Cephas")
    batter7ba = 60
    batter7bp = 33
    batter7bs = 6

    batter8name = ("Jeremiah")
    batter8ba = 62
    batter8bp = 16
    batter8bs = 8

    batter9name = ("Cain")
    batter9ba = 72
    batter9bp = 28
    batter9bs = 9
elif Hteam==("manitees"):
    import csv
    with open ('maniteesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
elif Hteam==("cheesestakes"):
    import csv
    with open ('cheesestakesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
elif Hteam == ("sheet 5"):
    import csv
    with open ('sheet5specs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
elif Hteam == ("monkeys"):
    import csv
    with open ('monkeysspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
elif Hteam == ("blondes"):
    import csv
    with open ('blondesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
elif Hteam == ("arches"):
    import csv
    with open ('archesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
elif Hteam == ("liberty"):
    import csv
    with open ('libertyspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
elif Hteam == ("knights"):
    import csv
    with open ('knightsspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter1name =(row[0])
            if index == 1:
                batter1ba =(row[1])
            if index == 1:
                batter1bp =(row[2])
            if index == 1:
                batter1bs =(row[3])
            if index == 2:
                batter2name =(row[0])
            if index == 2:
                batter2ba =(row[1])
            if index == 2:
                batter2bp =(row[2])
            if index == 2:
                batter2bs =(row[3])
            if index == 3:
                batter3name =(row[0])
            if index == 3:
                batter3ba =(row[1])
            if index == 3:
                batter3bp =(row[2])
            if index == 3:
                batter3bs =(row[3])
            if index == 4:
                batter4name =(row[0])
            if index == 4:
                batter4ba =(row[1])
            if index == 4:
                batter4bp =(row[2])
            if index == 4:
                batter4bs =(row[3])
            if index == 5:
                batter5name =(row[0])
            if index == 5:
                batter5ba =(row[1])
            if index == 5:
                batter5bp =(row[2])
            if index == 5:
                batter5bs =(row[3])
            if index == 6:
                batter6name =(row[0])
            if index == 6:
                batter6ba =(row[1])
            if index == 6:
                batter6bp =(row[2])
            if index == 6:
                batter6bs =(row[3])
            if index == 7:
                batter7name =(row[0])
            if index == 7:
                batter7ba =(row[1])
            if index == 7:
                batter7bp =(row[2])
            if index == 7:
                batter7bs =(row[3])
            if index == 8:
                batter8name =(row[0])
            if index == 8:
                batter8ba =(row[1])
            if index == 8:
                batter8bp =(row[2])
            if index == 8:
                batter8bs =(row[3])
            if index == 9:
                batter9name =(row[0])
            if index == 9:
                batter9ba =(row[1])
            if index == 9:
                batter9bp =(row[2])
            if index == 9:
                batter9bs =(row[3])
            if index == 10:
                home2b =(row[1])
            if index == 11:
                home3b =(row[1])
            if index == 12:
                homess =(row[1])
            if index == 13:
                homelf =(row[1])
            if index == 14:
                homecf =(row[1])
            if index == 15:
                homerf =(row[1])
#Away teams--------------------------------------------------
if Ateam==("brawlers"):
    batter10name = ("Logan")
    batter10ba = 109
    batter10bp = 37
    batter10bs = 5

    batter11name = ("Haley")
    batter11ba = 110
    batter11bp = 41
    batter11bs = 7

    batter12name = ("Katheryn")
    batter12ba = 109
    batter12bp = 39
    batter12bs = 13

    batter13name = ("Suzanna")
    batter13ba = 103
    batter13bp = 40
    batter13bs = 1

    batter14name = ("Haywood")
    batter14ba = 91
    batter14bp = 30
    batter14bs = 13

    batter15name = ("Shiori")
    batter15ba = 101
    batter15bp = 32
    batter15bs = 13

    batter16name = ("Sabella")
    batter16ba = 118
    batter16bp = 33
    batter16bs = 58

    batter17name = ("Duncan")
    batter17ba = 99
    batter17bp = 47
    batter17bs = 12

    batter18name = ("Luana")
    batter18ba = 105
    batter18bp = 42
    batter18bs = 3

    away2b = 13
    away3b = 10
    awayss = 0
    awaylf = 12
    awaycf = 13
    awayrf = 13

elif Ateam==("vulcans"):
    batter10name = ("Spock")
    batter10ba = 108
    batter10bp = 49
    batter10bs = 11

    batter11name = ("Horea")
    batter11ba = 72
    batter11bp = 43
    batter11bs = 12

    batter12name = ("Magdy")
    batter12ba = 81
    batter12bp = 52
    batter12bs = 12

    batter13name = ("Perce")
    batter13ba = 95
    batter13bp = 51
    batter13bs = 6

    batter14name = ("Rafiq")
    batter14ba = 104
    batter14bp = 30
    batter14bs = 8

    batter15name = ("Kirill")
    batter15ba = 84
    batter15bp = 37
    batter15bs = 7

    batter16name = ("Irune")
    batter16ba = 91
    batter16bp = 40
    batter16bs = 13

    batter17name = ("Satan")
    batter17ba = 98
    batter17bp = 36
    batter17bs = 14

    batter18name = ("Tawny")
    batter18ba = 82
    batter18bp = 51
    batter18bs = 9
elif Ateam==("americans"):
    batter10name = ("Rowan")
    batter10ba = 110
    batter10bp = 30
    batter10bs = 5

    batter11name = ("Tino")
    batter11ba = 98
    batter11bp = 30
    batter11bs = 8

    batter12name = ("Tirto")
    batter12ba = 97
    batter12bp = 44
    batter12bs = 8

    batter13name = ("Aldith")
    batter13ba = 95
    batter13bp = 48
    batter13bs = 10

    batter14name = ("Arbore")
    batter14ba = 94
    batter14bp = 34
    batter14bs = 9

    batter15name = ("Ughi")
    batter15ba = 89
    batter15bp = 29
    batter15bs = 14

    batter16name = ("Robinson")
    batter16ba = 86
    batter16bp = 28
    batter16bs = 6

    batter17name = ("Leonardi")
    batter17ba = 71
    batter17bp = 38
    batter17bs = 5

    batter18name = ("Porcher")
    batter18ba = 65
    batter18bp = 60
    batter18bs = 19
elif Ateam == ("wardogs"):
    batter10name = ("Boffy")
    batter10ba = 120
    batter10bp = 50
    batter10bs = 15

    batter11name = ("Romi")
    batter11ba = 111
    batter11bp = 20
    batter11bs = 9

    batter12name = ("Roxana")
    batter12ba = 114
    batter12bp = 45
    batter12bs = 11

    batter13name = ("Anthony")
    batter13ba = 116
    batter13bp = 47
    batter13bs = 14

    batter14name = ("Nevada")
    batter14ba = 110
    batter14bp = 15
    batter14bs = 8

    batter15name = ("Jase")
    batter15ba = 96
    batter15bp = 37
    batter15bs = 11

    batter16name = ("Ainara")
    batter16ba = 92
    batter16bp = 43
    batter16bs = 4

    batter17name = ("Marina")
    batter17ba = 92
    batter17bp = 29
    batter17bs = 11

    batter18name = ("Reina")
    batter18ba = 69
    batter18bp = 19
    batter18bs = 14

    away2b = 11
    away3b = 9
    awayss = 15
    awaylf = 14
    awaycf = 8
    awayrf = 11
elif Ateam ==("empire state university"):
    batter10name = ("River")
    batter10ba = 69
    batter10bp = 26
    batter10bs = 3

    batter11name = ("Jenae")
    batter11ba = 86
    batter11bp = 35
    batter11bs = 4

    batter12name = ("Addie")
    batter12ba = 64
    batter12bp = 16
    batter12bs = 11

    batter13name = ("Tawnya")
    batter13ba = 85
    batter13bp = 35
    batter13bs = 10

    batter14name = ("Arleen")
    batter14ba = 71
    batter14bp = 20
    batter14bs = 6

    batter15name = ("Kyler")
    batter15ba = 64
    batter15bp = 16
    batter15bs = 11

    batter16name = ("Deacon")
    batter16ba = 84
    batter16bp = 16
    batter16bs = 8

    batter17name = ("Valeria")
    batter17ba = 85
    batter17bp = 18
    batter17bs = 1

    batter18name = ("Grover")
    batter18ba = 70
    batter18bp = 19
    batter18bs = 11

elif Ateam == ("bumblyburg college"):
    batter10name = ("Pikachu")
    batter10ba = 76
    batter10bp = 22
    batter10bs = 4

    batter11name = ("Beavis")
    batter11ba = 83
    batter11bp = 29
    batter11bs = 7

    batter12name = ("Leia")
    batter12ba = 80
    batter12bp = 15
    batter12bs = 11

    batter13name = ("Goku")
    batter13ba = 81
    batter13bp = 34
    batter13bs = 11

    batter14name = ("Castiel")
    batter14ba = 86
    batter14bp = 16
    batter14bs = 6

    batter15name = ("Elora")
    batter15ba = 81
    batter15bp = 25
    batter15bs = 10

    batter16name = ("Aang")
    batter16ba = 74
    batter16bp = 27
    batter16bs = 5

    batter17name = ("Anakin")
    batter17ba = 88
    batter17bp = 17
    batter17bs = 8

    batter18name = ("Django")
    batter18ba = 90
    batter18bp = 25
    batter18bs = 9

elif Ateam == ("tokyo academy"):
    batter10name = ("Sang-Hun")
    batter10ba = 74
    batter10bp = 22
    batter10bs = 9

    batter11name = ("Dae-Jung")
    batter11ba = 61
    batter11bp = 24
    batter11bs = 1

    batter12name = ("Shin'ichi")
    batter12ba = 67
    batter12bp = 17
    batter12bs = 4

    batter13name = ("Ryuu")
    batter13ba = 65
    batter13bp = 28
    batter13bs = 1

    batter14name = ("Kota")
    batter14ba = 83
    batter14bp = 21
    batter14bs = 5

    batter15name = ("Joo-Won")
    batter15ba = 88
    batter15bp = 22
    batter15bs = 7

    batter16name = ("Young")
    batter16ba = 70
    batter16bp = 24
    batter16bs = 1

    batter17name = ("Hyeon")
    batter17ba = 62
    batter17bp = 21
    batter17bs = 8

    batter18name = ("Masao")
    batter18ba = 89
    batter18bp = 32
    batter18bs = 6

elif Ateam==("jerusalem college"):
    batter10name = ("Amit")
    batter10ba = 72
    batter10bp = 34
    batter10bs = 9

    batter11name = ("Ohad")
    batter11ba = 71
    batter11bp = 21
    batter11bs = 0

    batter12name = ("Debbora")
    batter12ba = 89
    batter12bp = 22
    batter12bs = 9

    batter13name = ("Ophir")
    batter13ba = 60
    batter13bp = 33
    batter13bs = 2

    batter14name = ("Gera")
    batter14ba = 74
    batter14bp = 23
    batter14bs = 3

    batter15name = ("Talia")
    batter15ba = 77
    batter15bp = 24
    batter15bs = 4

    batter16name = ("Cephas")
    batter16ba = 60
    batter16bp = 33
    batter16bs = 6

    batter17name = ("Jeremiah")
    batter17ba = 62
    batter17bp = 16
    batter17bs = 8

    batter18name = ("Cain")
    batter18ba = 72
    batter18bp = 28
    batter18bs = 9
elif Ateam==("manitees"):
    import csv
    with open ('maniteesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
elif Ateam==("cheesestakes"):
    import csv
    with open ('cheesestakesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
elif Ateam == ("sheet 5"):
    import csv
    with open ('sheet5specs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
elif Ateam == ("monkeys"):
    import csv
    with open ('monkeysspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
elif Ateam == ("blondes"):
    import csv
    with open ('blondesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
elif Ateam == ("arches"):
    import csv
    with open ('archesspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
elif Ateam == ("liberty"):
    import csv
    with open ('libertyspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
elif Ateam == ("knights"):
    import csv
    with open ('knightsspecs.csv') as test:
        csv_reader = csv.reader(test)
        for index, row in enumerate(csv_reader):
            if index == 1:
                batter10name =(row[0])
            if index == 1:
                batter10ba =(row[1])
            if index == 1:
                batter10bp =(row[2])
            if index == 1:
                batter10bs =(row[3])
            if index == 2:
                batter11name =(row[0])
            if index == 2:
                batter11ba =(row[1])
            if index == 2:
                batter11bp =(row[2])
            if index == 2:
                batter11bs =(row[3])
            if index == 3:
                batter12name =(row[0])
            if index == 3:
                batter12ba =(row[1])
            if index == 3:
                batter12bp =(row[2])
            if index == 3:
                batter12bs =(row[3])
            if index == 4:
                batter13name =(row[0])
            if index == 4:
                batter13ba =(row[1])
            if index == 4:
                batter13bp =(row[2])
            if index == 4:
                batter13bs =(row[3])
            if index == 5:
                batter14name =(row[0])
            if index == 5:
                batter14ba =(row[1])
            if index == 5:
                batter14bp =(row[2])
            if index == 5:
                batter14bs =(row[3])
            if index == 6:
                batter15name =(row[0])
            if index == 6:
                batter15ba =(row[1])
            if index == 6:
                batter15bp =(row[2])
            if index == 6:
                batter15bs =(row[3])
            if index == 7:
                batter16name =(row[0])
            if index == 7:
                batter16ba =(row[1])
            if index == 7:
                batter16bp =(row[2])
            if index == 7:
                batter16bs =(row[3])
            if index == 8:
                batter17name =(row[0])
            if index == 8:
                batter17ba =(row[1])
            if index == 8:
                batter17bp =(row[2])
            if index == 8:
                batter17bs =(row[3])
            if index == 9:
                batter18name =(row[0])
            if index == 9:
                batter18ba =(row[1])
            if index == 9:
                batter18bp =(row[2])
            if index == 9:
                batter18bs =(row[3])
            if index == 10:
                away2b =(row[1])
            if index == 11:
                away3b =(row[1])
            if index == 12:
                awayss =(row[1])
            if index == 13:
                awaylf =(row[1])
            if index == 14:
                awaycf =(row[1])
            if index == 15:
                awayrf =(row[1])
#Batter switcher
def batter1():
    global ba
    global bp
    global bs
    global battername, atbats, hits, hr, walks, batter1atbats, batter1hits, batter1hr, batter1walks
    ba = batter1ba
    bp = batter1bp
    bs = batter1bs
    battername = batter1name
    batter1atbats += atbats
    atbats = 0
    batter1hits += hits
    hits = 0
    batter1hr += hr
    hr = 0
    batter1walks += walks
    walks = 0
def batter2():
    global ba
    global bp
    global bs
    global battername
    ba = batter2ba
    bp = batter2bp
    bs = batter2bs
    battername = batter2name
def batter3():
    global ba
    global bp
    global bs
    global battername
    ba = batter3ba
    bp = batter3bp
    bs = batter3bs
    battername = batter3name
def batter4():
    global ba
    global bp
    global bs
    global battername
    ba = batter4ba
    bp = batter4bp
    bs = batter4bs
    battername = batter4name
def batter5():
    global ba
    global bp
    global bs
    global battername
    ba = batter5ba
    bp = batter5bp
    bs = batter5bs
    battername = batter5name
def batter6():
    global ba
    global bp
    global bs
    global battername
    ba = batter6ba
    bp = batter6bp
    bs = batter6bs
    battername = batter6name
def batter7():
    global ba
    global bp
    global bs
    global battername
    ba = batter7ba
    bp = batter7bp
    bs = batter7bs
    battername = batter7name
def batter8():
    global ba
    global bp
    global bs
    global battername
    ba = batter8ba
    bp = batter8bp
    bs = batter8bs
    battername = batter8name
def batter9():
    global ba
    global bp
    global bs
    global battername
    ba = batter9ba
    bp = batter9bp
    bs = batter9bs
    battername = batter9name
def batter10():
    global ba
    global bp
    global bs
    global battername
    ba = batter10ba
    bp = batter10bp
    bs = batter10bs
    battername = batter10name
def batter11():
    global ba
    global bp
    global bs
    global battername
    ba = batter11ba
    bp = batter11bp
    bs = batter11bs
    battername = batter11name
def batter12():
    global ba
    global bp
    global bs
    global battername
    ba = batter12ba
    bp = batter12bp
    bs = batter12bs
    battername = batter12name
def batter13():
    global ba
    global bp
    global bs
    global battername
    ba = batter13ba
    bp = batter13bp
    bs = batter13bs
    battername = batter13name
def batter14():
    global ba
    global bp
    global bs
    global battername
    ba = batter14ba
    bp = batter14bp
    bs = batter14bs
    battername = batter14name
def batter15():
    global ba
    global bp
    global bs
    global battername
    ba = batter15ba
    bp = batter15bp
    bs = batter15bs
    battername = batter15name
def batter16():
    global ba
    global bp
    global bs
    global battername
    ba = batter16ba
    bp = batter16bp
    bs = batter16bs
    battername = batter16name
def batter17():
    global ba
    global bp
    global bs
    global battername
    ba = batter17ba
    bp = batter17bp
    bs = batter17bs
    battername = batter17name
def batter18():
    global ba
    global bp
    global bs
    global battername
    ba = batter18ba
    bp = batter18bp
    bs = batter18bs
    battername = batter18name
