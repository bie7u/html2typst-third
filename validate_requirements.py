"""
Validation script to verify all requirements from the problem statement.
"""

from html2typst import translate_html_to_typst
import tempfile
import os


def validate_requirement(name, test_func):
    """Helper to run and validate a requirement."""
    print(f"\n{'=' * 70}")
    print(f"VALIDATING: {name}")
    print('=' * 70)
    try:
        result = test_func()
        if result:
            print(f"✓ PASSED: {name}")
            return True
        else:
            print(f"✗ FAILED: {name}")
            return False
    except Exception as e:
        print(f"✗ ERROR in {name}: {str(e)}")
        return False


def req_api_signature():
    """Verify API signature matches requirements."""
    print("\nTesting API signature...")
    
    # Test basic call
    result = translate_html_to_typst("<p>Test</p>")
    assert isinstance(result, str)
    
    # Test with debug=False
    result = translate_html_to_typst("<p>Test</p>", debug=False)
    assert isinstance(result, str)
    
    # Test with debug=True and log path
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        log_path = f.name
    
    try:
        result = translate_html_to_typst("<p>Test</p>", debug=True, debug_log_path=log_path)
        assert isinstance(result, str)
        assert os.path.exists(log_path)
    finally:
        if os.path.exists(log_path):
            os.unlink(log_path)
    
    print("API signature correct: translate_html_to_typst(html, debug, debug_log_path)")
    return True


def req_production_mode():
    """Verify production mode requirements."""
    print("\nTesting production mode...")
    
    html = '<p>Test <strong>bold</strong> with <span class="ql-align-center">style</span></p>'
    result = translate_html_to_typst(html, debug=False)
    
    # Must contain all text
    assert "Test" in result
    assert "bold" in result
    assert "style" in result
    
    # Must not contain debug info
    assert "DEBUG" not in result
    assert "INFO" not in result
    assert "WARNING" not in result
    assert "log" not in result.lower()
    
    print(f"Production output (clean): {repr(result)}")
    return True


def req_debug_mode():
    """Verify debug mode requirements."""
    print("\nTesting debug mode...")
    
    html = '<p class="ql-align-center">Test</p>'
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        log_path = f.name
    
    try:
        result = translate_html_to_typst(html, debug=True, debug_log_path=log_path)
        
        # Output must still be clean
        assert "DEBUG" not in result
        assert "INFO" not in result
        
        # Log file must exist and have content
        assert os.path.exists(log_path)
        with open(log_path, 'r') as f:
            log_content = f.read()
        
        assert len(log_content) > 0
        assert "DEBUG" in log_content or "INFO" in log_content
        
        print(f"Debug output (still clean): {repr(result)}")
        print(f"Log file exists: {os.path.exists(log_path)}")
        print(f"Log file has content: {len(log_content)} bytes")
        
        return True
    finally:
        if os.path.exists(log_path):
            os.unlink(log_path)


def req_text_preservation():
    """Verify 100% text preservation."""
    print("\nTesting text preservation...")
    
    html = '''
    <div>
        <p>Text 1</p>
        <span style="color: unknown;">Text 2</span>
        <unknown>Text 3</unknown>
        <p class="unsupported-class">Text 4</p>
    </div>
    '''
    
    result = translate_html_to_typst(html)
    
    # Every piece of text must be present
    assert "Text 1" in result
    assert "Text 2" in result
    assert "Text 3" in result
    assert "Text 4" in result
    
    print("All text preserved even with unknown elements/styles")
    return True


def req_quill_classes():
    """Verify Quill.js class handling."""
    print("\nTesting Quill.js classes...")
    
    # Test alignment
    html1 = '<p class="ql-align-center">Centered</p>'
    result1 = translate_html_to_typst(html1)
    assert "Centered" in result1
    assert "#align(center)" in result1
    
    # Test indent (text must be preserved)
    html2 = '<li class="ql-indent-2">Indented</li>'
    result2 = translate_html_to_typst(html2)
    assert "Indented" in result2
    
    # Test size (text must be preserved)
    html3 = '<span class="ql-size-large">Large</span>'
    result3 = translate_html_to_typst(html3)
    assert "Large" in result3
    
    # Test font (text must be preserved)
    html4 = '<span class="ql-font-serif">Serif</span>'
    result4 = translate_html_to_typst(html4)
    assert "Serif" in result4
    
    print("Quill.js classes handled correctly")
    return True


def req_edge_case():
    """Verify the specific edge case from requirements."""
    print("\nTesting edge case from requirements...")
    
    html = '''<li class="ql-indent-1" style="text-align: justify;">
        <span style="color: windowtext;"><strong>Tekst</strong></span>
    </li>'''
    
    result = translate_html_to_typst(html)
    
    # Must be a list item
    assert result.startswith('-') or result.startswith('+')
    
    # Must have bold text
    assert "*Tekst*" in result
    
    # Must not have unclosed delimiters
    assert result.count('*') % 2 == 0
    
    print(f"Edge case result: {repr(result)}")
    return True


