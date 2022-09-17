#include <stdio.h>

int main()
{
    float a[3];
    a[0] = 10;
    a[1] = a[0] / 3.0;
    a[2] = a[1] * 3.0;
    unsigned char* ptr = (unsigned char*)a;
    for (int i = 0; i < 12; i++) {
        if (i % 4 == 0)  printf("\n");
        printf("0x%x\n", *ptr++);
    }
    return 0;
}
