import sysconfig
import os

# Uninstall the current version of js2py if it exists
os.system('pip uninstall js2py')

# Install the specific version of js2py required for the patch
os.system('pip install js2py==0.74')

# Retrieve the path to the site-packages directory
site_packages = sysconfig.get_paths()['purelib']

# Define the files to modify and their corresponding replacements
files_to_modify = {
    'js2py/translators/translating_nodes.py': [
        # Update 'random.randrange(1e8))' to 'random.randrange(six.integer_types[-1](1e8)))'
        ('random.randrange(1e8))', 'random.randrange(six.integer_types[-1](1e8)))')
    ],
    'js2py/utils/injector.py': [
        # Add LOAD_ATTR opcode mapping for Python versions >= 3.12
        ("LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']\nSTORE_FAST = opcode.opmap['STORE_FAST']", 
         "LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']\nLOAD_ATTR = opcode.opmap['LOAD_ATTR']\nSTORE_FAST = opcode.opmap['STORE_FAST']"),
        # Add is_new_load_attr flag for Python versions >= 3.12
        ("is_new_bytecode = sys.version_info >= (3, 11)\n    # Now we modify the actual bytecode",
         "is_new_bytecode = sys.version_info >= (3, 11)\n    is_new_load_attr = sys.version_info >= (3, 12)\n    # Now we modify the actual bytecode"),
        # Handle new LOAD_ATTR opcode in addition to LOAD_GLOBAL
        ("if inst.opcode == LOAD_GLOBAL:\n            idx = inst.arg", 
         "if inst.opcode == LOAD_GLOBAL or (is_new_load_attr and inst.opcode == LOAD_ATTR):\n            idx = inst.arg")
    ]
}

# Apply modifications to the specified files
for file_rel_path, replacements in files_to_modify.items():
    # Construct the full file path
    file_path = os.path.join(site_packages, file_rel_path)

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Apply all the specified replacements
    for old, new in replacements:
        content = content.replace(old, new)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)
