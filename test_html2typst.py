"""
Test suite for HTML to Typst translator.
"""

import os
import tempfile
import unittest
from html2typst import translate_html_to_typst


class TestBasicElements(unittest.TestCase):
    """Test basic HTML element translations."""
    
    def test_simple_paragraph(self):
        """Test simple paragraph."""
        html = "<p>Hello World</p>"
        result = translate_html_to_typst(html)
        self.assertIn("Hello World", result)
    
    def test_bold_text(self):
        """Test bold text."""
        html = "<p><strong>Bold text</strong></p>"
        result = translate_html_to_typst(html)
        self.assertIn("*Bold text*", result)
    
    def test_italic_text(self):
        """Test italic text."""
        html = "<p><em>Italic text</em></p>"
        result = translate_html_to_typst(html)
        self.assertIn("_Italic text_", result)
    
    def test_bold_tag(self):
        """Test <b> tag."""
        html = "<p><b>Bold</b></p>"
        result = translate_html_to_typst(html)
        self.assertIn("*Bold*", result)
    
    def test_italic_tag(self):
        """Test <i> tag."""
        html = "<p><i>Italic</i></p>"
        result = translate_html_to_typst(html)
        self.assertIn("_Italic_", result)
    
    def test_underline(self):
        """Test underline."""
        html = "<p><u>Underlined</u></p>"
        result = translate_html_to_typst(html)
        self.assertIn("#underline[Underlined]", result)
    
    def test_strikethrough(self):
        """Test strikethrough."""
        html = "<p><s>Strikethrough</s></p>"
        result = translate_html_to_typst(html)
        self.assertIn("#strike[Strikethrough]", result)
    
    def test_line_break(self):
        """Test line break."""
        html = "<p>Line 1<br>Line 2</p>"
        result = translate_html_to_typst(html)
        self.assertIn("Line 1", result)
        self.assertIn("Line 2", result)
        self.assertIn("\\", result)


class TestLists(unittest.TestCase):
    """Test list translations."""
    
    def test_unordered_list(self):
        """Test unordered list."""
        html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        result = translate_html_to_typst(html)
        self.assertIn("- Item 1", result)
        self.assertIn("- Item 2", result)
    
    def test_ordered_list(self):
        """Test ordered list."""
        html = "<ol><li>First</li><li>Second</li></ol>"
        result = translate_html_to_typst(html)
        self.assertIn("+ First", result)
        self.assertIn("+ Second", result)
    
    def test_list_with_formatting(self):
        """Test list with formatted content."""
        html = "<ul><li><strong>Bold item</strong></li></ul>"
        result = translate_html_to_typst(html)
        self.assertIn("*Bold item*", result)


