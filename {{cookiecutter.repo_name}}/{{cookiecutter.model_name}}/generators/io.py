from dbgen import Generator, Const
from dbgen.core.node.common_extractors import FileExtractor
from ..schema import MyTable
from ..transforms.io.example_script import simple_io
from ..constants import DATA_PATH


with Generator("dummy_gen") as dummy_gen:
    MyTable.load(insert=True, label=Const("test_label"))


with Generator("read_file") as read_file:
    extract = FileExtractor(directory=DATA_PATH, extension="txt")
    file_names = FileExtractor(directory=DATA_PATH, extension="txt").results()
    file_contents = simple_io(file_names).results()
    MyTable.load(insert=True, label=file_contents)


io_gens = [read_file, dummy_gen]
