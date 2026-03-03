#!/bin/bash
#SBATCH --job-name=lab3
#SBATCH --account=eel6763
#SBATCH --qos=eel6763
#SBATCH --nodes=1  #(single node)
#SBATCH --ntasks=1  #(single process)
#SBATCH --cpus-per-task=16  #(32 total, class limit)
#SBATCH --mem-per-cpu=600mb
#SBATCH -t 00:05:00
#SBATCH -o Part1_Fig2_16_1600
#SBATCH -e errfile
export OMP_NUM_THREADS=8
./a.out 1600 1600 1600

