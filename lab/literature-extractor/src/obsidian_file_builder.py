import yaml
from tqdm import tqdm


class ObsidianFileBuilder:
    TEMPLATE = "---\n" "{tags}\n" "---\n" "\n# References\n\n" "{citations}"

    CITATION_TEMPLATE = "[[{to}|{ref}]]\n"

    def __init__(
        self, works: list[dict], citations: list[dict], target_folder="./result/works"
    ):
        self._target_folder = target_folder
        self._contents = works
        self._citations = citations

    def dump(self, target_folder="./result/works"):
        self._target_folder = target_folder
        created_pages = []
        for c in tqdm(self._contents, desc="Dumping content"):
            created_pages.append(self.dump_page(c))
        return created_pages

    def dump_page(self, content: dict):
        import os
        os.makedirs(self._target_folder, exist_ok=True)
        
        create_citation = lambda d: { "ref": "", **d }

        target = content.pop("target")
        
        target_citations = [create_citation(c) for c in self._citations if c["from"] == target]
        file_name = "{file_name}.md".format(file_name=target)
        file = os.path.join(self._target_folder, file_name)

        with open(file, "w") as f:
            yaml.dump(content, f)
        with open(file, "r") as f:
            file_content = f.read()
        with open(file, "w") as f:
            tags = file_content
            try:
                citations = "".join(
                    [self.CITATION_TEMPLATE.format(**c) for c in target_citations if c is not None]
                )
            except:
                import pdb; pdb.set_trace()
            f.write(self.TEMPLATE.format(tags=tags, citations=citations))

        return file

