#include <stdio.h>

int fcn_080486eb(char *ebp_8, char *ebp_c) {
  int local_14h;
  FILE *local_10h;
  char *local_ch;

  local_14h = 1;
  if ((local_10h = fopen(ebp_c, "rb")) == 0) {
    local_14h = 0;
  }
  if (fseek(local_10h, 0xfffffc00, 2) != 0) {
    local_14h = 0;
  }
  local_ch = fgets(ebp_8, 0x400, local_10h);

  return local_14h;
}

