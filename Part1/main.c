#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


/*   ttype: type to use for representing time */
typedef double ttype;
ttype tdiff(struct timespec a, struct timespec b)
/* Find the time difference. */
{
  ttype dt = (( b.tv_sec - a.tv_sec ) + ( b.tv_nsec - a.tv_nsec ) / 1E9);
  return dt;
}

struct timespec now()
/* Return the current time. */
{
  struct timespec t;
  clock_gettime(CLOCK_REALTIME, &t);
  return t;
}

struct timespec begin, end;
double time_spent;

int main(int argc, char* argv[]){

    if(argc != 4){
      printf("Please enter 3 arguments NRA NCA_RB, NCB\n");
      exit(EXIT_FAILURE);
    }
    int NRA =  atof(argv[1]); //rows in A
    int NCA_RB = atof(argv[2]); //rows in B = columns in B
    int NCB = atof(argv[3]); // columns in B

    
    int i, j, k;

    //changed to heap to avoid stack overflow for large matrices
    int (*A)[NCA_RB] = malloc(sizeof(int[NRA][NCA_RB]));
    int (*B)[NCB] = malloc(sizeof(int[NCA_RB][NCB]));
    int (*C)[NCB] = malloc(sizeof(int[NRA][NCB]));
    


    // printf("Initializing arrays...\n");
    for (i=0; i<NRA; i++){
      for (j=0; j<NCA_RB; j++){
          A[i][j]= i+j;
      }
    }


    // printf (" Contents of matrix A\n");
    // for (i=0; i<NRA; i++) {  
    //   for (j=0; j<NCA_RB; j++){
    //     printf("%d\t", A[i][j]);
    //   }
    //   printf("\n");
    //   printf("\n");
    // }    

            
    for (i=0; i<NCA_RB; i++){
      for (j=0; j<NCB; j++){
        B[i][j]= i-j;
      }
    }

    // printf (" Contents of matrix B\n");
    // for (i=0; i<NCA_RB; i++) {  
    //   for (j=0; j<NCB; j++){
    //     printf("%d\t", B[i][j]);
    //   }   
    //   printf("\n");
    //   printf("\n");
    // }     


    //start timer after array initialization 
    begin = now();
    #pragma omp parallel private(i, j, k) shared(A, B, C)
    {
      int sum;
      #pragma omp for
      
      for (i=0; i<NRA; i++){
        for (j=0; j<NCB; j++){
              C[i][j] = 0;
              for (k=0; k<NCA_RB; k++) {
                sum += C[i][j] + A[i][k] * B[k][j];
              }
              C[i][j] = sum;
        }
      }
    }
    end = now();
    time_spent = tdiff(begin, end);

    // printf ("Output Matrix contents:\n");
    //   for (i=0; i<NRA; i++) {  
    //     for (j=0; j<NCB; j++)
    //       printf("%d\t", C[i][j]);
    //       printf("\n");
    //       printf("\n");        
    //   }   

    printf("total time: %.8f sec\n", time_spent);

    free(A);
    free(B);
    free(C);
 
}