# ratp Bot


A bot that will provide schedules and alerts for RATP trains, subways, and buses in France.

This Bot is written in Python3 with the help from the pyTelegramBotAPI and RATP API.

Telegram Bot @ratpbot

Telegram Bot store : https://storebot.me/bot/ratpbot

If you like our bot, please put ⭐️⭐️⭐️⭐️⭐️ in the storebot

# Getting token

Open the file "bot.py" and replace following token with your options:

```
API_TOKEN = 'YOUR TOKEN'
```

This should be your Token received from @Botfather.


# Getting starting  

Starting bot in docker container :

```
docker build -t ratpbot:latest . && docker run -itd -h ratpbot --name ratpbot ratpbot:latest
```

# Commands

Syntaxe :

```
/metro - syntaxe -> /metro <ligne> <arret> : Affiche les horraires du metro
/rer - syntaxe -> /rer <ligne> <arret> : Affiche les horraires du RER
/tram - syntaxe -> /tram <ligne> <arret> : Affiche les horraires du tram
/bus - syntaxe -> /bus <ligne> <arret> : Affiche les horraires du bus
/noctilien - syntaxe -> /noctilien <ligne> <arret> : Affiche les horraires du noctilien
/alert - syntaxe -> /alert <{manif, travaux, alerte}> <{metro,tram,rer}> : Affiche les alertes
```

# Commands :

```
Username, [03.05.16 22:10]
/metro 1 Champs def

ratp 🚇, [03.05.16 22:10]
🚩 Prochains passages du metro ligne 1 à l'arrêt Champs Elysees Clemenceau :
🚉—Champs Elysees Clemenceau: Train a l'approche direction La Defense;
🚉—Champs Elysees Clemenceau: 4 mn direction La Defense;
🚉—Champs Elysees Clemenceau: 9 mn direction La Defense;
🚉—Champs Elysees Clemenceau: 14 mn direction La Defense;
```

```
Username, [03.05.16 22:10]
/metro 1 Champs def

ratp 🚇, [03.05.16 22:10]
🚩 Prochains passages du metro ligne 1 à l'arrêt Champs Elysees Clemenceau :
🚉—Champs Elysees Clemenceau: Train a l'approche direction La Defense;
🚉—Champs Elysees Clemenceau: 4 mn direction La Defense;
🚉—Champs Elysees Clemenceau: 9 mn direction La Defense;
🚉—Champs Elysees Clemenceau: 14 mn direction La Defense;

Username, [04.05.16 10:16]
/bus 132

ratp 🚇, [04.05.16 10:16]
🚉 Stations :
— Place de la Liberte ;
— Camille Risch ;
— Bibliotheque Chevaleret ;
— Edouard Til ;
— Solidarite A. Huon ;
— Groupe Scolaire Jean Jacques Rousseau ;
— Jean le Galleu ;
— Paul Armangot ;
— Bibliotheque F. Mitterrand ;
— Lucien Selva ;
— Audigeois ;
— Mairie d'Ivry Metro ;
— Cite Jardin ;
— Utrillo ;
— Regnault ;
— Hotel de Ville R. Derry ;
— Patay Tolbiac ;
— Porte de Vitry ;
— Julian Grimau Voie Verte ;
— Moulin Vert ;
— Rue des Jardins ;
— Louis Bertrand ;
— Eglise de Vitry ;
— Exploradome ;
— Colonel Fabien ;
— Ledru Rollin ;
— Malraux Ch. Infroit ;
— Oudine ;
— Lavoisier Carrieres ;
— Edouard Tremblay ;
— Fort d'Ivry ;
— Gymnase Auguste Delaune ;
— Camelinat ;
— Maurice Coutant ;
— Voltaire ;

Username, [04.05.16 10:16]
/bus 132 Utrillo

ratp 🚇, [04.05.16 10:16]
🚩 Prochains passages du bus ligne 132 à l'arrêt Utrillo :
🚉—Utrillo: 1 mn direction Vitry Moulin Vert;
🚉—Utrillo: 7 mn direction Vitry Moulin Vert;
🚉—Utrillo: 6 mn direction Bibliotheque F. Mitterrand;
🚉—Utrillo: 16 mn direction Bibliotheque F. Mitterrand;

Username, [04.05.16 10:17]
/bus 132 Utrillo vitry

ratp 🚇, [04.05.16 10:17]
🚩 Prochains passages du bus ligne 132 à l'arrêt Utrillo :
🚉—Utrillo: 0 mn direction Vitry Moulin Vert;
🚉—Utrillo: 7 mn direction Vitry Moulin Vert;
```


Update



```
Username, [27.05.16 18:28]
/go

ratp 🚇, [27.05.16 18:28]
[In reply to Username]
Heee salut tu veux prendre le metro, rer, tram, bus ou noctilien ?  😉😉

Username, [27.05.16 18:28]
metro

ratp 🚇, [27.05.16 18:28]
[In reply to Username]
Quelle ligne de metro ?

Clément, [27.05.16 18:28]
13

ratp 🚇, [27.05.16 18:29]
[In reply to Username]
Quel arret pour la ligne de metro 13 ?

Username, [27.05.16 18:29]
invalides

ratp 🚇, [27.05.16 18:29]
🚩 Prochains passages du metro ligne 13 à l'arrêt Invalides :
🚉—Invalides: 0 mn direction Saint Denis Universit;
🚉—Invalides: 2 mn direction Asnieres Gennevilliers Les Courtilles;
🚉—Invalides: 4 mn direction Saint Denis Universit;
🚉—Invalides: 6 mn direction Asnieres Gennevilliers Les Courtilles;
🚉—Invalides: Train a quai direction Chatillon Montrouge;
🚉—Invalides: 0 mn direction Chatillon Montrouge;
🚉—Invalides: 2 mn direction Chatillon Montrouge;
🚉—Invalides: 4 mn direction Chatillon Montrouge;
```
