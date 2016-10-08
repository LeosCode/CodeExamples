/*

Linked list include file

This contains utility functions for linked lists.
Some of these are the functions that are the coding test.
They are re-used in setting up lists for other tests.

There are also some rudimentary debug functions. The free IDE that
I am using doesn't have a working debugger so I have to do it
the hard but reliable way.

*/

//#define DEBUG  // If this is defined before inclusion the debug statements will print

#ifdef DEBUG
#define DEBUGPRINTX( VAL ) printf("\n(%s:%d) " #VAL " = %X", __FN__, __LINE__, VAL);
#define DEBUGPRINTD( VAL ) printf("\n(%s:%d) " #VAL " = %d", __FN__, __LINE__, VAL);
#define DEBUGPRINTS( VAL ) printf("\n(%s:%d) " #VAL , __FN__, __LINE__, VAL);
#else
#define DEBUGPRINTX( VAL )
#define DEBUGPRINTD( VAL )
#define DEBUGPRINTS( VAL )
#endif // NEVER


//
// Common code for all tests
//
//---------------------------------
//
// Define the linked list
//
typedef struct IntElement{
	struct IntElement *next;   // point to next element
	int			data;          // payload
}tIntElement;


//
// Test function to print out the linked list
//
#undef __FN__
#define __FN__ "printList"
void printList( tIntElement **head )
{
   //
   // point to start of list
   //
   DEBUGPRINTX( head )
	tIntElement	*ptr = *head;
	//
	// Loop over elements and print out
	//
	int count = 0;
	printf("\nLinked list contents");
    printf("\naddr\tindex\tdata");
	while( NULL != ptr )
	{
        //DEBUGPRINTX(ptr);
		printf("\n%0X\t%d\t%d", ptr, count++, ptr->data);
		ptr = ptr->next;
	}
   DEBUGPRINTX(ptr);
}
//
// Test function to free list nodes memory back to the system
//
#undef __FN__
#define __FN__ "freeList"
void freeList( tIntElement **head )
{
	//
	// point to start of list
	//
	DEBUGPRINTX( head )
	DEBUGPRINTS("Free elements from list.");
	tIntElement	*ptr = *head,
               *tmp = NULL;
	//
	// Loop over elements and free them
	//
	int count = 0;
	#ifdef DEBUG
	printf("\nLinked list contents");
    printf("\naddr\tindex\tdata");
	#endif
	while( NULL != ptr )
	{
      //DEBUGPRINTX(ptr);
#ifdef DEBUG
		printf("\n%0X\t%d\t%d", ptr, count++, ptr->data);
#endif
		tmp = ptr;
		ptr = ptr->next;
		free( tmp );
	}
   DEBUGPRINTX(ptr);
}
// ---------------------------------

#ifndef INSERT_C
//
// Insert a new element into the front of the list
// return: 0 = fail, 1 = success, head pointer updated
//
#undef __FN__
#define __FN__ "insertFront"
int insertFront( tIntElement **head, int data )
{
   //
	//Get storage for new data
	//
#ifdef DEBUG
   printf("\nInsert element on list.");
#endif
	tIntElement *newElement = (tIntElement *)malloc( sizeof(tIntElement));
	if( NULL == newElement )
   {
      printf("\n(%s:%d) Malloc failed!", __FN__, __LINE__);
      printf("\nnewElement = %X",newElement);
      return 0; 	// malloc failed
   }
   //
   // save the data value
   //
	newElement->data = data;
	//
	// put new element into the linked list at the start
   //
   DEBUGPRINTX( *head )
   DEBUGPRINTX( newElement )
   newElement->next = NULL;
   if( NULL != *head )
   {
      newElement->next = *head;		      // new element points to start of list
   }
	*head = newElement;					   // head of list pointer points to new element
	//
	return 1;
}
#endif
