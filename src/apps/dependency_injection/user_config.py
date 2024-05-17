from importlib import import_module
import yaml
import os


def get_user_repository():
    config_file_path = f"{os.getcwd()}/config/user-config.yaml"
    with open(config_file_path, "r") as f:
        config = yaml.safe_load(f)
    repository_path = config["user_repository"]["mysql"]["class"]
    module_path, class_name = repository_path.rsplit(".", 1)
    module = import_module(module_path)
    repository_class = getattr(module, class_name)
    return repository_class