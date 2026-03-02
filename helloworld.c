#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]) 
{
int nthreads, tid;

/* Fork a team of threads, each has own copy of variables */
#pragma omp parallel private(nthreads, tid)
  {

  tid = omp_get_thread_num(); // Obtain thread number
  printf("Hello World from thread = %d\n", tid);

  /* Only master thread does this */
  if (tid == 0) 
    {
    nthreads = omp_get_num_threads();
    printf("From Thread 0, # threads = %d\n", nthreads);
    }

  }  /* All threads join master thread and disband */

}