class TestQuillSpecific(unittest.TestCase):
    """Test Quill.js specific features."""
    
    def test_quill_indent(self):
        """Test Quill indent class."""
        html = '<li class="ql-indent-1">Indented item</li>'
        result = translate_html_to_typst(html)
        # Should preserve text even if indent not fully supported
        self.assertIn("Indented item", result)
    
    def test_quill_align_center(self):
        """Test Quill center alignment."""
        html = '<p class="ql-align-center">Centered text</p>'
        result = translate_html_to_typst(html)
        self.assertIn("Centered text", result)
        self.assertIn("#align(center)", result)
    
    def test_quill_align_right(self):
        """Test Quill right alignment."""
        html = '<p class="ql-align-right">Right aligned</p>'
        result = translate_html_to_typst(html)
        self.assertIn("Right aligned", result)
        self.assertIn("#align(right)", result)
    
    def test_quill_align_justify(self):
        """Test Quill justify alignment."""
        html = '<p class="ql-align-justify">Justified text</p>'
        result = translate_html_to_typst(html)
        # Should preserve text
        self.assertIn("Justified text", result)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and complex scenarios."""
    
    def test_edge_case_list_with_span_and_strong(self):
        """Test the specific edge case from requirements."""
        html = '''<li class="ql-indent-1" style="text-align: justify;">
            <span style="color: windowtext;"><strong>Tekst</strong></span>
        </li>'''
        result = translate_html_to_typst(html)
        
        # Must preserve the text
        self.assertIn("Tekst", result)
        # Should have bold formatting
        self.assertIn("*Tekst*", result)
        # Should be a list item - when <li> has no parent list, defaults to unordered
        self.assertIn("- *Tekst*", result)
    
    def test_nested_formatting(self):
        """Test nested formatting tags."""
        html = "<p><strong><em>Bold and italic</em></strong></p>"
        result = translate_html_to_typst(html)
        self.assertIn("Bold and italic", result)
    
    def test_empty_tags(self):
        """Test empty tags don't break output."""
        html = "<p><strong></strong>Text</p>"
        result = translate_html_to_typst(html)
        self.assertIn("Text", result)
    
    def test_whitespace_only_strong(self):
        """Test strong tags with only whitespace don't create invalid syntax."""
        html = "<p><strong>&nbsp;</strong>Text</p>"
        result = translate_html_to_typst(html)
        # Should not contain "* *" which would be interpreted as block comment
        self.assertNotIn("* *", result)
        self.assertIn("Text", result)
    
    def test_whitespace_only_em(self):
        """Test em tags with only whitespace don't create invalid syntax."""
        html = "<p><em> </em>Text</p>"
        result = translate_html_to_typst(html)
        # Should not contain "_ _" 
        self.assertNotIn("_ _", result)
        self.assertIn("Text", result)
    
    def test_whitespace_only_underline(self):
        """Test underline tags with only whitespace don't create invalid syntax."""
        html = "<p><u>&nbsp;</u>Text</p>"
        result = translate_html_to_typst(html)
        # Should not wrap whitespace in underline
        self.assertNotIn("#underline[ ]", result)
        self.assertIn("Text", result)
    
    def test_whitespace_only_strikethrough(self):
        """Test strikethrough tags with only whitespace don't create invalid syntax."""
        html = "<p><s> </s>Text</p>"
        result = translate_html_to_typst(html)
        # Should not wrap whitespace in strike
        self.assertNotIn("#strike[ ]", result)
        self.assertIn("Text", result)
    
    def test_issue_block_comment_error(self):
        """Test the specific HTML that caused 'unexpected end of block comment' error."""
        # This is a minimal reproduction of the reported issue
        html = '''<p style="text-align: justify;"><strong style="color: black;">&nbsp;</strong></p>
        <p style="text-align: center;"><strong style="color: black;">§ 1</strong></p>'''
        result = translate_html_to_typst(html)
        
        # Should not contain "* *" which causes block comment error
        self.assertNotIn("* *", result)
        # Should contain the actual content
        self.assertIn("§ 1", result)
    
    def test_unknown_tag(self):
        """Test unknown tags degrade gracefully."""
        html = "<p><custom>Unknown tag content</custom></p>"
        result = translate_html_to_typst(html)
        # Text must be preserved
        self.assertIn("Unknown tag content", result)
    
    def test_mixed_content(self):
        """Test mixed content with various elements."""
        html = """
        <h1>Title</h1>
        <p>Paragraph with <strong>bold</strong> and <em>italic</em>.</p>
        <ul>
            <li>List item 1</li>
            <li>List item 2</li>
        </ul>
        """
        result = translate_html_to_typst(html)
        
        # All text must be present
        self.assertIn("Title", result)
        self.assertIn("Paragraph", result)
        self.assertIn("bold", result)
        self.assertIn("italic", result)
        self.assertIn("List item 1", result)
        self.assertIn("List item 2", result)


