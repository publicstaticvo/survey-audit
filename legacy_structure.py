"""Run the original deterministic structural checks on a classified paper."""

import argparse
import asyncio
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path, help="Configured original checkout, named triage")
    parser.add_argument("classified_paper", type=Path, help="Original 02_classified_paper.json")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    checkout = args.checkout.resolve(strict=True)
    if checkout.name != "triage" or not (checkout / "structure" / "structure_check.py").is_file():
        parser.error("Pass the original triage checkout")
    sys.path.insert(0, str(checkout.parent))
    from triage.structure.structure_check import StructureCheck
    from triage.utility.paper_elements import Paper

    classified = json.loads(args.classified_paper.read_text(encoding="utf-8"))
    result = asyncio.run(StructureCheck()(Paper.from_skeleton(classified)))
    with args.output.open("x", encoding="utf-8", newline="\n") as output:
        json.dump(result, output, indent=2, ensure_ascii=False)
        output.write("\n")


if __name__ == "__main__":
    main()
