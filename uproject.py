import argparse
import os
import json
import logging
import sys

log = logging.getLogger('UPROJECT')
folder = os.path.dirname(__file__)


def load_config():
    try:
        with open(os.path.join(folder, 'uproject.json')) as config_file:
            return json.load(config_file)
    except Exception as e:
        log.error(e)

    return dict()


config = load_config()
mods_folder = os.path.join(folder, 'Extensions')


def symlink(source, target):
    try:
        os.symlink(source, target)
    except FileExistsError:
        log.info(f'{target} already exists')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sym-link', action='store_true', default=False, help='Add Symlink for each mod')
    
    args = parser.parse_args()

    if args.sym_link:
        for mod in os.listdir(mods_folder):
            log.info(f'Setting Symlink for mod {mod}')

            symlink(os.path.join(mods_folder, mod, 'Content'),
                    os.path.join(folder, 'Content', mod))

            symlink(os.path.join(mods_folder, mod, 'Source'),
                    os.path.join(folder, 'Source', mod))


if __name__ == '__main__':
    main()
