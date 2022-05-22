import re


def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    print(array)
    
    search_start = 0
    search_end = len(array) - 1

    replace={
      'start':-1,
      'end':-1
    }

    # ある一つの閾値で交換がすべて終わるまで繰り返し処理を行う
    while search_start <= search_end:
      # 左から条件に当てはまるものが見つかるまで繰り返し処理を行う
      while array[search_start] < pivot:
        search_start += 1
      replace['start'] = array[search_start]
      
      # 右から条件に当てはまるものが見つかるまで繰り返し処理を行う
      while array[search_end] >= pivot:
        search_end -= 1
      replace['end'] = array[search_end]

      array[search_start] = replace['end']
      array[search_end] = replace['start']
      

    def check(array):
      for i in range(len(array)-1):
        if array[i] > array[i+1]:
          return 1
      return 0
    
    if check(array) == 1:
      sort(array)

    # ここまで記述

if __name__ == '__main__':
    main()
