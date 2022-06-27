#include <iostream>
#pragma GCC optimize("O3")
using namespace std;


//i imported a linked list class i wrote previously and modified it because the vectors were giving me some trouble and i wanted complete control of the methods used in my data structure
template <typename T>
class Node
{
public:
    T data;
    Node<T>* next;
    Node()
    {
        this->next = NULL;
    }
    Node(T data)
    {
        this->data = data;
        this->next = NULL;
    }

};


template <typename T>
class linkedList
{
protected:

private:
    Node<T>* head;
    Node<T>* getEnd(Node<T>* head_ref);
    Node<T>* partition(Node<T>* head_ref, Node<T>* end, Node<T>** newHead, Node<T>** newEnd);
    Node<T>* quickSortRecursive(Node<T>* head_ref, Node<T>* end);
    Node<T>* SortedMerge(Node<T>* a, Node<T>* b);
    void FrontBackSplit(Node<T>* source, Node<T>** frontRef, Node<T>** backRef);
    void sortedInsert(Node<T>* newNode);
public:
    Node<T>* sorted{};
    linkedList()
    {
        head = NULL;

    }

    Node<T>* search(uint16_t firmId);
    Node<T>* search(uint16_t firmId, string symbol);
    Node<T>* modifySearch(uint16_t firmId, string symbol, float newPrice);
    int getLength();
    Node<T>* findHighestBuy(uint16_t firmId, string symbol);
    Node<T>* findLowestSell(uint16_t firmId, string symbol);
    void outputFirms();
    void add(T data);
    void sortedadd(Node<T>* node);
    bool searchDelete(uint16_t firmId, string symbol);
    void quickSort();
    void mergeSort(Node<T>**head_ref);
    void insertionSort();
};

template <typename T>
void linkedList<T>::add(T data) {
    Node<T>* newNode = new Node<T>(data);
    newNode->data = data;

    if (head == NULL)
    {
        head = newNode;
        return;
    }
    Node<T>* temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newNode;

}
template<typename T>
void linkedList<T>::sortedadd(Node<T>* node)
{
    Node<T>* current; 

    if (head==NULL || head->data->firmId>=node->data->firmId) {
        node->next = head;
        head = node;
    }
    else {
        current = head;
        while (current->next != NULL && current->data->firmId < node->data->firmId)
            current = current->next;
        node->next = current->next;
        current->next =node;
    }
}
template<typename T>
bool linkedList<T>::searchDelete(uint16_t firmId, string symbol)
{
    Node<T>* current = this->head;
    Node<T>* previous = NULL;

    if (current != NULL && current->data->firmId == firmId && current->data->getSymbol() == symbol) {
        this->head = current->next;
        delete current;
        return false;
    }
    else
        while (current != NULL && (current->data->firmId != firmId || current->data->getSymbol() != symbol)) {
            previous = current;
            current = current->next;
        }
    if (current == NULL) {
        return false;
    }

    previous->next = current->next;

    delete current;
    return true;
}

template<typename T>
Node<T>* linkedList<T>::getEnd(Node<T>* head_ref)
{
    Node<T>* current = head_ref;
    while (current != NULL && current->next != NULL) {
        current = current->next;
    }
    return current;
}

template <typename T>
Node<T>* linkedList<T>::partition(Node<T>* head_ref, Node<T>* end, Node<T>** newHead, Node<T>** newEnd)
{
    Node<T>* pivot = end;
    Node<T>* previous = NULL, * current = head_ref, * tail = pivot;

    while (current != pivot) {
        //checks if a node has a value less than the current pivot
        if (current->data->firmId <= pivot->data->firmId) {
            //then the pivot becomes the new head 
            if ((*newHead) == NULL)
                (*newHead) = current;

            previous = current;
            current = current->next;
        }
        else { //if the node does have a value greater than the pivot
            //move to to the next value of the tail
            if (previous) //checks the existience of the previous node
                previous->next = current->next;
            Node<T>* temp = current->next;
            current->next = NULL;
            tail->next = current;
            tail = current;
            current = temp;
        }
    }
    // if the pivot is the smallest value, aka no other nodes are smaller
    if ((*newHead) == NULL)
        (*newHead) = pivot; // assigns the pivot as the list head
    (*newEnd) = tail;

    return pivot;


}

