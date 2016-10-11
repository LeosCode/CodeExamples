/*

Arrays and Strings include file

This contains utility functions for arrays and strings.
Some of these are the functions that are the coding test.
They are re-used in setting up for other tests.

There are also some rudimentary debug functions. The free IDE that
I am using doesn't have a working debugger so I have to do it
the hard but reliable way.

*/

//#define DEBUG  // If this is defined before inclusion the debug statements will print

#ifdef DEBUG
#define DEBUG_X( VAL ) printf("\n(%s:%d) " #VAL " = %X", __FN__, __LINE__, VAL);
#define DEBUG_D( VAL ) printf("\n(%s:%d) " #VAL " = %d", __FN__, __LINE__, VAL);
#define DEBUG_S( VAL ) printf("\n(%s:%d) " #VAL " = %s"  , __FN__, __LINE__, VAL);
#else
#define DEBUG_X( VAL )
#define DEBUG_D( VAL )
#define DEBUG_S( VAL )
#endif // NEVER

