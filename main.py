import sysconfig
import os

os.system('pip uninstall js2py') #удаляем либу если таковая есть.
os.system('pip install js2py==0.74') #устанавливаем версию под которую писался патч.

# Получение пути к site-packages
site_packages = sysconfig.get_paths()['purelib']

# Файлы для модификации и соответствующие замены
files_to_modify = {
    'js2py/translators/translating_nodes.py': [
        ('random.randrange(1e8))', 'random.randrange(six.integer_types[-1](1e8)))')
    ],
    'js2py/utils/injector.py': [
        ("LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']\nSTORE_FAST = opcode.opmap['STORE_FAST']", 
         "LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']\nLOAD_ATTR = opcode.opmap['LOAD_ATTR']\nSTORE_FAST = opcode.opmap['STORE_FAST']"),
        ("is_new_bytecode = sys.version_info >= (3, 11)\n    # Now we modify the actual bytecode",
         "is_new_bytecode = sys.version_info >= (3, 11)\n    is_new_load_attr = sys.version_info >= (3, 12)\n    # Now we modify the actual bytecode"),
        ("if inst.opcode == LOAD_GLOBAL:\n            idx = inst.arg", 
         "if inst.opcode == LOAD_GLOBAL or (is_new_load_attr and inst.opcode == LOAD_ATTR):\n            idx = inst.arg")
    ]
}

# Модификация файлов
for file_rel_path, replacements in files_to_modify.items():
    file_path = os.path.join(site_packages, file_rel_path)

    # Читаем файл
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Применяем все замены
    for old, new in replacements:
        content = content.replace(old, new)
    
    # Записываем измененное содержимое обратно в файл
    with open(file_path, 'w') as file:
        file.write(content)