template<typename T>
Node<T>* linkedList<T>::quickSortRecursive(Node<T>* head_ref, Node<T>* end)
{
    if (!head_ref || head_ref == end)//checks if the function can be run ,returns the list head otherwise
        return head_ref;

    Node<T>* newHead = NULL, * newEnd = NULL;

    //partitions the list, passes newHead and newEnd by reference
    Node<T>* pivot = partition(head_ref, end, &newHead, &newEnd);

    //if there is no smaller element than the pivot, then you dont need recur
    if (newHead != pivot) {
        Node<T>* temp = newHead;
        while (temp->next != pivot)
            temp = temp->next;
        temp->next = NULL;

        //uses recursion for everything before the pivot
        newHead = quickSortRecursive(newHead, temp);

        temp = this->getEnd(newHead);
        temp->next = pivot;
    }

    //use recursion for everything after pivot
    pivot->next = quickSortRecursive(pivot->next, newEnd);
    this->outputFirms();
    cout << "sorted" << endl;
    return newHead;
}

template<typename T>
Node<T>* linkedList<T>::SortedMerge(Node<T>* x, Node<T>* y)
{
    Node<T>* result = NULL;

    if (x == NULL)
        return y;
    else if (x == NULL)
        return y;

    if (x->data->firmId <= y->data->firmId) {
        result = x;
        result->next = SortedMerge(x->next, y);
    }
    else {
        result = y;
        result->next = SortedMerge(x, y->next);
    }
    return result;
}

