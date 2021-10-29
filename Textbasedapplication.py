# Textbased application: Vluchtelingen verhaal
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
                print("Je mag het spel spelen, veel plezier! \nps. Wees eerlijk bij het invullen voor de beste ervaring\n")
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
import os

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
    print("""Je bent 16 jaar en wordt uitgehuwelijkt aan de 36-jarige Yebar.
    Hij is de machtigste man in je geboorteland en is hoofdmilitair.
    Sinds je bij hem woont, is je leven een hel.
    Hij heeft agressie problemen en je wordt vaak mishandeld.
    Je was bang, maar besloot
    """)
    time.sleep(1)
    print("""Wat ga je doen? 
    A) Vluchten 
    B) Terug vechten?
    """)
    answer = input(">>> ")
    if answer in answer_A:
        vluchten()
    elif answer in answer_B:
        terug_vechten()
    else:
        print(benodigheden)
        intro()

def vluchten():
    print("""Je besluit te vluchten. 
    Weg van dit afschuwelijke leven.
    """)
    Yebar()

def terug_vechten():
    print("""Je wilt dat het stopt en van binnen hebt je alle moed en kracht opgespaard.
    Dit wordt de dag dat alles anders gaat worden.
    """)
    Yebar()

def Yebar():
    print("""Yebar heeft je zoals gewoonlijk opgesloten in je kamer, 
    wanneer hij weg gaat vertelt hij ook nooit wat hij gaat doen.
    Toen hij weer weg ging, besluit je... 
    """)
    time.sleep(1)
    print("""Wat ga je doen?
    A) Raam inslaan
    B) Ontsnappen via de voordeur
    C) Op hem wachten
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Raam_inslaan()
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
    print("""Je wacht tot hij terugkomt. 
    Dit was al best snel en je hoort dat de voordeur weer dicht wordt gesmeten.
    Je weet dat jij weer het doelwit zou worden en dat dit niet zonder geweld zou uitgepraat worden.
    Je wilt verlost zijn van dit leven en je voelt opeens een hele sterke energie door je lichaam stromen.
    Je weet dat praten niet zou werken, daarom bereidt je je voor op een gevecht.
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
        print("""Diep van binnen weet je toch dat je geen schijn van kans maakt.
        Hij is bijna 1,5 keer zo groot dan jij en hij was ook veel gespierder.
        """)
        vaas()
    else:
        print(benodigheden)
        op_hem_wachten()


def vechten_met_je_handen():
    print("""Je wacht totdat hij dichtbij komt en je laat hem struikelen.
    Je pakt hem bij zijn nek en zegt dat dit nu moet ophouden.
    Even dacht je dat het lukte, maar hij wierp je overeind. 
    Hij knijpt jouw keel dicht, alles wordt zwart voor je ogen. 
    Game over!
    """)
    Speel_opnieuw = input("Wil je het opnieuw spelen? Zoja type 'ja'\n>>> ")
    if Speel_opnieuw == "ja":
        os.system("cls")
        intro()
    else:
        exit 

def vaas():
    print(""""Je pakt een vaas dat op je nachtkastje staat en wacht op hem.
    Je hoort voetstappen op de trap lopen en je hoort dat hij je naam roept.
    Je blijft stil en toen hij de deur open ging doen, gooide je een vaas tegen zijn hoofd aan.
    Je rent zo snel mogelijk het uit huis.
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

def Raam_inslaan():
    print("""Je ging het raam inslaan en klimt naar buiten.
    Dit voelt opeens weer zo gek. Je bent al maanden het huis niet uit geweest en nu sta je gewoon buiten.
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
        Raam_inslaan()

def Ontsnappen_via_deur():
    global paspoort
    print("""Je zoekt een manier om de deur open te krijgen.
    Je krabbelde aan je haar en voelt een speltje.
    ja, dit is het! Je probeert met het speltje de deur open te krijgen en het lukt!
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
    print("""Je rent naar de voordeur, helaas zit die op slot. 
    Je zoekt paniek de sleutel, alleen die was nergens te bekennen.
    """)
    Yebar_thuis()

def huis_doorzoeken():
    print("""Je doorzoekt het huis angstig en vindt in een kastje een paspoort van jezelf.
    Je pakt snel het paspoort en stopt 't in je broek.
    """)
    print(paspoort)
    Yebar_thuis()

def Yebar_thuis():
    print("""Je hoort opeens de sleutel van de voordeur. 
    Yebar komt thuis!
    """)
    time.sleep(1)
    print("""Wat nu?!
    A) Raam doorslaan
    B) Verstoppen in de keuken
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Raam_inslaan()
    elif answer in answer_B:
        verstoppen_keuken()
    else:
        print(benodigheden)
        Yebar_thuis()

def verstoppen_keuken():
    print("""Met je hart in je keel verstop je je in de keuken kastje. 
    Je hoort dat Yebar weer een woedenaanval heeft en hij sloeg keihard op het kastje waarin je verstop zat.
    Je schrok ervan en bonkte per ongeluk met je hoofd tegen de bovenkant aan. Yebar merkt dit op en je zag de keukendeurtjes opengaan.
    Hij pakt je bij je arm en smeet je op de grond.
    "Wat doe jij hier!" zei hij en je zag zijn hoofd rood worden.
    Dit wordt mijn einde dacht je, je kijkt opzij en zag een mes.
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
    print("""Je kan nog net het mes pakken en houdt het angstig voor je.
    Vuur brandt in zijn ogen en hij schold je helemaal verrot.
    Hij dreigde als je het mes niet weglegde, dit het einde was.
    """)
    time.sleep(1)
    print("""Leg je het mes weg?
    A) ja
    B) nee
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Niet_neersteken()
    elif answer in answer_B:
        Neersteken()
    else:
        print(benodigheden)
        mes_pakken()

