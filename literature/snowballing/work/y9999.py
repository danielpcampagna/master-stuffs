# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

cms9999a = DB(Work(
    9999, "",
    due="It does not propose a solution",
    display="cms",
    authors="CMS",
    place=Web,
    ID='GDPREnfo73:online',
    category='unrelated',
    entrytype='misc',
    scholar_ok='@misc{GDPREnfo73:online,\n    author = {CMS},\n    title = {GDPR Enforcement Tracker - list of GDPR fines},\n    howpublished = {https://www.enforcementtracker.com/},\n}',
    backward_steps=1,
))

ezennaya999a = DB(Work(
    9999, "Ezennaya-Gomez-Rethinking Privacy-Knowledge Modeling: About Uncovering Accepted Data Collection Business Practices as Privacy Risks",
    due="Not only unrelated to provenance, yet the submission process to this place is unknown. However, this paper presents a tiny systematic review of the literature of approaches proposing models against factors related to privacy. It can be useful to in our analysis of the state of the art.",
    display="ezennaya",
    authors="Ezennaya-Gomez, Salatiel",
    place=UnknownJournal,
    ID='ezennayaezennaya',
    category='unrelated',
    cluster_id='12010838145598797536',
    entrytype='article',
    link='https://www.inf.ovgu.de/inf_media/downloads/forschung/technical_reports_und_preprints/2020/TechnicalReport+03_2020-p-8396.pdf',
    scholar='https://scholar.google.com.br/scholar?cites=12010838145598797536&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='4LYgQ6gRr6YJ',
    scholar_ok=True,
    forward_steps=1,
))

pandit9999a = DB(Work(
    9999, "Data Privacy Vocabulary (DPV)",
    due="This content introduces import concepts that can be useful in constructing our solution.",
    display="pandit",
    authors="Harshvardhan J. Pandit",
    place=Web,
    ID='DataPriv29:online',
    category='unrelated',
    entrytype='misc',
    scholar_ok='@misc{DataPriv29:online,\nauthor = {Harshvardhan J. Pandit},\ntitle = {Data Privacy Vocabulary (DPV)},\nhowpublished = {https://w3c.github.io/dpv/dpv/},\n}',
    backward_steps=1,
))

pandit9999b = DB(Work(
    9999, "GDPR Data Interoperability Model",
    due="This approach has no direct relation to provenance. However, it provides a rich vocabulary to represent privacy concepts and be useful when for efforts to extends current models due to provide a plethora of terms.",
    display="pandit",
    authors="Harshvardhan J. Pandit, Declan O'Sullivan, Dave Lewis",
    place=Web,
    ID='GDPRData31:online',
    entrytype='misc',
    howpublished='https://openscience.adaptcentre.ie/pb/EURAS2018/',
    category='unrelated',
    backward_steps=1,
))

privacy9999a = DB(Work(
    9999, "Special Privacy – Internet y seguridad",
    due="Not a paper",
    display="privacy",
    authors="Special Privacy",
    place=Web,
    ID='SpecialP57:online',
    category='unrelated',
    entrytype='misc',
    scholar_ok='@misc{SpecialP57:online,\nauthor = {Special Privacy},\ntitle = {Special Privacy – Internet y seguridad},\nhowpublished = {https://specialprivacy.eu/},\n}',
    backward_steps=1,
))

restassured9999a = DB(Work(
    9999, "Erro de privacidade",
    due="Not peer-reviewed",
    display="restassured",
    authors="RestAssured",
    place=Web,
    ID='Errodepr77:online',
    category='unrelated',
    entrytype='misc',
    scholar_ok='@misc{Errodepr77:online,\nauthor = {RestAssured},\ntitle = {Erro de privacidade},\nhowpublished = {https://restassuredh2020.eu/},\n}',
    backward_steps=1,
))

saltarella0a = DB(Work(
    9999, "Privacy Design Strategies and the GDPR: a systematic",
    due="Unrelated to provenance",
    display="saltarella",
    authors="Saltarella, Marco and Desolda, Giuseppe and Lanzilotti, Rosa",
    place=UnknownConference,
    ID='saltarellaprivacy',
    category='unrelated',
    cluster_id='10990844069182628649',
    entrytype='article',
    link='https://www.researchgate.net/profile/Giuseppe-Desolda/publication/352939136_Privacy_Design_Strategies_and_the_GDPR_A_Systematic_Literature_Review/links/62babdc6056dae24e8e91610/Privacy-Design-Strategies-and-the-GDPR-A-Systematic-Literature-Review.pdf',
    scholar='https://scholar.google.com/scholar?cites=10990844069182628649&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='KeNW7XJSh5gJ',
    scholar_ok=True,
))

talha9999a = DB(Work(
    9999, "Towards Semantic Blockchain for Providing Provenance for GDPR Compliance",
    due="It is unclear whether such a paper was submitted to a peer-revision process. Additionally, this paper's aims are out of the scope of our review. In this concept paper, the authors argue in favor of storing the artifacts of the Semantic Web Technology (which have been promoted for representing the activities affected by the GDPR) into a distributed ledger technology to gain complete immutable and ensure traceability.",
    display="talha",
    authors="Talha, Muhammad and Ahmed, Mansoor and Khan, Abid",
    place=UnknownConference,
    ID='talhatowards',
    category='unrelated',
    cluster_id='16313016994856291447',
    entrytype='article',
    link='https://www.researchgate.net/profile/Muhammad-Talha-9/publication/329829616_Towards_Semantic_Blockchain_for_Providing_Provenance_for_GDPR_Compliance/links/5c554110299bf12be3f528d4/Towards-Semantic-Blockchain-for-Providing-Provenance-for-GDPR-Compliance.pdf',
    scholar='https://scholar.google.com.br/scholar?cites=16313016994856291447&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='d8xR2YZ6Y-IJ',
    scholar_ok=True,
    forward_steps=1,
))
