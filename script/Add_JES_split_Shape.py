#!/usr/bin/env python3

import argparse
import os
import shutil
import sys

import ROOT


def collect_object_paths(directory, prefix=""):
    """Collect all non-directory object paths before modifying the file."""
    object_paths = []

    for key in directory.GetListOfKeys():
        name = key.GetName()
        full_path = f"{prefix}/{name}" if prefix else name

        root_class = ROOT.TClass.GetClass(key.GetClassName())

        if root_class and root_class.InheritsFrom("TDirectory"):
            subdirectory = directory.GetDirectory(name)
            if subdirectory:
                object_paths.extend(
                    collect_object_paths(subdirectory, full_path)
                )
        else:
            object_paths.append(full_path)

    return object_paths


def make_directory(root_file, directory_path):
    """Create a nested directory structure and return the final directory."""
    current_directory = root_file

    for component in directory_path.strip("/").split("/"):
        next_directory = current_directory.GetDirectory(component)

        if not next_directory:
            next_directory = current_directory.mkdir(component)

        if not next_directory:
            raise RuntimeError(
                f"Failed to create directory: {directory_path}"
            )

        current_directory = next_directory

    return current_directory


def classify_histogram(histogram_name):
    """Return the target systematic directory for the histogram name."""
    if "Frombminus__HadronB" in histogram_name:
        return "jesbminus"

    if "Frombplus__HadronB" in histogram_name:
        return "jesbplus"

    return None


def delete_source_object(root_file, source_path):
    """Delete all key cycles of an object from its source directory."""
    directory_path, object_name = source_path.rsplit("/", 1)
    source_directory = root_file.GetDirectory(directory_path)

    if not source_directory:
        raise RuntimeError(
            f"Failed to access source directory: {directory_path}"
        )

    source_directory.Delete(f"{object_name};*")


def process_root_file(
    input_path,
    output_path,
    overwrite_existing=False,
    dry_run=False,
):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(
            f"Input file does not exist: {input_path}"
        )

    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)

    if input_path != output_path:
        shutil.copy2(input_path, output_path)

    open_mode = "READ" if dry_run else "UPDATE"
    root_file = ROOT.TFile.Open(output_path, open_mode)

    if not root_file or root_file.IsZombie():
        raise RuntimeError(
            f"Failed to open ROOT file: {output_path}"
        )

    moved_count = 0
    skipped_count = 0

    try:
        source_paths = collect_object_paths(root_file)

        for source_path in source_paths:
            components = source_path.split("/")

            # Expected structure:
            # SYS/<category>/<variable>/jes*/0/<Up|Down>/<histogram>
            if len(components) != 7:
                continue

            (
                top_directory,
                category_directory,
                variable_directory,
                source_systematic,
                zero_directory,
                variation,
                histogram_name,
            ) = components

            if top_directory != "SYS":
                continue

            if not source_systematic.startswith("jes"):
                continue

            if source_systematic in (
                "jesbminus",
                "jesbplus",
                "jesAsym",
            ):
                continue

            if zero_directory != "0":
                continue

            if variation not in ("Up", "Down"):
                continue

            target_systematic = classify_histogram(histogram_name)

            if target_systematic is None:
                continue

            source_histogram = root_file.Get(source_path)

            if not source_histogram:
                print(
                    f"WARNING: Failed to read {source_path}",
                    file=sys.stderr,
                )
                skipped_count += 1
                continue

            if not source_histogram.InheritsFrom("TH1"):
                print(
                    f"WARNING: Object is not a histogram: {source_path}",
                    file=sys.stderr,
                )
                skipped_count += 1
                continue

            target_directory_path = (
                f"SYS/{category_directory}/{variable_directory}/"
                f"{target_systematic}/0/{variation}"
            )
            target_path = (
                f"{target_directory_path}/{histogram_name}"
            )

            existing_object = root_file.Get(target_path)

            if existing_object and not overwrite_existing:
                print(
                    f"SKIP: Target already exists: {target_path}",
                    file=sys.stderr,
                )
                skipped_count += 1
                continue

            print(f"MOVE: {source_path}")
            print(f"   -> {target_path}")

            if dry_run:
                moved_count += 1
                continue

            target_directory = make_directory(
                root_file,
                target_directory_path,
            )

            cloned_histogram = source_histogram.Clone(histogram_name)
            cloned_histogram.SetDirectory(0)

            target_directory.cd()

            write_option = (
                ROOT.TObject.kOverwrite
                if overwrite_existing
                else 0
            )

            write_result = cloned_histogram.Write(
                histogram_name,
                write_option,
            )

            if write_result <= 0:
                print(
                    f"WARNING: Failed to write {target_path}",
                    file=sys.stderr,
                )
                skipped_count += 1
                del cloned_histogram
                continue

            delete_source_object(root_file, source_path)

            del cloned_histogram
            moved_count += 1

        if not dry_run:
            root_file.Write("", ROOT.TObject.kOverwrite)

    finally:
        root_file.Close()

    print()
    print(f"File: {output_path}")
    print(f"Moved histograms: {moved_count}")
    print(f"Skipped objects: {skipped_count}")

    if dry_run:
        print("Dry-run mode: no file was modified.")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Move bminus and bplus JES histograms into "
            "jesbminus and jesbplus directories."
        )
    )

    parser.add_argument(
        "input",
        help="Input ROOT file",
    )

    parser.add_argument(
        "output",
        help=(
            "Output ROOT file. Use the same path as input "
            "for in-place modification."
        ),
    )

    parser.add_argument(
        "--overwrite-existing",
        action="store_true",
        help="Overwrite existing target histograms",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned operations without modifying the file",
    )

    args = parser.parse_args()

    process_root_file(
        input_path=args.input,
        output_path=args.output,
        overwrite_existing=args.overwrite_existing,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()
