"""
Example usage of the HTML to Typst translator.
"""

from html2typst import translate_html_to_typst
import tempfile
import os


def example_basic():
    """Basic example."""
    print("=" * 60)
    print("EXAMPLE 1: Basic HTML Translation")
    print("=" * 60)
    
    html = """
    <h1>Document Title</h1>
    <p>This is a paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
    <p>Another paragraph with <u>underlined</u> text.</p>
    """
    
    result = translate_html_to_typst(html)
    print("\nHTML Input:")
    print(html)
    print("\nTypst Output:")
    print(result)
    print()


def example_lists():
    """Lists example."""
    print("=" * 60)
    print("EXAMPLE 2: Lists")
    print("=" * 60)
    
    html = """
    <h2>Shopping List</h2>
    <ul>
        <li>Apples</li>
        <li>Bananas</li>
        <li><strong>Oranges</strong></li>
    </ul>
    
    <h2>Instructions</h2>
    <ol>
        <li>First step</li>
        <li>Second step</li>
        <li>Final step</li>
    </ol>
    """
    
    result = translate_html_to_typst(html)
    print("\nHTML Input:")
    print(html)
    print("\nTypst Output:")
    print(result)
    print()


def example_quill():
    """Quill.js specific example."""
    print("=" * 60)
    print("EXAMPLE 3: Quill.js Features")
    print("=" * 60)
    
    html = """
    <p class="ql-align-center">Centered text</p>
    <p class="ql-align-right">Right aligned text</p>
    <p>Normal text with <span style="color: red;">colored</span> content.</p>
    <ul>
        <li class="ql-indent-1">Indented list item</li>
        <li>Normal list item</li>
    </ul>
    """
    
    result = translate_html_to_typst(html)
    print("\nHTML Input:")
    print(html)
    print("\nTypst Output:")
    print(result)
    print()


def example_edge_case():
    """Edge case from requirements."""
    print("=" * 60)
    print("EXAMPLE 4: Edge Case (Requirements)")
    print("=" * 60)
    
    html = '''<li class="ql-indent-1" style="text-align: justify;">
        <span style="color: windowtext;"><strong>Tekst</strong></span>
    </li>'''
    
    result = translate_html_to_typst(html)
    print("\nHTML Input:")
    print(html)
    print("\nTypst Output:")
    print(result)
    print()


def example_debug_mode():
    """Debug mode example."""
    print("=" * 60)
    print("EXAMPLE 5: Debug Mode")
    print("=" * 60)
    
    html = """
    <p>Test paragraph with <strong>bold</strong>.</p>
    <p class="ql-align-center">Centered text</p>
    <span style="color: blue; font-size: 20px;">Styled span</span>
    """
    
    # Create temporary log file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        log_path = f.name
    
    try:
        # Run in debug mode
        result = translate_html_to_typst(html, debug=True, debug_log_path=log_path)
        
        print("\nHTML Input:")
        print(html)
        print("\nTypst Output (still clean!):")
        print(result)
        print("\nDebug Log Contents:")
        with open(log_path, 'r') as f:
            log_content = f.read()
        print(log_content)
    finally:
        if os.path.exists(log_path):
            os.unlink(log_path)
    
    print()


def example_complex():
    """Complex real-world example."""
    print("=" * 60)
    print("EXAMPLE 6: Complex Document")
    print("=" * 60)
    
    html = """
    <h1>Annual Report 2024</h1>
    
    <h2>Executive Summary</h2>
    <p>This document presents the <strong>annual financial results</strong> for fiscal year 2024.</p>
    
    <h3>Key Highlights</h3>
    <ul>
        <li>Revenue increased by <strong>25%</strong></li>
        <li>Customer base grew to <em>1 million users</em></li>
        <li>Launched <u>3 new products</u></li>
    </ul>
    
    <h3>Financial Metrics</h3>
    <ol>
        <li>Total Revenue: $10M</li>
        <li>Operating Expenses: $6M</li>
        <li>Net Profit: $4M</li>
    </ol>
    
    <blockquote>
    "This has been our best year yet." - CEO
    </blockquote>
    
    <h2>Technical Details</h2>
    <p>Our platform uses the following stack:</p>
    <pre><code>
    - Frontend: React.js
    - Backend: Node.js
    - Database: PostgreSQL
    </code></pre>
    
    <p>For more information, visit <a href="https://example.com">our website</a>.</p>
    """
    
    result = translate_html_to_typst(html)
    print("\nHTML Input:")
    print(html)
    print("\nTypst Output:")
    print(result)
    print()


def example_production_vs_debug():
    """Compare production and debug modes."""
    print("=" * 60)
    print("EXAMPLE 7: Production vs Debug Mode")
    print("=" * 60)
    
    html = '<p>Test with <span class="ql-size-large" style="color: red;">styling</span></p>'
    
    # Production mode
    print("\n--- PRODUCTION MODE ---")
    result_prod = translate_html_to_typst(html, debug=False)
    print("Output:")
    print(result_prod)
    
    # Debug mode
    print("\n--- DEBUG MODE ---")
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        log_path = f.name
    
    try:
        result_debug = translate_html_to_typst(html, debug=True, debug_log_path=log_path)
        print("Output (identical to production!):")
        print(result_debug)
        print("\nLog file:")
        with open(log_path, 'r') as f:
            print(f.read())
        
        print("\nVerification:")
        print(f"Production output == Debug output: {result_prod == result_debug}")
    finally:
        if os.path.exists(log_path):
            os.unlink(log_path)
    
    print()


if __name__ == '__main__':
    example_basic()
    example_lists()
    example_quill()
    example_edge_case()
    example_debug_mode()
    example_complex()
    example_production_vs_debug()
    
    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)
