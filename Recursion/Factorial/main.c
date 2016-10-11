#include <stdio.h>
#include <stdlib.h>

#define DEBUG  // If this is defined before inclusion the debug statements will print

#ifdef DEBUG
#define DEBUG_X( VAL ) printf("\n(%s:%d) " #VAL " = %X", __FN__, __LINE__, VAL);
#define DEBUG_D( VAL ) printf("\n(%s:%d) " #VAL " = %d", __FN__, __LINE__, VAL);
#define DEBUG_S( VAL ) printf("\n(%s:%d) " #VAL , __FN__, __LINE__, VAL);
#else
#define DEBUG_X( VAL )
#define DEBUG_D( VAL )
#define DEBUG_S( VAL )
#endif // NEVER

#undef __FN__
#define __FN__ "factorialIterate"
//
// Compute N! by looping N times to calculate
// This may be more efficient time and space wise
// depending on how the compiler has to set up and tear down
// the calls to the function and how it optimizes the for loop.
//
// returns the N! answer
//
int factorialIterate( int n )
{
   int i,
   retVal = 1;
   //
   DEBUG_D(n)
   //
   // Caclulate N! by summing * [1 . . . n]
   //
   for( i = n; i > 1; --i )
   {
      retVal *= i;
   }
   return retVal;
}
//
// Calculate N! by calling the function recursively
// Each recursive call passes N-1 until it equals 0
// Then
//
#undef __FN__
#define __FN__ "factorial"
int factorial( int n )
{
   static int count = 0;   // This is how to keep track in recursive calls
   if( 0 == count )
   {
      DEBUG_D(n)
   }
   if( n > 0 )
   {
      // recursion case - return (n-1) * n
      int   nMinus1 = 0,
            nMinus1Timesn = 1;

      #ifdef DEBUG
      printf("\nRecursion iteration %d value %d", ++count, n);
    
      //
      // Break these out just to see the operations
      //
      nMinus1 = factorial(n - 1);         // sequence of n! . . . 0!
      nMinus1Timesn = nMinus1 * n;        // multiply [n! . . .0!] * n
      DEBUG_D(n)
      DEBUG_D(nMinus1)
      DEBUG_D(nMinus1Timesn)
      //
      // The magic is N! = N * (N-1)!
      // 5! = 4! * 5
      // But to get 4! you need 3!, 2!, and 1!
      // Each return from recursive call of factorial() is an answer in the sequence
      // The final return gives the final answer to the original call
      //
      return nMinus1Timesn;               // returns to factorial() n times, and then to the original caller.
     #else
      return factorial(n - 1) * n;        // Usual, cryptic way to write this
      #endif
   }
   // base case - if n equal 0 or 1 return 1
   #ifdef DEBUG
   printf("\nRecursion %d iterations.", count);
   #endif
   count = 0;
   return 1;
}
//
//
//
#undef __FN__
#define __FN__ "main"
int main()
{
   //
   // Exersize the factorial functions
   //
   printf("\nfactorial() 4! = %d", factorial( 4 ));
   printf("\nfactorial() 5! = %d", factorial( 5 ));
   printf("\nfactorialIterate 4! = %d", factorialIterate( 4 ));
   printf("\nfactorialIterate 5! = %d", factorialIterate( 5 ));
   //
   printf("\n");
   system("pause");
   return 0;
}
