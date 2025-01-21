import ast

from tqdm import tqdm


class ABCExtractor:
    def __init__(self, files: list[str] = None):
        self.reset()
        if not isinstance(files, list):
            files = [files]
        self._files = files

    def reset(self):
        self._files = []
        self._items = []

    def parse_all(self):
        for file in tqdm(self._files, desc="Extracting content"):
            with open(file) as f:
                self.parse(f.read())

    def parse(self, code: str):
        tree = ast.parse(code)
        for node in tree.body:
            self.append(node)

    def append(self, node: ast.Assign):
        raise NotImplementedError()


class WorkExtractor(ABCExtractor):
    def append(self, node: ast.Assign):
        if not isinstance(node, ast.Assign):
            return
        new_item = dict()
        if not WorkExtractor.is_work(node):
            raise Exception(f"Invalid work. {node}")

        new_item["target"] = node.targets[0].id
        new_item["year"] = node.value.args[0].args[0].value
        new_item["name"] = node.value.args[0].args[1].value

        keywords = node.value.args[0].keywords
        for k in keywords:
            if isinstance(k.value, ast.Constant):
                new_item[k.arg] = k.value.value
            elif isinstance(k.value, ast.Name):
                new_item[k.arg] = k.value.id
            else:
                raise Exception(f"Invalid Keyword: {k}")

        self._items.append(new_item)

    @property
    def work(self):
        return self._items

    @staticmethod
    def is_work(node: ast.Assign):
        return (
            isinstance(node, ast.Assign)
            and isinstance(node.value, ast.Call)
            and len(node.value.args) == 1
            and isinstance(node.value.args[0], ast.Call)
        )


class CitationExtractor(ABCExtractor):
    @property
    def citations(self):
        return self._items

    def append(self, node: ast.Expr):
        if not isinstance(node, ast.Expr):
            return
        new_item = dict()
        if not CitationExtractor.is_citation(node):
            # import pdb; pdb.set_trace()
            # raise Exception(f"Invalid work. {node}")
            return
        new_item["from"] = node.value.args[0].args[0].id
        new_item["to"] = node.value.args[0].args[1].id

        keywords = node.value.args[0].keywords
        for k in keywords:
            if isinstance(k.value, ast.Constant):
                new_item[k.arg] = k.value.value
            elif isinstance(k.value, ast.Name):
                new_item[k.arg] = k.value.id
            elif isinstance(k.value, ast.List):
                new_item[k.arg] = k.value.elts
            else:
                import pdb

                pdb.set_trace()
                raise Exception(f"Invalid Keyword: {k}")

        self._items.append(new_item)

    @staticmethod
    def is_citation(node: ast.Expr):
        return (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and len(node.value.args) == 1
            and isinstance(node.value.args[0], ast.Call)
        )
