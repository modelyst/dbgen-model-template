from dbgen import Model
from {{cookiecutter.model_name}}.generators import add_generators


def make_model():
    model = Model(name="alice_bob_lab")
    add_generators(model)
    return model
