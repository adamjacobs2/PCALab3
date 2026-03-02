#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int arg, char* argv[]){
    int NRA =  atof(argv[1]); //rows in A
    int NCA_RB = atof(argv[2]); //rows in B = columns in B
    int NCB = atof(argv[3]); // columns in B

   
    

    int A[NRA][NCA_RB], B[NCA_RB][NCB], C[NRA][NCB];



    
    int i, j, k;
    for (i=0; i<NRA; i++){
        for (j=0; j<NCB; j++){
             C[i][j] = 0;
              for (k=0; k<NCA_RB; k++) {
                C[i][j] = C[i][j] + A[i][k] * B[k][j];
              }
        }
    }
    
 
}