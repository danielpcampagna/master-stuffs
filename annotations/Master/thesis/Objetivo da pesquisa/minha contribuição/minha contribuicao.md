Minha principal contribuição com essa dissertação é propor uma extensão de um modelo de proveniência já existente. Algumas dessas contribuições já foram publicadas [neste artigo](https://sbbd.org.br/2020/wp-content/uploads/sites/13/2020/09/Archieving-GDPR-ST1.pdf) no SBBD. As tabelas abaixo as apresenta. Perceba que algumas faz sentido serem analisadas (por exemplo, a extensão de existir uma relação entre justificativas afins. Vale o esforçe de verificar se na literatura essa relação existe);

<table>
	<caption>
		<b>Table 2. Plumbing extensions change the GDPR data provenance model highlevel classes or relations by adding new elements or changing their use. </b>
		Available in <a href="https://sbbd.org.br/2020/wp-content/uploads/sites/13/2020/09/Archieving-GDPR-ST1.pdf">this article</a>.
	</caption>
	<tr>
		<th> GDPR Text </th>
		<th> Limitations </th>
		<th> Extensions </th>
	</tr>
	<tr>
		<td>
			“Where personal data relating to a data subject are collected from the data subject, the controller shall provide [. . . ] the fact that the controller intends to transfer personal data to a third country or international organization [. . . ].” [Council of European Union 2016, point f ) of Art. 13(1)].
		</td>
		<td>
			The GDPR model enables subjects to know whether the controller intends to transfer their data; however, the model does not provide a direct relationship between the controllers.
		</td>
		<td>
			(i) A new self-relationship (wasAttributedTo) for Controller; and (ii) use Disclose class to represent this transfer.
		</td>
	</tr>

	<tr>
		<td>
			“The controller shall [. . . ] provide the data subject with [. . . ] the period for which [her] personal data will be stored, or if that is not possible, the criteria used to determine that period” [Council of European Union 2016, point a) of Art. 13(2)].
		</td>
		<td>
			Although it is possible to represent when a purpose ends, the authors of the GDPR model design patterns explicitly suggest that the obtention of that purpose-ending information does not occur at the beginning.
		</td>
		<td>
			When personal data are obtained, both startedAtTime and endedAtTime relations should be created with their Time annotation, denoting the Valid Time [Ozsoyoglu and Snodgrass 1995], those personal data will be stored.
		</td>
	</tr>

	<tr>
		<td>
			“Where the controller intends to further process [. . . ] for a purpose other than that for which the personal data were collected, the controller shall [. . . ]” reveal to data subject its intentions. [Council of European Union 2016, Art. 13(3)].
		</td>
		<td>
			The current model does not inform whether a Justify is compatible with another one.
		</td>
		<td>
			(i) A new self-relationship (wasCompatibleWith) for Justify; (ii) A new PseudonymizedData class, as a PersonalData subclass, which instances representing pseudonymized information from all person; and (iii) all those further processes informed by a Justify that wasCompatibleWith another must only use PseudonymizedData [Council of European Union 2016, point e) of Art. 6(4)].
		</td>
	</tr>
</table>

<table>
	<caption>
		<b>Table 3. Porcelain extensions are focused on improving the GDPR data provenance model understanding by providing new subclasses that better express some GDPR articles’ points.</b>
		Available in <a href="https://sbbd.org.br/2020/wp-content/uploads/sites/13/2020/09/Archieving-GDPR-ST1.pdf">this article</a>.
	</caption>

	<tr>
		<th>Limitation</th>
		<th>Extension</th>
	</tr>
	
	<tr>
		<td>
			The further processing for archiving purposes in the public interest, scientific or historical research purposes, or statistical purposes are often cited in the text of the law [Council of European Union 2016, Art. 5, 9, 14, 17, 21, 89].
		</td>
		<td>
			A new ArchivingResearchingStatisticalPurposesJustify class, as sublclass of Justify, which represents those purposes.
		</td>
	</tr>

	<tr>
		<td>
			Article 9 lists a set of purposes categories of personal data, which demands special justification to process. [Council of European Union 2016, Art. 9(1)]
		</td>
		<td>
			We suggest the following new classes, all of them subclasses of PersonalData: RacialEthnicData, PoliticalOpinionsData, BeliefData, MembershipData, GeneticData, BiometricData, HealthData, SexLifeData, and SexualOrientationData.
		</td>
	</tr>

	<tr>
		<td>
			Points b), d), e), and i) of Article 9 explain situations in which the special categories of personal data must not be prohibited [Council of European Union 2016, Art. 9(2)].
		</td>
		<td>
			We suggest the following new classes: EmploymentSecurityObligation, as a subclass of LegalObligation (point b)); CommunityInterest (point b)) and PublicHealthInterest (point i)), both subclasses of PublicInterest; and PublicData, as a subclass of PersonalData, and Publish, as a subclass of Process (point e)).
		</td>
	</tr>

	<tr>
		<td>
			Article 16 lays down rectification processes; however, the GDPR model does not propose a class representing that
		</td>
		<td>
			A new Rectification, subclass of Process, that represents a rectification process.
		</td>
	</tr>

	<tr>
		<td>
			Article 21 defines the right of objection; however, the GDPR model does not propose a class to represent this right.
		</td>
		<td>
			A new class ObjectionRequest, as a subclass of Request, that represents a subject’s objection.
		</td>
	</tr>
</table>

<table>
	<caption>
		<b>Table 4. Wallpaper extensions present new additions to enrich the model with the information to be compliant with GDPR, although there are other means to present that information to the data owners.</b>
		Available in <a href="https://sbbd.org.br/2020/wp-content/uploads/sites/13/2020/09/Archieving-GDPR-ST1.pdf">this article</a>.
	</caption>

	<tr>
		<th>GDPR Text</th>
		<th>Limitations</th>
		<th>Extensions</th>
	</tr>

	<tr>
		<td>
			“The data subject shall have the right to obtain from the controller [. . . ] any available information as to their source.” [Council of European Union 2016, point g) of Art. 15(1)].
		</td>
		<td>
			The GDPR model does not present any information about the data source.
		</td>
		<td>
			A new SourceExplanation entity, in which a PersonalData is associated with it, representing a document that describes the source of this data
		</td>
	</tr>

	<tr>
		<td>
			The data subject shall have the right to obtain from the controller [. . . ] the existence of automated decision-making [. . . ] [and] meaningful information about the logic involved [. . . ].” [Council of European Union 2016, point h) of Art. 15(1)].
		</td>
		<td>
			The GDPR model does not present any that different information about the existence of automated decision-making.
		</td>
		<td>
			A new AlgorithmExplanation entity, in which an automated Process is associated with it, representing a document that describes the logic involved in that process.
		</td>
	</tr>

	<tr>
		<td>
			“Where personal data are transferred [. . . ] the data subject shall have the right to be informed of the appropriate safeguards [. . . ].” [Council of European Union 2016, Art. 15(2)] such as describe Art. 46, 47, and 49, also “the means by which to obtain a copy of them or where they have been made available” [Council of European Union 2016, point f ) of Art. 13(1), 14(1)].
		</td>
		<td>
			The GDPR model does not represent any information about the appropriate safeguards of the controller, by concerning their availability to lawfully transfer of personal data.
		</td>
		<td>
			A new EvaluationOfAdequacy entity, in which a Controller is associated with it, representing a document that describes that required information.
		</td>
	</tr>
</table>

