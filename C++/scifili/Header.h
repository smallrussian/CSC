#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>
#include <iostream>
#include <tuple>
#include <istream>
using namespace std;
class Book
{
private:
	string title;
	string author;
	bool checkstatus; //true or false
	int importance; //unique to each book
	int getAuthorSize();
	int getTitleSize();
public:
	Book();
	Book(string newtitle, string newauthor, int newcheckstatus, int newimportance);
	

	string getTitle();
	string getAuthor();
	char* getAuthor(bool charindicator);
	char* getTitle(bool charindicator);
	bool getCheckStatus();
	int getImportance();
	void updateStatus(int newstatus);

	
	

};
//decided to throw some class inheritance in there to clean up my classes
class Node
{
protected:
	Book data;
	
};

class LinkNode : protected Node
{
protected:
	LinkNode* next;
public:
	LinkNode();
	LinkNode(Book data);
	friend class LinkedList;
	Book getData();
	LinkNode* getNext();
};

class TNode : protected Node
{
protected:
	TNode* left;
	TNode* right;
	TNode* parent;
public:
	friend class SearchTree;
	TNode();
	TNode(Book data);


};


class LinkedList
{
	int count();
	LinkNode* head;
	void deleteNode(int importance); //deletes by importance cause its unique to each book and is easier than pointers
	void swapData(LinkNode* a, LinkNode* b);
	void sortedInsert(LinkNode* newnode, LinkNode* sorted);
	LinkNode* getTail(LinkNode* cur);
	LinkNode* partition(LinkNode* end, LinkNode** newHead, LinkNode** newEnd);
	LinkNode* quickSortRecur(LinkNode*headref,LinkNode* end);
	void swapNodes(LinkNode** head_ref, LinkNode* currX, LinkNode* currY, LinkNode* prevY);
	LinkNode* recurSelectionSort(LinkNode* head);


public:
	LinkedList();
	void add(Book new_data);
	Book searchTitle(string title);
	vector<Book> searchAuthor(string author);
	void checkCleaner();
	void insertionSort();
	void printList();
	void sort();
	LinkNode* getHead();
	void quickSort();
	friend class TNode;
	friend class SearchTree;

};

class SearchTree
{
protected:
	TNode* root;
	TNode* sortedListToBST(LinkNode* rhead, LinkedList list);
	TNode* sortedListToBSTRecursive(LinkNode** rhead, int count);

public:
	friend class LinkedList;
	SearchTree();
	void displayTree(TNode* node);
	void add(LinkedList list);
	TNode* getRoot();
	Book search(TNode* node, string author);
	Book search(TNode* node, string title);

};
static inline void strip(std::string& s);
vector<Book> read_file(string filename);
LinkedList makeInventoryList(LinkedList list);
int compareABC(string str1, string str2);

// im using a c++ queue bc i am tired
class Librarian
{
public:
	void checkIn();
	void searchByAuthor();
	void searchByTitle();
	void resuce(); //iterate through importance values with a search through the bst 
	void open();
	void EndofDay();
};