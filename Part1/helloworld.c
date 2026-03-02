#include <omp.h>
#include <stdio.h>
int main(){
    #pragma omp parralel
    {
        int ID = 0;
        printf("hello(%d)\n", ID);
        printf("world(%d)\n", ID);
    }
}

