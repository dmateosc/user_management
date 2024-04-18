from importlib import import_module
import yaml


def get_user_repository():
    with open("user-config.yaml", "r") as f:
        config = yaml.safe_load(f)
    repository_path = config["user_repository"]
    module_path, class_name = repository_path.rsplit(".", 1)
    module = import_module(module_path)
    repository_class = getattr(module, class_name)
    return repository_class()