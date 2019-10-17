# 1. Motivácia
Počasie patrí medzi najvýraznejšie faktory, ktoré vplývajú na ľudksý život na Zemi. Človek sa odjakživa snažil čo najpresnejšie predpovedať počasie práve kvôli jeho veľkému vplyvu na život každého jedinca. Od predpovedi počasia sú v súčasnosti takisto závislé mnohé odvetvia, či už poľnohospodárstvo, doprava(letecká, lodná), výroba elektrickej energie (veterné elektrárne a solárne panely) a mnohé ďalšie. Z týchto dôvodov je čo najpresnejšia predpoveď počasia veľmi dôležitá.


V posledných rokoch sa začala na predpoveď počasia využívať nová technika - predpoveď pomocou neurónových sietí. Pri predpovedi počasia ide prakticky o predikciu časových radov. Kvôli premenlivosti sa počasia sa často na tieto problémy využívajú rekurentné neurónové siete.


V našom projekte sme sa rohodli zaoberať predikciou časových radov a teda predpoveďou počasia. Našim cieľom je využiť rekurentné neurónové siete.

# 2. Súvisiaca práca
- *Sequence to Sequence Weather Forecasting with Long Short-Term Memory Recurrent Neural Networks 2016*


V tejto práci sa autori zaoberajú predikciou počasia pre 9 miest v Maroku. Snažia sa o predpoveď teploty, vlhkosti a rýchlosti vetra na dva časové intervaly - 24 a 72 hodín. Používajú pri tom LSTM neurónové siete, ktoré patria do skupiny rekurentných neurónových sietí.

Na natrénovanie modelu neorónovej siete použili približne 15 rokov meteorologických dát, ktoré boli zaznamenané v časovom intervale jednej hodiny. Model dosiahol dobrú úspešnnosť predpovedí, porovnateľnú s úspešnosťou metód, ktoré sa na predpoveď počasia používajú v dnešnej dobe.

Ďalšie práce v tejto oblasti:
- *An ensemble of neural networks for weather forecasting 2004*
- *An Efficient Weather Forecasting System using Artificial Neural Network 2010*

# 3. Dataset
Vstupný dataset obsahuje 4000 obrázkov z dvadsiatich rôznych kategórií, ako napríklad Object, Pattern, Social, Art atď.
Obrázky sú rozdelené do dvoch rovnako veľkých skupín po 2000 obrázkov - vstupné a výstupné. Veľkosť jednotlivých obrázkov je 1920 x 1080px. Taktiež obsahuje body, na ktoré sa ľudia pri jetnotlivých obrázkoch pozerali. Tieto dáta boli získané pozorovaním očí testovaných osôb počas premietania obrázkov. Každá osoba mala 5 sekúnd na prezretie jedného obrázku.

## Vstupný obrázok:

![jazdec](./images/006.jpg)
## Výstupná saliency mapa:

![jazdecsaliency](./images/006_SaliencyMap.jpg "Input")


# 4. Návrh riešenia
Náš model sa bude skladať z viacvrstvovej konvolučnej neurónovej siete. Túto sieť budeme trénovať na vopred opísanom datasete a chceme aby predikovala miesta, kde sa budú ľudia najčastejšie pozerať.
