"""
Test for the specific issue: "unexpected end of block comment" error
This validates that the fix prevents the error from occurring.
"""

import unittest
from html2typst import translate_html_to_typst


class TestBlockCommentIssue(unittest.TestCase):
    """Test the fix for the block comment issue."""
    
    def test_original_problematic_html(self):
        """Test with the exact HTML that caused the issue."""
        html = """<p style="text-align: center;"><strong style="color: black;">UCdsfsaf7</strong><span
        style="color: black;">/</span><strong style="color: black;">fdsaf</strong></p>
<p style="text-align: center;"><span style="color: black;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: black;">Właścidfsafsafawie </span></p>
<p style="text-align: center;"><span style="color: black;"> </span></p>
<p style="text-align: center;"><span style="color: black;"> </span></p>
<p style="text-align: center;"><span style="color: black;">&nbsp;</span></p>
<p><span style="color: black;">&nbsp;</span></p>
<p style="text-align: justify;"><span style="color: black;">w sprawie: </span><strong style="color: black;">monfdsfsafastorów</strong></p>
<p style="text-align: justify;"><strong style="color: black;">&nbsp;</strong></p>
<p style="text-align: justify;"><span style="color: black;">Dziafdsafdasdsfsafsafco
        następuje:</span></p>
<p style="text-align: justify;"><span style="color: black;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: black;">&nbsp;</span></p>
<p style="text-align: center;"><strong style="color: black;">§ 1</strong></p>
<p style="text-align: justify;"><span style="color: black;">Ogół fdsafdasfsach warunkach:</span></p>
<p style="text-align: justify;"><span style="color: black;">- Wfdsfasfaowych,</span></p>
<p style="text-align: justify;"><span style="color: black;">- jednostka klifdsafdasfsafdasścianie elewacji
        lub też innym elemencie budynku,</span></p>
<p style="text-align: justify;"><span style="color: black;">- przejście fdsafdasfdasfasdieczone
        substancją uszczelniającą,</span></p>
<p style="text-align: justify;"><span style="color: black;">- odprowadsfdasfasć przeprowadzone w
        obrębie lokalu (np. do kanalizacji),</span></p>
<p style="text-align: justify;"><span style="color: black;">- Właścicielfdsfsafasrządzenie ponosi
        wszelkie konsekwencje związane z montażem i następstwa z tego wynikające,</span></p>
<p style="text-align: justify;"><span style="color: black;">- bieżąca konsedfssafsa konstrukcji
        posadowieniafdsafsafasnależy jednostka,</span></p>
<p style="text-align: justify;"><span style="color: black;">- prace wykofdsfdsafasdy koszt
        Właściciela danego lokalu. </span></p>
<p style="text-align: justify;"><strong style="color: black;">&nbsp;</strong></p>
<p style="text-align: center;"><strong style="color: black;">§ 2</strong></p>
<p style="text-align: justify;">W przyfdsafsafasfsafsafasrzeniesienia
    urządzefdsfasfaszkaniowej. &nbsp;</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: center;"><strong style="color: black;">§3</strong></p>
<p style="text-align: justify;">Właściciele , którzy zamonsdfsafasały
    zobowiązasdfdsafsastosowanie się do niniejszych
    fsdafsafsafa
    postanowienfdsafdaseznaczone&nbsp;będą na funduszfsdafsaiowej</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: center;"><strong style="color: black;">§4</strong></p>
<p style="text-align: justify;">Uchwałdsfsafsia. </p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: justify;"><strong style="color: black;">&nbsp;</strong></p>
<p style="text-align: justify;"><span style="color: black;">&nbsp;</span></p>
<p style="text-align: justify;"><strong style="color: black;">Za</strong><span style="color: black;"> uchwałą
        głosowało:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%
        udziałów</span></p>
<p style="text-align: justify;"><strong style="color: black;">Przeciw</strong><span style="color: black;"> uchwale
        głosowało:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; % udziałów</span></p>
<p style="text-align: justify;"><strong style="color: black;">Łącznie</strong><span style="color: black;">
        głosowało:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%
        udziałów</span></p>
<p style="text-align: justify;"><span style="color: black;">&nbsp;</span></p>
<p><span style="color: black;">&nbsp;</span></p>
<p><span style="color: black;">&nbsp;</span></p>
<p><span
        style="color: black;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><strong
        style="color: black;">Zarząfdsafdsaaniowej</strong></p>
<p><strong style="color: black;">&nbsp;</strong></p>"""
        
        # Should not raise an exception
        result = translate_html_to_typst(html)
        
        # Should not contain the problematic "* *" pattern that Typst interprets as "/*"
        self.assertNotIn("* *", result)
        
        # Should contain the important text content
        self.assertIn("UCdsfsaf7", result)
        self.assertIn("§ 1", result)
        self.assertIn("§ 2", result)
        self.assertIn("§3", result)
        self.assertIn("§4", result)
        self.assertIn("Za", result)
        self.assertIn("Przeciw", result)
        self.assertIn("Łącznie", result)
    
    def test_bold_with_nbsp_inline(self):
        """Test inline bold with &nbsp; doesn't create block comment."""
        html = '<p>Text before <strong>&nbsp;</strong> text after</p>'
        result = translate_html_to_typst(html)
        
        # Should not contain "* *"
        self.assertNotIn("* *", result)
        
        # Should contain the actual text
        self.assertIn("Text before", result)
        self.assertIn("text after", result)
    
    def test_bold_with_regular_space(self):
        """Test bold with regular space."""
        html = '<p><strong> </strong></p>'
        result = translate_html_to_typst(html)
        
        # Should not contain "* *"
        self.assertNotIn("* *", result)
    
    def test_mixed_whitespace_formatting(self):
        """Test various whitespace formatting combinations."""
        html = '''
        <p><strong>&nbsp;</strong></p>
        <p><em> </em></p>
        <p><u>&nbsp;</u></p>
        <p><s> </s></p>
        '''
        result = translate_html_to_typst(html)
        
        # None of these should create problematic patterns
        self.assertNotIn("* *", result)
        self.assertNotIn("_ _", result)
        self.assertNotIn("#underline[ ]", result)
        self.assertNotIn("#strike[ ]", result)


if __name__ == '__main__':
    unittest.main()
