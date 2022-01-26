{% if cookiecutter.clean=="false" %}# Add generators here
from .io import io_gens

generators_to_add = [*io_gens]
{% else %}# Add generators here
generators_to_add = []
{% endif %}