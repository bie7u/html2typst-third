#!/usr/bin/env python3
"""
Final verification that all problem statement HTML cases compile successfully.
This script demonstrates that the "unclosed delimiter" errors are now fixed.
"""

import sys
import os
import subprocess
import tempfile

sys.path.insert(0, '/home/runner/work/html2typst-third/html2typst-third')
from html2typst import translate_html_to_typst

# All 5 HTML cases from the problem statement
html_cases = [
    {
        "id": 1,
        "description": "Complex centered and justified paragraphs with spans and strong tags",
        "html": '<p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: center;"><strong>testtest</strong><strong style="color: black;">testtest</strong><strong>testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span><strong>testtest</strong><span style="color: black;">testtest</span><strong style="color: black;">testtest</strong><span style="color: black;">testtest</span></p><ul><li style="text-align: justify;">zaliczka na koszty utrzymania nieruchomości wspólnej dla miejsc garażowych w hali garażowej wynosi <strong>testtest</strong> od jednego stanowiska.</li><li style="text-align: justify;">zaliczka na koszty utrzymania nieruchomości wspólnej dla komórek lokatorskich wynosi <strong>testtest</strong> od komórki.</li></ul><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span><strong style="color: black;">testtest</strong><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p><br/></p>'
    },
    {
        "id": 2,
        "description": "Simple paragraphs with strong and br tags",
        "html": '<p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: center;"><br/></p><p>właścicieli lokali członkófdsfsadfsa sda fdasfdasw sprawie: <strong>testtest</strong></p><p><br/></p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p><br/></p><p><br/></p>'
    },
    {
        "id": 3,
        "description": "Centered and regular paragraphs with strong and br",
        "html": '<p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: center;"><br/></p><p style="text-align: center;"><strong>testtest</strong></p><p><br/></p><p>testtest</p><p><br/></p><p style="text-align: center;">testtest</p><p><br/></p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p>testtest</p><p><br/></p><p style="text-align: center;">testtest</p><p><br/></p><p>testtest</p><p><br/></p><p style="text-align: center;">testtest</p><p><br/></p><p>testtest</p><p><br/></p><p style="text-align: center;">testtest</p><p><br/></p><p>testtest</p><p><br/></p><p style="text-align: center;">testtest</p><p><br/></p><p>testtest</p><p>testtest</p><p>testtest</p>'
    },
    {
        "id": 4,
        "description": "Complex with RGB colors and section sign",
        "html": '<p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: center;"><strong style="color: black;">testtest</strong><strong>testtest</strong></p><p style="text-align: center;">testtest</p><p style="text-align: center;">testtest</p><p style="text-align: justify;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;">testtest</p><p><br/></p><p style="text-align: center;"><strong>testtest</strong></p><p>testtest</p><p>testtest</p><p><br/></p><p><br/></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p><span style="color: rgb(34, 34, 34);">testtest</span>§1<strong>testtest</strong><span style="color: rgb(34, 34, 34);">testtest</span></p><p><span style="color: rgb(34, 34, 34);">testtest</span><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;">testtest</p><p><br/></p><p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: justify;">testtest</p><p><br/></p><p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: justify;">testtest</p><p><br/></p><p><br/></p><p><br/></p><p><strong>testtest</strong></p><p><br/></p><p>testtest</p><p><br/></p><p>testtest</p><p><br/></p><p><br/></p><p>testtest</p><p><br/></p><p style="text-align: right;">testtest</p><p style="text-align: right;">testtest</p><p style="text-align: right;">testtest</p><p style="text-align: right;">testtest</p><p><br/></p>'
    },
    {
        "id": 5,
        "description": "More align center with strong",
        "html": '<p style="text-align: center;"><strong>testtest</strong></p><p style="text-align: center;"><br/></p><p style="text-align: center;"><strong>testtest</strong><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: center;"><strong style="color: black;">testtest</strong></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><span style="color: black;">testtest</span></p><p style="text-align: justify;"><strong>testtest</strong></p><p><br/></p>'
    }
]

def compile_with_typst(typst_content):
    """Attempt to compile Typst content and return success status."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.typ', delete=False) as f:
        f.write(typst_content)
        temp_file = f.name
    
    try:
        result = subprocess.run(
            ['/tmp/typst', 'compile', temp_file, '--root', '/tmp'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Clean up
        pdf_file = temp_file.replace('.typ', '.pdf')
        if os.path.exists(pdf_file):
            os.unlink(pdf_file)
        
        return result.returncode == 0, result.stderr
    except Exception as e:
        return False, str(e)
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)

print("="*80)
print("FINAL VERIFICATION: All Problem Statement Cases")
print("="*80)
print()
print("This script verifies that all 5 HTML cases from the problem statement")
print("now compile successfully with Typst, confirming that the 'unclosed")
print("delimiter' errors have been fixed.")
print("="*80)

all_passed = True
results = []

for case in html_cases:
    print(f"\n{'='*80}")
    print(f"Case {case['id']}: {case['description']}")
    print(f"{'='*80}")
    print(f"HTML length: {len(case['html'])} characters")
    
    # Convert HTML to Typst
    typst = translate_html_to_typst(case['html'])
    print(f"Typst length: {len(typst)} characters")
    
    # Show a snippet
    lines = [l for l in typst.split('\n') if l.strip()][:3]
    print(f"\nFirst few lines of Typst output:")
    for line in lines:
        print(f"  {line[:75]}{'...' if len(line) > 75 else ''}")
    
    # Try to compile
    print(f"\nAttempting Typst compilation...")
    success, error = compile_with_typst(typst)
    
    if success:
        print(f"✅ COMPILATION SUCCESSFUL!")
        results.append((case['id'], True))
    else:
        print(f"❌ COMPILATION FAILED!")
        print(f"Error: {error[:200]}")
        results.append((case['id'], False))
        all_passed = False

# Summary
print(f"\n{'='*80}")
print("FINAL RESULTS")
print(f"{'='*80}")

for case_id, success in results:
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status}  Case {case_id}")

print(f"{'='*80}")

if all_passed:
    print("\n🎉 SUCCESS! All 5 problem statement cases compile successfully!")
    print("The 'unclosed delimiter' errors have been completely fixed.")
    print(f"{'='*80}\n")
    sys.exit(0)
else:
    print("\n⚠️ WARNING: Some cases failed to compile")
    print(f"{'='*80}\n")
    sys.exit(1)
