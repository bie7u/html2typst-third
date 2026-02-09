# Quick Start Guide

## Installation

No installation needed - this is a pure Python implementation with no external dependencies.

## Basic Usage

```python
from html2typst import translate_html_to_typst

# Convert HTML to Typst
html = "<p>Hello <strong>World</strong>!</p>"
typst = translate_html_to_typst(html)
print(typst)
# Output: Hello *World*!
```

## With Debug Logging

```python
from html2typst import translate_html_to_typst

html = '<p class="ql-align-center">Centered text</p>'
typst = translate_html_to_typst(
    html,
    debug=True,
    debug_log_path="conversion.log"
)

# typst contains clean Typst output
# conversion.log contains detailed diagnostic information
```

## Running Tests

```bash
# Run all tests
python -m unittest test_html2typst -v

# Validate all requirements
python validate_requirements.py

# Run examples
python examples.py
```

## Key Features

✅ **Production Ready**: Clean output, no debug artifacts  
✅ **Text Preservation**: 100% of text content is preserved  
✅ **Quill.js Support**: Full support for Quill.js HTML  
✅ **Safe Output**: Always valid Typst syntax  
✅ **Debug Mode**: Optional logging without affecting output  
✅ **No Dependencies**: Pure Python standard library  

## Supported Elements

- Text formatting: `<strong>`, `<em>`, `<u>`, `<s>`
- Structure: `<p>`, `<div>`, `<h1>`-`<h6>`, `<br>`
- Lists: `<ul>`, `<ol>`, `<li>`
- Code: `<code>`, `<pre>`
- Links: `<a>`
- Quotes: `<blockquote>`
- Quill classes: `ql-align-*`, `ql-indent-*`, etc.

## Examples

See `examples.py` for comprehensive usage examples including:
- Basic formatting
- Lists
- Quill.js features
- Edge cases
- Debug mode
- Complex documents
