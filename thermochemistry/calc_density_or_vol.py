#!/usr/bin/env python3

import argparse

CONVERSION_FACTOR = 1.660600


def main():
    parser = argparse.ArgumentParser(
        description="Convert between molecular density (g/cm^3) and volume (Ang^3)."
    )
    parser.add_argument("-m", "--molwt", type=float, required=True,
                        help="Molecular weight (g/mol)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--density", type=float,
                       help="Density (g/cm^3); computes volume")
    group.add_argument("-v", "--volume", type=float,
                       help="Volume (Ang^3); computes density")

    args = parser.parse_args()

    print(f"Mol. wt. (g/mol)  = {args.molwt}")

    if args.volume is not None:
        density = args.molwt / args.volume * CONVERSION_FACTOR
        print(f"Volume  (Ang^3)   = {args.volume}")
        print(f"=> Density (g/cm^3) = {density:.6f}")
    elif args.density is not None:
        volume = args.molwt / args.density * CONVERSION_FACTOR
        print(f"Density (g/cm^3)  = {args.density}")
        print(f"=> Volume  (Ang^3) = {volume:.6f}")


if __name__ == "__main__":
    main()
