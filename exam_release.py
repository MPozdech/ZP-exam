import tkinter as tk
from tkinter import ttk
import pandas as pd
import random
import time 

# Lists of questions 
a1 = [("Vymenujte zakázané zbrane podľa zákona o zbraniach a strelive (§ 4).", "[pozn. V príncípe stačí vedieť 5 až 7.]\n\n\u2022 vojenská zbraň, odpaľovacie zariadenie na vojenské výbušné strely,\n\u2022 samočinná zbraň,\n\u2022 zbraň, pri ktorej bol jej pôvodný charakter alebo podoba zmenená tak, aby sa jej použitím mohol spôsobiť ťažší následok ako pred jej úpravou, alebo zbraň, ktorá má vzhľad iného predmetu,\n\u2022 palná zbraň vyrobená z nekovového materiálu a neidentifikovateľná za pomoci detekčných prístrojov a röntgenových prístrojov,\n\u2022 zbraň vybavená zakázaným doplnkom zbrane,\n\u2022 zbraň, ktorá využíva elektrické napätie alebo elektrický prúd na zasiahnutie človeka alebo zvieraťa,\n\u2022 vyrobená zbraň alebo upravená zbraň, ak nejde o dovolenú výrobu alebo dovolenú úpravu,\n\u2022 zbraň s úpravami sťažujúcimi jej kriminalistickú identifikáciu, \n\u2022 zbraň s pozmeneným alebo odstráneným výrobným číslom, \n\u2022 expandzná zbraň, ktorá bola upravená zo zbrane kategórie A, \n\u2022 zbraň, ktorá bola upravená zo zbrane kategórie A na zbraň kategórie D, okrem zbrane uvedenej v písmene  j), § 7 ods. 1 písm. i), j) alebo písm. l) [znehodnotené zbrane a rezy], \n\u2022 samonabíjacia palná zbraň, ktorá bola upravená zo samočinnej zbrane, \n\u2022 krátka samonabíjacia/opakovacia zbraň s kapacitou zásobníka viac ako 20 nábojov, \n\u2022 dlhá samonabíjacia/opakovacia zbraň s kapacitou zásobníka viac ako 10 nábojov, \n\u2022 dlhá samonabíjacia zbraň, ktorú možno skrátit bez straty funkčnosti na celkovú dĺžku menej ako 600mm, \n\u2022 zbraň kategórie A s neodnímateľným tlmičom hluku výstrelu spĺňajúcim podmienky podľa osobitného predpisu."),("Uveďte, aký vek musí spĺňať žiadateľ o vydanie zbrojného preukazu (§18).","21 rokov, s výnimkou ak ide o: \n\u2022 Zbrojný preukaz skupiny D alebo F, kde žiadateľ môže mať 18 rokov (a má platný polovný lístok v prípade skupiny D), alebo \n\u2022 Zbrojný preukaz skupiny E, kde žiadateľ môže mať 15 rokov ak je členom štátnej reprezentácie v streleckej disciplíne a jeho zákonný zástupca dá súhlas."),("Kto a na aký čas vydáva nákupné povolenie na nadobudnutie vlastníctva zbrane (§ 11)?","Vydáva ho policajný útvar na čas nevyhnutný na nadobudnutie zbrane, avšak najdlšie na dobu 6-mesiacov.")]
a2 = [("Podliehajú zbrane kategórie C povoľovaciemu konaniu a evidenčnej povinnosti (§ 6)?","Zbrane kategórie C podliehajú ohlasujúcej a evidenčnej povinnosti. Povoľovaciemu konaniu podliehajú iba zbrane kategórie A a B."),("Definujte zbrojný preukaz a vymenujte jednotlivé skupiny zbrojného preukazu (§ 15).","Zbrojný preukaz je verejná listina ktorá umožnuje jeho držiteľa držať strelné zbrane a strelivo v rozsahu podľa skupiny. Skupiný sú: \n\u2022 A - nosenie zbrane a streliva na ochranu osoby a majetku, \n\u2022 B - držanie zbrane a streliva na ochranu osoby a majetku, \n\u2022 C - držanie zbrane a streliva na výkon zamestnania alebo oprávnenia podľa osobitného predpisu, \n\u2022 D - držanie zbrane a streliva na poľovné účely, \n\u2022 E - držanie zbrane a streliva na športové účely, \n\u2022 F - držanie zbrane a streliva na múzejné alebo zberateľské účely."),("Čím preukazuje žiadateľ o zbrojný preukaz zdravotnú spôsobilosť (§20)?","Potdvrdením od všeobecného lekára alebo pediatra.")]
a3 = [("Je povinný držiteľ zbrojného preukazu viesť záznamovú knihu? Ak áno, držiteľ ktorej skupiny zbrojného preukazu?","Áno, a to držiteľ zbrojného preukazu skupiny F."),("Kto môže byť správcom strelnice podľa zákona o zbraniach a strelive (§50)?","Osoba staršia ako 25 rokov, ktorá je už minimálne 3 roky držiteľom zbrojného preukazu skupiny A, B, C, D, alebo E."),("Do koľkých dní od podania žiadosti o vydanie zbrojného preukazu je potrebné vykonať skúšku odbornej spôsobilosti na vydanie zbrojného preukazu (§ 3 Vyhlášky)?","60 dní")]
b1 = [("Pri čistení krátkej guľovej zbrane, ktorú má držiteľ v legálnej držbe na zbrojný preukaz skupiny „A“ došlo k náhodnému výstrelu, pričom držiteľ zbrane neúmyselne usmrtil svoju manželku. Je konanie držiteľa zbrane trestné? Bude držiteľ zbrane stíhaný podľa Trestného zákona, alebo riešený podľa zákona o zbraniach a strelive?","Áno, dopustil sa trestného činu usmrtenia. Bude stíhaný podľa Trestného zákona"),("Čo je trestným činom podľa Trestného zákona?","Trestný čin je protiprávny čin, ktorého znaky sú uvedené v tomto zákone [300/2005 Trestný zákon], ak tento zákon neustanovuje inak"), ("Aké zavinenia rozlišujeme podľa Trestného zákona?", "Rozlišujeme úmyselné zavinenie a zavinenie z nedbanlivosti")]
b2 = [("Držiteľa zbrojného preukazu s oprávnením skupiny „B“ sused požiadal, aby mu pomohol zadržať dvoch neznámych mužov, ktorí sa vlámali do jeho domu a odnášajú bytové zariadenie. Je držiteľ zbrojného preukazu oprávnený pri zadržaní uvedených osôb použiť hrozbu namierenou zbraňou, aj keď nebol napadnutý jeho vlastný majetok? Sú držiteľ zbrojného preukazu a jeho sused oprávnení obmedziť slobodu neznámych mužov až do príchodu príslušníkov Policajného zboru?","Áno a áno."),("Vymenujte súdy na účely Trestného poriadku.","Obecný súd, krajsky súd, najvyšší súd, a špecializovaný trestný súd."),("Do bytu držiteľa zbrojného preukazu skupiny „B“ sa dostavil vyšetrovateľ Policajného zboru a vyzval ho, aby mu vydal krátku guľovú zbraň, ktorú je potrebné zaistiť na účely trestného konania. Uvedenou zbraňou 17-ročný syn držiteľa zbrojného preukazu zastrelil susedovi vo dvore psa, čím mu spôsobil škodu minimálne 1 659,-- Eur. Držiteľ zbrojného preukazu odmietol vydať zbraň s tým, že chce na to písomný súhlas prokurátora. Možno držiteľa zbrojného preukazu postihnúť za to, že nevyhovel výzve vydať zbraň ako vec, ktorú je potrebné zaistiť na účely trestného konania?","Áno, možno ho postihnút pokutou za to, že neuposlúchol výzvu policajta.")]
b3 = [("Môže sa držiteľ zbrojnej licencie dopustiť priestupku? Ak nie, čoho sa dopúšťa?","Nie, dopúšta sa správneho deliktu."),("Možno prejednať držiteľa zbrojnej licencie v blokovom konaní?","Nie, v blokovom konaní sa môžu prejednať priestupky, a licencia sa dopúšťa správneho deliktu."),("Dopúšťa sa ten, kto urobí nepravdivé čestné vyhlásenie podľa zákona o zbraniach a strelive priestupku?","Áno, dopúšta sa priestupku podla Zákonu o zbraniach a strelive.")]
b4 = [("Kto udeľuje výnimku na nadobudnutie vlastníctva a na držanie alebo nosenie zbrane kategórie A?","Ministerstvo, presnejšie Prezídium Policajného Zboru, odbor dokladov a evidencií."),("Podľa čoho sa určuje miestna príslušnosť pre držiteľa zbrojného preukazu?","Podľa miesta trvalého pobytu."),("Súkromný detektív prišiel na základe písomného predvolania na okresný súd vypovedať ako svedok a mal pri sebe pištoľ, ktorú je oprávnený nosiť na ochranu osoby a majetku. Pri vstupe do budovy okresného súdu ho kontrolovali príslušníci Zboru väzenskej a justičnej stráže Slovenskej republiky a oznámili mu, že pištoľ mu musia odobrať a to na dobu, kým sa bude zdržiavať v budove súdu. Sú príslušníci Zboru väzenskej a justičnej stráže Slovenskej republiky oprávnení odobrať uvedenú zbraň? Ak nie, vysvetlite, prečo.","Áno, sú oprávnení.")]
c1 = [("Čo sa podľa zákona o zbraniach a strelive považuje za historickú zbraň?","Zbraň vyrobená pred 31.12.1890."),("Aký je rozdiel v konštrukcií pištole a revolvera?","Pištol ma cyklujúci záver, ktorý podáva náboje zo zásobníku do nábojovéj komory. Revolvér má viacero nábojových komor, ktoré sú usporiadané v rotujúcom cylindri."),("Považujú sa hlavné časti zbrane podľa zákona o zbraniach a strelive za zbraň? Vymenujte hlavné časti zbrane podľa zákona o zbraniach a strelive","Áno. Hlavné časti sú: \n\u2022 Hlaveň, \n\u2022 Vložná hlaveň, \n\u2022 Nábojová komora, \n\u2022 Rám, \n\u2022 Ťelo, \n\u2022 Záver, \n\u2022 Závorník, \n\u2022 Púzdro závorníka.")]
c2 = [("Je povolené priniesť si na strelnicu v zime na zahriatie alkoholický nápoj a požiť ho v malom množstve?","Nie. Manipulácia so zbranou pod vplyvom alkoholu je priestupok pod zákonom o zbraní a strelive."),("Čo sa podľa zákona o zbraniach a strelive rozumie strelnicou?","Súbor zariadení určených na bezpečnú streľbu zo zbrane."),("Čo sa rozumie manipuláciou so zbraňou alebo strelivom?","Hocijaký fyzický kontakt.")]
d  = [("Vymenujte tiesňové linky","\u2022 112 - Ťiesnová linka, \n\u2022 150 - Hasiči, \n\u2022 155 - Záchranná zdravotná služba, \n\u2022 158 - Polícia, \n\u2022 159 - Mestká polícia."),("Ako sa prejavujú povrchové poranenia tvárovej časti hlavy a v čom spočíva poskytnutie prvej pomoci?","Značné krvácanie. Prvá pomoc spočíva v držanie obväzu pod tlakom na mieste rany."),("Aké sú tri základné zásady pri poskytovaní prvej pomoci?","\n 1. Zabezpečiť osobu, \n 2. Zabrániť zhoršenie stavu, \n 3. Zabezpečit dalšiu zdravotnú starostlivosť.")]
e  = [("Uveďte a popíšte základné pravidlá bezpečnej manipulácie so zbraňou na strelnici.","\n\u2022 So zbranou vždy manipulujeme ako keby bola nabitá, \n\u2022 Nikdy nemierime na nič čo nechceme zničiť, \n\u2022 Prst máme značne mimo spúšte do momentu tesné pred tým, ako ideme vystreliť, \n\u2022 Zbraň vždy mieri do bezpečného priestoru - do streliska, \n\u2022 Po ukončení streľby sa uistíme že zbraň je nenabitá."),("Prakticky predveďte a vysvetlite podstatu mierenia so strelnou zbraňou na určený bod.","Do cielníka si dáme mušku tak, aby bola s cielníkom urovnená vodorovno aj zvislo."), ("Prakticky predveďte nabitie a vybitie zbrane.","Vybitie: \n 1. Vyberemie zásobník, \n 2. Pocyklujujeme záverom tak, aby náboj v komore bol vyhodený. \n 3. Pozrieme sa do komory cez vyhadzovacieho otvoru v závere. \n 4. Namierime zbraň do bezpečného priestoru a vykonáme ranu istoty. \n\n Nabitie: \n 1. Zasunieme zásobník do šachty. \n 2. Sputsíme záver.")]
no_recall = 2 #in how many question generations can a question be asked again
list_of_question_lists = [a1,a2,a3,b1,b2,b3,b4,c1,c2,d,e] #a matrix containing the different question lists
question_names = ["A1","A2","A3","B1","B2","B3","B4","C1","C2","D","E"] #the names of the question series
selected_questions = [] #initializes the list of questions asked in one exam
asked_questions = [] #initializes the list of questions that have been asked already and should not be repeated 

