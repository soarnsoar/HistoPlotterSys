#!/usr/bin/env python3

import argparse
import os
import shutil
import sys

import ROOT


def collect_object_paths(directory, prefix=""):
    """Collect object paths before creating any new directories or histograms."""
    paths = []

    for key in directory.GetListOfKeys():
        name = key.GetName()
        full_path = f"{prefix}/{name}" if prefix else name

        root_class = ROOT.TClass.GetClass(key.GetClassName())

        if root_class and root_class.InheritsFrom("TDirectory"):
            subdirectory = directory.GetDirectory(name)
            if subdirectory:
                paths.extend(collect_object_paths(subdirectory, full_path))
        else:
            paths.append(full_path)

    return paths


def make_directory(root_file, directory_path):
    """Create a nested ROOT directory and return the final directory."""
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


def get_target_variation(source_variation, histogram_name):
    """
    Apply the requested mapping:

    bminus Up   -> jesAsym Down
    bminus Down -> jesAsym Up
    bplus Up    -> jesAsym Up
    bplus Down  -> jesAsym Down
    """
    is_bminus = "Frombminus__HadronB" in histogram_name
    is_bplus = "Frombplus__HadronB" in histogram_name

    if is_bminus:
        return "Down" if source_variation == "Up" else "Up"

    if is_bplus:
        return source_variation

    return None


def process_root_file(input_path, output_path, overwrite_existing=False):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)

    if input_path != output_path:
        shutil.copy2(input_path, output_path)

    root_file = ROOT.TFile.Open(output_path, "UPDATE")

    if not root_file or root_file.IsZombie():
        raise RuntimeError(f"Failed to open ROOT file: {output_path}")

    try:
        source_paths = collect_object_paths(root_file)

        copied_count = 0
        skipped_count = 0

        for source_path in source_paths:
            components = source_path.split("/")

            # Required structure:
            # SYS/<dir1>/<dir2>/jes*/0/<Up|Down>/<histogram>
            if len(components) != 7:
                continue

            (
                top_directory,
                first_directory,
                second_directory,
                systematic_directory,
                zero_directory,
                source_variation,
                histogram_name,
            ) = components

            if top_directory != "SYS":
                continue

            if not systematic_directory.startswith("jes"):
                continue

            # Prevent an existing jesAsym directory from being used as input.
            if systematic_directory == "jesAsym":
                continue

            if zero_directory != "0":
                continue

            if source_variation not in ("Up", "Down"):
                continue

            target_variation = get_target_variation(
                source_variation,
                histogram_name,
            )

            if target_variation is None:
                continue

            source_histogram = root_file.Get(source_path)

            if not source_histogram:
                print(f"WARNING: Failed to read {source_path}", file=sys.stderr)
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
                f"SYS/{first_directory}/{second_directory}"
                f"/jesAsym/0/{target_variation}"
            )
            target_path = f"{target_directory_path}/{histogram_name}"

            existing_object = root_file.Get(target_path)

            if existing_object and not overwrite_existing:
                print(f"SKIP: {target_path} already exists")
                skipped_count += 1
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
            else:
                print(f"COPY: {source_path}")
                print(f"   -> {target_path}")
                copied_count += 1

            del cloned_histogram

        root_file.Write()

        print()
        print(f"Output file: {output_path}")
        print(f"Copied histograms: {copied_count}")
        print(f"Skipped objects: {skipped_count}")

    finally:
        root_file.Close()


def main():
    parser = argparse.ArgumentParser(
        description="Create jesAsym histogram shapes in a ROOT file."
    )
    parser.add_argument(
        "input",
        help="Input ROOT file",
    )
    parser.add_argument(
        "output",
        help="Output ROOT file; use the same path for in-place modification",
    )
    parser.add_argument(
        "--overwrite-existing",
        action="store_true",
        help="Overwrite existing histograms in jesAsym directories",
    )

    args = parser.parse_args()

    process_root_file(
        input_path=args.input,
        output_path=args.output,
        overwrite_existing=args.overwrite_existing,
    )


if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()
