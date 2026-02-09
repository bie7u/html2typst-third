"""
Test the error case from the issue
"""

from html2typst import translate_html_to_typst

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

print("Testing HTML conversion...")
try:
    result = translate_html_to_typst(html, debug=True, debug_log_path="/tmp/debug.log")
    print("SUCCESS! Output:")
    print(result)
    print("\n" + "="*50)
    print("Check /tmp/debug.log for details")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
