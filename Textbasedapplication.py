# minstens 21 vragen
# 4 verschillende eindes
# 5 november af

#region Leeftijd controle-------------------------------------------------------------------------------------------------------------------
def Leeftijd_controler():
    while True:
        leeftijd = input("Omdat dit verhaal best heftige content kan bevatten, is dit alleen geschikt voor leeftijden boven de 16+, please vul je leeftijd hier in >>> ")
        try:
            controle = int(leeftijd)
            if controle >= 16 :
                print("Je mag het spel spelen, veel plezier! \nps. Wees eerlijk bij het invullen voor de beste ervaring")
                break
            else:
                print("Je mag het spel helaas niet spelen")
        except ValueError:
            print("Het moet een nummer zijn, please probeer het opnieuw")
    return controle
Leeftijd_controler()
#endregion

#region keuzes-------------------------------------------------------------------------------------------------------------------------------
import time

answer_A = ["A" , "a"]
answer_B = ["B" , "b"]
answer_C = ["C" , "c"]
benodigheden = ("Je kunt alleen kiezen tussen A/a, B/b en C/c.")

global paspoort
paspoort = False
#endregion
#--------------------------------------------------------------------------------------------------------------------------------------------
#region begin van het verhaallijn
def intro():
    print("""Je bent 16 jaar en werd uitgehuwelijkt aan de 36-jarige Yebar.
    Hij is de machtigste man in je geboorteland en is hoofdmilitair.
    Sinds je bij hem woonde, was je leven een hell.
    Hij heeft agressie problemen en je werd vaak mishandeld.
    Je was bang, maar besloot
    """)
    time.sleep(1)
    print("""Wat ga je doen? 
    A) Niets doen 
    B) Vluchten 
    C) Terug vechten?
    """)
    answer = input(">>> ")
    if answer in answer_A:
        niets_doen()
    elif answer in answer_B:
        vluchten()
    elif answer in answer_C:
        terug_vechten()
    else:
        print(benodigheden)
        intro()

def vluchten():
    print("""Je besluit te vluchten. 
    Weg van dit afschuwelijk leven.
    """)
    Yebar()

def niets_doen():
    print("Je besluit net zoals alle andere dagen te bidden, hopen dat je de dag weer overleefd")
    Yebar()

def terug_vechten():
    print("""Je wilde dat het stopte en van binnen had je alle moed en kracht opgespaard.
    Dit wordt de dag dat alles anders gaat worden.
    """)
    Yebar()

