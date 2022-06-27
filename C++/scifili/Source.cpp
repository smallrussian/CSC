
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <iostream>
#include <tuple>
#include "Header.h"
#include <istream>
#include <queue>
using namespace std;




 

//the return pile will be a queue  

int main()
{
	Librarian MadamPince;
	SearchTree Library;
	vector<Book> books;
	books = read_file("SciFiLiBooks.txt");
	LinkedList booklist;
	
	MadamPince.open(Library);
	//checklist.printList();
	Library.displayTree(Library.getRoot());
	//cout << books[1].getAuthor();
}
