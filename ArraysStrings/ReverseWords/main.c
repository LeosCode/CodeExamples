#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define REVERSEWORDS_C

//#define DEBUG

#include <ArrayStrings.h>
//
// Reverse words in a string in place
// "The quick brown fox jumped over the lazy dog."
// -> "dog. lazy the over jumped fox brown quick The"
//
// Method used is:
//    Starting string
//       -> "Hellow world!"
//    Reverse characters of the string
//       -> "dlrow! olleH"
//    Reverse characters in the words of the string
//       -> "world! olleH"
//
#undef __FN__
#define __FN__ "reverseSubString"
//
// Reverse a string in place
//
// Returns the passed string with the characters reversed.
// Pass the length of the string so any sequence of characters
// can be reversed in any location of a string.
//
// Note: The string must be writeable.
// Not all compilers allow string literal constants to be changed.
//
void reverseSubString( char *str, int len )
{
   int count = len / 2;       // Swap takes 1/2 length
   char *dst = str;           // Destination is the start of the string
   char *src = &str[len-1];   // Source is the end of the string
   char temp;
   DEBUG_S( str )
   //
   // Scan over half the string
   //
   for( count = len/2; count > 0; --count )
   {
      //
      // Swap characters in place
      //
      temp = *dst;
      *dst = *src;
      *src = temp;
      //
      // Advance destination and source
      //
      ++dst;
      --src;
   }
}
//
// Reverse a string
//
// This is a wrapper function to use the substring reversal function
//
#undef __FN__
#define __FN__ "reverseString"
void reverseString( char *str )
{
   DEBUG_S( str )
   reverseSubString( str, strlen(str));
}
//
// Find the words in a string and reverse the letters in place
// Words are separated by spaces
//
#undef __FN__
#define __FN__ "reverseWords"
void reverseWords( char *str )
{
   char *start, *end, tmp;
   DEBUG_S( str )
   //
   start = str;
   end = str;
   //
   // Scan over the whole string
   //
   while( '\0' != *end )
   {
      //
      // Scan over characters looking for word breaks
      //
      if( ' ' != *end && '.' != *end && ',' != *end)
         {
            ++end;      // Advance end of word index
         }
         else
         {
            //
            // Found a word separator character
            //
            tmp = *end;                            // Save the break between the words
            reverseSubString( start, end-start );  // Reverse the word
            *end = tmp;                            // Replace the break character
            start = ++end;                         // Pont past the break to the start of the next word
         }
   }
   reverseSubString( start, end-start );
}
//
//
//
#undef __FN__
#define __FN__ "main"
int main()
{
   char *constString = "The quick brown fox jumped over the lazy dog.";
   char inputString[128];

   //
   // Copy the string to an array so that it can safely be modified
   //
   strncpy(inputString, constString, strlen(constString));
   printf("\nStart string:\t%s", inputString );
   //
   // Start by reversing the whole string
   //
   reverseString( inputString );
   printf("\nReverse string:\t%s", inputString );
   //
   // Reverse the words in the string
   //
   reverseWords( inputString );
   printf("\nReverse words:\t%s", inputString );

   printf("\n\n");
   system("pause");
   return 0;
}
