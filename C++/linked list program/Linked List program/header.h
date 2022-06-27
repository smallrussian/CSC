#include <iostream>
#include <string>
#include <vector>
using namespace std;

string read_file(string filename);

class Word 
{	
public:
	string word;
	int count=1;
	Word(string w);
	
};
template <class T>
class Node 
{
public:
	T data;
	int key;
	Node* next;
	Node();
	~Node();
	
};
template <class T>
class linkedList
{
	Node<T> * head, * tail;
public:
	linkedList();
	void add(T new_data, int key);
	T search(int index);
	int count();
}; 
