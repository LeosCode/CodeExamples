#include <stdio.h>
#include <stdlib.h>

#define INSERT_C

//#define DEBUG

#include <LinkedList.h>
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
   printf("\n\nInsert element on list.");
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




//
//
//
#undef __FN__
#define __FN__ "main"
int main(int argc, char *argv[])
{
   //
   // Linked list exists as long as main() is in scope
   //
    tIntElement *linkedList;   // head of list pointer
	linkedList = NULL;	      // no entries in the list yet
	int i = 1;
   //
   // Insert first element on empty list
   //
   DEBUGPRINTX( &linkedList )
   printf("\nInsert first element on empty list.");
	if( 0 == insertFront( &linkedList, i++ ) )
   {
      // Malloc failed
   }
   else {
      printList( &linkedList);         // Test the result
      //
      // Insert element into a list of elements
      //
      for( i; i < 4; ++i )
      {
          if( 0 == insertFront( &linkedList, i )  )
         {
            break;   // malloc failed
         } else {
            printList( &linkedList);
         }
      }
      //
      // free list memory back to the system
      //
      freeList( &linkedList );
   }
	//system("pause");
	return 0;
}
