#include <stdio.h>

int sum(int[], int);

int main()
{
  int local_4h = 0;
  int eax = 0;
  int edx = 0;
  int ebp_8[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

  int array_8048980[12] = {4885, 10656, 14249, 7244,
  17152, -22439, -41829, -7222,
  -12530, 18797, 13201, 22623};

  for (local_4h = 0; local_4h <= 11; local_4h++) {
    edx = sum(ebp_8, local_4h);
    eax = array_8048980[local_4h];
//    if (edx != eax) {
//      return 1;
//    }
  }
  return 0;
}


int sum(int ebp_8[], int ebp_c)
{
  int local_8h = 0;
  int local_4h = 0;
  int eax = 0;
  int ecx = 0;
  int edx = 0;

  int coff[] = {-72, -74, 91, 59, 53, -95, -32, -39, 93, 76, -31, 22, 
  78, -84, -96, 69, -21, -72, 89, -26, 21, 65, 3, 49, -46, 11, -39, 54,
  57, -14, 59, -10, 77, -34, 0, 99, 27, 4, 52, 23, -1, 43, -41, 13,
  9, -70, -16, 91, 60, -92, 84, 58, -8, -6, 91, 8, -30, -11, -5, -96,
  -91, -16, -96, 51, -56, -85, -52, 46, -78, 87, 96, -83, -32, -80, -80, 54,
  -28, -85, -38, -75, 5, 32, -80, -72, 5, -18, 6, 74, -9, -64, 30, -44,
  -26, -6, -22, 13, 30, 61, -100, 63, -19, -92, 68, -38, -11, -96, 44, -50,
  59, 4, 99, -62, -34, -89, -52, 87, 22, 38, 86, 15, -75, -92, -21, 62,
  -77, -31, -10, 90, 83, 89, 66, -17, -5, 23, -29, 16, 25, 50, 95, 65,
  -57, 35, 4, 22
  };

  printf("%d loop:\n", ebp_c);
  for (local_4h = 0; local_4h <= 11; local_4h++) {
    ecx = ebp_8[local_4h];
    edx = ebp_c;
    eax = 3 * ebp_c;
    eax = eax << 0x2;
    edx = local_4h;
    eax = eax + local_4h;
    printf("coff[%d] = %d, ecx = %d\n", eax, coff[eax], ecx);
    eax = coff[eax] * ecx;
    local_8h += eax;
  }
  return local_8h;
}