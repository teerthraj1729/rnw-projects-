import importlib
import pkgutil

def list_module_attributes(module_name: str):   
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        raise ImportError(f"Could not import {module_name}: {e}")
    attrs = dir(module)
    return sorted(attrs)

def list_installed_packages():
    return sorted([m.name for m in pkgutil.iter_modules()])