template<typename T>
void linkedList<T>::FrontBackSplit(Node<T>* source, Node<T>** frontRef, Node<T>** backRef)
{
    Node<T>* fast;
    Node<T>* slow;
    slow = source;
    fast = source->next;

    while (fast != NULL) {
        fast = fast->next;
        if (fast != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
    }

    *frontRef = source;
    *backRef = slow->next;
    slow->next = NULL;
}

template<typename T>
void linkedList<T>::sortedInsert(Node<T>* newNode)
{
    if (this->sorted == NULL || sorted->data->firmId >= newNode->data->firmId) {
        newNode->next = sorted;
        sorted = newNode;
    }
    else {
        Node<T>* current = sorted;
        while (current->next != NULL && current->next->data->firmId < newNode->data->firmId) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
}

template <typename T>
void linkedList<T>::quickSort() {
    this->quickSortRecursive(this->head, getEnd(this->head)); //public call to the recursive sort funcion
    return;
}
template<typename T>
void linkedList<T>::mergeSort(Node<T>** head_ref)
{
    Node <T>* temphead = *head_ref;
    Node<T>* x;
    Node<T>* y;

    if ((temphead == NULL) || temphead->next == NULL)
        return;

    FrontBackSplit(temphead, &x, &y);

    mergeSort(&x);
    mergeSort(&y);

    this->head = SortedMerge(&x, &y);
}
template<typename T>
void linkedList<T>::insertionSort()
{
    this->sorted = NULL;
    Node<T>* current = this->head;

    while (current != NULL) {
        Node<T>* next = current->next;
        sortedInsert(current);
        current = next;
    }
    this->head = sorted;
}
template <typename T>
Node<T>* linkedList<T>::search(uint16_t firmId) {// tried to make this function universal between the orders and firms linked list, we'll see how it goes
    Node<T>* current = head;
    while (current != NULL) {

        if (current->data->firmId == firmId)
        {
            return current;
        }
        current = current->next;
    }
    return NULL;
}

template <typename T>
Node<T>* linkedList<T>::search(uint16_t firmId, string symbol) {// tried to make this function universal between the orders and firms linked list, we'll see how it goes
    Node<T>* current = head;
    while (current != NULL) {
        //cout <<"firmId:" << current->data->firmId << endl;
        if (current->data->firmId == firmId && current->data->getSymbol() == symbol)
        {
            return current;
        }
        current = current->next;
    }
    return NULL;
}
template <typename T>
int linkedList<T>::getLength()
{
    Node<T>* current = head;
    int count = 0;
    while (current != NULL)
    {
        count++;
        current = current->next;
    }
    return count;
}

template <typename T>
Node<T>* linkedList<T>::modifySearch(uint16_t firmId, string symbol, float newPrice) {
    Node<T>* current = head;
    while (current != NULL) {
        if (current->data->firmId == firmId && current->data->getSymbol() == symbol) {
            current->data->setPrice(newPrice);
            return current;
        }
        current = current->next;
    }
    return NULL;
}





template <typename T>
Node<T>* linkedList<T>::findHighestBuy(uint16_t firmId, string symbol) {
    Node<T>* highest = NULL;
    Node<T>* current = head;
    while (current != NULL) {
        if (current->data->firmId != firmId && current->data->getSymbol() == symbol && current->data->getSide() == 'B') {
            highest = current;
            if (current->data->getPrice() >= highest->data->getPrice()) {
                highest = current;
            }
        }
        current = current->next;
    }
    return highest;
}

template <typename T>
Node<T>* linkedList<T>::findLowestSell(uint16_t firmId, string symbol) {
    Node<T>* current = head;
    Node<T>* lowest = NULL;
    while (current != NULL) {
        if (current->data->firmId != firmId && current->data->getSymbol() == symbol && current->data->getSide() == 'S') {
            lowest = current;
            if (current->data->getPrice() <= lowest->data->getPrice()) {
                lowest = current;
            }
        }
        current = current->next;
    }
    return lowest;
}

template <typename T>
void linkedList<T>::outputFirms() {
    Node<T>* current = head;
    while (current != NULL) {
        cout << current->data->firmId << " " << current->data->getLiveOrders() << " " << current->data->getFills() << " " << current->data->getBalance() << " " << endl;
        current = current->next;
    }
    return;
}


class Order

{
protected:
    string symbol;
    char side;
    float price;
    bool filled;
public:
    uint16_t firmId;

    Order(uint16_t firmId, string symbol, char side, float price) {
        this->firmId = firmId;
        this->symbol = symbol;
        this->side = side;
        this->price = price;
        this->filled = false;
    }
    //i left these cause i neede firm id public but i didnt want to mess with the code i already had 
    void setfirmId(uint16_t firmId) {
        this->firmId = firmId;
    }
    uint16_t getfirmId() {
        return this->firmId;
    }
    void setSymbol(string symbol) {
        this->symbol = symbol;
    }
    string getSymbol() {
        return this->symbol;
    }
    void setSide(char side) {
        this->side = side;
    }
    char getSide() {
        return this->side;
    }
    void setPrice(float price) {
        this->price = price;
    }
    float getPrice() {
        return this->price;
    }
};

struct Firm {
protected:
    int numOfLiveOrders;
    int numOfFills;
    float balance;
public:
    uint16_t firmId;
    void editLiveOrders(int increment);
    void editFills(int increment);
    void editBalance(float increment);
    int getLiveOrders();
    int getFills();
    float getBalance();
    void setLiveOrders(int value);

    Firm(uint16_t firmId) {
        this->numOfFills = 0;
        this->numOfLiveOrders = 1;
        this->firmId = firmId;
        this->balance = 0.0f;
    }

};

void Firm::editLiveOrders(int increment) {
    this->numOfLiveOrders = this->numOfLiveOrders + increment; //i could have done ++ but i wanted to adapt it in case it was more than 1
    return;
}

void Firm::setLiveOrders(int value) {
    this->numOfLiveOrders = value;
}

void Firm::editFills(int increment) {
    this->numOfFills = this->numOfFills + increment;
    return;
}

void Firm::editBalance(float increment) {
    this->balance = this->balance + increment;
}

int Firm::getLiveOrders()
{
    return this->numOfLiveOrders;
}

int Firm::getFills()
{
    return this->numOfFills;
}

float Firm::getBalance()
{
    return this->balance;
}

class MatchingEngine
{


public:
    linkedList<Firm*> firms;
    // use of these functions is not required
    linkedList<Order*> orders;
    void onNewOrder(uint16_t firmId, string symbol, char side, float price) {
        if (orders.search(firmId, symbol) != NULL) {
            //cout << "This firm already as an existing order for " << symbol;
            return;
        }
        Order* newOrder = new Order(firmId, symbol, side, price);
        if (firms.search(firmId) == NULL) {
            Firm* newFirm = new Firm(firmId);
            firms.add(newFirm);

        }
        else {
            firms.search(firmId)->data->editLiveOrders(1);
        }

        orders.add(newOrder);
        //cout << "added" << endl;
        match(orders.search(firmId, symbol));
        return;

    }
    //finds the order in the orders vector and modifies its values
    void onModify(uint16_t firmId, string symbol, float price) {
        if (orders.search(firmId, symbol) != NULL) {
            Node<Order*>* order = orders.modifySearch(firmId, symbol, price);
            match(order);
            return;
        }
        else
            return;
    }
    //finds the order and deletes it from the vector
    void onCancel(uint16_t firmId, string symbol) {
        if (orders.search(firmId, symbol) != NULL) {
            orders.searchDelete(firmId, symbol);
            Node<Firm*>* firm = firms.search(firmId);
            firm->data->editLiveOrders(-1);
            return;
        }
        else
            return;
    }
    void match(Node<Order*>* order) {
        //cout << "matching" << order->data->firmId << " " << order->data->getSymbol()<< endl;
        Node<Order*>* sellOrder;
        Node<Order*>* buyOrder;
        if (order->data->getSide() == 'B') {
            buyOrder = orders.search(order->data->firmId, order->data->getSymbol());
            sellOrder = orders.findLowestSell(order->data->firmId, order->data->getSymbol());
            if (sellOrder == NULL)
                return;

        }
        else if (order->data->getSide() == 'S')
        {
            //cout << "sellOrder" << endl;
            sellOrder = orders.search(order->data->firmId, order->data->getSymbol());

            //iterate to find the highest buy value of that same symbol
            buyOrder = orders.findHighestBuy(order->data->firmId, order->data->getSymbol());
            if (buyOrder == NULL)
                return;
        }
        else {
            return;
        }
        if (sellOrder->data->getPrice() > buyOrder->data->getPrice())
            return;


        if (buyOrder->data->getPrice() >= sellOrder->data->getPrice()) {
            Node<Firm*>* buyFirm;
            buyFirm = firms.search(buyOrder->data->firmId);
            //Firm* buyFirm = firms[std::find (firmIds.begin(), firmIds.end(), buyOrder->getfirmId())];
            Node<Firm*>* sellFirm;
            sellFirm = firms.search(sellOrder->data->firmId);
            //minus the buy price for the buy firm balance and add the sell price to the sell firm balance
            //add a filled order to each one
            buyFirm->data->editBalance(-1 * (sellOrder->data->getPrice()));
            sellFirm->data->editBalance(sellOrder->data->getPrice());
            buyFirm->data->editLiveOrders(-1);
            orders.searchDelete(buyOrder->data->firmId, buyOrder->data->getSymbol());
            buyFirm->data->editFills(1);
            sellFirm->data->editLiveOrders(-1);
            orders.searchDelete(sellOrder->data->firmId, sellOrder->data->getSymbol());
            sellFirm->data->editFills(1);
            return;
        }
        else
            return;



    }
    //finds the order, could have done it differently but wanted to adapt it to this existing for loop

//iterates through orders and checks for an order with the same symbol, then compares the prices
    void print() {
        firms.insertionSort();
        firms.outputFirms();
    }


};

int main()
{
    MatchingEngine me;
    uint16_t N = 0;

    cin >> N;

    char orderType;
    uint16_t firmId;
    string symbol;
    char side;
    float price;



    for (size_t i = 0; i < N; i++)
    {
        // feel free to modify how the input read in from stdin
        cin >> orderType >> firmId >> symbol;

        switch (orderType)
        {
        case 'N':
            //cout << "new" << endl;
            cin >> side >> price;
            me.onNewOrder(firmId, symbol, side, price);
            break;
        case 'M':
            //cout << "mod" << endl;
            cin >> price;
            //cout << firmId << " " << symbol << " " << price << endl;
            me.onModify(firmId, symbol, price);
            break;
        case 'C':
            //cout << "cancel" << endl;
            me.onCancel(firmId, symbol);
            break;
        default:
            break;
        }
    }

    me.print();
}


