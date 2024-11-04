#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "/home/sugurusa/Downloads/matgeo-main/codes/msoft/libs/matfun.h"
#include "/home/sugurusa/Downloads/matgeo-main/codes/msoft/libs/geofun.h"

// Calculate the points of intersection
void calculate_intersection(double **points) {
    double a = 2; // Coefficient for x^2 in the equation x^2 + y^2 = 32
    double b = 0; // Coefficient for x in the equation
    double c = -32; // Constant term
    
    double **roots = Matquad(a, b, c); // Get roots of the quadratic equation
    points[0][0] = roots[0][0]; //x-coordinate of the point P
    points[1][0] = roots[1][0]; //x-coordinate of the point Q
}

// Circle center at (0, 0)
void circle_center(double **center) {
    center[0][0] = 0; // x-coordinate
    center[1][0] = 0; // y-coordinate
}

int main() {
    double **points = createMat(2, 1);
    double **center = createMat(2, 1);
    
    calculate_intersection(points);
    circle_center(center);
    
    //printf("Center of Circle: (%.2f, %.2f)\n", center[0][0], center[1][0]);
    
    
    // Free allocated memory
    free(points);
    free(center);
    
    return 0;
}