def Yebar():
    print("""Yebar had je zoals altijd opgesloten in je kamer, 
    wanneer hij weg moest. Vertelde hij nooit wat hij ging doen.
    Toen hij weer weg moest, ging je 
    """)
    time.sleep(1)
    print("""Wat ga je doen?
    A) Raam doorslaan
    B) Ontsnappen via de voordeur
    C) Op hem wachten
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Raam_Door_Slaan()
    elif answer in answer_B:
        Ontsnappen_via_deur()
    elif answer in answer_C:
        op_hem_wachten()
    else:
        print(benodigheden)
        Yebar()

#endregion 

#region slecht einde: Terugvechten 3 keuzes------------------------------------------------------------------------------------------------
def op_hem_wachten():
    print("""Je wachtte tot hij terugkwam. 
    Dit was al best snel en je hoorde de dat de voordeur weer dicht gesmeten werd.
    Je wist dat jij weer het doelwit zou worden en dat dit niet zonder geweld zou uitgepraat kon worden.
    Je wilde verlost zijn van dit leven en je voelde opeens een hele sterke energie door je lichaam stromen.
    Je wist dat praten niet zou werken, daarom bereidde je je voor op een gevecht.
    """)
    time.sleep(1)
    print("""Weet je zeker dat je dit wilt gaan doen?
    A) ja, ik voel me zelfverzekerd genoeg en ik weet dat ik 'm aankan!
    B) nee, ik denk toch niet dat dit verstandig is.
    """)
    answer = input(">>> ")
    if answer in answer_A:
        vechten_met_je_handen()
    elif answer in answer_B:
        print("""Diep van binnen wist je toch dat je geen schijn van kanst maakte.
        Hij was bijna 1,5 keer zo groot dan jij en hij was ook veel gespierde.
        """)
        vaas()
    else:
        print(benodigheden)
        op_hem_wachten()


def vechten_met_je_handen():
    print("""Je wachtte tot hij dichtbij naderde en liet hem struikelen.
    Je pakte hem bij zijn nek en zei dat dit nu moest ophouden.
    Even dacht je dat het lukte, maar hij wierp je overeind. 
    Hij kneep je kil dicht en alles werd zwart voor je ogen. 
    Game over!
    """)

def vaas():
    print(""""Je pakte een vaas dat op je nachtkastje stond en wachtte op hem.
    Toen hij de deur opendeed, gooide je de bloempot tegen zijn hoofd aan en rende je het huis uit.
    """)
    time.sleep(1)
    print("""Waar vlucht je naartoe?
    A) Naar je familie
    B) Ergens naartoe rennen
    """)
    answer = input(">>> ")
    if answer in answer_A:
        familie()
    elif answer in answer_B:
        Ergens_naartoe_rennen()
    else:
        print(benodigheden)
        vaas()

#endregion

#region goed einde: Vluchten en met de vreemdeling meegaan 

def Raam_Door_Slaan():
    print("""Je sloeg het raam kapot en klom naar buiten.
    Toen je op de grond stond, hoorde je Yebar zijn auto.
    Hij parkeerde de auto en liep naar zijn huis toe.
    Je wachtte tot hij naar binnen was en vluchtte.
    """)
    time.sleep(1)
    print("""Waar vlucht je naartoe?
    A) Naar familie vluchten
    B) Ergens naartoe rennen
    """)
    answer = input(">>> ")
    if answer in answer_A:
        familie()
    elif answer in answer_B:
        Ergens_naartoe_rennen()
    else:
        print(benodigheden)
        Raam_Door_Slaan()

def Ontsnappen_via_deur():
    global paspoort
    print("""Je zocht een manier om de deur open te krijgen.
    Toen je aan je haar krabbelde, voelde je een speltje in je haar.
    Je probeerde met het speltje de deur open te krijgen en het lukte!
    """)
    time.sleep(1)
    print(""" Wat ga je nu doen?
    A) Zo snel mogelijk uit het huis vluchten
    B) Huis doorzoeken
    """)
    answer = input(">>> ")
    if answer in answer_A:
        paspoort = False
        huis_uitvluchten()
    elif answer in answer_B:
        paspoort = True
        print(paspoort)
        huis_doorzoeken()

def huis_uitvluchten():
    print("""Je rende naar de voordeur, helaas was die op slot. 
    Je zocht paniekerig een sleutel, alleen dat was nergens te bevinden.
    """)
    Yebar_thuis()

def huis_doorzoeken():
    print("""Je doorzocht het huis angstig en vond in een kastje een paspoort van jezelf.
    Die stopte je in je broek.
    """)
    print(paspoort)
    Yebar_thuis()

def Yebar_thuis():
    print("""Je hoorde opeens de sleutel van de voordeur. 
    Yebar kwam thuis!
    """)
    time.sleep(1)
    print("""Wat nu?!
    A) Raam doorslaan
    B) Verstoppen in de keuken
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Raam_Door_Slaan()
    elif answer in answer_B:
        verstoppen_keuken()
    else:
        print(benodigheden)
        Yebar_thuis()

def verstoppen_keuken():
    print("""Met je hart in je keel verstopte je in de keuken kastje. 
    Je hoorde dat Yebar weer een woedenaanval had en sloeg keihard op het kastje waarin je verstop zat.
    Je schrok ervan en bonkte per ongeluk met je hoofd tegen de bovenkant aan. Yebar merkte dit op en had je gevonden.
    Hij werd nog bozer en smeet je op de grond. 
    Je dacht dat dit het einde was en keek opzij. Je zag een mes liggen.
    """)
    time.sleep(1)
    print("""Probeer je het mes te pakken?
    A) Ja! nooit geschoten is altijd mis!
    B) Nee.. dan wordt hij alleen maar bozer en dat gaat me sowieso niet lukken.
    """)
    answer = input (">>> ")
    if answer in answer_A:
        mes_pakken()
    elif answer in answer_B:
        vechten_met_je_handen()
    else:
        print(benodigheden)
        verstoppen_keuken()

