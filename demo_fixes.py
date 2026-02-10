#!/usr/bin/env python3
"""
Demonstration of the fixes for all 9 error cases.
This script shows the before and after Typst output.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from html2typst import translate_html_to_typst

print("="*80)
print("DEMONSTRATION: Typst Compilation Error Fixes")
print("="*80)

examples = [
    {
        "name": "Strong tag followed by parenthesis",
        "html": '<p>Szczecinie<strong>testtest</strong>(dalej „Wspólnota")</p>',
        "issue": "Creates #strong[text]( which looks like a function call",
    },
    {
        "name": "Adjacent strong tags",
        "html": '<p style="text-align: center;"><strong>text1</strong><strong>text2</strong></p>',
        "issue": "Creates ]# pattern without spacing",
    },
    {
        "name": "Sup tag with strong",
        "html": '<p><strong>price</strong><sup><strong>2</strong></sup>monthly</p>',
        "issue": "Sup tag not handled, creates adjacent strong tags",
    },
    {
        "name": "Strong in long text with parenthesis",
        "html": '<p>prac do kwoty <strong>100zł</strong>(oferta w załączniku)</p>',
        "issue": "Strong followed by parenthesis in flowing text",
    },
    {
        "name": "Section sign with strong",
        "html": '<p>paragraph §1<strong>important</strong>text</p>',
        "issue": "Special character followed by strong tag",
    },
]

for i, example in enumerate(examples, 1):
    print(f"\n{'='*80}")
    print(f"Example {i}: {example['name']}")
    print(f"{'='*80}")
    print(f"\nHTML Input:")
    print(f"  {example['html']}")
    print(f"\nIssue: {example['issue']}")
    
    result = translate_html_to_typst(example['html'])
    
    print(f"\nFixed Typst Output:")
    for line in result.split('\n'):
        if line:
            print(f"  {line}")
    
    # Check for problematic patterns
    issues = []
    if '](' in result:
        issues.append("]( pattern found")
    if ']#' in result:
        issues.append("]# pattern found")
    
    if issues:
        print(f"\n❌ WARNING: {', '.join(issues)}")
    else:
        print(f"\n✅ No problematic patterns detected!")

print(f"\n{'='*80}")
print("All examples processed successfully!")
print(f"{'='*80}\n")
