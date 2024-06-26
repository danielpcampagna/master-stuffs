# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import piras2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, piras2019a, ref="Piras, Luca, Mohammed Ghazi Al-Obeidallah, Andrea Praitano, Aggeliki Tsohou, Haralambos Mouratidis, Beatriz Gallego-Nicasio Crespo, Jean Baptiste Bernard, et al. 2019. “DEFeND Architecture: A Privacy by Design Platform for GDPR Compliance.” In Trust, Privacy and Security in Digital Business, edited by Stefanos Gritzalis, Edgar R. Weippl, Sokratis K. Katsikas, Gabriele Anderst-Kotsis, A Min Tjoa, and Ismail Khalil, 78–93. Lecture Notes in Computer Science. Springer International Publishing.",
    contexts=[],
))

