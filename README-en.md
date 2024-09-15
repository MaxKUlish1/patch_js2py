# js2py Compatibility Fix

## Overview

This repository provides a patch for the `js2py` library to ensure compatibility with Python versions 3.12 and above. The `js2py` library, a popular JavaScript-to-Python transpiler, has compatibility issues with newer Python versions due to changes in bytecode and opcode mappings. This patch addresses these issues to restore functionality.

## Purpose

`js2py` does not work properly with Python versions 3.12 and above due to changes in Python's internal bytecode representation and opcode mappings. This repository offers a solution by modifying the relevant files in the `js2py` package to support these newer Python versions.

## Installation

1. **Apply the compatibility patch: Run the provided Python script to modify the necessary files in the `js2py` package:**

    ```bash
    python apply_patch.py
    ```

## Files Modified

- `js2py/translators/translating_nodes.py`: Updates the random number generation for compatibility.
- `js2py/utils/injector.py`: Adds `LOAD_ATTR` opcode mapping and adjusts bytecode handling for newer Python versions.

## Example

To demonstrate the use of this patched `js2py` library, here is a basic example:

```python
from js2py import eval_js

js_code = 'function add(a, b) { return a + b; }'
result = eval_js(js_code).add(5, 3)
print(result)  # Output should be 8
