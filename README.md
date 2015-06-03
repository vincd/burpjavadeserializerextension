MISC : Introduction au développement d'extensions Burp, Exemple Java sérialization
==================================================================================

Description
-----------
Ce dépôt contient les sources et binaires mentionnés dans l'article MISC.
 * La librairie Java `Jython` permet d'utiliser un script écrit en Python comme extension de Burp.
 * Le script `JavaSerializeXML.py` permet d'ajouter un onglet de visualisation des requêtes Java désérialisées au sein de Burp.
 * La librarie Java `xstream` permet de convertir une requête Java sérialisée en un fichier XML et inversement.

Afin d'utiliser l'extension, il convient d'ajouter le chemin du dossier `jar` de ce repository dans le champ `Folder for loading modules (optional)` de l'onglet `Extender/Options` de Burp. Une fois l'extension lancée, un onglet `Java Serialized XML viewer` apparait lors de la visualisation (onglet Proxy) et de la modification (onglet Repeater) des requêtes au sein de Burp.

Copyright et licence
---------------------
Toutes les ressources de ce dépôt sont distribuées sous licence GPLv3.

Crédits
-------
* Vincent Dépériers
* Thomas Debize
