import os

LINE = "Good news: the deploy worked perfectly. Bad news: it deployed the version where I 'fixed' the bug by deleting the users who reported it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write((LINE + "\n").encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