class TestCodeElements(unittest.TestCase):
    """Test code and pre elements."""
    
    def test_inline_code(self):
        """Test inline code."""
        html = "<p>This is <code>inline code</code></p>"
        result = translate_html_to_typst(html)
        self.assertIn("`inline code`", result)
    
    def test_code_block(self):
        """Test code block."""
        html = "<pre><code>def hello():\n    print('world')</code></pre>"
        result = translate_html_to_typst(html)
        self.assertIn("```", result)
        self.assertIn("def hello()", result)


class TestLinks(unittest.TestCase):
    """Test link elements."""
    
    def test_link_with_href(self):
        """Test link with href."""
        html = '<p><a href="https://example.com">Click here</a></p>'
        result = translate_html_to_typst(html)
        self.assertIn("Click here", result)
        self.assertIn("https://example.com", result)
        self.assertIn("#link", result)
    
    def test_link_without_href(self):
        """Test link without href."""
        html = '<p><a>Just text</a></p>'
        result = translate_html_to_typst(html)
        self.assertIn("Just text", result)


class TestImages(unittest.TestCase):
    """Test image elements."""
    
    def test_image_with_alt(self):
        """Test image with alt text."""
        html = '<img src="image.jpg" alt="Description">'
        result = translate_html_to_typst(html)
        # Should include alt text in some form
        self.assertIn("Description", result)
    
    def test_image_without_alt(self):
        """Test image without alt text."""
        html = '<img src="image.jpg">'
        result = translate_html_to_typst(html)
        # Should not break
        self.assertIsInstance(result, str)


class TestHeadings(unittest.TestCase):
    """Test heading elements."""
    
    def test_h1(self):
        """Test h1."""
        html = "<h1>Heading 1</h1>"
        result = translate_html_to_typst(html)
        self.assertIn("= Heading 1", result)
    
    def test_h2(self):
        """Test h2."""
        html = "<h2>Heading 2</h2>"
        result = translate_html_to_typst(html)
        self.assertIn("== Heading 2", result)
    
    def test_h3(self):
        """Test h3."""
        html = "<h3>Heading 3</h3>"
        result = translate_html_to_typst(html)
        self.assertIn("=== Heading 3", result)


class TestBlockquote(unittest.TestCase):
    """Test blockquote elements."""
    
    def test_blockquote(self):
        """Test blockquote."""
        html = "<blockquote>Quoted text</blockquote>"
        result = translate_html_to_typst(html)
        self.assertIn("Quoted text", result)
        self.assertIn(">", result)


class TestDebugMode(unittest.TestCase):
    """Test debug mode functionality."""
    
    def test_debug_mode_creates_log(self):
        """Test that debug mode creates a log file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
            log_path = f.name
        
        try:
            html = "<p><strong>Test</strong></p>"
            result = translate_html_to_typst(html, debug=True, debug_log_path=log_path)
            
            # Output should still be clean
            self.assertIn("*Test*", result)
            self.assertNotIn("DEBUG", result)
            self.assertNotIn("INFO", result)
            
            # Log file should exist and have content
            self.assertTrue(os.path.exists(log_path))
            with open(log_path, 'r') as f:
                log_content = f.read()
            self.assertTrue(len(log_content) > 0)
            
        finally:
            if os.path.exists(log_path):
                os.unlink(log_path)
    
    def test_production_mode_no_log(self):
        """Test that production mode doesn't create log."""
        html = "<p>Test</p>"
        result = translate_html_to_typst(html, debug=False)
        
        # Should be clean output
        self.assertIn("Test", result)


class TestTextPreservation(unittest.TestCase):
    """Test that all text is preserved."""
    
    def test_all_text_preserved(self):
        """Test that all text content is preserved."""
        html = """
        <div>
            <p>First paragraph</p>
            <p>Second <strong>paragraph</strong> with <em>formatting</em></p>
            <ul>
                <li>Item one</li>
                <li>Item two</li>
            </ul>
            <span style="color: red;">Colored text</span>
        </div>
        """
        result = translate_html_to_typst(html)
        
        # Every piece of text must be present
        texts = ["First paragraph", "Second", "paragraph", "with", "formatting",
                 "Item one", "Item two", "Colored text"]
        for text in texts:
            self.assertIn(text, result)


