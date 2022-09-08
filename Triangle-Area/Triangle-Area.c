#include <stdio.h>
#include <math.h>

int isValid(int a, int b, int c){
    if(a + b > c && a + c > b && b + c > a && a > 0 && b > 0 && c > 0)
        return 1;
    else return 0;
}

int main(){
    printf("Please input 3 sides of triangle, separated by enter.\n");
    double a = 0;
    double b = 0;
    double c = 0;
    if(scanf("%lf %lf %lf", &a, &b, &c) != 3 || !isValid(a, b, c)){
        printf("Invalid input.\n");
        return 1;
    }
    double p = (a + b + c) / 2;
    double S = sqrt(p * (p - a) * (p - b) * (p - c));
    printf("Area of triangle is %lf.\n", S);
    return 0;
}
