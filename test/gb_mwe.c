#include "GraphBLAS.h"
//
#include <tau/tau.h>

TAU_MAIN()  // sets up Tau (+ main function)

TEST_CASE(DIM_CHECK, ROWS) {
  const int N = 10;

  GrB_Matrix A = NULL;
  GrB_Matrix_new(&A, GrB_FP64, N, N);
  GrB_Index nrows;
  GrB_Matrix_nrows(nrows, A);
  CHECK(nrows == N);
}