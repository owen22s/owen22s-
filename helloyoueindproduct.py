from ast import If
import time
import os
repeat = True
while repeat == True:
    antwoord1=input("Hallo welkom bij deze tekst based applicatie! In deze applicatie speel je als vluchteling uit Syrië waarin je keuzes moet maken. Je hoort allemaal knallen om jou.  Jouw doel is om een veilig te zijn. Ga je jouw familie redden (type FAM) of red je eerst jezelf(type JEZ)? (Dit programma is bedoeld voor educatieve doel einden.) ")
    if antwoord1 == 'FAM': 
        os.system('cls')
        antwoord2=input("Je kiest ervoor om samen met je familie te vluchten. Je stapt samen met je familie het huis uit. Je hoort een enorme knal achter je. BOEEEEEEEEEEM!! Je huis is opgeblazen. Samen met je familie ga je op zoek naar een plek om te schuilen. Je komt onderweg een bus tegen, niet wetend van wie deze is en waar het vandaan komt. Stap je samen met je familie (type BUS) in of blijf je verder zoeken naar een schuilplaats?(type SCHUIL)")
        if antwoord2 == 'SCHUIL':
            os.system('cls')
            antwoord4 = input("je hebt besloten om te schuilen. De bus zag er erg verdacht uit en ja hoor nog geen 2 minuten nadat je had besloten om de bus niet te nemen hoor je een keiharde explosie. Je hoopt maar dat je snel een goeie schuilplaats vindt. Je ziet een grot het ziet er gevaarlijk uit maar wel vellig. Ga je naar de grot (type GROT) of zoek je verder? type (VERDER)")
            if antwoord4 =='GROT':
                print("je hebt besloten om in de grot te schuilen. Het is erg donker en je hebt geen licht. Het stinkt het is erg vies. Je familie is er moe na jullie vlucht. Je doet je best om het moraal hoog te houden. Maar je weet zelf ook dat het niet beter gaat worden. Tenminste niet snel. Je hebt het koud en je familie ook. Jullie hebben geen water geen eten en geen hoop. Je wordt ziek en sterft in de grot net als je familie. Je bent dood.")
                time.sleep(10)
                opnieuw = input(" wil je nog een keer door het verhaal gaan?")
                if opnieuw == 'nee':
                    repeat = False
                    os.system('cls')
            if antwoord4 =='VERDER':
                os.system('cls')
                print(" je gaat verder lopen geen idee naar waar je heen gaat. Het is erg warm en je hebt geen water je raakt uit gedroogd en sterft aan uitdroging. Je bent dood. ")
                time.sleep(3)
            opnieuw = input(" wil je nog een keer door het verhaal gaan?")
            if opnieuw == 'nee':
                repeat = False
                os.system('cls')
        elif antwoord2 == 'BUS':
            os.system('cls')
            antwoord5 = input("Je stapt de bus in en kunt eindelijk met je familie uit Syrië vluchten. Ga je naar Rusland (type RUS) of Brazilië? (type BRA)")
            if antwoord5 == 'BRA':
                os.system('cls')
                antwoord6=input("je hebt besloten om met de bus naar het vliegveld te gaan om een vliegtuig naar Brazilië na heel veel geld en heel lang in het vliegtuig te zitten ben je dan eindelijk in Brazilië maar je begrijpt helemaal niks van de letter daar en je geld is ook op dus je kan nergens slapen behalve op straat je familie heeft honger en je zoon is ziek. Je ziet een man met een hele grote portemonnee. Steel jij zijn geld (type STEEL) of slaap je op straat (type STRAAT)?")
                if antwoord6 == 'STEEL':
                    os.system('cls')
                    print("je hebt gekozen om de man zijn portemonnee te stelen je volgt de man naar zijn huis terwijl hij zijn huissleutel valt zijn portemonnee op de grond. Hij stapt binnen in zijn huis en dan hoor je dit achter je Olá senhor o que você está fazendo? Je begrijpt niet wat hij zegt maar het klinkt niet goed. Hij schreeuwt tegen je allemaal woorden die je niet begrijp je wordt meegenomen naar het braziliaanse politie bureau. En word daar vast gehouden Je weet niet waar je famillie is en je bent erg bang. Maar je hebt wel eten en water. Dus het kon slechter gaan. je zit vast. einde.")
                    time.sleep(5)
                    opnieuw = input("wil je nog een keer door het verhaal heen?")
                    if opnieuw == 'nee':
                        repeat = False
                        os.system('cls')
                if antwoord6 == 'STRAAT':
                    os.system('cls')
                    print("je kiest er voor om de portomonee niet te stelen maar daarom heb je geen slaap plek nu en je moet op straat slapen maar je gaat dood van de hitte op straat. ")
            elif antwoord5 == 'RUS':
                print(" je hebt besloten om met de bus helemaal naar Rusland te rijden en je komt daaraan bij de grenswachter ze kijken naar je paspoort en ze nemen je mee je hebt geen idee waarheen en je kan niemand verstaan je raakt je familie kwijt en je wordt gebracht naar Russische mijn en daar moet je grondstoffen hakken tot je er dood bij neervalt")
    elif antwoord1 == 'JEZ':
        os.system('cls')
        antwoord3=input("In alle haast heb je niet je familie mee kunnen nemen. Je beseft je dat niks je meer in dit land houdt. En besluit te vluchten. Je hebt geen geld en geen tijd je ziet 2 opties voor je. Je steelt wat geld(type GELD) of je steelt een boot.(type BOOT) ")
        os.system('cls')
        if antwoord3 == 'BOOT':
            antwoord8 = input("Je hebt besloten om een boot te stelen. Je ziet 2 logische plekken voor jou om heen te vluchten: Griekenland (type GRIEK) of Italië(type ITAL). Waar ga je heen? ")
            if antwoord8 == 'ITAL':
                print("je bent met je boot naar Italië gegaan. Je kiest daar om met een vliegtuig te gaan. Je hebt besloten om voor je geld met het vliegtuig te gaan. Je neemt alles mee wat je kan maar het past niet en je moet je spullen achterlaten. Je bent benieuwd waar je heen gaat. ")
                time.sleep(5)
                os.system('cls')
                print("Het is je gelukt om te reizen naar Nederland je bent erg blij maar je vind het wel erg spannend om helemaal naar de anderenkant van de wereld te gaan. Je kent er niemand en je hoopt dat je goed ontvangen wordt. Je moet van de Nederlandse staat een inburgering programma volgen en als je dat niet af hebt binnen 3 jaar dan word je weer teruggestuurd je kan ook de taal niet maar die ga jij tijdens dat programma leren. Je wordt in een noodgebouw geplaats maar je hebt tenminste een bed  ")
                time.sleep(7)
                opnieuw = input("wil je nog een keer door het verhaal heen?")
                if opnieuw == 'nee':
                        repeat = False
                        os.system('cls')
                if antwoord8 == 'GRIEK':
                 antwoord9 = input("Je bent met boot naar Griekenland gevaren en je kiest daarna met een vliegtuig te gaan naar Brazilië. Op het moment dat je aan bent gekomen kom je erachter dat je geen geld hebt weet je niet wat je moet doen. Je ziet een man met wat geld in zijn portemonnee. Steel jij zijn geld (type STEEL) of slaap je op straat (type STRAAT)? ")
                if antwoord9 == 'STRAAT':
                    print("je kiest er voor om de portomonee niet te stelen maar daarom heb je geen slaap plek nu en je moet op straat slapen maar je gaat dood van de hitte op straat.")
                    time.sleep(6)
                    os.system('cls')
                    if antwoord9 == 'STEEL':
                        print("je hebt gekozen om de man zijn portemonnee te stelen je volgt de man naar zijn huis terwijl hij zijn huissleutel valt zijn portemonnee op de grond. Hij stapt binnen in zijn huis en dan hoor je dit achter je Olá senhor o que você está fazendo? Je begrijpt niet wat hij zegt maar het klinkt niet goed. Hij schreeuwt tegen je allemaal woorden die je niet begrijp je wordt meegenomen naar het braziliaanse politie bureau. En word daar vast gehouden en je bent erg bang. Maar je hebt wel eten en water. Dus het kon slechter gaan. ")
                        time.sleep(8)
                        opnieuw = input("wil je nog een keer door het verhaal heen?")
                        if opnieuw == 'nee':
                         repeat = False
                         os.system('cls')
        if antwoord3 == 'GELD':
            antwoord7 = input("Je ziet een koppel met 3 kinderen staan. De vader is even bezig met zijn kinderen en hij laat per ongeluk zijn geld vallen. Je pakt het geld die anderen mensen hebben dat geld toch niet nodig. Je ziet een auto staan die te koop staan. Maar vliegtickets zijn goedkoper! Ga je met het vliegtuig (type VLIEG) of koop je de auto?(type AUTO) ")
            if antwoord7 =='VLIEG':
                print("Je hebt besloten om voor je geld met het vliegtuig te gaan. Je neemt alles mee wat je kan maar het past niet en je moet je spullen achterlaten. Je bent benieuwd waar je heen gaat. ")
                time.sleep(4)
                os.system('cls')
                print("Het is je gelukt om te reizen naar Nederland je bent erg blij maar je vind het wel erg spannend om helemaal naar de anderenkant van de wereld te gaan. Je kent er niemand en je hoopt dat je goed ontvangen wordt. Je moet van de Nederlandse staat een inburgering programma volgen en als je dat niet af hebt binnen 3 jaar dan word je weer teruggestuurd je kan ook de taal niet maar die ga jij tijdens dat programma leren. Je wordt in een noodgebouw geplaats maar je hebt tenminste een bed  ")
                time.sleep(10)
            if antwoord7 == 'AUTO':
                os.system('cls')
                antwoord10 = input("Je hebt besloten om een auto te kopen met je geld. Je besluit dat de beste plek waar je heen kan gaan Europa is. Je komt aan in Europa. Verkoop je jouw auto en ga je in een hotel(HOTEL) slapen of slaap je in je auto?(type AUTO)") 
                if antwoord10 == 'HOTEL':
                    os.system('cls')
                    print("je hebt besloten om je auto te verkopen en naar het hotel te gaan maar zodra je de deur open wilt doen zie je dat het helemaal donker is in het hotel. Op de deur staat een heel klein bordje waar “gesloten” op staat je doet je best om nog een plek te vinden waar je kan slapen maar het is te vergeefs. Je probeert op straat te slapen alleen het is te koud. Je bent dood. ")
                    opnieuw = input("wil je nog een keer door het verhaal heen?")
                    if opnieuw == 'nee':
                     repeat = False
                     
                if antwoord10 == 'AUTO':
                    os.system('cls')
                    print("Je valt in slaap in je auto maar je wordt niet meer wakker en dat komt door zuurstoftekort want je airco was stuk en er stond geen raam open ")
                    opnieuw = input("wil je nog een keer door het verhaal heen?")
                    if opnieuw == 'nee':
                     repeat = False
                     os.system("cls")
                     
                    
    else: print("error dit kan niet vul een geldig antwoord in.")
    time.sleep(2)