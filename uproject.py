import argparse
import os
import json
import logging
import sys
import re

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


def symlink(source, target, force=False):
    if force:
        try:
            os.remove(target)
        except:
            pass

    try:
        os.symlink(source, target)
    except FileExistsError:
        log.info(f'{target} already exists')


def insert_mod_to_build(mod_name):
    REGEX = r'ExtraModuleNames\.AddRange\(new string\[\] \{(.*)\}\);'

    def replacement(modules):
        return f'ExtraModuleNames.AddRange(new string[] {{ {", ".join(modules)}}});'

    for file in ('FactoryGame.Target.cs', 'FactoryGameEditor.Target.cs'):
        build_file_path = os.path.join(folder, 'Source', file)

        # find all the currently listed modules
        with open(build_file_path, 'r') as build_file:
            full = build_file.read()

            # Add our module
            result = [name.strip() for name in re.findall(REGEX, full)[0].split(',')]
            cs_name = f'"{mod_name}"'

        # if our module is not included add it
        if cs_name not in result:
            result.append(cs_name)
            full = re.sub(REGEX, replacement(result), full)

            with open(build_file_path, 'w') as build_file:
                build_file.write(full)


def add_symlink(mod_name):
    symlink(os.path.join(mods_folder, mod_name, 'Content'),
            os.path.join(folder, 'Content', mod_name), args.force)

    symlink(os.path.join(mods_folder, mod, 'Source'),
            os.path.join(folder, 'Source', mod_name), args.force)


def generate_new_mod(mod_name):
    from cookiecutter.main import cookiecutter

    # Generate a new mod
    cookiecutter('https://github.com/Delaunay/SatisfactoryModCookieCutter',
                 no_input=True,
                 extra_context={'ModName': mod_name},
                 output_dir=mods_folder)

    add_symlink(mod_name)
    insert_mod_to_build(mod_name)


def clone_mod(url):
    import subprocess
    name = url.split('/')[-1]

    out = subprocess.check_output(['git', 'submodule', 'add', url, os.path.join(mods_folder, name)])
    print(out.decode('utf-8'))

    add_symlink(name)
    insert_mod_to_build(name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sym-link', action='store_true', default=False, help='Add Symlink for each mod')

    parser.add_argument(
        '--force', action='store_true', default=False, help='Force link creation')

    parser.add_argument(
        '--new-mod', type='str', default=None, help='Create a new mod')

    parser.add_argument(
        '--clone-mod', type='str', default=None, help='Add a new mod as a submodule')

    args = parser.parse_args()

    if args.sym_link:
        for mod in os.listdir(mods_folder):
            log.info(f'Setting Symlink for mod {mod}')
            add_symlink(mod)

    if args.new_mod:
        generate_new_mod(args.new_mod)

    if args.clone_mod:
        clone_mod(arfs.clone_mod)


if __name__ == '__main__':
    main()
