# 문제

[912. Sort an Array](https://leetcode.com/problems/sort-an-array/description/)

# 정렬 알고리즘

다음은 대표적인 정렬 알고리즘들의 시간 복잡도입니다. 여기서 n은 입력 데이터의 크기입니다.

- 버블 정렬(Bubble Sort): O(n^2)
- 선택 정렬(Selection Sort): O(n^2)
- 삽입 정렬(Insertion Sort): O(n^2)
- 퀵 정렬(Quick Sort):
- 평균 시간 복잡도: O(n log n)
- 최악 시간 복잡도: O(n^2)
- 병합 정렬(Merge Sort): O(n log n)
- 힙 정렬(Heap Sort): O(n log n)

일반적으로 n이 큰 경우 퀵 정렬, 병합 정렬, 힙 정렬과 같은 O(n log n)의 시간 복잡도를 갖는 알고리즘이 빠른 속도로 정렬을 수행합니다. 그러나 입력 데이터가 이미 정렬되어 있는 경우나 거의 정렬된 경우, 버블 정렬, 선택 정렬, 삽입 정렬과 같은 O(n^2)의 시간 복잡도를 갖는 알고리즘들이 더 효율적일 수 있습니다. 따라서 알고리즘을 선택할 때는 입력 데이터의 특성에 따라 적절한 알고리즘을 선택해야 합니다.

가장 기본적인 정렬 알고리즘은 버블 정렬(Bubble Sort)입니다. 버블 정렬은 서로 인접한 두 원소를 비교하여 정해진 기준에 따라 위치를 교환하는 방식으로 정렬을 수행합니다. 이 때, 인접한 두 원소의 대소 관계를 비교하는 횟수는 배열의 길이에 비례하므로 시간 복잡도는 O(n^2)입니다.

선택 정렬은 가장 작은 원소를 찾아서 배열의 가장 앞으로 이동시키는 방식으로 정렬을 수행합니다. 삽입 정렬은 이미 정렬된 부분 배열에 새로운 원소를 삽입하면서 정렬을 수행합니다. 퀵 정렬은 pivot을 기준으로 작은 값은 pivot의 왼쪽, 큰 값은 pivot의 오른쪽으로 분할하고 분할된 부분 배열에 대해 재귀적으로 정렬을 수행합니다. 병합 정렬은 분할 정복 방식을 이용하여 배열을 계속해서 반으로 나누고, 나눈 부분 배열을 합치면서 정렬을 수행합니다. 힙 정렬은 최대 힙 구조를 이용하여 원소를 하나씩 꺼내면서 정렬을 수행합니다.

# 코드

```javascript
const bubbleSort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
};

const selectionSort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    let minIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }
    [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
  }
  return arr;
};

const insertionSort = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    let j = i - 1;
    const temp = arr[i];
    while (j >= 0 && arr[j] > temp) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = temp;
  }
  return arr;
};

const quickSort = (arr) => {
  const sort = (arr, left = 0, right = arr.length - 1) => {
    if (left >= right) {
      return;
    }
    let i = left;
    let j = right;
    const pivot = arr[left];
    while (i < j) {
      while (i < j && arr[j] >= pivot) {
        j--;
      }
      arr[i] = arr[j];
      while (i < j && arr[i] <= pivot) {
        i++;
      }
      arr[j] = arr[i];
    }
    arr[i] = pivot;
    sort(arr, left, i - 1);
    sort(arr, i + 1, right);
  };

  sort(arr);
  return arr;
};

const heapSort = (arr) => {
  const heapify = (arr, i, len) => {
    let left = 2 * i + 1;
    let right = 2 * i + 2;
    let largest = i;
    if (left < len && arr[left] > arr[largest]) {
      largest = left;
    }
    if (right < len && arr[right] > arr[largest]) {
      largest = right;
    }
    if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]];
      heapify(arr, largest, len);
    }
  };

  for (let i = Math.floor(arr.length / 2); i >= 0; i--) {
    heapify(arr, i, arr.length);
  }

  for (let i = arr.length - 1; i > 0; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]];
    heapify(arr, 0, i);
  }

  return arr;
};

const mergeSort = (arr) => {
  const merge = (left, right) => {
    const res = [];
    while (left.length && right.length) {
      if (left[0] < right[0]) {
        res.push(left.shift());
      } else {
        res.push(right.shift());
      }
    }
    while (left.length) {
      res.push(left.shift());
    }
    while (right.length) {
      res.push(right.shift());
    }
    return res;
  };

  const sort = (arr) => {
    const { length } = arr;
    if (length < 2) {
      return arr;
    }
    const mid = Math.floor(length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid, length);
    return merge(sort(left), sort(right));
  };

  return sort(arr);
};
```

# 결과

Accepted
Runtime : 62.36%
Memory: 83.10%
