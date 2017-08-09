#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int auth(char *user, char *pass)
{
  printf("user: %s\n", user);
  printf("pass: %s\n", pass);
}

int evil()
{
   printf("H@ck3d!!!\n");
   exit(1);
}

int input()
{
  int a = 0x33333333;
  int b = 0x44444444;
  char user[8] = "";
  char pass[8] = "";

  setreuid(geteuid(), -1);

  printf("addr: 0x%08x\n", (unsigned int)pass);
  scanf("%s", user);
  scanf("%s", pass);

  auth(user, pass);
}

int main() {
  input();
}