# Root window setup
root = tk.Tk()
root.title("Exam script")
root.geometry('700x900')

# Scrolbar logic
canvas = tk.Canvas(root) 
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview) 
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind( "<Configure>", 
    lambda e: canvas.configure( 
        scrollregion=canvas.bbox("all") ) ) #has the scroll input be registered for the entire window
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw") 
canvas.configure(yscrollcommand=scrollbar.set)
# Sets the content to scroll on mousewheel input
def on_mouse_wheel(event): 
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
    
canvas.bind_all("<MouseWheel>", on_mouse_wheel)
scrollbar.pack(side="right", fill="y") 
canvas.pack(side="left", fill="both", expand=True) 

# Creates the frames used for the different script functions
expansion_frame = ttk.Frame(scrollable_frame)
expansion_frame.grid(row=0, column=0, sticky="nsew")
menu_frame = ttk.Frame(expansion_frame)
question_frame = ttk.Frame(expansion_frame)
answer_frame = ttk.Frame(expansion_frame)
button_frame = ttk.Frame(expansion_frame)

# Function to show questions
def show_questions():
    global asked_questions,selected_questions,tot_time #points to the global var inside of the function
    selected_questions = []
    menu_frame.pack_forget() #hides the menu frame
    question_frame.pack(side=tk.LEFT, anchor="w", pady=20) #shows the question frame
    if len(asked_questions) > len(list_of_question_lists) * no_recall: #[0,1,2,3,4,...] * 2 duration for how far back to not repeat questions
        del asked_questions[:len(list_of_question_lists)] #deletes [0,1,2], so 3 = questions being asked
            
    i = 0 #initializes the index that will go over the question "classes"        
    while len(selected_questions) < len(list_of_question_lists): #while there are series which have no questions asked
        question = random.choice(list_of_question_lists[i]) #randomly selects a question from the 1st series of questions [a1]
        if question not in asked_questions: #has this question already been asked?
            selected_questions.append(question) #add this to the question list of this generation
            asked_questions.append(question)  #add this to the list of questions asked previously
            i += 1 #increase i to move onto the next question series
        
    row_index = 1 #sets the row into which the label should be inserted 
    series_counter = 0 #increments the labels for the question series
    # Loop to create labels for the questions selected in the prior loop
    for question, answer in selected_questions:
        series_label = tk.Label(question_frame, text=question_names[series_counter], anchor="e", font=("Helvetica",12))
        series_label.grid(column=0,row=row_index, sticky=tk.E, padx=5, pady=5)
        series_counter = series_counter + 1
        label = tk.Label(question_frame, text=question, bg="lightgrey", font=("Helvetica", 12), anchor="w")
        label.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=(10,0), columnspan=4)
        root.bind("<Configure>", update_wraplength(label)) #function call to change how text wraps based on window size
        row_index = row_index + 1
    
    timer_label = tk.Label(question_frame, text="30:00")
    timer_label.grid(column=3, row=0, sticky=tk.W, padx=5, pady=5)
    tot_time = 60*30 #initializes the timer, 30 mins in seconds
    
    def update_timer():
        global tot_time
        mins, secs = divmod(tot_time, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        if tot_time > 0:
            tot_time -= 1
            mins, secs = divmod(tot_time, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            timer_label.config(text=time_str)
            question_frame.update()
            question_frame.after(1000, update_timer) #every 1000ms the update timer call is repeated
            
    update_timer() #function is called for the first time when the question frame is opened 
    
def show_answers():
    question_frame.pack_forget() #hides the question menu
    tot_time = 0 #timer is stopped
    answer_frame.pack(side=tk.LEFT, anchor="nw", pady=20)
    global selected_questions #loads the list which contains the asked questions
    for widget in question_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    
    row_index = 1
    series_counter = 0
    for question, answer in selected_questions:
        series_label = tk.Label(answer_frame, text=question_names[series_counter], anchor="e", font=("Helvetica",12))
        series_label.grid(column=0,row=row_index, sticky=tk.E, padx=5, pady=5)
        series_counter = series_counter + 1
        question_label = tk.Label(answer_frame, text=question, bg="lightgrey", anchor="w", justify=tk.LEFT, font=("Helvetica", 12))
        question_label.grid(column=1, row=row_index, sticky=tk.EW, padx=5, pady=(10,0), columnspan=4)
        answer_label = tk.Label(answer_frame, text=answer, bg="yellow", anchor="w", justify=tk.LEFT, font=("Helvetica", 12))
        answer_label.grid(column=1, row=row_index+1, sticky=tk.EW, padx=5, pady=(0,0), columnspan=4)
        row_index = row_index + 2
        question_label.bind("<Configure>", update_wraplength(question_label))
        answer_label.bind("<Configure>", update_wraplength(answer_label))
        
    root.bind("<Configure>", update_wraplength)
        
def update_wraplength(label): 
    wrap_length = root.winfo_width() - 80
    label.config(wraplength=wrap_length)

# Function to show the menu
def show_menu():
    question_frame.pack_forget()
    # Remove the labels so next generation is not drawing over them
    for widget in question_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    answer_frame.pack_forget()
    for widget in answer_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    menu_frame.pack(pady=20, side="left")

# Menu frame
question_button = tk.Button(menu_frame, text="Start exam", command=show_questions)
question_button.pack(pady=10,side = "top")
exit_button = tk.Button(menu_frame, text="Quit", command=root.destroy)
exit_button.pack(pady=10, side = "top")

# Question frame
back_button = tk.Button(question_frame, text="Back to Menu", command=show_menu)
back_button.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
end_button = tk.Button(question_frame, text="Show answers", command=show_answers)
end_button.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)
timer_label = tk.Label(question_frame, text="30:00")
timer_label.grid(column=3, row=0, sticky=tk.W, padx=5, pady=5)

# Answer frame
back_button = tk.Button(answer_frame, text="Back to Menu", command=show_menu)
back_button.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

# Script starts with the menu window
menu_frame.pack(pady=20, side="left")
root.mainloop() #the gui is started
