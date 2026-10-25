"""Point the notebooks and README at a different GitHub repository.

Usage:  python tools/set_repo.py OWNER REPO [BRANCH]

Example: python tools/set_repo.py my-user my-think-python main
"""
import sys, glob, pathlib

OLD_OWNER, OLD_REPO, OLD_BRANCH = "Alireza-Akhavan", "ThinkPython", "main"

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    owner, repo = sys.argv[1], sys.argv[2]
    branch = sys.argv[3] if len(sys.argv) > 3 else OLD_BRANCH
    root = pathlib.Path(__file__).resolve().parent.parent
    old = f"{OLD_OWNER}/{OLD_REPO}"
    new = f"{owner}/{repo}"
    files = list(root.glob("chapters_fa/*.ipynb")) + [root / "README.md", root / "TRANSLATION_NOTES.md"]
    for f in files:
        t = f.read_text(encoding="utf-8")
        t2 = t.replace(f"{old}/{OLD_BRANCH}/", f"{new}/{branch}/")
        t2 = t2.replace(f"{old}/blob/{OLD_BRANCH}/", f"{new}/blob/{branch}/")
        t2 = t2.replace(old, new)
        if t2 != t:
            f.write_text(t2, encoding="utf-8")
            print("updated", f.relative_to(root))

if __name__ == "__main__":
    main()
