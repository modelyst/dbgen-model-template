from dbgen import Model
from . import schema  # noqa: F401
from .generators import generators_to_add


def make_model():
    model = Model(name="{{cookiecutter.model_name}}")
    # add gens to model
    for gen in generators_to_add:
        model.add_gen(gen)
    return model
