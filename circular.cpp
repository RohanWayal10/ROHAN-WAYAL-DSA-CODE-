#include <iostream>
using namespace std;

#define SIZE 5

class CircularQueue {
private:
    int arr[SIZE];
    int front, rear;

public:
    CircularQueue() {
        front = -1;
        rear = -1;
    }

    void enqueue(int value) {
        if ((front == 0 && rear == SIZE - 1) || (rear == (front - 1) % (SIZE - 1))) {
            cout << "Queue is Full!" << endl;
            return;
        } 
        else if (front == -1) {
            front = rear = 0;
            arr[rear] = value;
        } 
        else if (rear == SIZE - 1 && front != 0) {
            rear = 0;
            arr[rear] = value;
        } 
        else {
            rear++;
            arr[rear] = value;
        }
    }

    void dequeue() {
        if (front == -1) {
            cout << "Queue is Empty!" << endl;
            return;
        }

        cout << "Deleted element: " << arr[front] << endl;

        if (front == rear) {
            front = rear = -1;
        } 
        else if (front == SIZE - 1) {
            front = 0;
        } 
        else {
            front++;
        }
    }

    void display() {
        if (front == -1) {
            cout << "Queue is Empty!" << endl;
            return;
        }

        cout << "Queue elements: ";
        if (rear >= front) {
            for (int i = front; i <= rear; i++)
                cout << arr[i] << " ";
        } 
        else {
            for (int i = front; i < SIZE; i++)
                cout << arr[i] << " ";
            for (int i = 0; i <= rear; i++)
                cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {

    CircularQueue q;
    int choice, value;

    while (true) {
        cout << "\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to insert: ";
                cin >> value;
                q.enqueue(value);
                break;

            case 2:
                q.dequeue();
                break;

            case 3:
                q.display();
                break;

            case 4:
                cout << "Exiting program..." << endl;
                return 0;

            default:
                cout << "Invalid choice! Try again." << endl;
        }
    }
}
