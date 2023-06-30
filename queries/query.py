import pathlib
import os

import rdflib
import fire


def query(question: str, save: bool = False):
    basedir = f"./questions/{question}/"
    dataset = os.path.join(basedir, "database.ttl")
    query = os.path.join(basedir, "query.sparql")

    g = rdflib.Graph()
    g.parse(dataset)

    with open(query, "r") as fr:
        knows_query = fr.read()
        qres = g.query(knows_query)

        result_path = os.path.join(os.path.dirname(query), "result.ttl")
        
        save_method = print
        if save:
            fw = open(result_path, "w")
            save_method = fw.write

        # save_method(f"{len(qres)}")
        # for q in qres.quads():
        #     print(q)
        for row in qres:
            # import pdb; pdb.set_trace()
            save_method(", ".join([f"'{c}'" for c in row]))
            save_method("\n")
        
        if save:
            fw.close()

if __name__ == "__main__":
    fire.Fire(query)
    # import rdflib
    # g = rdflib.Graph()
    # g.parse("./coolharsh55-data.ttl")
    # # g.parse("./questions/Q08/database.ttl", format="turtle")


    # knows_query = """
    # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    # PREFIX rdf: <https://www.w3.org/1999/02/22-rdf-syntax-ns#>
    # PREFIX owl: <http://www.w3.org/2002/07/owl#>
    # PREFIX time: <https://www.w3.org/TR/owl-time/>
    # PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    # PREFIX : <http://example.org/GDPRov-v0.8#>


    # SELECT ?dataCategory ?durationTime ?duration ?durationUnit ?durationComment ?hasDuration
    # WHERE {
    #     ?dataCategory a*/rdfs:subClassOf* :PersonalData .
    #     ?step :generatesData ?dataCategory ;
    #         :isPartOfProcess/:hasStorageCondition ?storageCondition .

    #     ?storageCondition :hasDuration ?duration .
    #     ?duration rdf:comment ?durationComment ;
    #         time:numericDuration ?durationTime ;
    #         time:unitType ?durationUnit .
    # }
    # """
    
    # qres = g.query(knows_query)
    # print(len(qres))
    # for row in qres:
    #     print(row)
    #     # print(f"{row.aname} knows {row.bname}")