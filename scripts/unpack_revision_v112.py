"""Validate the immutable v1.1.0 payload and overlay the v1.1.2 S11 Part 2 correction.

The original ZIP parts and v1.1.0 payload index are not modified.
No training or archived code is executed.
"""
from pathlib import Path, PurePosixPath
import argparse
import csv
import hashlib
import json
import zipfile
import shutil

EXPECTED_PARTS = 69
EXPECTED_BASE_VERSION = "v1.1.0"
EXPECTED_LEGACY_S11_ROWS = 6
EXPECTED_CORRECTED_S11_ROWS = 12

EXPECTED_S11_HEADER = [
    "Replacement set", "Dataset", "Regime pair",
    "Seed 42", "Seed 123", "Seed 2026",
]

LEGACY_S11_PATH = PurePosixPath(
    "external_90/final_table_exports/Revised-Supplementary-table-12.csv"
)

CORRECTED_S11_REPO_PATH = Path(
    "revisions/v1.1.0/final_table_exports/Revised-Supplementary-table-12.csv"
)


def csv_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    return [row for row in rows if row and any(cell.strip() for cell in row)]


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_member_path(name):
    posix_path = PurePosixPath(name)
    return (
        bool(name)
        and not name.startswith("/")
        and "\\" not in name
        and ":" not in name
        and ".." not in posix_path.parts
        and not posix_path.is_absolute()
    )


def unpack(output):
    repository_root = Path(__file__).resolve().parents[1]
    output_dir = Path(output).expanduser().resolve()

    if (
        output_dir == repository_root
        or repository_root in output_dir.parents
        or output_dir in repository_root.parents
    ):
        raise ValueError(
            "Choose a new output directory outside the repository and not its parent."
        )

    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError("Output directory must be empty.")

    index_path = repository_root / "revisions/v1.1.0/payload_index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))

    if index.get("version") != EXPECTED_BASE_VERSION:
        raise ValueError("Unexpected base payload version.")

    if len(index.get("parts", [])) != EXPECTED_PARTS:
        raise ValueError("Expected exactly 69 ZIP parts.")

    all_members = set()

    # Validate all original ZIP parts before extraction.
    for part_info in index["parts"]:
        part_path = (repository_root / part_info["path"]).resolve()

        if repository_root not in part_path.parents:
            raise ValueError("ZIP part path escapes repository.")

        if part_path.stat().st_size != part_info["bytes"]:
            raise ValueError("ZIP part size mismatch: " + part_info["path"])

        if sha256_file(part_path) != part_info["sha256"]:
            raise ValueError("ZIP SHA256 mismatch: " + part_info["path"])

        with zipfile.ZipFile(part_path) as archive:
            bad_member = archive.testzip()

            if bad_member is not None:
                raise ValueError("ZIP CRC mismatch: " + part_info["path"])

            names = archive.namelist()

            if len(names) != part_info["members"]:
                raise ValueError("ZIP member-count mismatch.")

            for name in names:
                if not safe_member_path(name):
                    raise ValueError("Unsafe ZIP member path: " + name)

                if name in all_members:
                    raise ValueError("Duplicate ZIP member path: " + name)

                all_members.add(name)

    if len(all_members) != index["files"]:
        raise ValueError("Total payload member-count mismatch.")

    if LEGACY_S11_PATH.as_posix() not in all_members:
        raise ValueError("Historical S11 CSV is missing.")

    corrected_source = repository_root / CORRECTED_S11_REPO_PATH

    if not corrected_source.is_file():
        raise FileNotFoundError("Corrected S11 CSV is missing.")

    corrected_rows = csv_rows(corrected_source)

    if not corrected_rows or corrected_rows[0] != EXPECTED_S11_HEADER:
        raise ValueError("Corrected S11 CSV has an unexpected header.")

    if len(corrected_rows) - 1 != EXPECTED_CORRECTED_S11_ROWS:
        raise ValueError("Corrected S11 CSV must contain exactly 12 data rows.")

    if any(len(row) != len(EXPECTED_S11_HEADER) for row in corrected_rows):
        raise ValueError("Unexpected S11 column count.")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Extract the original, unchanged v1.1.0 ZIP parts.
    for part_info in index["parts"]:
        part_path = repository_root / part_info["path"]

        with zipfile.ZipFile(part_path) as archive:
            archive.extractall(output_dir)

    # Verify the original payload mapping before applying the correction.
    mapping_path = output_dir / "PUBLIC_SOURCE_MAPPING.json"
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))

    for item in mapping:
        if not safe_member_path(item["path"]):
            raise ValueError("Unsafe source-mapping path.")

        relative_path = PurePosixPath(item["path"])
        mapped_path = output_dir.joinpath(*relative_path.parts).resolve()

        if output_dir not in mapped_path.parents:
            raise ValueError("Source-mapping path escapes output.")

        if sha256_file(mapped_path) != item["sha256"]:
            raise ValueError("Payload hash mismatch: " + item["path"])

    legacy_s11_path = output_dir.joinpath(*LEGACY_S11_PATH.parts)
    legacy_rows = csv_rows(legacy_s11_path)

    if len(legacy_rows) - 1 != EXPECTED_LEGACY_S11_ROWS:
        raise ValueError("Expected the historical six-row S11 copy.")

    # Overlay the corrected v1.1.2 public CSV.
    # Original ZIP files and payload_index.json remain unchanged.
    shutil.copyfile(corrected_source, legacy_s11_path)

    final_rows = csv_rows(legacy_s11_path)

    if len(final_rows) - 1 != EXPECTED_CORRECTED_S11_ROWS:
        raise ValueError("S11 overlay verification failed.")

    if final_rows != corrected_rows:
        raise ValueError("S11 overlay differs from corrected source.")

    result = {
        "base_payload_version": index["version"],
        "correction_overlay": "v1.1.2",
        "parts_verified": len(index["parts"]),
        "files_extracted": len(all_members),
        "source_mapped_payloads_verified": len(mapping),
        "historical_s11_rows_before_overlay": len(legacy_rows) - 1,
        "corrected_s11_rows_after_overlay": len(final_rows) - 1,
        "corrected_s11_sha256": sha256_file(legacy_s11_path),
        "output": str(output_dir),
        "no_training_or_archived_code_executed": True,
        "original_zip_parts_and_v1_1_0_index_modified": False,
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    unpack(parser.parse_args().output)
