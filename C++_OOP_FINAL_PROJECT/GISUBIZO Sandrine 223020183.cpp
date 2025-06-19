//E-Commerce Order Processing system
#include <iostream>
#include <cstring>
using namespace std;

//Definition of struct Product 
struct Product {
    char sku[10];
    char name[30];
    float price;
};

// Definition of struct  OrderItem 
struct OrderItem {
    Product* prod;
    int qty;
};

class Order {
protected:
    OrderItem* items;
    int itemCount;
    int orderId;

public:
    Order(int id, int count) : orderId(id), itemCount(count) {
        items = new OrderItem[itemCount];
    }

    virtual ~Order() {
        delete[] items;
    }

    void setItem(int index, Product* p, int q) {
        if (index < itemCount) {
            items[index].prod = p;
            items[index].qty = q;
        }
    }

    int getOrderId() const {
        return orderId;
    }

    virtual float calcTotal() = 0;
};

class OnlineOrder : public Order {
    float shippingCost;

public:
    OnlineOrder(int id, int count, float shipping)
        : Order(id, count), shippingCost(shipping) {}

    float calcTotal() override {
        float total = 0;
        for (int i = 0; i < itemCount; ++i) {
            total += items[i].prod->price * items[i].qty;
        }
        return total + shippingCost;
    }
};

class InStoreOrder : public Order {
    float discount;

public:
    InStoreOrder(int id, int count, float disc)
        : Order(id, count), discount(disc) {}

    float calcTotal() override {
        float total = 0;
        for (int i = 0; i < itemCount; ++i) {
            total += items[i].prod->price * items[i].qty;
        }
        return total * (1 - discount);
    }
};

void addOrder(Order**& allOrders, int& size, Order* newOrder) {
    Order** temp = new Order*[size + 1];
    for (int i = 0; i < size; ++i) {
        temp[i] = allOrders[i];
    }
    temp[size] = newOrder;
    delete[] allOrders;
    allOrders = temp;
    size++;
}

void removeOrder(Order**& allOrders, int& size, int orderId) {
    int index = -1;
    for (int i = 0; i < size; ++i) {
        if (allOrders[i]->getOrderId() == orderId) {
            index = i;
            break;
        }
    }

    if (index != -1) {
        delete allOrders[index];
        for (int i = index; i < size - 1; ++i) {
            allOrders[i] = allOrders[i + 1];
        }
        size--;
        Order** temp = new Order*[size];
        for (int i = 0; i < size; ++i) {
            temp[i] = allOrders[i];
        }
        delete[] allOrders;
        allOrders = temp;
    }
}

int main() {
    Product p1 = {"SKU01", "desktop", 120000};
    Product p2 = {"SKU02", "other equipments", 2500};
    Order** allOrders = nullptr;
    int orderCount = 0;

    OnlineOrder* online = new OnlineOrder(101, 2, 1500);
    online->setItem(0, &p1, 1);
    online->setItem(1, &p2, 2);
    addOrder(allOrders, orderCount, online);

       InStoreOrder* instore = new InStoreOrder(102, 2, 0.10);
    instore->setItem(0, &p1, 1);
    instore->setItem(1, &p2, 1);
    addOrder(allOrders, orderCount, instore);


    for (int i = 0; i < orderCount; ++i) {
        cout << "Order ID: " << allOrders[i]->getOrderId()
             << ", Total: $" << allOrders[i]->calcTotal() << endl;
    }

    // Remove an order
    removeOrder(allOrders, orderCount, 101);
    cout << "\nAfter removing Order 101:\n";
    for (int i = 0; i < orderCount; ++i) {
        cout << "Order ID: " << allOrders[i]->getOrderId()
             << ", Total: $" << allOrders[i]->calcTotal() << endl;
    }

    // delete an order
    for (int i = 0; i < orderCount; ++i) {
        delete allOrders[i];
    }
    delete[] allOrders;

    return 0;
}