def req_basic_mappings():
    """Verify basic HTML to Typst mappings."""
    print("\nTesting basic mappings...")
    
    tests = [
        ('<p>Para</p>', 'Para'),
        ('<strong>Bold</strong>', '*Bold*'),
        ('<b>Bold</b>', '*Bold*'),
        ('<em>Italic</em>', '_Italic_'),
        ('<i>Italic</i>', '_Italic_'),
        ('<u>Under</u>', '#underline[Under]'),
        ('<br>', '\\'),
        ('<ul><li>Item</li></ul>', '- Item'),
        ('<ol><li>Item</li></ol>', '+ Item'),
        ('<h1>H1</h1>', '= H1'),
        ('<h2>H2</h2>', '== H2'),
        ('<code>code</code>', '`code`'),
        ('<a href="url">Link</a>', '#link("url")[Link]'),
    ]
    
    for html, expected in tests:
        result = translate_html_to_typst(html)
        assert expected in result, f"Expected '{expected}' in result for '{html}'"
        print(f"  ✓ {html[:30]:30} → {expected[:30]}")
    
    return True


def req_typst_safety():
    """Verify Typst output is always valid."""
    print("\nTesting Typst safety...")
    
    # Test delimiter balancing
    html = '<p><strong>Bold</strong> and <em>italic</em></p>'
    result = translate_html_to_typst(html)
    
    # Count delimiters
    assert result.count('*') % 2 == 0, "Asterisks must be balanced"
    assert result.count('_') % 2 == 0, "Underscores must be balanced"
    
    # Test complex nesting
    html2 = '<div><p><strong><em>Nested</em></strong></p></div>'
    result2 = translate_html_to_typst(html2)
    assert "Nested" in result2
    
    # Test empty tags don't break output
    html3 = '<p><strong></strong>Text</p>'
    result3 = translate_html_to_typst(html3)
    assert "Text" in result3
    
    print("Typst output is syntactically valid")
    return True


def req_inline_styles():
    """Verify inline style handling."""
    print("\nTesting inline style handling...")
    
    # Styles should be ignored but text preserved
    html = '''
    <span style="color: red;">Red</span>
    <span style="background-color: yellow;">Yellow</span>
    <span style="font-size: 20px;">Big</span>
    '''
    
    result = translate_html_to_typst(html)
    
    assert "Red" in result
    assert "Yellow" in result
    assert "Big" in result
    
    print("Inline styles gracefully ignored, text preserved")
    return True


def req_fail_safe():
    """Verify fail-safe behavior."""
    print("\nTesting fail-safe behavior...")
    
    # Unknown tags
    html = '<custom>Unknown</custom>'
    result = translate_html_to_typst(html)
    assert "Unknown" in result
    
    # Malformed HTML should still work
    html2 = '<p>Unclosed paragraph'
    result2 = translate_html_to_typst(html2)
    assert "Unclosed paragraph" in result2
    
    # Empty input
    result3 = translate_html_to_typst('')
    assert isinstance(result3, str)
    
    print("Fail-safe: unknown tags degrade gracefully")
    return True


def main():
    """Run all validations."""
    print("\n" + "=" * 70)
    print("HTML TO TYPST TRANSLATOR - REQUIREMENTS VALIDATION")
    print("=" * 70)
    
    results = {}
    
    # Run all requirement tests
    results['API Signature'] = validate_requirement(
        "API Signature", req_api_signature
    )
    
    results['Production Mode'] = validate_requirement(
        "Production Mode (clean output)", req_production_mode
    )
    
    results['Debug Mode'] = validate_requirement(
        "Debug Mode (logging to file)", req_debug_mode
    )
    
    results['Text Preservation'] = validate_requirement(
        "100% Text Preservation", req_text_preservation
    )
    
    results['Quill.js Classes'] = validate_requirement(
        "Quill.js Class Support", req_quill_classes
    )
    
    results['Edge Case'] = validate_requirement(
        "Edge Case (from requirements)", req_edge_case
    )
    
    results['Basic Mappings'] = validate_requirement(
        "Basic HTML → Typst Mappings", req_basic_mappings
    )
    
    results['Typst Safety'] = validate_requirement(
        "Typst Syntax Safety", req_typst_safety
    )
    
    results['Inline Styles'] = validate_requirement(
        "Inline Style Handling", req_inline_styles
    )
    
    results['Fail-Safe'] = validate_requirement(
        "Fail-Safe Degradation", req_fail_safe
    )
    
    # Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:8} | {name}")
    
    print("=" * 70)
    print(f"TOTAL: {passed}/{total} requirements validated")
    print("=" * 70)
    
    if passed == total:
        print("\n🎉 ALL REQUIREMENTS VALIDATED SUCCESSFULLY! 🎉\n")
        return 0
    else:
        print("\n⚠️  SOME REQUIREMENTS FAILED ⚠️\n")
        return 1


if __name__ == '__main__':
    exit(main())
