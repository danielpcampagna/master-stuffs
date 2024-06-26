from N2G import drawio_diagram

from diagrams import REDiagram, RDFDiagram
# from .diagrams.helpers import clone_diagram


# def build_diagram(diagram_path: str, target_path: str, diagram_name: str = None):
#     diagram = drawio_diagram()
#     diagram.from_file(diagram_path)

#     if diagram_name is not None:
#         diagram.go_to_diagram(diagram_name=diagram_name)

#     name = diagram.current_diagram.get("name")
#     diagram.current_diagram.set("name", name + "-build")

#     # new_id = diagram.current_diagram_id + "-build"
#     # new_name = diagram.current_diagram.get("name") + "-build"
#     # diagram = clone_diagram(diagram, new_id, new_name)

#     # Select cloned diagram
#     # diagram.go_to_diagram(diagram_name=new_name)

#     d = REDiagram(diagram)

#     d._diagram.delete_node(ids=[n.get("id") for n in d.note_nodes])
#     d._diagram.delete_link(ids=[n.get("id") for n in d.note_edges])

#     d._diagram.dump_file(target_path)


if __name__ == "__main__":
    # build_diagram("./.data/Solar.drawio", "Solar-build.drawio")
    diagram_path = "base.drawio"
    diagram_name = "CQ28"

    diagram = RDFDiagram.from_drawio(diagram_path, diagram_name)
    # diagram.to_turtle("data.ttl")
