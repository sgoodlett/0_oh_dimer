#!/bin/bash
#SBATCH --job-name=sps  		# Job name (testBowtie2)
#SBATCH --partition=batch		# Partition name (batch, highmem_p, or gpu_p)
#SBATCH --ntasks=1			# Run job in single task, by default using 1 CPU core on a single node
#SBATCH --cpus-per-task=1	 	# CPU core count per task, by default 1 CPU core per task
#SBATCH --mem=5G			# Memory per node (4GB); by default using M as unit
#SBATCH --time=2:00:00              	# Time limit hrs:min:sec or days-hours:minutes:seconds
#SBATCH --export=NONE                   # Do not export any user’s explicit environment variables to compute node
#SBATCH --output=r2%A_%a.out		# Standard output log, e.g., testBowtie2_12345.out
#SBATCH --error=r3%A_%a.err		# Standard error log, e.g., testBowtie2_12345.err
#SBATCH --array=0-1999%200
cd $SLURM_SUBMIT_DIR			# Change directory to job submission directory (Optional!)

ml PSI4/1.4.0_conda

source activate ${ROOT_PSI4}
python batches.py arrdir/$(($SLURM_ARRAY_TASK_ID+4000))
conda deactivate

