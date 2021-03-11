#!/bin/bash
#SBATCH --partition=batch
#SBATCH --constraint="EPYC|Intel"
#SBATCH --job-name=STEP--13
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --time=6-20:00:00
#SBATCH --mem=40GB
#SBATCH --output="%x.%j".out    # Standard output log
#SBATCH --error="%x.%j".err     # Standard error log

cd $SLURM_SUBMIT_DIR
export NSLOTS=12

module=cfour/2.1-iompi-2018a-serial
export OMP_NUM_THREADS=$NSLOTS

scratch_dir=/lscratch/$USER/tmp/$SLURM_JOB_ID
mkdir -p $scratch_dir


# make sure MRCC is around just in case
export PATH=$PATH:/work/jttlab/mrcc/2019/
prefix=/apps/eb/$module/
module load $module

# Copy job data
cp $SLURM_SUBMIT_DIR/ZMAT $scratch_dir
cp $prefix/basis/GENBAS $scratch_dir
cp $prefix/basis/ECPDATA $scratch_dir
if [ -e JAINDX ]; then cp JAINDX $scratch_dir ; fi
if [ -e JOBARC ]; then cp JOBARC $scratch_dir ; fi
if [ -e FCMINT ]; then cp FCMINT $scratch_dir ; fi
if [ -e GENBAS ]; then cp GENBAS $scratch_dir ; fi
if [ -e ECPDATA ]; then cp ECPDATA $scratch_dir ; fi
if [ -e OPTARC ]; then cp OPTARC $scratch_dir ; fi
if [ -e ISOTOPES ]; then cp ISOTOPES $scratch_dir ; fi
if [ -e ISOMASS ]; then cp ISOMASS $scratch_dir ; fi
if [ -e initden.dat ]; then cp initden.dat $scratch_dir ; fi
if [ -e OLDMOS ]; then cp OLDMOS $scratch_dir ; fi 

echo " Running cfour on `hostname`"
echo " Running calculation..."

cd $scratch_dir
xcfour >& $SLURM_SUBMIT_DIR/output.dat
xja2fja

echo " Saving data and cleaning up..."
if [ -e ZMATnew ]; then cp -f ZMATnew $SLURM_SUBMIT_DIR/ZMATnew ; fi

# Create a job data archive file
tar --transform "s,^,Job_Data_$SLURM_JOB_ID/," -vcf $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID.tar OPTARC FCMINT FCMFINAL ZMATnew JMOL.plot JOBARC JAINDX FJOBARC DIPDER HESSIAN MOLDEN NEWMOS den.dat
if [ -e zmat001 ]; then tar --transform "s,^,Job_Data_$SLURM_JOB_ID/," -vrf $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID.tar zmat* ; fi
gzip $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID.tar

echo " Job complete on `hostname`."

rm $scratch_dir -r

# ignored line -- do not remove
