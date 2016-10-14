//
// Debug statement printout macros
//
// Using compile flag to turn on and turn off the debug printout
//

//#define DEBUG  // If this is defined before inclusion the debug statements will print

#ifdef DEBUG
#define DEBUG_X( VAL ) printf("\n(%s:%d) " #VAL " = 0x%X", __FN__, __LINE__, VAL);
#define DEBUG_D( VAL ) printf("\n(%s:%d) " #VAL " = %d", __FN__, __LINE__, VAL);
#define DEBUG_C( VAL ) printf("\n(%s:%d) " #VAL " = %c", __FN__, __LINE__, VAL);
#define DEBUG_STR( VAL ) printf("\n(%s:%d) " #VAL,  __FN__, __LINE__);
#define DEBUG_S( VAL ) printf("\n(%s:%d) " #VAL " = %s", __FN__, __LINE__, VAL);
#else
#define DEBUG_X( VAL )
#define DEBUG_D( VAL )
#define DEBUG_C( VAL )
#define DEBUG_STR( VAL )
#define DEBUG_S( VAL )
#endif // NEVER
//
// undefine and re-define the symbol __FN__ with the name of the function
// that follows. This allows the debug printouts to include the function
// name in the identification.
// Example use:
/*
#undef __FN__
#define __FN__ "main"
*/
#if defined(__FN__)
#define __FN__ "UNDEFINED __FN__"
#endif

#ifndef ALWAYS
#define ALWAYS
#endif

