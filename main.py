"""One-Liner Laughs entry: write a single funny line to the output file.

The joke is a one-liner of at most 200 characters. The grader runs this
program in a sandbox; it writes the line to ``entry.txt`` under the output
directory (``MAKEFUN_OUTPUT_DIR`` or ``/output``).
"""

import os

JOKE = "I asked my GPS for the scenic route; it took me past my ex's house twice and called it closure."
LIMIT = 200


def main():
    line = JOKE
    if not line or line != line.strip():
        raise SystemExit("joke must not be blank or padded with whitespace")
    if len(line) > LIMIT:
        raise SystemExit("joke is %d characters, over the %d limit" % (len(line), LIMIT))
    if "\n" in line or "\r" in line:
        raise SystemExit("joke must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(target, "r", encoding="utf-8") as handle:
        if handle.read() != line:
            raise SystemExit("written entry does not match the joke")


if __name__ == "__main__":
    main()
