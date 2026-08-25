class DynamicArray {
private:

    int len;
    int capacity;
    int* arr;

public:

    DynamicArray(int capacity) : capacity(capacity), len(0) {
        arr = new int[capacity];
        for (int i = 0; i < capacity; i++) {
            arr[i] = 0;
        }
    }

    int get(int i) {
        if (i < len) {
            return arr[i];
        }
    }

    void set(int i, int n) {
        if (i < len) {
            arr[i] = n;
        }
    }

    void pushback(int n) {
        if (len == capacity) {
            resize();
        }
        arr[len] = n;
        len++;
    }

    int popback() {
        if (len > 0) {
            len--;
        }
        return arr[len];
    }

    void resize() {
        capacity = capacity*2;
        int* newArr = new int[capacity];
        for (int i = 0; i < len; i++) {
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return len;
    }

    int getCapacity() {
        return capacity;
    }
};
