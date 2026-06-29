# research_utilities

Collection of scripts and utilities for computational chemistry workflows,
developed over years of research involving **BOSS**, **Gaussian**, **HostDesigner**,
and **Spartan** software packages. Covers free energy perturbation (FEP), potential
of mean force (PMF) calculations, electronic structure benchmarking, conformer
analysis, file format conversion, and job queue management.

## Repository Structure

```
research_utilities/
├── boss/                    # BOSS (free energy perturbation / PMF) scripts
│   ├── keto-enol/           #  Keto-enol tautomerization PMF workflow
│   ├── mutase/              #  Imidazole mutase / protonation study
│   ├── 2D_pmf.sh            #  Set up 2D PMF calculations
│   ├── boss_thermodynamic_summary  #  Extract thermodynamics from BOSS .sum files
│   ├── go_xopt.sh           #  Optimize z-matrix to full convergence
│   ├── mk_zopts.sh          #  Create arrays of optimized z-matrices
│   ├── mk_1D_mutation_dirs.sh     #  Create 1D mutation directories
│   ├── z_spread.sh          #  Spread z-matrix to subdirectories with midpoints
│   ├── mv_sum2zmat.sh       #  Convert BOSS sum file to pmfzmat
│   ├── Ewald.equil.py       #  Set up Ewald alternative calculations (ionic liquids)
│   ├── SinglePoints.py      #  Set up BOSS single-point calculations in batch
│   ├── ...
├── conformer_analysis/      #  Conformer population analysis tools
│   ├── conformer_boltzmann_distribution  #  Boltzmann populations from delta G's
│   ├── conformers_percent_composition    #  Delta G's from percent abundances
│   ├── convert_deltaGs_to_histogram      #  Histogram data from delta G file
├── file_conversion/         #  Molecular file format conversion
│   ├── convert_c3d_to_pdb_and_pcm  #  Chem3D → PDB + PCM via OpenBabel
│   ├── convert_xyz_to_cc1          #  XYZ → CC1 format via OpenBabel
│   ├── pdb_2_smiles.sh             #  PDB → SMILES via OpenBabel
├── gaussian/                #  Gaussian electronic structure setup/analysis
│   ├── check_all_log_files         #  Check Gaussian outputs for termination/freqs
│   ├── check_gaussian_log_files    #  Check Gaussian outputs for stationary points
│   ├── check_imodes_and_energy     #  Check for imaginary modes + free energies
│   ├── convert_gjf_to_pdb          #  Gaussian output → PDB
│   ├── create_composite_calculation_inputs  #  CBS-QB3, G4, etc. inputs
│   ├── create_gaussian_inputs_for_basisset_jobs  #  Batch basis set inputs
│   ├── create_inputs_for_benchmarking*  #  Benchmarking setup (3 variants)
│   ├── create_inputs_for_ism_jobs       #  ISM solvation model inputs
│   ├── extract_Es_from_log_files       #  Extract energies from keto/enol logs
│   ├── gather_cavity_*            #  Cavity size/volume analysis
│   ├── run_gaussian_jobs          #  Batch Gaussian job submission
│   ├── run_multiple_gaussian_jobs #  Submit all .gjf files in directory
│   └── ...
├── hostdesigner/            #  HostDesigner host-guest design utilities
│   ├── run_hostdesigner     #  Run hostdesigner with required files
│   ├── filter_duplicates_from_hd_run  #  Filter duplicate structures
│   ├── hostd_union_difference.py     #  Compare two HostDesigner output sets
│   ├── run_pcm_engine       #  Automate PCM engine submissions
│   ├── separate             #  Separate output into individual complex PDBs
│   └── sort_pcm_engine_output  #  Sort PCM engine output
├── queue_management/        #  PBS/Torque batch queue management
│   ├── check_jobs           #  Check if jobs from jobs.txt are still running
│   ├── kill_all_jobs        #  Kill all jobs for current user
│   ├── kill_jobs_in_range   #  Kill jobs in a numeric ID range
│   ├── kill_jobs_in_text_file  #  Kill jobs listed in jobs.txt
│   ├── kill_queued_jobs     #  Kill only queued (not running) jobs
│   └── run_gaussian_asc     #  Submit Gaussian jobs to batch queue
├── spartan/                 #  Spartan dihedral scan plotting
│   └── spartan_plot_dihedral_scan  #  Parse + plot dihedral scans (NumPy/SciPy/Matplotlib)
├── thermochemistry/         #  Thermochemical property calculators
│   └── calc_density_or_vol  #  Convert between density (g/cm³) and volume (Å³)
├── LICENSE                  #  BSD 2-Clause license
└── README.md                #  This file
```

## Software Dependencies

| Software | Used by | Purpose |
|---|---|---|
| **BOSS** | `boss/` | Free energy perturbation / PMF calculations |
| **Gaussian** | `gaussian/` | Electronic structure calculations |
| **HostDesigner** | `hostdesigner/` | Host-guest design |
| **Spartan** | `spartan/` | Molecular modeling (dihedral scans) |
| **OpenBabel** | `file_conversion/` | Molecular file format conversion |
| **Python 3** + NumPy, SciPy, Matplotlib | Various `.py` scripts | Data analysis and plotting |

## Usage Notes

### Hardcoded Paths
Some scripts originally contained hardcoded paths (e.g., `/home/aubbwc/`, `~/billy/`). Where
possible, these have been parameterized via environment variables. Check the script headers
for configurable variables such as:

- `TEMPLATE_DIR` — path to template directory (BOSS)
- `HOSTD_BIN` / `HOSTD_LIB` — HostDesigner binary/library paths
- `RUNBOSS` — path to the BOSS job submission script
- `ZMAT_DIR` — path to pre-optimized z-matrix directory

### Batch Queue System
The queue management scripts assume a PBS/Torque-like environment with `qstat`, `qdel`,
and `q` commands. Several scripts default to the username set in the `USER` environment
variable.

### Boltzmann/Conformer Analysis
The `conformer_analysis/` scripts use the standard formula:
```
P_i = exp(-ΔG_i / RT) / Σ_j exp(-ΔG_j / RT)
```
with `RT = 0.5921 kcal/mol` at 298 K.

## License

BSD 2-Clause. See `LICENSE`.
