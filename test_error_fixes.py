"""Test cases for the specific error patterns from the issue."""
import unittest
import sys
sys.path.insert(0, '/home/runner/work/html2typst-third/html2typst-third')

from html2typst import translate_html_to_typst


class TestErrorPatternFixes(unittest.TestCase):
    """Test cases for fixing specific Typst compilation errors."""
    
    def test_strong_followed_by_parenthesis(self):
        """Test that #strong[text](text) is fixed to #strong[text] (text)."""
        html = '<p>Szczecinie<strong>testtest</strong>(dalej „Wspólnota")</p>'
        result = translate_html_to_typst(html)
        
        # Should have space after ] before (
        self.assertIn('#strong[testtest] (', result)
        # Should NOT have ]( pattern
        self.assertNotIn('](', result)
    
    def test_strong_followed_by_strong(self):
        """Test that adjacent strong tags have proper spacing."""
        html = '<p><strong>text1</strong><strong>text2</strong></p>'
        result = translate_html_to_typst(html)
        
        # Should have space between commands
        self.assertIn('] #', result)
        # Should NOT have ]# pattern
        self.assertNotIn(']#', result)
    
    def test_sup_tag_handling(self):
        """Test that <sup> tag is properly rendered."""
        html = '<p><strong>testtest</strong><sup><strong>testtest</strong></sup>miesięcznie</p>'
        result = translate_html_to_typst(html)
        
        # Should have super command
        self.assertIn('#super[', result)
        # Should have both strong tags
        self.assertEqual(result.count('#strong['), 2)
    
    def test_sub_tag_handling(self):
        """Test that <sub> tag is properly rendered."""
        html = '<p>H<sub>2</sub>O</p>'
        result = translate_html_to_typst(html)
        
        # Should have sub command
        self.assertIn('#sub[', result)
        self.assertIn('#sub[2]', result)
    
    def test_special_character_section_sign(self):
        """Test that § character is handled properly."""
        html = '<p>testtest§1<strong>testtest</strong>testtest</p>'
        result = translate_html_to_typst(html)
        
        # Should contain the text
        self.assertIn('testtest', result)
        # Should not break syntax
        self.assertNotIn(']#', result)
    
    def test_strong_with_parentheses_in_text(self):
        """Test patterns like testtest(something)testtest."""
        html = '<p><span>testtest</span>(sdafasdfsam.)<span>testtest</span></p>'
        result = translate_html_to_typst(html)
        
        # Should preserve parentheses
        self.assertIn('(sdafasdfsam.)', result)
    
    def test_inline_strong_with_parentheses(self):
        """Test inline strong followed by parentheses in longer text."""
        html = '<p>Właściciele lokali wyrażają zgodę na częściową wymianę płytek ordsfsafasfsjazdem do garażu przy założeniu kosztu wykonania prac do kwoty <strong>testtest</strong>(oferta na wfasdfasfłącznik nr 1 do niniejszej uchwały).</p>'
        result = translate_html_to_typst(html)
        
        # Should have space after strong before parenthesis
        self.assertIn('#strong[testtest] (', result)
        # Should NOT have ]( without space
        self.assertNotIn('](', result)
    
    def test_strong_in_align_center(self):
        """Test strong tags within align(center) blocks."""
        html = '<p style="text-align: center;"><strong style="color: black;">testtest</strong><strong>testtest</strong></p>'
        result = translate_html_to_typst(html)
        
        # Should have align center
        self.assertIn('#align(center)[', result)
        # Should have both strong tags
        self.assertEqual(result.count('#strong['), 2)
        # Should have space between them
        self.assertIn('] #', result)
    
    def test_text_align_justify_with_spans(self):
        """Test text-align: justify with color spans."""
        html = '<p style="text-align: justify;"><span style="color: black;">testtest</span></p>'
        result = translate_html_to_typst(html)
        
        # Should preserve text
        self.assertIn('testtest', result)
        # Should not have align for justify (it's default or ignored)
        self.assertNotIn('#align(justify)', result)
    
    def test_complex_case_with_multiple_issues(self):
        """Test a complex case with multiple patterns."""
        html = '''<p style="text-align: justify;">Na podstawie przepisów ustawy z dnia 24 czerwca 1994 r. o własności lokali (tj. Dz. U. z 2018 r. poz. 716) ogół właścicieli lokali tworzący Wspólnotę Mieszkfasdfasfi przy fasdfasf w Szczecinie<strong>testtest</strong>(dalej „Wspólnota") postanawiają:</p>'''
        result = translate_html_to_typst(html)
        
        # Should have space after strong before parenthesis
        self.assertIn('#strong[testtest] (', result)
        # Should preserve all text
        self.assertIn('Na podstawie', result)
        self.assertIn('Wspólnota', result)
        self.assertIn('postanawiają:', result)
    
    def test_underline_with_strong(self):
        """Test underline nested with strong."""
        html = '<p style="text-align: justify;"><strong style="color: black;"><u>testtest</u></strong></p>'
        result = translate_html_to_typst(html)
        
        # Should have both strong and underline
        self.assertIn('#strong[', result)
        self.assertIn('#underline[', result)
    
    def test_list_items_with_strong(self):
        """Test list items with strong tags."""
        html = '''<ul>
            <li style="text-align: justify;">zaliczka na koszty utrzymania nieruchomości wspólnej dla miejsc garażowych w hali garażowej wynosi <strong>testtest</strong> od jednego stanowiska.</li>
            <li style="text-align: justify;">zaliczka na koszty utrfsdfaskomórek lokatorskich wynosi <strong>testtest</strong> od komórki.</li>
        </ul>'''
        result = translate_html_to_typst(html)
        
        # Should have list items
        self.assertEqual(result.count('- '), 2)
        # Should have strong tags
        self.assertEqual(result.count('#strong['), 2)
        # Should preserve text
        self.assertIn('zaliczka', result)


if __name__ == '__main__':
    unittest.main()
