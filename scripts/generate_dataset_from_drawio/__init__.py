from N2G import drawio_diagram

from diagrams import RDFDiagram
from diagrams.base import Diagram
from library import Library
from rdf import RDFConstructorFromGraffoo


if __name__ == "__main__":
    diagram_path = "base.drawio"
    diagram_name = "CQ28 | Dataset"
    library_path = "graffoo v1.1.xml"

    # diagram = Diagram.from_drawio(diagram_path, diagram_name)
    # library = Library.from_file(library_path)
    # components = library.generate_components_from_elements(diagram.all_nodes)
    # # [print(c["label"], c["category"].category) for c in components]
    # # print("---")

    # subcomponents = library.generate_components_from_elements(components[1]["children"])
    # # [print(c["label"], c["category"].category) for c in subcomponents]

    RDFConstructorFromGraffoo(library_path).construct(diagram_path, diagram_name)
