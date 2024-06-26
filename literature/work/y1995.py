# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

directive1995a = DB(Work(
    1995, "Directive 95/46/EC of the European Parliament and of the Council of 24 October 1995 on the protection of individuals with regard to the processing of personal data and on the free movement of such data",
    due="Unrelated to GDPR",
    display="directive",
    authors="Directive, EU",
    place=OJEO,
    ID='directive1995directive',
    category='unrelated',
    entrytype='article',
    number='281',
    pp='31--50',
    scholar='https://scholar.google.com/scholar?cites=17779553495450173854&as_sdt=2005&sciodt=0,5&hl=pt-BR',
    scholar_ok='@article{directive1995directive,\n  title={Directive 95/46/EC of the European Parliament and of the Council of 24 October 1995 on the protection of individuals with regard to the processing of personal data and on the free movement of such data},\n  author={Directive, EU},\n  journal={Official Journal of the European Communities},\n  volume={38},\n  number={281},\n  pages={31--50},\n  year={1995}\n}',
    volume='38',
    backward_steps=1,
))

gruber1995a = DB(Work(
    1995, "Toward principles for the design of ontologies used for knowledge sharing?",
    due="unrelated to GDPR",
    display="gruber",
    authors="Gruber, Thomas R",
    place=IJHCS,
    ID='gruber1995toward',
    category='unrelated',
    cluster_id='5645037946590867660',
    entrytype='article',
    link='https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.101.9025&rep=rep1&type=pdf',
    number='5-6',
    organization='Elsevier',
    pp='907--928',
    scholar='https://scholar.google.com/scholar?cites=5645037946590867660&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='zDAmjho0V04J',
    scholar_ok=True,
    volume='43',
    backward_steps=1,
))

ozsoyoglu1995a = DB(Work(
    1995, "Temporal and real-time databases: A survey",
    due="unrelated to GDPR",
    display="ozsoyoglu",
    authors="Ozsoyoglu, Gultekin and Snodgrass, Richard T",
    place=IEEETKDE,
    ID='ozsoyoglu1995temporal',
    category='unrelated',
    cluster_id='15778634429168857601',
    entrytype='article',
    link='https://raptor.cs.arizona.edu/people/rts/pubs/TKDEAug95.pdf',
    number='4',
    organization='IEEE',
    pp='513--532',
    scholar='https://scholar.google.com/scholar?cites=15778634429168857601&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='AbJbH2r4-NoJ',
    scholar_ok=True,
    volume='7',
    backward_steps=1,
))
