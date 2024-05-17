import os
import yaml
import re

def load_config(file_path):
    # Cargar el contenido del archivo YAML como una cadena
    with open(file_path, 'r') as f:
        yaml_content = f.read()

    # Procesar manualmente las variables de entorno en el formato ${VARNAME:default}
    def env_var_replacer(match):
        var_name, default_value = match.groups()
        return os.getenv(var_name, default_value)

    yaml_content = re.sub(r'\$\{([^:}]+):([^}]+)\}', env_var_replacer, yaml_content)

    # Cargar el contenido procesado del YAML
    config = yaml.safe_load(yaml_content)
    return config