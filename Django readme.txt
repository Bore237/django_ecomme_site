Etappe django
- Creer un repertoire project
- Ouvrir invite de commande et se positionner sur ce repertoire
- Creer un dossier(django-wepp-app)
- Faire un git init 
- Creer un environement virtuel (python -m ven ___non dossier)
- Activer environement virtuel ./nom/Scripts/activate
- Revenir sur le dossier source Installer Django pip django
- installer freeze (pip freeze > requirements.txt
- Lancer environement django (django-admin startproject __merchex
- Se positioner sur le fichier et Lancer le serveur (python manage.py  runserver)
- recuperer adress et ouvrir dans un navigateurs

- Creer une base de données avec (python manage.py migrate
- creer le repertoitre application (python manage.py startapp listings) 
- Ajouter listing a notre projet (setings.py ajouter listing)

//Creer une vue 
- Le principe est simple on créé un modèle URL pour etre a ecoute d'une  réquêtte pour 
une URL donnéé puis appeler une vue specifique pour genérer une page
- lancer le serveur et appliquer le lien
- il faut utiliser les pages ((listings)views => definie les function et (merchex)utls=> les modèle url)
- inclure listings dans utls et configurer les vue et les modeles
- from django.http import HttpResponse (Exemple de vues)
def hello(request): 
    return HttpResponse('<h1>Hello Django! </h1>')
	
////////Base de doneée
- Pour utiliserune base de donné il faut créé un modele qui n'est rien d'autre qu'une class  
donc c'est attribut sont stoker dans une base de donnée  d'ou le non de champs
- class Band(models.Model):  
    name = models.fields.CharField(max_length =100)
- Ajouté le chanmpss sur dans notre base de donnée en utilisantla migration
- Avec la commande(python manage.py makemigrations) Django parcours notre fichier models et creer les bases de 
données en fonction des différentes modifications
- Puis avec (python manage.py migrate) on ce rassure de l'etat des migration

/********Passons au shell python avec (python manage.py shell)******/
- importer notre models au niveau du shell (listings.models import Band)
- import l'object (from listings.models import __nom)
- extencier object (band = Band())
- Initialiser le champs name de la table (band.name = 'Borel'
- sauvegader (band.save) et automatiquement id sera créé
- le racourci pour cette comande est: (band = Band.objects.create(name='salot bbb'))
- (Band.objects.count()) liste le nombre d'élément contenue dans la base de donnée)
- pour plus de detail entrer(Band.objects.all())

/***********Design pattern (les bonnes pratique) => utiliser les gabarit de Django)*******/
- il faut creer un fichier html pour chaque vue (listings/template/listings/__nom.html)
- if faut utiliser objet render comme suit(return render(request, 'listings/hello.html', {'band': bands}))
- ecrire le meme extension dans le fi html entre deux guillemet {{first_band.name}}
- pour utiliser les information d'une bansee de donnée dans le fichier html on utiille ({{Nom.index.attribut}})
- il serai difficile de lorsque les variable deviene nombreux pour cela on utilise les balises de gabarits qui 
sont appeler comme suite: ( {% for band in band %}
							<li>{{bands.name}}</li>
							{% endfor %}) 
- Utiliser un filtre on'utilise le (|) <li>{{band.name|upper}}</li>

/**********Creer un gabarit de style avec django***********/
- Creer un fichier html qui contiendra lec ode html de notre page générique dans le body inserer la commande:
({% block content %}{% endblock %})
- puis creer un dossier static et listings qui vont contenir mon fichier de style css pour la mise en forme de notre page
- inclu notre feuillle de style dans notre fichiier html(<link rel="stylesheet" href="{% static  'chemin' %}"/>) et charger 
le fichier de style ({%load static%})
- inclule le fichier html dans tous les autres vues avce les commandes
{% extends 'listings/base.html' %}
{% block content %}  {% endblock %}


/*************Les methodes CRUD ********************/
- Creer un supperutilisateur (python manage.py createsuperuser)
- Modifier le fichier admin.py dans listings
	user : Django_User
	Password: Borel237
- Modifier le fichier admin dans listing pour importe nos bases de donnée
- on 'utilise de commande (admin.site.register(Band, BandAdmin)) il faut prealable importer nos base de donées dans models
- Utiliser la classe class BandAdmin(admin.ModelAdmin):
    list_display = ('id',.... nons colones)
- ouvrer le navigateurs et réaliser les operation CRUD 

/*************Gerer les erreurs de maigrations********************/
- Afficher toutes les migrations (python manage.py showmigrations)
- Annuler la migration actuelle en se repositionant sur la une migration précédente avec la commande 
	(python manage.py migrate nom de la migration precedente)
- Une fois le migrations annuler nous pouvont la suprimer	
- modifier le model et fareune migration 

 /**************Les operations CRUD pour les operateur finaux ********///////
 /////////Vue en liste
 - renomer le nom de nos fichiers en (nom du models types de vue.html)
 - creer la vue avec (non_moddel = modele.objects.all()) pui executer render(request, 'chemins', {nom_model : model}) 
  
/////Vue détailler////////////////////////
- On creer url avec la commande(path('bands/<int:band_id>/')
-  On creer la vue la vue associer avec comme d'habitude cette fois on utilise la 
commmande(band = Band.objects.get(band_id = id)) qui nous permet d'obtemir un object en fonction de id
- On creer une gabarit dans un fichier html et utiliser la commande({band.get_tables_display)
- Pour lier une liste de vue et une vue détailer on ajuste url comme suite (path('bands/<int:band_id>/', views.band_detail, name = 'band-detail'),)
- on peut grace a la commande("{URL 'name'}")  aceder a n'importe quelle gabarit de page


/*********************Creation d'un formulaire*****************************/
- il faut créér un fichier form.py et definie une fonction qui designera notre page
- importer le fichier et notre fonctionn dans notre fichier de vue
- Creer le gabbarit html et executer notre fichier python avec ({{ non fichier}} précédé de la commande ({% csrf_token%}))
- donner url de notre vue
- syntace html pour gerer les formulaire:     
	<form action="" methode="post" novalidate>
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Envoyer">
    </form>
	
- envoyer les messages avec send_mail et form.is_valid():
	        if form.is_valid():
            send_mail(subject= f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us form',
                      message= form.cleaned_data['message'],
                      from_email = form.cleaned_data['email'],
                      recipient_list = ['admin@merchex.xyz'],
                      ) 
/******simuller envoie des message: inserer la commande si dessous dans le fichier settings.py
EMAIL_BACKEND = \
'django.core.mail.backend.console.EmailBackend'
-  faire la redirection pour ecité les doublons en important  (django.shortcuts import redirection) et faire un return redirect('email-sent')


/***********Enregistrer les donn"e dans la base  de donnée **********/
- Ici on ne créée plus la base de donnée une foir notre url renseigner
- Dans notre fichier form.py on appel juste le base de donnée donc on veut insérer les informations (from listings.models import Band)
- on defini notre class qui vaas designer de facon automatique notre foemulaire (    class Meta:
																						model = Band
																						field ='__all__')
- Dans notre vue on save notre basae de donnée quand il s'agit d'une requette post (nonbase.save())

