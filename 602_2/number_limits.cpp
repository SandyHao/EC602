#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>
//Copyright 2018 SichunHao sichunh@bu.edu
int main()
{

  double Rs,Ri,Rm;

//Rs = 1 / smallest_float_greater_than_zero
//Rm = maximum_float_value / maximum_int_value
//Ri = maximum_int_value / N
//N is the largest integer such that all integers 1,2,3,...,N can be represented without loss of accuracy by a float of this size
  float t=(pow(2,24)-1)*pow(2,-23)*pow(2,127);
  double t2=(pow(2,24)-1)*pow(2,-23)*pow(2,127);
  double N1=pow(2,11)-1;
  double N2=pow(2,24)-1;
  double N3=pow(2,53)-1;
  double HALF_MIN=pow(2,-14);
  double HALF_MAX=pow(2,15)*(1+1-pow(2,-10));

  // calculate Rs, Ri, and Rm for half/binary16 vs int16_t

  std::cout<< "16 : Ri= " << (pow(2,15)-1)/N1 << " Rm= " << HALF_MAX/(pow(2,15)-1) << " Rs= " << 1/HALF_MIN << std::endl;

  // calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t

  std::cout<< "32 : Ri= " << (pow(2,31)-1)/N2 << " Rm= " << FLT_MAX/(pow(2,31)-1) << " Rs= " << 1/FLT_MIN << std::endl;

  // calculate Rs, Ri, and Rm for double/binary64 vs int64_t

  std::cout<< "64 : Ri= " << (pow(2,63)-1)/N3 << " Rm= " << DBL_MAX/(pow(2,63)-1) << " Rs= " << 1/DBL_MIN << std::endl;
 printf("%f",t);
printf("%f",t2);
  
  return 0;
}