
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <iostream>
#include <tuple>
#include "Header.h"
#include <istream>
using namespace std;




 

//the return pile will be a queue  

int main()
{
	vector<Book> books;
	books = read_file("SciFiLiBooks.txt");
	LinkedList booklist;

	
	//booklist.printList();
	LinkedList checklist = makeInventoryList(booklist);
	
	checklist.sort();
	//checklist.printList();
	SearchTree Library;
	Library.listAdd(checklist);
	Library.displayTree(Library.getRoot());
	//cout << books[1].getAuthor();
}
