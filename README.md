# HTML to Typst Translator

Production-quality translator for converting HTML (especially from Quill.js editor) to Typst markup format.

## Features

- **Production-Ready**: Clean, safe Typst output with no debug artifacts
- **Quill.js Support**: Full support for Quill.js generated HTML including classes like `ql-indent-*`, `ql-align-*`, `ql-size-*`, `ql-font-*`
- **Text Preservation**: 100% of text content is preserved, even when styles are not supported
- **Debug Mode**: Optional detailed logging to separate file without affecting output
- **Safe Output**: Guaranteed syntactically valid Typst with properly closed delimiters
- **Fail-Safe**: Graceful degradation - unknown tags render as plain text

## Installation

No external dependencies required - uses only Python standard library.

```bash
# Just copy html2typst.py to your project
cp html2typst.py /path/to/your/project/
```

## Quick Start

```python
from html2typst import translate_html_to_typst

# Basic usage
html = "<p>Hello <strong>World</strong>!</p>"
typst = translate_html_to_typst(html)
print(typst)  # Hello *World*!

# With debug logging
typst = translate_html_to_typst(
    html, 
    debug=True, 
    debug_log_path="conversion.log"
)
```

## API

### `translate_html_to_typst(html, debug=False, debug_log_path=None)`

Converts HTML string to Typst format.

**Parameters:**
- `html` (str): HTML string to convert
- `debug` (bool): Enable debug mode (default: False)
- `debug_log_path` (str|None): Path to debug log file (required if debug=True)

**Returns:**
- `str`: Typst formatted string

**Modes:**

1. **PRODUCTION** (debug=False):
   - Clean Typst output
   - No comments, markers, or warnings
   - No logging
   - 100% text content preserved

2. **DEBUG** (debug=True):
   - Same clean Typst output as production
   - Diagnostic info written to separate log file
   - No debug information in Typst output
   - Useful for troubleshooting conversions

## Supported HTML Elements

### Text Formatting
- `<strong>`, `<b>` → `*bold*`
- `<em>`, `<i>` → `_italic_`
- `<u>` → `#underline[text]`
- `<s>`, `<strike>`, `<del>` → `#strike[text]`

### Structure
- `<p>`, `<div>` → Paragraphs
- `<br>` → Line breaks (`\`)
- `<h1>` - `<h6>` → Headings (`=` to `======`)

### Lists
- `<ul>` → Unordered lists
- `<ol>` → Ordered lists
- `<li>` → List items (`-` or `+`)

### Code
- `<code>` → Inline code (`` `code` ``)
- `<pre><code>` → Code blocks (` ``` `)

### Other
- `<blockquote>` → Quoted blocks (`>`)
- `<a href="...">` → `#link("url")[text]`
- `<img alt="...">` → `[Image: alt text]`
- `<span>` → Transparent (preserves content)

### Quill.js Classes

- `ql-align-center` → `#align(center)[...]`
- `ql-align-right` → `#align(right)[...]`
- `ql-align-justify` → (text preserved, alignment ignored)
- `ql-indent-*` → (text preserved, indent logged in debug)
- `ql-size-*` → (text preserved, size ignored)
- `ql-font-*` → (text preserved, font ignored)

### Inline Styles

Most inline styles (color, background-color, font-size, etc.) are ignored but text is always preserved.

## Examples

### Basic Conversion

```python
html = """
<h1>My Document</h1>
<p>This is <strong>important</strong> text.</p>
<ul>
    <li>First item</li>
    <li>Second item</li>
</ul>
"""

typst = translate_html_to_typst(html)
```

Output:
```typst
= My Document

This is *important* text.

- First item
- Second item
```

### Quill.js Content

```python
html = """
<p class="ql-align-center">Centered Text</p>
<p>Normal text with <span style="color: red;">colored</span> content.</p>
"""

typst = translate_html_to_typst(html)
```

Output:
```typst
#align(center)[Centered Text]

Normal text with colored content.
```

### Debug Mode

```python
html = '<p class="ql-align-center">Test</p>'

typst = translate_html_to_typst(
    html,
    debug=True,
    debug_log_path="debug.log"
)

# typst contains clean output
# debug.log contains detailed processing information
```

### Edge Case Handling

The translator handles complex nested structures safely:

```python
html = '''
<li class="ql-indent-1" style="text-align: justify;">
    <span style="color: windowtext;"><strong>Text</strong></span>
</li>
'''

typst = translate_html_to_typst(html)
# Output: - *Text*
```

## Design Principles

1. **Text > Style**: Text preservation is priority #1
2. **Structure > Style**: Document structure takes precedence over visual styling
3. **Fail-Safe**: Unknown elements degrade to plain text
4. **Clean Output**: No debug artifacts in production mode
5. **Valid Typst**: Output is always syntactically correct

## Testing

Run the comprehensive test suite:

```bash
python -m unittest test_html2typst -v
```

Run examples:

```bash
python examples.py
```

## Requirements

- Python 3.7+
- No external dependencies

## License

MIT

## Contributing

Contributions welcome! Please ensure:
- All tests pass
- New features include tests
- Text preservation is maintained
- Typst output remains syntactically valid