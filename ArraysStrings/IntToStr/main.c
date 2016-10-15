#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAIN_C

#define DEBUG

#include <debug.h>

//
// Convert integer to a string
// Pass in the value and a string result location
//
// Thread safe because temporary data is on the stack and
// the result location is passed from the calling function
//
#undef __FN__
#define __FN__ "intToStr"
void intToStr( int val, char *retStr )
{
   char buf[30];          // temporary string buffer
   int index = 0;
   int tmp;
   //
   // Test if the value is negative
   //
   DEBUG_D( val )
   if( val < 0 )
   {
      DEBUG_STR("Negative value")
      *(retStr++) = '-';   // first character in result is '-'
   }
   //
   // if the value is 0, put a 0 into the buffer
   //
   if( 0 == val )
   {
      DEBUG_STR("value = 0")
      buf[index++] = '0';          // force a single entry as 0
   }
   //
   // Build up digit string until value reaches 0
   //
   if( val >= 0 )
   {
      //
      // dealing with positive values
      //
      while( 0 != val )
      {
         buf[index++] = val % 10 + '0';   // extract 0 to 9 digit value and save
         val /= 10;                       // reduce value by 1 decimal digit
         DEBUG_C(buf[index-1])
      }
   }
   else
   {
      //
      // dealing with negative values
      //
      // have to convert individual digits to positive numbers
      // because you cannot represent the largest negative number
      // in the positive number space of an integer variable
      //
      // computer math :P
      //
      while( 0 != val )
      {
         //
         // convert digit to positive number
         //
         tmp = val % 10;
         tmp = ~tmp;
         ++tmp;
         DEBUG_D(tmp)
         buf[index++] = tmp + '0';        // extract 0 to 9 digit value and save
         val /= 10;                       // reduce value by 1 decimal digit
         DEBUG_C(buf[index-1])
      }
   }
   //
   // Reverse copy the buffer into the result string
   //
   while( --index >= 0 )
   {
      *(retStr++) = buf[index];     // reverse copy digits to result
   }
   *retStr = '\0';                  // finish the string
   return;
}
//
//
//
#undef __FN__
#define __FN__ "main"
int main()
{
   char str[128];
   int testVal = 123;
   //
   // Test with various int limit numbers
   //
   testVal = sizeof(int)*8;
   printf("\nsizeof(int) = %d bits", testVal);

   testVal = 123456789;
   intToStr( testVal, (char *) &str );
   printf("\nConvert (%d)\t= \"%s\"", testVal, str );

   testVal = -123456789;
   intToStr( testVal, (char *) &str );
   printf("\nConvert (%d)\t= \"%s\"", testVal, str );

   testVal = -1;
   intToStr( testVal, (char *) &str );
   printf("\nConvert (%d)\t\t= \"%s\"", testVal, str );

   testVal = 0x80 << ((sizeof(int)-1)*8);      // max negative number
   intToStr( testVal, (char *) &str );
   printf("\nConvert (%d)\t= \"%s\"", testVal, str );

   testVal = ~testVal;
   intToStr( testVal, (char *) &str );
   printf("\nConvert (%d) \t= \"%s\"", testVal, str );
   
   testVal = 0;
   intToStr( testVal, (char *) &str );
   printf("\nConvert (%d) \t\t= \"%s\"", testVal, str );

   printf("\n\n");
   system("Pause");
   return 0;
}
