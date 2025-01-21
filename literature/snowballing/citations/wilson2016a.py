# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import wilson2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, wilson2016a, ref="Wilson, Shomir, Florian Schaub, Aswarth Abhilash Dara, Frederick Liu, Sushain Cherivirala, Pedro Giovanni Leon, Mads Schaarup Andersen, et al. 2016. “The Creation and Analysis of a Website Privacy Policy Corpus.” In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 1330–40. Berlin, Germany: Association for Computational Linguistics. https://doi.org/10/gf9t98.",
    contexts=[],
))

