#!/usr/bin/env python
import os
import shutil
import sys
from distutils.sysconfig import get_python_lib

def uninstall_package(package_name):
    # Locate the installation directory
    lib_path = get_python_lib()
    package_path = os.path.join(lib_path, package_name)

    # If the package exists, remove it
    if os.path.exists(package_path):
        print("Removing package directory: {0}".format(package_path))
        shutil.rmtree(package_path)
    else:
        print("Package {0} not found at {1}".format(package_name, package_path))

def uninstall_scripts(scripts):
    # Find the location of the Python scripts directory
    if sys.platform == "win32":
        # On Windows, the scripts are located in the "Scripts" directory
        scripts_path = os.path.join(os.path.dirname(sys.executable), 'Scripts')
    else:
        # On Unix-like systems, the scripts are in the "bin" directory
        scripts_path = os.path.join(os.path.dirname(sys.executable), 'bin')

    # Uninstall each script
    for script in scripts:
        script_path = os.path.join(scripts_path, script)
        if os.path.exists(script_path):
            print("Removing script: {0}".format(script_path))
            os.remove(script_path)
        else:
            print("Script {0} not found in {1}".format(script, scripts_path))

def main():
    # The package name to uninstall
    package_name = 'rfidiot'

    # List of installed scripts to uninstall
    scripts = ['cardselect.py', 'ChAP.py', 'copytag.py', 'demotag.py',
               'eeprom.py', 'fdxbnum.py', 'formatmifare1kvalue.py', 'froschtest.py', 'hidprox.py',
               'hitag2brute.py', 'hitag2reset.py', 'isotype.py', 'jcopmifare.py', 'jcopsetatrhist.py', 'jcoptool.py',
               'lfxtype.py', 'loginall.py', 'mifarekeys.py', 'mrpkey.py', 'multiselect.py', 'pn532emulate.py',
               'pn532mitm.py', 'q5reset.py', 'readlfx.py', 'readmifare1k.py',
               'readmifaresimple.py', 'readmifareultra.py', 'readtag.py', 'rfidiot-cli.py', 'send_apdu.py', 'sod.py',
               'transit.py', 'unique.py', 'writelfx.py', 'writemifare1k.py', 'testacg.sh', 'testlahf.sh']

    # Uninstall the package
    uninstall_package(package_name)

    # Uninstall the scripts
    uninstall_scripts(scripts)

    print("Uninstallation complete!")

if __name__ == "__main__":
    main()