import importlib


def get_version(name: str) -> str | None:
    try:
        module = importlib.import_module(name)
        return str(module.__version__)
    except ImportError:
        return None


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    reagents: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
    ]
    all_present: bool = True
    for name, description in reagents:
        version = get_version(name)
        if version is None:
            print(f"[MISSING] {name}")
            print("pip: pip install -r ex0/requirements.txt")
            print("Poetry: poetry install")
            all_present = False
        else:
            print(f"[OK] {name} ({version}) - {description}")
    print("")
    print("pip vs Poetry:")
    print("requirements.txt declares what to install;",
          "pip resolves it at install time.")
    print("pyproject.toml declares the same constraints,",
          "and Poetry pins the resolved")
    print("versions in poetry.lock so every install is identical.")
    print("")
    if all_present:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
