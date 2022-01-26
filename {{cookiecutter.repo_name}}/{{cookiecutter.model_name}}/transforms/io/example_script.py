from dbgen import transform



@transform
def simple_io(file_path:str)->str:
    with open(file_path, 'r') as f:
        return f.read()