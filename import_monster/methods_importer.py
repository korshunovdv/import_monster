# -*- coding: utf-8 -*-

import importlib
from types import ModuleType
from typing import Callable, List, Union


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    """Search for target method in all modules and return list of callables

    Args:
        method_name: desired method
        modules: where will be serching

    Returns:
        methods: list with callable method if exists
    """
    methods = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType")

            met = getattr(mod, method_name, None)

            if met and callable(met):
                methods.append(met)

        except ImportError:
            continue

    return methods
