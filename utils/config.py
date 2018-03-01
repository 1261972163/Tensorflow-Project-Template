import json
#from bunch import Bunch
import os

class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self


def get_config_from_json(json_file):
    """
    Get the config from a json file
    :param json_file:
    :return: config(namespace) or config(dictionary)
    """
    # parse the configurations from the config json file provided
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)

    # convert the dictionary to a namespace using bunch lib
    config = Bunch(config_dict)

    return config, config_dict


def process_config(jsonfile):
    config, _ = get_config_from_json(jsonfile)
    config.summary_dir = os.path.join("../experiments", config.exp_name, "summary/")
    config.checkpoint_dir = os.path.join("../experiments", config.exp_name, "checkpoint/")
    return config

if __name__ == '__main__':
    config = process_config("../configs/example.json")
    print(config)
    