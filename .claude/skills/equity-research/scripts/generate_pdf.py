#!/usr/bin/env python3
"""
Generate a PDF from a markdown investment memo.

Usage:
    python generate_pdf.py <input.md> <output.pdf>

Requires:
    pip install markdown weasyprint

If weasyprint isn't available, will try to install it automatically.
"""

import sys
import subprocess


def ensure_dependencies():
    """Install markdown and weasyprint if missing."""
    try:
        import markdown  # noqa
        from weasyprint import HTML  # noqa
    except ImportError:
        print("Installing missing dependencies...", file=sys.stderr)
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet", "markdown", "weasyprint"]
        )


CSS = """
@page {
    size: letter;
    margin: 1in 0.9in;
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #888;
    }
}
body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #1a1a1a;
}
h1 {
    font-size: 22pt;
    font-weight: 700;
    color: #111;
    border-bottom: 3px solid #111;
    padding-bottom: 8px;
    margin-bottom: 4px;
}
h1 + p {
    font-size: 11pt;
    color: #555;
    margin-top: 0;
}
h2 {
    font-size: 14pt;
    font-weight: 700;
    color: #222;
    margin-top: 28px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
}
h3 {
    font-size: 11pt;
    font-weight: 700;
    color: #333;
    margin-top: 18px;
    margin-bottom: 6px;
}
p { margin: 8px 0; }
strong { color: #111; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 9.5pt;
}
th {
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    padding: 6px 10px;
    text-align: left;
    font-weight: 700;
}
td {
    border: 1px solid #ddd;
    padding: 5px 10px;
}
tr:nth-child(even) { background-color: #fafafa; }
hr { border: none; border-top: 1px solid #ddd; margin: 20px 0; }
ul, ol { margin: 8px 0; padding-left: 24px; }
li { margin: 4px 0; }
blockquote {
    border-left: 3px solid #999;
    margin: 12px 0;
    padding: 4px 16px;
    color: #555;
    font-style: italic;
    background: #f9f9f9;
}
em { color: #666; }
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_pdf.py <input.md> <output.pdf>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    ensure_dependencies()

    import markdown
    from weasyprint import HTML

    with open(input_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

    html_doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{html_body}
</body>
</html>"""

    HTML(string=html_doc).write_pdf(output_path)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    main()
