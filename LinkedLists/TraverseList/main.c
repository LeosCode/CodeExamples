#include <stdio.h>
#include <stdlib.h>

#define TRAVERSE_C

//#define DEBUG

#include <LinkedList.h>
//
// Traverse a linked list searching for a match for a node
//
// return the node address or NULL
//
#undef __FN__
#define __FN__ "traverseList"
tIntElement *traverseList( tIntElement **head, int data)
{
    tIntElement *ptr = NULL,
                *retValue = NULL;

    DEBUGPRINTD(data)
    //
    // Check that the list isn't empty
    //
    if( (tIntElement *) NULL == *head )
    {
        printf("\n*Empty list.");
        return retValue;
    }
	//
	// Scan over the list
	//
    ptr = *head;
    while( NULL != ptr )
    {
    	DEBUGPRINTX(ptr)
    	DEBUGPRINTX(ptr->data)
		//
		// Compare the node to the list
		//
        if( ptr->data != data )
		{
			//
			// Move to next node
			//
            ptr = ptr->next;
        } else
		{
			//
			// Matched node to list
			//
            printf("\nMatch %0X: %d == %d", ptr, ptr->data, data);
            retValue = ptr;
            break;
        }
    }
	//
	// Not really necessary but good to know in an example
	//
    if( NULL == ptr )
    {
        printf("\nNo match for %d", data);
    }
    return retValue;
}
//
//
//
#undef __FN__
#define __FN__ "main"
int main(int argc, char *argv[]) {

    int i = 0;
    tIntElement *linkedList;				// head of list pointer
	linkedList = NULL;						// no entries in the list yet
	//
	// Create a list of data
	//
	for( i = 1; i < 10; ++i )
    {
       	insertFront( &linkedList, i );
    }
	printList( &linkedList);
	//
	// Search the list for data items
	//
	traverseList( &linkedList, 1);
	traverseList( &linkedList, 9);
	traverseList( &linkedList, 0);
	//
	// Free the data list nodes back to the system
	//
	freeList(&linkedList);

	printf("\n");
	system("pause");
	return 0;
}
