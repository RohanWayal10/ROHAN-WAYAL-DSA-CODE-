
#include <iostream>
#include <vector>
#include <string>
#include <ctime>
using namespace std;

struct Student
{
    int id;
    string name;
    float cgpa;
};

vector<Student> students;

// Function Prototypes
void addStudent();
void displayStudents();
int linearSearch(int id);
int binarySearch(int id);
void bubbleSortCGPA(int order);
void selectionSortName();
void analyzePerformance(int searchID);

int main()
{
    cout << "Program by: Rohan Wayal\n"; // First line output

    int choice, id, result;

    while (true)
    {
        cout << "\n---- Student Database Menu ----\n";
        cout << "1. Add Student\n";
        cout << "2. Display Students\n";
        cout << "3. Linear Search by ID\n";
        cout << "4. Binary Search by ID\n";
        cout << "5. Sort by Name (Selection Sort)\n";
        cout << "6. Sort by CGPA (Bubble Sort)\n";
        cout << "7. Analyze Search Performance\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            addStudent();
            break;
        case 2:
            displayStudents();
            break;
        case 3:
            cout << "Enter ID to search: ";
            cin >> id;
            result = linearSearch(id);
            if (result != -1)
                cout << "Found: " << students[result].id << " "
                     << students[result].name << " "
                     << students[result].cgpa << endl;
            else
                cout << "Student not found.\n";
            break;
        case 4:
            cout << "Enter ID to search: ";
            cin >> id;
            result = binarySearch(id);
            if (result != -1)
                cout << "Found: " << students[result].id << " "
                     << students[result].name << " "
                     << students[result].cgpa << endl;
            else
                cout << "Student not found.\n";
            break;
        case 5:
            selectionSortName();
            cout << "Sorted by Name.\n";
            break;
        case 6:
            cout << "Enter order (1=Ascending, 2=Descending): ";
            int order;
            cin >> order;
            bubbleSortCGPA(order);
            cout << "Sorted by CGPA.\n";
            break;
        case 7:
            cout << "Enter ID to analyze search performance: ";
            cin >> id;
            analyzePerformance(id);
            break;
        case 8:
            return 0;
        default:
            cout << "Invalid choice.\n";
        }
    }
}

// Add Student
void addStudent()
{
    Student s;
    cout << "Enter ID: ";
    cin >> s.id;
    cout << "Enter Name: ";
    cin >> s.name;
    cout << "Enter CGPA: ";
    cin >> s.cgpa;
    students.push_back(s);
}

// Display Students
void displayStudents()
{
    cout << "\nStudent Records:\n";
    for (auto &s : students)
    {
        cout << s.id << "\t" << s.name << "\t" << s.cgpa << endl;
    }
}

// Linear Search
int linearSearch(int id)
{
    for (int i = 0; i < students.size(); i++)
    {
        if (students[i].id == id)
            return i;
    }
    return -1;
}

// Binary Search (requires ID sorted)
int binarySearch(int id)
{
    int low = 0, high = students.size() - 1, mid;
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (students[mid].id == id)
            return mid;
        else if (students[mid].id < id)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

// Bubble Sort by CGPA
void bubbleSortCGPA(int order)
{
    for (int i = 0; i < students.size() - 1; i++)
    {
        for (int j = 0; j < students.size() - i - 1; j++)
        {
            bool condition = (order == 1) ? (students[j].cgpa > students[j + 1].cgpa) : (students[j].cgpa < students[j + 1].cgpa);
            if (condition)
            {
                swap(students[j], students[j + 1]);
            }
        }
    }
}

// Selection Sort by Name
void selectionSortName()
{
    for (int i = 0; i < students.size() - 1; i++)
    {
        int minIndex = i;
        for (int j = i + 1; j < students.size(); j++)
        {
            if (students[j].name < students[minIndex].name)
                minIndex = j;
        }
        if (minIndex != i)
        {
            swap(students[i], students[minIndex]);
        }
    }
}

// Performance Analysis
void analyzePerformance(int searchID)
{
    clock_t start, end;
    double time_linear, time_binary;

    // Linear search
    start = clock();
    linearSearch(searchID);
    end = clock();
    time_linear = ((double)(end - start)) / CLOCKS_PER_SEC;

    // Sort by ID for binary search
    for (int i = 0; i < students.size() - 1; i++)
    {
        for (int j = 0; j < students.size() - i - 1; j++)
        {
            if (students[j].id > students[j + 1].id)
            {
                swap(students[j], students[j + 1]);
            }
        }
    }

    // Binary search
    start = clock();
    binarySearch(searchID);
    end = clock();
    time_binary = ((double)(end - start)) / CLOCKS_PER_SEC;

    cout << "\nSearch Performance:\n";
    cout << "Linear Search Time: " << time_linear << " seconds\n";
    cout << "Binary Search Time: " << time_binary << " seconds (after sorting)\n";
}