class TestTypstSafety(unittest.TestCase):
    """Test that output is always valid Typst."""
    
    def test_no_unclosed_delimiters(self):
        """Test that delimiters are properly closed."""
        html = "<p><strong>Bold</strong> and <em>italic</em></p>"
        result = translate_html_to_typst(html)
        
        # Count opening and closing markers
        self.assertEqual(result.count('*') % 2, 0, "Asterisks should be balanced")
        self.assertEqual(result.count('_') % 2, 0, "Underscores should be balanced")
    
    def test_complex_nesting(self):
        """Test complex nesting doesn't break syntax."""
        html = """
        <div>
            <p><strong><em>Bold italic</em></strong></p>
            <ul>
                <li><strong>Bold item</strong></li>
                <li><em>Italic item</em></li>
            </ul>
        </div>
        """
        result = translate_html_to_typst(html)
        
        # Should contain the text
        self.assertIn("Bold italic", result)
        self.assertIn("Bold item", result)
        self.assertIn("Italic item", result)


class TestInlineStyles(unittest.TestCase):
    """Test inline style handling."""
    
    def test_color_style_ignored(self):
        """Test that color styles are gracefully ignored."""
        html = '<span style="color: red;">Red text</span>'
        result = translate_html_to_typst(html)
        # Text must be preserved
        self.assertIn("Red text", result)
    
    def test_background_color_ignored(self):
        """Test that background color is ignored."""
        html = '<span style="background-color: yellow;">Highlighted</span>'
        result = translate_html_to_typst(html)
        self.assertIn("Highlighted", result)
    
    def test_font_size_ignored(self):
        """Test that font size is ignored."""
        html = '<span style="font-size: 20px;">Big text</span>'
        result = translate_html_to_typst(html)
        self.assertIn("Big text", result)


class TestQuillClasses(unittest.TestCase):
    """Test Quill class handling."""
    
    def test_ql_size_classes_ignored(self):
        """Test that size classes preserve text."""
        html = '<span class="ql-size-large">Large text</span>'
        result = translate_html_to_typst(html)
        self.assertIn("Large text", result)
    
    def test_ql_font_classes_ignored(self):
        """Test that font classes preserve text."""
        html = '<span class="ql-font-serif">Serif text</span>'
        result = translate_html_to_typst(html)
        self.assertIn("Serif text", result)


class TestRealWorldQuill(unittest.TestCase):
    """Test with real-world Quill.js examples."""
    
    def test_quill_basic_formatting(self):
        """Test basic Quill formatting."""
        html = """
        <p>Normal text</p>
        <p><strong>Bold text</strong></p>
        <p><em>Italic text</em></p>
        <p><u>Underlined text</u></p>
        """
        result = translate_html_to_typst(html)
        
        self.assertIn("Normal text", result)
        self.assertIn("*Bold text*", result)
        self.assertIn("_Italic text_", result)
        self.assertIn("#underline[Underlined text]", result)
    
    def test_quill_lists(self):
        """Test Quill lists."""
        html = """
        <ul>
            <li>Unordered 1</li>
            <li>Unordered 2</li>
        </ul>
        <ol>
            <li>Ordered 1</li>
            <li>Ordered 2</li>
        </ol>
        """
        result = translate_html_to_typst(html)
        
        self.assertIn("- Unordered 1", result)
        self.assertIn("- Unordered 2", result)
        self.assertIn("+ Ordered 1", result)
        self.assertIn("+ Ordered 2", result)
    
    def test_quill_alignment(self):
        """Test Quill text alignment."""
        html = """
        <p class="ql-align-center">Centered</p>
        <p class="ql-align-right">Right aligned</p>
        """
        result = translate_html_to_typst(html)
        
        self.assertIn("Centered", result)
        self.assertIn("Right aligned", result)


if __name__ == '__main__':
    unittest.main()
