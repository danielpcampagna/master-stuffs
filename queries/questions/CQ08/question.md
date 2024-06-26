For each category of personal data, list the period for which the data will be retained e.g. one month? one year?
As a general rule data must be retained for no longer than is necessary for the purpose for which it was collected in the first place.

---

In Pandit's model[1], the category of personal data is defined as subclasses of the PersonalData class. The definition of the existing categories thus lies in the context where the model is instantiated.
<!-- . Additionally, Pandit has argued that this question demands the  -->

Looking at the question, the expected result is a list of tuples containing the category of data and the respective period (or retention rule) for which the data will be retained. Both Ujcich [2] and DPV [3] ontologies have designed this information attached to the legal (or justification) base that legitimates this data collection.

Concerning the retention rule, Pandit [1] has argued that this information should be fed from the privacy policy graph. Hence, it can be represented retrospectively.

Besik and Freytag [4] have proposed the RetentionPolicy class to represent the data retention period. However, they lack proposing an example of how to use this. The further literature addressing this issue [5,6,7] has identified four possible cases that describe the retention period regarding some data, namely:

(1) Fixed period: when the retention period is explicit (e.g., 30 days). According to Oltramari, Alessandro, et al.'s [5] analysis of privacy policies describing how long they store user data, this case corresponds to 40% of them.
(2) Fixed date: when the validity time is indicated (e.g., 31 December 2022);
(3) After purpose: when the data is stored as long as it is needed to perform a requested process;
(4) Indefinite: when the retention period is not explicit, corresponding to 7% of the total [5].

---
# References:

[1] Pandit, Harshvardhan J. "Representing activities associated with processing of personal data and consent using semantic web for GDPR compliance." Trinity College Dublin, School of Computer Science & Statistics (2020).
[2] Ujcich, Benjamin E., Adam Bates, and William H. Sanders. "A provenance model for the European Union general data protection regulation." International Provenance and Annotation Workshop. Springer, Cham, 2018.
[3] ?
[4] ?
[5] Oltramari, Alessandro, et al. "PrivOnto: A semantic framework for the analysis of privacy policies." Semantic Web 9.2 (2018): 185-203.
[6] Gerl, Armin, and Dirk Pohl. "Critical Analysis of LPL according to Articles 12-14 of the GDPR." Proceedings of the 13th International Conference on Availability, Reliability, and Security. 2018.
[7] Pandit, Harshvardhan J., Axel Polleres, Bert Bos, Rob Brennan, Bud Bruegger, Fajar J Ekaputra, Javier D Fernández, et al. 2019. “Creating A Vocabulary for Data Privacy.” In The 18th International Conference on Ontologies, DataBases, and Applications of Semantics (ODBASE2019), 17. Rhodes, Greece.