MISC 82 Introduction au développement d'extensions Burp - Exemple sérialisation Java
==================================================================================

Description
-----------
Ce dépôt contient les sources et binaires de l'extension Burp `sérialisation Java` décrite dans l'article `Introduction au développement d'extensions Burp` du MISC n°82.  
Les ressources sont regroupées ainsi :
```
+---JavaSerializeXML.py	: Le code Jython de l'extension
|
+---exemple				: Un exemple d'application Java échangeant des objets Java sérialisés-compressés en HTTP
|   +---bin				: Les fichiers .class de l'application et le fichier jar de la classe Employee
|   +---src				: Les fichiers sources des classes de l'application
```


Usage
-----
### Extension
0. Sélectionner le chemin vers l'interpréteur Jython au sein de Burp ; 
1. Sélectionner un dossier dans le champ `Folder for loading modules (optional)` de l'onglet `Extender/Options` de Burp ;
2. Ajouter les fichiers JAR de la bibliothèques XStream et de la classe Java `Employee` dans le dossier sélectionné précédemment ;
3. Charger l'extension `JavaSerializeXML.py` au sein de l'onglet `Extender` : un onglet `Java serialized-to-XML editor` apparait lors de la visualisation (onglet Proxy) et de la modification (onglet Repeater) des requêtes au sein de Burp.

### Exemple d'application échangeant des objets Java sérialisés-compressés
0. Démarrer le serveur Web `cd exemple/bin && java ServerWeb`
1. Démarrer le client Web en spécifiant un proxy `cd exemple/bin && java -Dhttp.proxyHost=localhost -Dhttp.proxyPort=8080 ClientWeb`

Dépendances
-----------
### Pour l'extension
* La bibliothèque `Jython`, téléchargeable [ici](http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar)
* La bibliothèque `XStream`, téléchargeable [ici](https://nexus.codehaus.org/content/repositories/releases/com/thoughtworks/xstream/xstream/1.4.8/xstream-1.4.8.jar), qui assure la conversion objet Java sérialisé-compressé en XML et inversement


Copyright et licence
---------------------
Toutes les ressources de ce dépôt sont distribuées sous licence GPLv3.


Crédits
-------
* Vincent Dépériers
* Thomas Debize
