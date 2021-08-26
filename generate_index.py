import os

for root, dirs, files in os.walk("."):
    entries = list(f for f in sorted(files) if f.endswith(".whl")) + list(sorted(dirs))
    filelist = "\n".join(
        f'<a href="https://dfm.io/custom-wheels/{root}/{f}">{f}</a><br>'
        for f in entries
    )
    with open(os.path.join(root, "index.html"), "w") as f:
        f.write(f"""
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>
<body>
{filelist}
</body>
</html>
""")
