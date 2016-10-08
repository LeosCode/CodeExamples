#include <stdio.h>
#include <stdlib.h>

#define DELETE_C

//#define DEBUG

#include <LinkedList.h>

//
// Scan the list for the matching element and delete from the list
//
#undef __FN__
#define __FN__ "deleteElement"
int deleteElement( tIntElement **head, tIntElement *pdelete )
{
	//
	// Need temp pointers to list nodes
	//
    tIntElement *ptr = NULL,
                 *tmp = NULL;

    DEBUGPRINTX( *head )
    DEBUGPRINTX( pdelete )
    //
    // Special case if the list is empty or if the element to delete is empty.
	// Check if the list is empty.
    //
    if( (tIntElement*) NULL == *head || (tIntElement *) NULL == pdelete )
    {
    	printf("\n*List is empty or delete element is empty.");
        return 0; // delete failed
    }
    printf("\nLooking for data %d", pdelete->data);
	//
	// Special case if the head is the element to delete
	//
    if( *head == pdelete )
    {
    	//
    	// Point the head to the next node
    	// and free the deleted node
    	//
    	printf("\nDelete the head of the list node.");
        tmp = *head;			// Save the head node
        *head = tmp->next;		// Point the head to the next node
        DEBUGPRINTX( tmp )
        free( tmp );			// Free the original head node
        return 1;
    }
	//
	// Scan the list looking for the element to delete
	//
    ptr = *head;
    while( ptr->next )
    {
    	//
    	// Found the element to delete?
    	//
        if( ptr->next != pdelete )
        {
            ptr = ptr->next;		// No - move to next element
        }
        else
        {
	       	//
	    	// Point to the next node
	    	// and free the deleted node
	    	//
	    	printf("\nDelete the node.");
            tmp = ptr->next;			// Save the delete node
            ptr->next = tmp->next;		// Point to the next node
            DEBUGPRINTX( tmp )
            free( tmp );				// Free the saved node
            return 1;
        }
    }
    printf("\n*Did not find node.");
    return 0;
}
//
// Test the delete element function
//
#undef __FN__
#define __FN__ "main"
int main(int argc, char *argv[])
{
	tIntElement *linkedList;		// head of list pointer
    linkedList = NULL;	// no entries in the list yet
    tIntElement node;
    int i = 0;
    
    node.data = 0;
    node.next = NULL;
    printf("\nDelete from empty list.");
    if( 1 == deleteElement( &linkedList, &node ) )
    {
    	printList( &linkedList);
	}
    //
    // Fill in the list with entries
    //
    for( i = 1; i < 10; ++i )
    {
        insertFront( &linkedList, i );
    }
	//
	// Show the list
	//
	printf("\nStarting list.");
	//
	// Delete empty node
	//
    printList( &linkedList);
        printf("\nDelete empty node.");
    if( 1 == deleteElement( &linkedList, NULL ) )
    {
    	printList( &linkedList);
	}
	//
	// Delete the second entry
	//
	printf("\nDelete the second entry on the list.");
    if( 1 == deleteElement( &linkedList, linkedList->next ) )
    {
    	printList( &linkedList);
	}
    //
    // Delete the first entry
    //
	printf("\nDelete the first entry on the list.");    
    if( 1 == deleteElement( &linkedList, linkedList ) )
    {
    	printList( &linkedList);
	}
	//
	// Delete missing entry
	//
	printf("\nDelete missing entry.");
	node.data = 9;
	node.next = NULL;
    if( 1 == deleteElement( &linkedList, &node ) )
    {
    	printList( &linkedList);
	}
    //
    // Return list to system memory
    //
    freeList( &linkedList );
    //
    printf("\n");
    system("pause");
    return 0;
}
