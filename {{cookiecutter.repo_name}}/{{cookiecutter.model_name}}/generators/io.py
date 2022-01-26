from dbgen import Generator, Const, Model
from dbgen.core.node.common_extractors import FileExtractor
from ..schema import MyTable
from ..transforms.io import simple_io
from ..constants import DATA_PATH


def add_io_gens(model: Model):
    with model:
        with Generator("dummy_gen"):
            MyTable.load(insert=True, label=Const("test_label"))


        with Generator("read_file"):
            file_names = FileExtractor(directory=DATA_PATH, extension="txt").results()
            file_contents = simple_io(file_names).results()
            MyTable.load(insert=True, label=file_contents)