#Slechtte keuze in het onderdeel huis
def Niet_neersteken():
    print("""Je legt het mes weg. 
    Zo ben jij niet en god zou je hiervoor ook nooit vergeven.
    Yebar komt op je af gestormd en je weet dat dit het einde is.
    Je hoofd krijgt een paar klappen tegen de vloer aan en je verliest je bewustzijnde. 
    Alles wordt zwart voor jouw ogen. Ten minste ben ik nu verlost van dit leven...
    Game over!
    """)
    Speel_opnieuw = input("Wil je het opnieuw spelen? Zoja type 'ja'\n>>> ")
    if Speel_opnieuw == "ja":
        os.system("cls")
        intro()
    else:
        exit 
#--------------------------------

def Neersteken():
    print("""Je houdt het mes stevig vast en zegt "als je nog 1 stap dichterbij komt, gebruikt ik dit mes."
    Hij ging niet luisteren en komt woedend op je afgerend.
    Je ontwijkt zijn aanval en zonder er bij na te denken steek je 'm neer.
    Bloed druppelt op de grond en je kan even niet helder meer nadenken.
    Je hoort mensen bij de voordeur. Je verzamelt alle moed bij elkaar en ging vuchten.
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
    print("""Je rent naar je ouders huis toe en vertelt huilend wat er gebeurd is.
    Je moeder was geschokt, maar ze zegt dat je hier niet meer veilig bent, al helemaal niet als je vader hier achter komt. 
    Ze gaf je een stevige knuffel en je ging maar ergens naartoe vluchten.
    """)
    vreemdeling()

def Ergens_naartoe_rennen():
    print("""Als een kip zonder kop ren je maar ergens naartoe. 
    Je voelt je verloren en je vroeg jezelf af of je toch beter je familie ten hulp kon vragen.
    Je weet alleen niet wat je vader zou doen, aangezien hij juist wilde dat jij met Yebar zou gaan trouwen.
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
    print("""Je zegt dat hij zich vergist.
    Je ziet de man twijfelen, maar hij zei toen dat hij naar Nederland gaat.
    Hij vraagt wat jij hierzo doet en jij loog ook dat je op weg was naar Nederland.
    Hij vraagt of je met hem mee wilt gaan.
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
    print("""Dit is de enige manier dat je kan bedenken om veilig te kunnen ontsnappen.
    Je besluit met hem mee te gaan.
    """)
    gered()

def gered():
    print("""Je komt op je eind bestemming en je ziet eindelijk weer een beetje hoop in je leven.
    Je wilt opnieuw beginnen met je leven en daarom besluit je je identiteit te veranderen.
    Ook wil je nog contact opzoeken met je moeder om te vertellen dat je veilig bent.
    Ondanks deze traumatische gebeurtenis, kijk je uit naar een nieuw begin in Nederland.
    Je hebt het gered!
    """)
    Speel_opnieuw = input("Wil je het opnieuw spelen? Zoja type 'ja'\n>>> ")
    if Speel_opnieuw == "ja":
        os.system("cls")
        intro()
    else:
        exit 
#endregion goed einde
#--------------------------------------------------------------------------------------------------------------------------------------------
#region slecht einde: 2 Niet met de groep meegaan
def waarheid_vertellen():
    print(""" Je vertelt de waarheid, maar dat je op de vlucht van hem was.
    Je smeekt hem om zijn hulp, de man kijkt je met grote ogen aan
    en vertelt dat Yebar de machtigste man van ons geboorteland was.
    Hij wilt hier niks mee te maken hebben en hij liep snel weg.
    """)
    time.sleep(1)
    groep_mensen()

def groep_mensen():
    print("""Je weet niet wat je moet doen en vlucht de stad uit.
    In de verte zie je een groep mensen. 
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
    print("Je vertrouwt niemand meer en probeert in je eentje te overleven")
    slecht_einde()

def slecht_einde():
    print("""Je weet niet waar je bent en je hebt honger en dorst.
    Na nog uren lopen vindt je nog niks.
    Het is super heet en je zakt op de grond neer.
    Game over!
    """)
    Speel_opnieuw = input("Wil je het opnieuw spelen? Zoja type 'ja'\n>>> ")
    if Speel_opnieuw == "ja":
        os.system("cls")
        intro()
    else:
        exit 
#endregion
#--------------------------------------------------------------------------------------------------------------------------------------------
#region goed einde: Met de groep naar Engeland gaan
def gaan():
    print("""Je stap op de groep mensen af en ziet dat ze vol beladen met spullen zijn.
    Je vraagt waar ze naartoe gaan en ze zeiden dat ze opweg naar Engeland zijn.
    "Wil je met ons mee gaan?" vroegen ze en je zei:
    """)
    time.sleep(1)
    print("""Ga je met ze mee naar Engeland?
    A) Natuurlijk ga ik mee!
    B) Dat is heel aardig van jullie, maar ik reis alleen.
    """)
    answer = input(">>> ")
    if answer in answer_A:
        Engeland()
    elif answer in answer_B:
        niet_gaan()
    else:
        print(benodigheden)
        gaan()

def Engeland():
    print("""
    Je was heel erg blij dat je met ze mee bent gegaan, want iedereen was super aardig.
    Heel af en toe had je een kleine rust pauze, om te eten en te drinken, maar daarna gingen jullie weer gauw door.
    Na enkele uren lopen zie je dat je bij de grens aankomt en je weet dat daar douanes zijn.
    Omdat sommige leden van de groep geen paspoort bij zich hebben, gingen jullie splitsen.
    jij ging:
    """)
    time.sleep(1)
    print("""Wat ga je doen?
    A) Langs de douane proberen te sneaken
    B) Met de rest van de groep meegaan die ook geen paspoort hebben""")
    if paspoort: 
        print("C) langs de douane, want je hebt een paspoort bij je")
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
        print("""Gelukkig hebt je het paspoort thuis meegenomen.
        Jullie gingen afscheid nemen van de andere groep, je had wel medelijden met ze en je hoopte dat zij ook veilig aan zouden komen.
        Zenuwachtig loop je richting de douane en liet je het paspoort zien, de douane knikte naar je en je mocht veilig doorlopen.
        """)
        vliegtuig()

def vliegtuig():
    print("""Na uren wachten mag je eindelijk het vliegtuig in.
    Het vliegtuig ging naar Nederland vliegen.
    Het is een lange en zware reis geweest, maar je hebt het overleefd.
    Ook hebt je tijdens dit avontuur, goede connecties gemaakt.
    """)
    toekomstbeeld_Engeland()

#groep zonder paspoort over zee naar Engeland
def groep_zonder_paspoort():
    print("Je loopt naar de andere groep toe.")
    overzee()

def langs_douane_sneaken():
    print(""""Je probeert langs de douane te sneaken.
    Helaas zien ze je en je bent even bang dat je gevangen genomen zou worden, maar je wordt gewoon weggestuurd.
    Je loopt naar de andere groep toe.
    """)
    overzee()

def overzee():
    print("""De groep is van plan om over zee te gaan in de hoop dat ze gevonden worden.
    Jullie zitten dagen lang dicht op elkaar in een bootje van 9 bij 6 meter.
    Je wordt wakker omdat de boot heel erg hard begon te wiebelen, je probeert te kijken waardoor dit komt en je ziet licht in de verte.
    """)
    time.sleep(1)
    print("""Wat ga je doen?
    A) schreeuwen voor hulp
    B) stil zijn
    """)    
    answer = input(">>> ")
    if answer in answer_A:
        print("Je roept zo hard als je kon, toen de andere de boot ook zagen, riepen jullie gezamelijk.")
        opgevangen_Engeland()
    elif answer in answer_B:
        print("""Je vindt het akward om als enige te roepen.
        Je ziet dat de andere ook wakker worden en toen ze om zich heen gingen kijken, zagen ze ook de boot. 
        Ze gingen gelijk roepen voor hulp.
        """)
        opgevangen_Engeland()
    else:
        print(benodigheden)
        overzee()

def opgevangen_Engeland():
    print(""" Er wordt op jullie geschenen met een licht en de boot komt jullie kant op.
    Toen de boot dichtbij jullie was, werden jullie opgenomen.
    De boot gaat richting Engeland en daar zouden jullie worden opgevangen.
    EIndelijk is de nachtmerrie voorbij en kan je een nieuw leven opbouwen.
    """)
    toekomstbeeld_Engeland()

def toekomstbeeld_Engeland():
    print("""Na een jaar hebt je een eigen huis en woon je samen met je vriend "Shahin" die je tijdens de reis hebt ontmoet.
    Jullie worden nog goed geholpen door social worker 'Emily Patterson.'
    Je bewondert haar en haar beroep zo erg en daarom wil jij hier ook je beroep van maken.
    Je hebt het gered!
    """)
    Speel_opnieuw = input("Wil je het opnieuw spelen? Zoja type 'ja'\n>>> ")
    if Speel_opnieuw == "ja":
        os.system("cls")
        intro()
    else:
        exit 

intro()
#endregion


