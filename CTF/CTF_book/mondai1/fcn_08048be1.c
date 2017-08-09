#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void fcn_08048be1(char *arg_8, char *arg_c, char *arg_10) {
  int local_10h;
  int local_14h;
  int local_ch;

  int eax;
  int edx;
  
  local_10h = strlen(arg_c);
  srand(local_10h);
  local_14h = 0;
  for (local_14h = 0; local_14h < local_10h; local_14h++) {
    eax = rand();
    edx = eax;
    eax = eax / 31;
    eax = eax >> 22;
    edx = edx + eax;
    edx = edx & 1023;
    edx = edx - eax;
    arg_8[local_14h] = arg_c[local_14h] ^ arg_10[edx];
  }
}






