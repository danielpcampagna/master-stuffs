import glob

from .src.snowballing_extractor import WorkExtractor, CitationExtractor
from .src.obsidian_file_builder import ObsidianFileBuilder


if __name__ == "__main__":
    # # Development
    # work_extractor = WorkExtractor(glob.glob("./samples/work.py"))
    # citation_extractor = CitationExtractor(glob.glob("./samples/citations.py"))
    
    # Production
    work_extractor = WorkExtractor(glob.glob("../../literature/work/*.py"))
    citation_extractor = CitationExtractor(glob.glob("../../literature/citations/*.py"))

    work_extractor.parse_all()
    citation_extractor.parse_all()

    pages = ObsidianFileBuilder(work_extractor.work, citation_extractor.citations).dump()
