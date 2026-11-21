"""Write the competition's one-line AI coding agent joke to /output/entry.txt."""

from pathlib import Path

JOKE = "I told my AI coding agent the demo must not crash, so it replaced the demo with a video of the demo working."


def main():
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("JOKE must be exactly one line")
    if not JOKE.strip():
        raise ValueError("JOKE must not be blank")
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("JOKE must be between 1 and 280 Unicode code points")

    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
