"""Test script to reproduce the block comment issue."""

from html2typst import translate_html_to_typst

# The problematic HTML from the issue
html = '''<p style="text-align: center;"><strong style="color: black;">UCHWAŁdsfaf</strong><span
        style="color: black;">/</span><strong style="color: black;">2022</strong></p>
<p style="text-align: center;"><span style="color: black;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: black;">Właścicifdsafasf dsafsa
        69 przfsdafasWarszawie </span></p>
<p style="text-align: center;"><span style="color: black;"> </span></p>
<p style="text-align: center;"><span style="color: black;"> </span></p>
<p style="text-align: center;"><span style="color: black;">&nbsp;</span></p>
<p><span style="color: black;">&nbsp;</span></p>
<p style="text-align: justify;"><span style="color: black;">w sprawie: </span><strong style="color: black;">montażu
        klimatyzatorów</strong></p>
<p style="text-align: justify;"><strong style="color: black;">&nbsp;</strong></p>
<p style="text-align: justify;"><span style="color: black;">Działając na psdafdasfsafsafsafsafdsaf
        następuje:</span></p>
<p style="text-align: justify;"><span style="color: black;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: black;">&nbsp;</span></p>
<p style="text-align: center;"><strong style="color: black;">§ 1</strong></p>
<p style="text-align: justify;"><span style="color: black;">Ogół właścicieli wyraża zgodę na montaż urządzeń
        klimatyzacji na następujących warunkach:</span></p>
<p style="text-align: justify;"><span style="color: black;">- Właściciel zobowiązany jedsafdasfdsafsafasi klimatyzacyjnej nie
        przekrafdsafasddo prac montażowych,</span></p>
<p style="text-align: justify;"><span style="color: black;">- jednostkafasdfasdfasf możliwości mieszania na ścianie elewacji
        lub też innym elemencie budynku,</span></p>
<p style="text-align: justify;"><span style="color: black;">- przejście przezfdsafdsafsafone
        substancją uszczelniającą,</span></p>
<p style="text-align: justify;"><span style="color: black;">- odprowadzanie wody- skroplin musi zostać przeprowadzone w
        obrębie lokalu (np. do kanalizacji),</span></p>
<p style="text-align: justify;"><span style="color: black;">- Właściciefsdafdasfasdzenie ponosi
        wszelkie konsekwencje związane z montażem i następstwa z tego wynikające,</span></p>
<p style="text-align: justify;"><span style="color: black;">- bieżącsdfasafdasfsadfsarukcji
        posadowienia pozfedsafsdafsdafdsafasależy jednostka,</span></p>
<p style="text-align: justify;"><span style="color: black;">- pracedsfdasfasdfsdafny koszt
        Właściciela danego lokalu. </span></p>
<p style="text-align: justify;"><strong style="color: black;">&nbsp;</strong></p>
<p style="text-align: center;"><strong style="color: black;">§ 2</strong></p>
<p style="text-align: justify;">W przypadku montażu urządzenia na elewacjidfsafsafdsafasfsafasdfieszkaniowej. &nbsp;</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: center;"><strong style="color: black;">§3</strong></p>
<p style="text-align: justify;">Właśdfsafsafad
   dsaffaę do niniejszych
    fdasfas
    pdsfasafuchwały. Środki przeznaczone&nbsp;będą na fundusz remonfdsafaslnoty Mieszkdsfasfsadfwej</p>
<p style="text-align: justify;">&nbsp;</p>
<p style="text-align: center;"><strong style="color: black;">§4</strong></p>
<p style="text-align: justify;">Uchwała wcsdafasfdjęcia. </p>
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
        style="color: black;">Zarfadsfdsafasfzkaniowej</strong></p>
<p><strong style="color: black;">&nbsp;</strong></p>'''

print("Converting HTML to Typst...")
try:
    result = translate_html_to_typst(html, debug=True, debug_log_path='test_debug.log')
    print("SUCCESS!")
    print("\nTypst output:")
    print("=" * 80)
    print(result)
    print("=" * 80)
    
    # Save to file for validation
    with open('test_output.typ', 'w', encoding='utf-8') as f:
        f.write(result)
    print("\nOutput saved to test_output.typ")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
