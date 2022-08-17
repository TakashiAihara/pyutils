from copy import deepcopy


def generate_dict(dict: dict, add_dict: dict = {}, remove_keys: list = []) -> dict:
    cloned_dict = deepcopy(dict)
    for key in remove_keys:
        del cloned_dict[key]
    cloned_dict.update(add_dict)
    return cloned_dict