def mes_pakken():
    print("""Je kon nog net het mes pakken en hield het angstig voor je.
    Vuur brandde in zijn ogen en hij schold je helemaal verrot.
    Hij dreigde als je het mes niet weglegde, dit het einde was.
    """)
    time.sleep(1)
    print("""Leg je het mes weg?
    A) ja
    B) nee
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Neersteken()
    elif answer in answer_B:
        Niet_neersteken()
    else:
        print(benodigheden)
        mes_pakken()

#Slechtte keuze in het onderdeel huis
def Niet_neersteken():
    print("""Je legde het mes weg. 
    Zo ben jij niet en god zou je hiervoor nooit vergeven.
    Yebar stormde op je af en je wist dat dit het einde was.
    Je hoofd kreeg een paar klappen tegen de vloer aan en je verloor je bewustzijnde. 
    Alles werd zwart voor jouw ogen. Ten minste ben ik nu verlost van dit leven...
    Game over!
    """)
#--------------------------------

def Neersteken():
    print("""Je hield het mes stevig vast en dreigde tegen hem dat je het mes zou gebruiken als hij nog 1 stap dichterbij kwam.
    Hij luisterde niet en kwam woedend op je afgerend.
    Je ontweek zijn aanval en zonder er bij na te denken stak je hem neer.
    Bloed druppelde op de grond en je kon even niet helder meer nadenken.
    Je hoorde mensen bij de voordeur. Je verzamelde alle moed bij elkaar en vluchtte.
    """)
    time.sleep(1)
    print("""Waar ga je naartoe
    A) Naar je familie toe
    B) Ergens naartoe rennen
    """)
    answer = input(">>> ")
    if answer in answer_A:
        familie()
    elif answer in answer_B:
        Ergens_naartoe_rennen()
    else:
        print(benodigheden)
        mes_pakken

def familie():
    print("""Je rende naar je ouders huis toe en vertelde huilend wat er was gebeurd.
    Je moeder was geschokt, maar zei dat je hier niet meer veilig was. 
    Ze gaf je een knuffel en je vluchtte maar ergens naartoe.
    """)
    vreemdeling()

def Ergens_naartoe_rennen():
    print("""Als een kip zonder kop rende je maar ergens naartoe. 
    Je voelde je verloren en je vroeg jezelf af of je toch beter je familie ten hulp kon vragen.
    Je wist alleen niet wat je vader zou doen, aangezien hij juist wilde dat jij met Yebar zou trouwen.
    """)
    vreemdeling()

def vreemdeling():
    print("Je was net buiten de stad om even uit te rusten tot je een stem hoorde zeggen: 'Ben jij de vriendin van Yebar?' ")
    time.sleep(1)
    print("""Wat doe je?
    A) Liegen
    B) Waarheid vertellen
    """)
    answer = input(">>> ")
    if answer in answer_A:
        liegen()
    elif answer in answer_B:
        waarheid_vertellen()
    else:
        print(benodigheden)
        vreemdeling()

def liegen():
    print("""Je zei dat hij zich vergist.
    De man twijfelde, maar vertelde toen dat hij naar Nederland gaat.
    Hij vroeg wat jij ging doen en jij loog ook dat je opweg was naar Nederland.
    Hij vroeg toen of je met hem mee wilt gaat
    """)
    time.sleep(1)
    print("""Ga je met de vreemdeling mee?
    A) Ja
    B) nee
    """)
    answer = input(">>> ")
    if answer in answer_A:
        met_vreemdeling_meegaan()
    elif answer in answer_B:
        niet_gaan()
    else:
        print(benodigheden)
        liegen()

def met_vreemdeling_meegaan():
    print("""Dit was de enige manier dat je kon bedenken om veilig te kunnen ontsnappen.
    Je besloot met hem mee te gaan.
    """)
    gered()

def gered():
    print("""Je kwam op je eind bestemming en je zag eindelijk weer een beetje hoop in je leven.
    Je wilde opnieuw beginnen met je leven en daarom besloot je je identiteit te veranderen.
    Je had ook nog contact opgezocht met je ouders en waarbij je had verteld dat je veilig was.
    Ondanks deze traumatische gebeurtenis, keek je uit naar een nieuw begin in Nederland.
    Je hebt het gered!
    """)
#endregion goed einde
#--------------------------------------------------------------------------------------------------------------------------------------------
#region slecht einde: 2 Niet met de groep meegaan
def waarheid_vertellen():
    print(""" Je vertelde de waarheid, maar dat je op de vlucht van hem was.
    Je smeekte hem om zijn hulp, de man keek je met grote ogen aan
    en vertelde dat Yebar de machtigste man van ons geboorteland was.
    Hij wilde hier niks mee te maken hebben en liep snel weg.
    """)
    time.sleep(1)
    groep_mensen()

def groep_mensen():
    print("""Je wist niet wat je moest doen en vluchtte de stad uit.
    In de verte zag je een groep mensen. 
    """)
    time.sleep(1)
    print("""Ga je er naartoe?
    A) Ja
    B) Nee
    """)
    answer = input(">>> ")
    if answer in answer_A:
        gaan()
    elif answer in answer_B:
        niet_gaan()
    else: 
        print(benodigheden)
        groep_mensen()
    
def niet_gaan():
    print("Je vertrouwde niemand meer en probeerde in je eentje te overleven")
    slecht_einde()

def slecht_einde():
    print("""Je was verdwaald, je had honger en dorst.
    Na nog uren lopen vond je nog niks
    Het was super heet en je zakte op de grond neer.
    Game over!
    """)
#endregion
#--------------------------------------------------------------------------------------------------------------------------------------------
#region goed einde: Met de groep naar Engeland gaan
def gaan():
    print("""Je liep op de groep mensen af en zag dat ze vol belanden waren met spullen.
    Je vroeg waar ze naartoe gingen en ze zeiden dat ze opweg waren naar Engeland.
    Ze vroegen of je met ze mee wilde gaan.
    """)
    time.sleep(1)
    print("""Ga je met ze mee naar Engeland?
    A) Ja 
    B) Nee
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Engeland()
    elif answer in answer_B:
        niet_gaan()
    else:
        print(benodigheden)
        gaan()

