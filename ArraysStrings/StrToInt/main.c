#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAIN_C

//#define DEBUG

#include <debug.h>
//
// Convert a string of decimal digits to an integer
// Will scan over leading blanks
// A leading '-' will make a negative number
// Any other characters will cause an error
//
// The reason for this design is these routines usually
// fail in the middle of the night while converting log files
// and the error silently propigates through the system.
// By checking and returning errors the calling code can
// detect the failure and take appropriate action.
//
// A 0 succesful return code allows for usage by the form:
//
//    if( strtoint( str, &val ) ) { val = 0; errorHandler( "conversion error" ); }
//
// Returns 0 for okay and 1 for error
//          retVal contains the result
//
#undef __FN__
#define __FN__ "strtoint"
int strtoint(char *str, int *retVal )
{
   int sign = 1;        // Carefull! This must be 1 for positive numbers
   *retVal = 0;          // Default value
   //
   // Scan over leading blanks
   //
   while('\0' != *str && isspace(*str) )
      ++str;
   //
   // check for empty string
   //
   if('\0' == *str)
   {
      DEBUG_STR("*Empty string")
      return 1;         // empty string is not okay
   }
   //
   // if there is a '-' remember to invert the result
   //
   if( '-' == *str )
   {
      sign = -1;        // multiply result by this at the end
      ++str;
   }
   //
   // convert characters to integer
   //
   while( '\0' != *str )
   {
      if( '9' >= *str && '0' <= *str )    // check for valid digit
      {
         *retVal *= 10;                   // increase value by 10's digit
         *retVal += *str - '0';           // add in 1's digit
      }
      else
      {
         DEBUG_STR("*Invalid digit")
         DEBUG_C( *str )
         return 1;                        // invalid digit
      }
      ++str;
   }
   //
   // invert the result if this is a negative number
   //
   *retVal *= sign;
   return 0;                             // return success
}
//
//
//
#undef __FN__
#define __FN__ "main"
int main()
{
   char *strval;
   char buf[30];
   int val, tmp;

#define TEST_N( VAL ) \
    strval = #VAL; \
    if( strtoint( strval, &tmp ) ) \
      printf("\nstrtoint() conversion error (" #VAL ")"); \
    else \
      printf("\nConvert %s\t= %d", strval, tmp);

#define TEST_V( VAL )\
   sprintf( buf,"%d", val);\
   strval = buf;\
   if( strtoint( strval, &tmp ) ) \
      printf("\nstrtoint() conversion error (" #VAL ")"); \
   else \
      printf("\nConvert %s\t= %d", strval, tmp );
   //
   tmp = sizeof(int)*8;
   printf("\nsizeof(int) = %d bits\n", tmp);
   //
   // test simple limits
   //
   TEST_N(0)
   TEST_N(1)
   TEST_N(-1)
   //
   // calculate max negative number
   // depending on architecture of this CPU
   //
   val = 0x80 << ((sizeof(int)-1) * 8);
   DEBUG_X( val )
   TEST_V( val )
   //
   // calculate max positive number
   //
   val = ~val;
   DEBUG_X( val )
   TEST_V( val )
   //
   // generate errors with invalid strings
   //
   TEST_N( 123.4 )
   TEST_N( 1-3 )
   
   printf("\n\n");
   return 0;
}
