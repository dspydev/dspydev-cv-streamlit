import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Damien Soulé", page_icon=":brain:", layout="centered")

# Display information about Damien Soulé
def display_about():
    st.markdown(
        "<h1 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem; padding-bottom: 50px;'>🧠 À propos</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        Je m'appelle Damien Soulé, je suis né en 1990 à La Réunion (France).
        **Je suis développeur Python IA & Web**. J'utilise également Python pour l'analyse et la visualisation de données. 
        """
    )

    st.markdown("### Avant de devenir développeur Python IA & Web")
    st.markdown(
        """
        \n Avant de devenir développeur Python IA & Web, **j'ai analysé durant 7 ans des données pour des TPE et start-up avec l'approche Evidence-Based Practice**
        en vue d'accompagner les décisions stratégiques. 
        """
    )
    with st.expander("Qu'est-ce que l'Evidence-Based Practice (EBP) ?"):
        st.markdown(
            """
        L'Evidence-Based Practice (EBP) ou la pratique fondée sur des preuves, des faits ou des données en français, consiste 
        à prendre des décisions en utilisant de manière **consciencieuse, explicite et judicieuse les données les plus pertinentes disponibles** 
        pour répondre à une problématique dans dans un contexte donné. 
        L'objectif de cette approche est d'augmenter la probabilité d’obtenir un résultat favorable.
        \n L'analyse de données avec le protocole de l'Evidence-Based Practice peut se faire en 6 étapes itératives :
        \n 1) Formuler une question ou identifier les problématiques à résoudre
        \n 2) Collecter, extraire et transformer des données provenant de plusieurs sources, à savoir :  
        \n 3) Évaluer la fiabilité et la qualité des données
        \n 4) Peser et regrouper les données
        \n 5) Intégrer les données au processus de décision
        \n 6) Évaluer l'impact des décisions
        \n J'explique brièvement les techniques utilisées dans chacune des étapes. Ces étapes sont indicatives bien entendu. 
        """
        )

    with st.expander(
        "**Étape 1** : Formuler une question ou identifier les problématiques à résoudre"
    ):
        st.markdown(
            """
        \n Il s'agit de formuler une question ou d'identifier les problématiques à résoudre par exemple avec le cadre conceptuel PICRC : 
            \n    - **Population** : Quelle est la population concernée ?
            \n    - **Intervention** : Quelle est l’intervention ?
            \n    - **Comparaison** : À quoi l’intervention est-elle comparée ou quelle est l’intervention alternative ?
            \n    - **Résultats** : Quels sont les résultats attendus ? 
            \n    - **Contexte** : Dans quel contexte l’intervention a-t-elle lieu (type d'organisation, secteur, etc.) ?
            """
        )
    with st.expander(
        "**Étape 2** : Collecter, extraire et transformer des données provenant de plusieurs sources"
    ):
        st.markdown(
            """
        \n Une fois la problématique clairement définie, il s'agit de collecter, d'extraire et de transformer 
        des données provenant de plusieurs sources, à savoir : 
        \n    - Les **résultats d'études scientifiques** (par ex. : méta-analyses, revues systématiques, essais randomisés contrôlés). 
        Quelques techniques et outils :
        \n      - Thesaurus
        \n      - Bases de données scientifiques (par ex. : Google Scholar, ABI/INFORM Global, Business Source Elite, PsycINFO)
        \n      - Recherche par titre (TI) et/ou extrait (AB)
        \n      - Utilisation des opérateurs booléens (AND, OR, NOT)
        \n      - Utilisation de la troncature (*)
        \n      - Filtrage (méta-analyses, revues systématiques, essais randomisés contrôlés, etc.)
        \n    - Les **données organisationnelles** (par ex. : ventes, marketing, risques, production, rh, avis des clients).
        Quelques techniques et outils :
        \n      - Python
        \n      - SQL
        \n      - Excel
        \n      - Google Analytics
        \n      - KPI
        \n      - Benchmarks 
        \n      - Sondages internes (par ex. : SurveyMonkey)
        \n      - Lecture de rapports internes  
        \n    - L'avis de plusieurs **professionnels expérimentés** ayant rencontré des problèmes similaires.
        Quelques outils et techniques :
        \n      - Discussion
        \n      - Méthode Delphi
        \n    - Les **préférences et valeurs des personnes impliquées par les décisions** 
        (par ex. : actionnaires, gestionnaires, employés, clients, fournisseurs). 
        Quelques techniques et outils :
        \n      - Groupe de discussion
        \n      - Méthodes quantitatives
        \n      - Méthodes qualitatives
        \n      - Entrevue qualitative semi-structurée  
        """
        )
    with st.expander("**Étape 3** : Évaluer la qualité et la fiabilité"):
        st.markdown(
            """
        Il s'agit d'évaluer la qualité et la fiabilité des données par rapport à la problématique. Voici une checklist des questions
        pour évaluer la pertinence des données de chacune des sources : 
        \n **Concernant les données issues de la littérature scientifique**
        \n - *Questions d’évaluation critique pour déterminer les faiblesses dans une méta-analyse ou une revue systématique* :
        \n   - Est-il peu probable que des études importantes et pertinentes aient été manquées ?		
        \n   - Le processus de sélection des études était-il clairement défini et reproductible ?		
        \n   - Le processus d’extraction des données était-il clairement défini et les résultats présentés dans un tableau ?		
        \n   - La qualité méthodologique de chaque étude a-t-elle été évaluée ?
        \n - *Questions d’évaluation critique pour déterminer les faiblesses dans une étude contrôlée non-randomisée avant-après, ou une étude contrôlée non-randomisée sans pré-test* :
        \n   - Le groupe témoin était-il similaire au groupe d’intervention au début de l’étude ?		
        \n   - Moins de 20 % des sujets ont-ils abandonné ?		
        \n   - Des méthodes de mesure fiables et valides ont-elles été utilisées ?
        \n - *Questions d’évaluation critique pour déterminer les faiblesses dans une étude contrôlée non-randomisée avant-après, ou une étude contrôlée non-randomisée sans pré-test* :
        \n   - Le groupe témoin était-il similaire au groupe d’intervention au début de l’étude ?		
        \n   - L’étude a-t-elle commencé avant l’intervention/exposition ?		
        \n   - L’intervention (ou l’exposition) était-elle indépendante des autres changements dans le temps ?		
        \n   - Des méthodes de mesure fiables et valides ont-elles été utilisées ?
        \n - *Questions d’évaluation critique pour déterminer les faiblesses dans une étude avant-après ou une étude de série chronologique interrompue* :
        \n   - Les critères utilisés pour sélectionner les sujets étaient-ils clairement définis ?		
        \n   - L’étude a-t-elle commencé avant l’intervention/exposition ?		
        \n   - L’intervention (ou l’exposition) était-elle indépendante des autres changements dans le temps ?		
        \n   - Des méthodes de mesure fiables et valides ont-elles été utilisées ?
        \n - *Questions d’évaluation critique pour déterminer les faiblesses dans une étude transversale* :
        \n   - L’échantillon a-t-il été sélectionné aléatoirement ?		
        \n   - La taille de l’échantillon était-elle suffisante ?		
        \n   - Est-il peu probable que la fouille de données ait eu lieu ?		
        \n   - Des méthodes de mesure fiables et valides ont-elles été utilisées ?
        \n - *Questions d’évaluation critique pour déterminer les faiblesses dans une étude qualitative* :
        \n   - La perspective du chercheur est-elle clairement décrite et prise en compte ?		
        \n   - Les méthodes de collecte des données sont-elles clairement décrites ?		
        \n   - Des mesures de contrôle qualité sont-elles utilisées ?
        \n **Concernant les données issues de l'avis de professionnels expérimentés**
        \n - Le praticien a-t-il une expérience approfondie de la question (problème/solution) ? 
        \n - Le praticien a-t-il pu évaluer le résultat et, si oui, des commentaires directs et objectifs étaient-ils disponibles ? 
        \n - Le contexte organisationnel dans lequel le praticien a acquis son expérience peut-il être considéré comme suffisamment régulier et prévisible ? 
        \n - Si applicable, des efforts ont-ils été faits pour réduire les biais en prenant des mesures telles que :
        \n   - Évaluation à l’aveugle
        \n   - Falsification des opinions et jugements
        \n   - Recherche de désaccord
        \n   - Introduction d’un point de vue opposé (par exemple l’avocat du diable)
        \n - Dans quelle mesure les biais cognitifs ont-ils pu affecter le jugement du praticien, tels que :
        \n   - Biais de désirabilité sociale
        \n   - Patternicité/illusion de causalité
        \n   - Biais de confirmation
        \n   - Conformité de groupe
        \n   - Biais de disponibilité
        \n   - Biais d’autorité
        \n   - Biais de résultat
        \n   - Biais de sur-confiance 
        \n - Les preuves ont-elles été acquises de manière valide et fiable ? 
        \n - Les questions ont-elles été formulées de manière adéquate ?
        \n **Concernant l'évaluation des données organisationnelles**
        \n - *Collecte de données organisationnelles*
        \n   - La collecte de données organisationnelles est-elle basée sur un modèle logique ?
        \n   - Les données sont-elles pertinentes pour les processus décisionnels de l’organisation ?
        \n   - Les données sont-elles précises ?
        \n - *Précision des données*
        \n   - Comment les données ont-elles été capturées ?
        \n   - Comment les données ont-elles été traitées ?
        \n   - L’interprétation et le résumé des données ont-ils été basés sur des règles et des directives claires ?
        \n   - Combien de personnes ont été impliquées dans ces étapes ?
        \n   - Le contexte des données est-il pris en compte ?
        \n   - Les données sont-elles fiables - y a-t-il une erreur de mesure ?
        \n - *Fiabilité des données*
        \n   - Les données sont-elles basées sur des mesures objectives/directes ou subjectives/indirectes ?
        \n   - Les mesures rapportées ont-elles une différence de score ?
        \n   - L’ensemble de données est-il suffisamment grand pour éviter le problème du petit nombre ?
        \n   - Lorsqu’un changement ou une différence sous forme de pourcentage est présenté, est-il clair s’il s’agit d’un changement relatif ou absolu ?
        \n   - Lorsqu’une moyenne (moyenne, médiane, mode) est présentée, la variance est-elle claire - l’écart-type est-il rapporté ?
        \n - *Présentation graphique*
        \n   - Lorsqu’un graphique est présenté, peut-il être trompeur ?
        \n   - Y a-t-il une ligne de base ?
        \n   - Les unités sur les axes représentent-elles des étapes égales ?
        \n   - Les nombres s’additionnent-ils ?
        \n   - Le graphique présente-t-il des données manquantes ?
        \n   - Le graphique présente-t-il des données cumulatives ou intervalles ?
        \n - *Corrélation et coefficient de régression*
        \n   - Lorsqu’un coefficient de corrélation ou de régression est présenté, est-il précis ?
        \n   - Y a-t-il des valeurs aberrantes ?
        \n   - R2
        \n   - Restriction de plage
        \n - **Concernant les données issues des valeurs et préférences des parties prenantes**
        \n - L’impact de la décision sur les parties prenantes est-il pertinent ?
        \n - L’impact de la décision sur les parties prenantes est-il éthiquement pertinent ?
        \n - La méthode utilisée pour obtenir les preuves a-t-elle permis aux parties prenantes d’exprimer 
        librement leurs opinions et sentiments concernant le problème ou la décision ?
        \n - Les questions posées étaient-elles formulées de manière adéquate ?
        \n - Un échantillon a-t-il été utilisé ?
        \n - L’échantillon a-t-il été sélectionné aléatoirement ?
        \n - Y a-t-il un biais de sélection ?
        \n - Les statistiques de base de l’échantillon sont-elles comparables à celles de l’ensemble de la population ?
        
        """
        )
    with st.expander("**Étape 4** : Peser et regrouper les données"):
        st.write(
            """
        La pensée bayésienne est un processus de raisonnement qui utilise la formule de Bayes pour mettre à jour nos croyances 
        en fonction de nouvelles informations. 
        \n Elle peut être utilisée pour peser et regrouper les données et aider à la prise de décision en nous permettant 
        d’adapter nos croyances en fonction des données disponibles. 
        \n La formule de Bayes  : $$P(H|E) = \\frac{P(H) P(E|H)}{P(E)}$$
        \n La formule de Bayes peut être décomposée en plusieurs parties:
        \n - **P(H∣E)** est la probabilité de l’événement H étant donné que l’événement E s’est produit (c’est ce qu’on appelle la probabilité postérieure).
        \n - **P(H)** est la probabilité de l’événement H avant que l’événement E ne se produise (c’est ce qu’on appelle la probabilité a priori).
        \n - **P(E∣H)** est la probabilité de l’événement E étant donné que l’événement H s’est produit (c’est ce qu’on appelle la vraisemblance).
        \n - **P(E)** est la probabilité de l’événement E (c’est ce qu’on appelle l’évidence).
        \n Dans le cadre de l'Evidence-Based Practice, pour peser et regrouper les données avec le théorème de Bayes, on peut procéder comme suit :
        \n - **Déterminer P(Htrue)** : Quelle est la probabilité a priori de l'hypothèse d'être vrai ?
        \n - **Peser et regrouper les données issues de l'avis d'experts** : Déterminer la probabilité P(E|Htrue) vs P(E|Hfalse) puis, 
        calculer la probabilité a posteriori P(Htrue|E)
        \n - **Peser et regrouper les données issues de la littérature scientifique** : Déterminer la vraisemblance P(E|Htrue) vs P(E|Hfalse) puis, 
        mettre à jour la probabilité a posteriori P(Htrue|E)
        \n - **Peser et regrouper les données organisationnelles** : Déterminer la vraisemblance P(E|Htrue) vs P(E|Hfalse) puis,
        mettre à jour la probabilité a posteriori P(Htrue|E)
        \n - **Peser et regrouper les données issues de l'avis des parties prenantes** : Déterminer la probabilité P(E|Htrue) vs P(E|Hfalse) puis,
        mettre à jour la probabilité a posteriori P(Htrue|E)
        \n Enfin, après avoir pesé et regroupé les données de plusieurs sources, calculé leur probabilité a priori 
        et mis à jour leur probabilité a posteriori, il s'agit de se poser la question suivante :
        \n - **Les données soutiennent-elle l'hypothèse de départ ?**
        \n ➡️ Voici le calculateur de Bayes du Center for Evidence-Based Management : https://cebma.org/resources-and-tools/bayes/  
            """
        )
    with st.expander("**Étape 5** : Intégrer les données au processus de décision"):
        st.markdown(
            """
        Il s'agit d'intégrer les données de différentes sources au processus de décision. Ces questions guident le processus de décision :
        \n - Les données collectées et analysées fournissent-elles des informations applicables ?
        \n - Si oui, comment traduire ces informations en solution concrète susceptible de résoudre la problématique de départ ?
        \n - Quelle est la valeur attendue (expected value) ? (Expected value = (P1)(outcome 1) + (P2)(outcome 2))
        \n - Est-ce que les résultats possibles pourraient être meilleurs que ceux obtenus auparavant ?
        \n - Le niveau de risque est-il acceptable ?
        \n - Y a-t-il des questions éthiques à considérer ?
        \n - Y a-t-il des variables modératrices à prendre en considération qui peuvent affecter la direction ou la force entre deux variables ?
        
        """
        )
    with st.expander("**Étape 6** : Évaluer l'impact des décisions"):
        st.markdown(
            """
        L'évaluation après action (After Action Review) est une méthode opérationnelle 
        qui a été utilisée par l'armée américaine. 
        \n Aujourd'hui, cette méthode d'évaluation est utilisée par de nombreuses organisation pour son efficacité et sa simplicité.
        Elle est centrée sur quatre questions :
        \n - Que devait-il se passer ?
        \n - Que s'est-il réellement passé ?
        \n - Qu'est-ce qui s'est bien passé et pourquoi ?
        \n - Que peut-on améliorer et comment ?
        
        \n Un AAR comporte :

        \n - Une discussion professionnelle ouverte et honnête
        \n - Participation de tous les membres de l'équipe
        \n - Un accent sur les résultats d'un événement ou d'un projet
        \n - Identification des moyens de pérenniser ce qui a été bien fait
        \n - Élaboration de recommandations sur les moyens de surmonter les obstacles
        \n ➡️ Voici le guide de l'After Action Review : https://www.cebma.org/wp-content/uploads/Guide-to-the-after_action_review.pdf  
        """
        )
    st.success(
        """ 
        \n  ☝️ Pour analyser les données avec l'Evidence-Based Practice, j'utilisais en partie le guide de référence [Evidence-Based Management: How to Use Evidence to Make
        Better Organizational Decisions](https://cebma.org/resources-and-tools/evidence-based-management-book/).
        \n Ce guide méthodologique d'environ 400 pages a été rédigé par les chercheurs et professionnels du
        [Center for Evidence-Based Management (CEBMA)](https://cebma.org/).
        \n Le CEBMA est composé de chercheurs de grandes universités (par ex. : Harvard, Stanford) et de professionnels désireux
        de promouvoir une prise de décision fondée sur des données probantes. 
        """
    )
    st.markdown("### Aujourd'hui, je développe des applications IA & Web")
    st.markdown(
        """
        Aujourd'hui, **je focalise beaucoup plus mon temps sur la création d'application IA & Web** avec Streamlit, Flask ou Django.
        Cependant, il peut m'arriver de faire de l'analyse de données en fonction des besoins. 
        \n Et dans ce cas, j'aime bien utiliser l'approche de l'Evidence-Based Practice car je la trouve plus complète
        que l'analyse de données traditionnelle telle qu'on la connaît aujourd'hui. 
        \n Quoi qu'il en soit, **j'aime la combinaison entre l'analyse de données, l'intelligence artificielle et le développement Web**. 
        De nos jours, ces activités sont de plus en plus interconnectées. 
        """
    )
    st.markdown("### Dans mon temps libre")
    st.markdown(
        """
        \n Dans mon temps libre :
        \n - Je lis et synthétise des articles scientifiques sur l'IA  
        \n - Je continue à programmer, à tester des idées ou à apprendre de nouveaux langages
        \n - Je m'occupe d'un refuge pour les chats errants (environ 15 h/sem)
        \n - Je fais beaucoup de vélo (je me déplace presque totalement à vélo)
        \n - J'aime lire des ouvrages scientifiques (les sciences en général m'intéressent) 
        \n - Je passe du temps avec les personnes que j'aime
        \n - J'aime rencontrer de nouvelles personnes pour échanger sur la Data Science, l'IA et disciplines connexes
        \n Et c'est à peu près tout. Ma vie est très simple. Je suis plutôt casanier 
        même si j'apprécie de travailler dans des espaces de coworking, des cafés ou des médiathèques.
        \n Et ça me va très bien, je me sens heureux comme ça :smiley:  
        La simplicité me permet d'être moins stressé, plus efficace et focalisé dans la réalisation de mes projets. 
        """
    )

    st.success(
        """ 
        PS : J'aime travailler à distance, que ce soit dans des médiathèques, bureaux privatisés 
        ou espaces de coworking proches de mon lieu d'habitation (moins de 20 km).
        \n Je n'aime pas les déplacements inutiles (sauf pour de la formation sur place) qui génèrent du stress, 
        de la perte de temps, coûtent de l'argent et qui plus est, j'ose l'argument, ne sont pas écologiques.
        \n Je n'ai pas peur de travailler dur mais faire 1 à 2 h de trajet par jour 
        pour aller poser mon ordinateur à un autre endroit ne me correspond pas.
        \n De plus, j'utilise ProtonMail et ProtonVPN pour sécuriser les échanges et la connexion (chiffrement AES 256).
        Je peux utiliser le VPN et les critères de sécurité de votre choix. 
        """
    )

    st.markdown(
        """
        <style>
        .icons {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="icons">
            <a href="https://www.linkedin.com/in/damiensoule" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width=32></a>
            <a href="https://github.com/dspydev" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width=32></a>
            <a href="mailto:dspydev@protonmail.com"><img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width=32></a>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ...
def display_experience():
    st.markdown(
        "<h1 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem; padding-bottom: 50px;'> 💼 Expérience</h1>",
        unsafe_allow_html=True,
    )
    experience = [
        {
            "title": "Développeur Python IA & Web",
            "company": "Github.com/dspydev",
            "location": "La Réunion (France)",
            "start_date": "2021",
            "end_date": "Présent",
            "description": """
                Je développe des applications Web avec ou sans solutions IA.
                Je peux également faire de l'analyse de données avec Python, ses librairies et frameworks dédiés. 
                \n J'aime la combinaison entre l'analyse de données, l'intelligence artificielle et le développememnt Web. 
                Mes compétences évoluent en fonction des besoins. 
                \n ➡️ Pour avoir plus d'informations me concernant :
                \n - Retrouvez mes projets et études de cas sur GitHub : https://github.com/dspydev
                \n - Tous mes liens sur Linktr.ee : https://linktr.ee/damiensoule
                \n - Réserver un entretien (45 min) : https://calendly.com/dspydev
                """,
        },
        {
            "title": "Analyste de données",
            "company": "PickaForm",
            "location": "La Réunion (France)",
            "start_date": "2019",
            "end_date": "2022",
            "description": """
            
            \n J'ai analysé les données de différentes sources selon l'approche Evidence-Based Practice pour accompagner le développement stratégique
            d'une start-up d'application métier (No Code) fondée par un ancien ingénieur IBM et IBM Champion, David Grossi.
            \n Avec 25 ans dans l'optimisation de processus métier,
            David Grossi a développé son propre framework [kissjs.net](https://kissjs.net/) pour créer 
            [PickaForm](https://pickaform.fr/index.html#themeColor=dark&ui=start&content=landing).
            
            \n ➡️ **Activités clés** :
            \n Il s'agissait notamment de collecter et d'analyser des données en vue d'aider à :
            \n - Clarifier la mission et la vision de la société 
            \n - Évaluer la situation de la société par rapport à la concurrence
            \n - Travailler sur la stratégie de différenciation
            \n - Analyser les forces et faiblesses
            \n - Analyser les opportunités de croissance et les menaces
            \n - Identifier les axes d'innovation et d'optimisation de l'application 
            \n ➡️ **Méthodologie** :
            \n L'analyse de données avec le protocole de l'Evidence-Based Practice peut se faire en 6 étapes itératives :
            \n 1) Formuler une question ou identifier les problématiques à résoudre
            \n 2) Collecter, extraire et transformer des données provenant de plusieurs sources 
            (littérature scientifiques, experts, organisation, parties prenantes)
            \n 3) Évaluer la fiabilité et la qualité des données
            \n 4) Regrouper et synthétiser les données en vue de répondre à la question, puis, rédiger un rapport
            \n 5) Intégrer les données au processus de décision
            \n 6) Évaluer l'impact des décisions
            \n Pour plus de détails sur la méthodologie utilisée, consultez ma section "À propos".

            """,
        },
        {
            "title": "Analyste de données",
            "company": "Expérience Audio",
            "location": "La Réunion (France)",
            "start_date": "2019",
            "end_date": "2022",
            "description": """
            
            J'ai analysé les données de différentes sources selon l'approche Evidence-Based Practice pour accompagner le développement stratégique
            d'Expérience Audio, une société qui vend du matériel audio Hi-Fi (Haute-Fidélité).
                        
            \n ➡️ **Activités clés** :
            \n Il s'agissait notamment de collecter et d'analyser des données en vue d'aider à :
            \n - Clarifier la mission et la vision de la société 
            \n - Évaluer la situation de la société par rapport à la concurrence
            \n - Travailler sur la stratégie de différenciation
            \n - Analyser les forces et faiblesses
            \n - Analyser les opportunités de croissance et les menaces
            \n - Identifier les axes d'innovation et d'optimisation des services
            
            \n ➡️ **Méthodologie** :
            \n L'analyse de données avec le protocole de l'Evidence-Based Practice peut se faire en 6 étapes itératives :
            \n 1) Formuler une question ou identifier les problématiques à résoudre
            \n 2) Collecter, extraire et transformer des données provenant de plusieurs sources
            (littérature scientifiques, experts, organisation, parties prenantes)
            \n 3) Évaluer la fiabilité et la qualité des données
            \n 4) Regrouper et synthétiser les données en vue de répondre à la question, puis, rédiger un rapport
            \n 5) Intégrer les données au processus de décision
            \n 6) Évaluer l'impact des décisions
            \n Pour plus de détails sur la méthodologie utilisée, consultez ma section "À propos".
                
            """,
        },
        {
            "title": "Autoéditeur",
            "company": "Editions DS",
            "location": "La Réunion (France)",
            "start_date": "2019",
            "end_date": "2022",
            "description": """
            
            Parallèlement à mes activités, j'ai écrit un livre de vulgarisation sur l'Evidence-Based Management sans prétention.
            Je voulais juste mettre quelques-unes de mes synthèses au format papier. 
            
            \n ➡️ **Activités clés** :
             
            \n - Collecter et sélectionner des articles scientifiques (méta-analyses, revues systématiques, essais randomisés contrôlés, etc.)
            \n - Synthétiser les résultats d'études scientifiques (vulgarisation scientifique)
            \n - Corriger, reformuler et vérifier les sources (normes de l'APA)
            \n - Mettre en page le livre au format Kindle et papier
            \n - Créer la charte graphique
            \n - Autopublier le livre Devenez un manager efficace en 21 points clés 
            : managez plus efficacement sur la base de preuves scientifiques sur Amazon et TheBookEdition
            
            """,
        },
        {
            "title": "Président & Analyste de données",
            "company": "DS Partnership",
            "location": "La Réunion (France)",
            "start_date": "2017",
            "end_date": "2022",
            "description": """
            
            J'ai analysé des données pour des start-up avec l'approche Evidence-Based Practice 
            en vue d'accompagner les décisions stratégiques.
            
            \n ➡️ **Activités clés** :
            
            \n L'analyse de données avec le protocole de l'Evidence-Based Practice peut se faire en 6 étapes itératives :
            \n 1) Formuler une question ou identifier les problématiques à résoudre
            \n 2) Collecter, extraire et transformer des données provenant de plusieurs sources
            \n 3) Évaluer la fiabilité et la qualité des données
            \n 4) Regrouper et synthétiser les données en vue de répondre à la question, puis, rédiger un rapport
            \n 5) Intégrer les données au processus de décision
            \n 6) Évaluer l'impact des décisions
            \n Pour plus de détails sur la méthodologie utilisée, consultez ma section "À propos".
            
            """,
        },
        {
            "title": "Manager & Animateur d'unités commerciales",
            "company": "NL International",
            "location": "La Réunion (France)",
            "start_date": "2012",
            "end_date": "2013",
            "description": """
            
            J'ai été animateur d'unités commerciales dans le secteur de l'équilibre alimentaire. 
            
            \n ➡️ **Activités clés** : 

            \n - Préparer le plan d'action commercial (PAC)
            \n - Piloter l'action commerciale
            \n - Prospecter
            \n - Préparer les entretiens de présentation
            \n - Recruter et animer une équipe de distributeurs indépendants
            
            """,
        },
    ]

    for experience in experience:
        st.markdown(f"### {experience['title']}")
        st.markdown(f"**{experience['company']}** - {experience['location']}")
        st.markdown(f"{experience['start_date']} - {experience['end_date']}")
        st.markdown(experience["description"])

    st.markdown(
        """
        <style>
        .icons {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="icons">
            <a href="https://www.linkedin.com/in/damiensoule" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width=32></a>
            <a href="https://github.com/dspydev" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width=32></a>
            <a href="mailto:dspydev@protonmail.com"><img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width=32></a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def display_skills():
    st.markdown(
        "<h1 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem; padding-bottom: 50px;'>🔧 Compétences</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    Je ne reste pas figé. Je m'inscris dans une logique de développeur Python IA & Web généraliste (Full Stack). 
    Sans s'y limiter, voici un aperçu des technologies et outils que je peux utiliser :
    """
    )

    tools_list = [
        ("Langages de programmation", "**Python, JavaScript, SQL, PowerShell**"),
        ("Langages de balisage et de style", "**HTML, CSS**"),
        ("Analyse de données", "**NumPy, pandas, SciPy**"),
        ("Visualisation", "**Seaborn, Plotly, matplotlib**"),
        ("Machine Learning", "**Scikit-learn**"),
        ("Deep Learning", "**TensorFlow, Keras, PyTorch**"),
        ("Traitement du langage naturel", "**spaCy, NLTK**"),
        ("Vision par ordinateur", "**OpenCV**"),
        ("Frameworks Web", "**Django/Flask (Back-End), React (Front-End)**"),
        ("CMS basé sur Django", "**Wagtail**"),
        ("Framework Large Language Models (LLMs)", "**LangChain**"),
        ("Framework Data", "**Streamlit**"),
        ("Feuilles de calculs", "**Excel, Google Sheets**"),
        ("Bases de données", "**MySQL, PostgreSQL**"),
        ("Cloud", "**Microsoft Azure**"),
        ("IDE", "**Jupyter Notebook, Google Colab, VS Code**"),
        ("Contrôle de version / Collaboration", "**Git, GitHub**"),
        ("Système d'exploitation", "**Windows**"),
    ]

    col1, col2 = st.columns(2)
    for i in range(len(tools_list)):
        if i % 2 == 0:
            with col1:
                expander = st.expander(tools_list[i][0])
                expander.markdown(f"{tools_list[i][1]}")
        else:
            with col2:
                expander = st.expander(tools_list[i][0])
                expander.markdown(f"{tools_list[i][1]}")

    st.markdown(
        """
        <style>
        .icons {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="icons">
            <a href="https://www.linkedin.com/in/damiensoule" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width=32></a>
            <a href="https://github.com/dspydev" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width=32></a>
            <a href="mailto:dspydev@protonmail.com"><img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width=32></a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def display_services():
    st.markdown(
        "<h1 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem; padding-bottom: 50px;'>💻 Services </h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        Je propose mes services en freelance en tant que développeur Python IA & Web Full Stack.
        Dans les grandes lignes, je propose les services suivants :
        \n - Développement d'application Web IA (Streamlit, Flask, Django)
        \n - Analyse de données avec Python et les algorithmes Machine Learning si nécessaire (via Google Colab)
        \n - Développement d'application Web avec Django/React (+ possibilité d'intégrer l'IA par la suite)
        \n - Conseils & accompagnement à l'intégration de solutions IA avec Microsoft Azure Cognitive Services.
        """
    )

    st.sidebar.markdown(
    "Réserver un entretien (45 min)<a href='https://calendly.com/dspydev' target=\"_blank\">Prendre un rendez-vous</a>",
    unsafe_allow_html=True,
    )

    st.markdown(
        """
    ### Comment je peux procéder ?
    Je peux développer des applications Web IA en utilisant les librairies (par ex. : Scikit-learn, TensorFlow, Keras, Pytorch) 
    et frameworks habituels (par ex. : Streamlit, Flask, Django)
    ainsi que les outils IA de Microsoft Azure Cognitive Services, un des leaders mondiaux de l'IA.
    \n :gear: **Les librairies et frameworks habituels de l'IA offrent une grande flexibilité et un contrôle sur le processus de développement de modèles IA**. 
    Pour entraîner les modèles IA, ça demande beaucoup :
    \n - d'expertise
    \n - de temps
    \n - de puissance de calculs
    \n - de ressources financières 
    \n :zap: **Si vous êtes limité par le temps et que vous avez des contraintes financières, 
    les API pré-entraînées d'Azure Cognitive Services permettent d'intégrer l'IA dans les applications**,
    notamment avec : 
    \n - les API REST
    \n - les SDK Python fournis par Azure
    \n Les outils d'Azure Cognitive Services offrent de nombreux avantages, à savoir :
    \n - des performances élevées
    \n - l'accès aux dernières avancées en matière d'IA 
    \n - la possibilité de se concentrer sur la création de fonctionnalités innovantes pour les applications plutôt que d'entraîner soi-même des modèles."""
    )

    st.markdown(
        """
    ### Exemples de solutions IA à intégrer dans vos applications
    \n
    Voici une liste indicative de quelques applications possibles avec Azure Cognitive Services :
    """
    )

    col1, col2 = st.columns(2)

    with col1:
        expander = st.expander("Reconnaissance vocale")
        expander.markdown(
            "**Transcrire le discours audible en texte lisible et interrogeable.**"
        )

        expander = st.expander("Synthèse vocale")
        expander.markdown(
            "**Convertir le texte en langage réaliste pour des interfaces plus naturelles.**"
        )

        expander = st.expander("Traduction vocale")
        expander.markdown(
            "**Intégrer la traduction vocale en temps réel à vos applications.**"
        )

        expander = st.expander("Reconnaissance du locuteur")
        expander.markdown(
            "**Identifier et vérifier les personnes qui parlent en fonction de l'audio.**"
        )

        expander = st.expander("Traitement automatique des documents")
        expander.markdown(
            "**Automatiser le traitement des documents pour améliorer l'efficacité et réduire les erreurs.**"
        )

        expander = st.expander("Amélioration du service client")
        expander.markdown(
            "**Améliorer l'expérience client et fournir un service plus rapide et plus précis.**"
        )

        expander = st.expander("Analyse de sentiments")
        expander.markdown(
            "**Analyser les sentiments exprimés dans le texte et comprendre les opinions et les émotions des utilisateurs.**"
        )

        expander = st.expander("Recommandation")
        expander.markdown(
            "**Fournir des recommandations personnalisées aux utilisateurs en fonction de leurs préférences et de leur historique.**"
        )

    with col2:
        expander = st.expander("Compréhension de la cause profonde des anomalies")
        expander.markdown(
            "**Comprendre les causes profondes des anomalies et améliorer les processus métier.**"
        )

        expander = st.expander("Extraction d'informations à partir du contenu")
        expander.markdown(
            "**Extraire des informations précieuses à partir du contenu et prendre des décisions éclairées.**"
        )

        expander = st.expander("Recherche")
        expander.markdown(
            "**Améliorer la recherche de contenu et fournir des résultats plus pertinents.**"
        )

        expander = st.expander("Vision")
        expander.markdown(
            "**Analyser, comprendre et manipuler les images et les vidéos.**"
        )

        expander = st.expander("Langage")
        expander.markdown("**Comprendre, générer et traduire le langage humain.**")

        expander = st.expander("Décision")
        expander.markdown(
            "**Prendre des décisions éclairées en utilisant des données et des modèles prédictifs.**"
        )

        expander = st.expander("Création de chatbots")
        expander.markdown(
            "**Créer des chatbots avancés capables de comprendre et de générer du langage naturel en utilisant les services Azure Bot Service et Azure OpenAI Service.**"
        )

    st.markdown(
        """
        <style>
        .icons {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="icons">
            <a href="https://www.linkedin.com/in/damiensoule" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width=32></a>
            <a href="https://github.com/dspydev" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width=32></a>
            <a href="mailto:dspydev@protonmail.com"><img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width=32></a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def display_qualifications():
    st.markdown(
        "<h1 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem; padding-bottom: 50px;'>🎓 Qualifications</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        J'ai obtenu des dizaines de certificats et badges (et je continue à en obtenir) mais plutôt que de les lister tous, 
        je vous présente ci-dessous quelques-uns d'entre eux :
        """
    )

    qualifications_list = [
        "[**Machine Learning Specialization**](https://www.coursera.org/account/accomplishments/specialization/VJQJCKG4QWGD), Stanford University et DeepLearning.AI",
        "[**Introduction to Statistics**](https://www.coursera.org/account/accomplishments/verify/R7X2G7868MJE), Stanford University",
        "[**Building Artificial Intelligence**](https://certificates.mooc.fi/validate/0lfq8g2h06uq), University of Helsinki",
        "[**Elements of Artificial Intelligence**](https://certificates.mooc.fi/validate/h8833da9k2a), University of Helsinki",
        "[**Google Data-Analytics Certificate (équivalent Bachelor)**](https://www.coursera.org/account/accomplishments/professional-cert/C2HHS5LM4YTF), Google Career Certificates",
        "[**Computer Science (Python Specialization)**](https://www.codecademy.com/profiles/damiensoule/certificates/05009c20e9174378acd37e6c2d0fbfc4), Codecademy",
        "[**Front-End Engineer**](https://www.codecademy.com/profiles/damiensoule/certificates/2682884a0719474f96407efe432fdd87), Codecademy",
    ]

    for qualification in qualifications_list:
        st.markdown(f"- {qualification}")

    st.success(
        """Pour consulter tous mes certificats et badges, 
        visitez mon profil Linkedin : https://www.linkedin.com/in/damiensoule/details/certifications/
        """
    )

    st.markdown(
        """
        <style>
        .icons {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="icons">
            <a href="https://www.linkedin.com/in/damiensoule" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width=32></a>
            <a href="https://github.com/dspydev" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width=32></a>
            <a href="mailto:dspydev@protonmail.com"><img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width=32></a>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.sidebar.image("./avatar.PNG", width=200)

st.sidebar.markdown(
    """
<a href="https://www.linkedin.com/in/damiensoule" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width=32></a>
<a href="https://github.com/dspydev" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width=32></a>
<a href="mailto:dspydev@protonmail.com"><img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width=32></a>
""",
    unsafe_allow_html=True,
)

st.sidebar.title("Damien SOULÉ")
st.sidebar.markdown(
    """
    Je suis développeur Python avec une orientation IA & Web (Full Stack).
    Je suis également Data-Analyst.
    J'ai créé ce CV en ligne avec Python et Streamlit, et un peu d'HTLM et de CSS.
    """
)

st.sidebar.markdown(
    "Réserver un entretien (45 min)<a href='https://calendly.com/dspydev' target=\"_blank\">Prendre un rendez-vous</a>",
    unsafe_allow_html=True,
)

nav = st.sidebar.radio(
    " ", ["À propos", "Expérience", "Compétences", "Services", "Qualifications"]
)
if nav == "À propos":
    display_about()
elif nav == "Expérience":
    display_experience()
elif nav == "Compétences":
    display_skills()
elif nav == "Services":
    display_services()
elif nav == "Qualifications":
    display_qualifications()
