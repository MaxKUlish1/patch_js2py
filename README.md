[ENGLISH](https://github.com/MaxKUlish1/patch_js2py/blob/main/README-en.md)

# Исправление совместимости js2py

## Обзор

Этот репозиторий предоставляет патч для библиотеки `js2py`, чтобы обеспечить её совместимость с версиями Python 3.12 и выше. Библиотека `js2py`, популярный транспилятор JavaScript в Python, имеет проблемы совместимости с новыми версиями Python из-за изменений в байт-коде и сопоставлении опкодов. Этот патч устраняет эти проблемы и восстанавливает функциональность.

## Установка

1. **Примените патч совместимости: Запустите предоставленный скрипт на Python для модификации необходимых файлов в пакете `js2py`:**

    ```bash
    python apply_patch.py
    ```

## Изменённые файлы

- `js2py/translators/translating_nodes.py`: Обновляет генерацию случайных чисел для совместимости.
- `js2py/utils/injector.py`: Добавляет сопоставление опкодов `LOAD_ATTR` и корректирует обработку байт-кода для новых версий Python.

## Пример

Чтобы продемонстрировать использование этой исправленной библиотеки `js2py`, базовый пример:

```python
from js2py import eval_js

js_code = 'function add(a, b) { return a + b; }'
js_function = eval_js(js_code)
result = js_function(5, 3)
print(result)  # Ожидаемый результат: 8
```

[HIDDEN_CODING](https://t.me/hidden_codding_chat)
