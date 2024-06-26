from prov.dot import prov_to_dot
import prov.model as prov

base_path = "./questions/CQ08/"

with open(base_path + "database.ttl") as f:
    rdf_content = f.read()

prov_doc = prov.ProvDocument.deserialize(content=rdf_content, format="rdf", rdf_format="turtle")
dot = prov_to_dot(prov_doc)
dot.write_png(path=base_path + 'database.png')