# ! Oplossing bedenken hoe ik hier het paspoort kan gebruiken !
def Engeland():
    print("""Je besloot om met ze mee te gaan. 
    Iedereen was super aardig en jullie stopte af en toe om even uit te rusten, te eten en te drinken.
    Toen jullie bij de grens waren, zagen jullie dat jullie door de douane heen moest.
    De groep ging splitsen, want sommige hadden geen paspoort bij zich.
    """)
    time.sleep(1)
    print("""Wat ga je doen?
    A) Langs de douane proberen te sneaken
    B) Met de rest van de groep meegaan die ook geen paspoort hebben""")
    if paspoort: 
        print("C) Ik ga langs de douane, want ik heb een paspoort bij me")
    answer = input(">>> ")
    if answer in answer_A:
        langs_douane_sneaken()
    elif answer in answer_B:
        groep_zonder_paspoort()
    elif answer in answer_C and paspoort:
        langs_duane_paspoort()
    else:
        print(benodigheden)
        Engeland()

#Groep met paspoort naar Engeland
def langs_duane_paspoort():
    if paspoort:
        print("Je hebt hier een paspoort voor nodig, selecteer een van de andere opties.")
        Engeland()
    else:
        print("""Gelukkig had je het paspoort thuis meegenomen, 
        je liet het paspoort zien en je kon veilig doorlopen.
        Je nam afscheid van de andere groep en had wel medelijden met ze.
        Je hoopte voor ze dat zij het ook zouden gaan redden.
        """)
        vliegtuig()

def vliegtuig():
    print("""Jullie vlogen met het vliegtuig naar Nederland.
    Het was een lange en zware reis, maar je had het overleefd.
    Ook had je tijdens dit avontuur, goede connecties gemaakt met de groep die ook het land uitvluchtte.
    """)
    toekomstbeeld_Engeland()

#groep zonder paspoort over zee naar Engeland
def groep_zonder_paspoort():
    print("Je liep naar de andere groep toe.")
    overzee()

def langs_douane_sneaken():
    print(""""Je probeerde langs de douane te sneaken.
    Helaas hadden ze je opgemerkt en werd je weggestuurd. 
    Je liep naar de andere groep toe
    """)
    overzee()

def overzee():
    print("""De groep was van plan om over zee te gaan in de hoop dat ze gevonden worden.
    Jullie zaten dagen dicht op elkaar in een bootje van 9 bij 6 meter.
    Na bijna 7 dagen zag je een boot in de verte.
    """)
    time.sleep(1)
    print("""Wat ga je doen?
    A) schreeuwen voor hulp
    B) stil zijn
    """)    
    answer = input(">>> ")
    if answer in answer_A:
        print("Je riep zo hard als je kon, toen de andere het ook opmerkte riepen jullie gezamelijk")
        opgevangen_Engeland()
    elif answer in answer_B:
        print("""Je vond het akward om als enige te roepen.
        Doordat er golvenkwamen, merkte de andere het ook op en riepen voor hulp.
        """)
        opgevangen_Engeland()
    else:
        print(benodigheden)
        overzee()

def opgevangen_Engeland():
    print(""" De boot zag jullie en jullie werden door de boot opgenomen.
    De boot ging richting Engeland en jullie werden daar opgevangen.
    Eindelijk was de nachtmerrie voorbij en kon je een nieuw leven opbouwen.""")
    toekomstbeeld_Engeland()

def toekomstbeeld_Engeland():
    print("""
    Na een jaar woonde je samen met een goede vriend die je had ontmoet tijdens de reis.
    Jullie werden goed geholpen door social worker 'Emily Patterson.'
    Je bewonderde haar en haar beroep en daarom wilde jij dit ook gaan doen.
    Je hebt het gered!
    """)


intro()
#endregion


