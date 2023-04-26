#include <iostream>
#include <fstream>
#include <time.h>

using namespace std;
clock_t start_clk = clock();

void insertionSort(int arr[], int n){

    for (int i = 1; i < n; i++){
        int key = arr[i];
        int j = i - 1; 
        while (j >= 0 && arr[j] > key){
            arr[j+1] = arr[j];
            j = j - 1;
        } 
    arr[j+1] = key;

    }
}



int main() {
    int arr[] = {88, 74, 41, 3,12,123,1,11,245, 8};
    int n = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < n; i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    insertionSort(arr, n);

    for (int i = 0; i < n; i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    printf("\nProcessor time used by insertionSort: %lg sec.\n", (clock() - start_clk) / (long double) CLOCKS_PER_SEC);


    return 0;
}


/*
int main(){
    ifstream inputFile("input.txt");
    if(!inputFile) {
        cerr << "Error: Unable to open input file!" << endl;
        return 1;
    }
    cout << "Status: Opened input file!" << endl;
    
    int n;
    inputFile >> n; // read the first value as the size of the array

    int* arr = new int[n]; // dynamically allocate memory for the array of size n
    for (int i = 0; i < n; i++){
        inputFile >> arr[i]; // read the remaining values as elements of the array
    }
    inputFile.close(); // close the input file

    for (int i = 0; i < n; i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    insertionSort(arr, n);

    for (int i = 0; i < n; i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    delete[] arr; // free the memory allocated for the array

    return 0;
}
*/

/*
Insertion Sort Algorithm:

1. Iterate through the array from arr[1] to arr[n], where n is the size of the array
2. For each element in the iteration, compare it with the elements to its left
3. If the element is smaller than the elements to its left, then swap it with the larger element
4. Repeat step 3 until the element is in its correct position
5. Continue with the next element in the iteration until the array is sorted

Pseudocode:

for i = 1 to n-1 do
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key do
        arr[j+1] = arr[j]
        j = j - 1
    end while
    arr[j+1] = key
end for

*/
