def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 12345
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # まずは初期位置のindexを求める．indexは整数であるため中間の位置は以下のように表される
    i = len(sorted_array)//2

    # 次に探索時のリストの最小indexと最大indexを設定する．
    i_min = 0
    i_max = len(sorted_array) - 1

    # indexの制限の辞書
    i_limit = {
      'min' : i_min,
      'max' : i_max
    }

    # indexでの値がtargetでない場合処理を続ける．
    while sorted_array[i] != target_number:
      # 探索要素が一つの場合はループを抜けて確認する
      if i_max-i_min == 1:
        break
      
      # 探索要素が2つで値がない場合ループが抜けなくなるので．
      if i_max-i_min == 2:
        break

      if sorted_array[i] < target_number:
        i_min = i + 1
        i = i + len(sorted_array[i_min:i_max])//2 + 1
        # indexが最大値より大きく行こうとする場合はないに等しい
        if i > i_limit['max']:
          return -1
      else:
        i_max = i - 1
        i = i - len(sorted_array[i_min:i_max])//2 - 1
        # indexが最小値より小さく行こうとする場合はないに等しい
        if i < i_limit['min']:
          return -1
      
    
    if sorted_array[i] == target_number:
      return i
    if sorted_array[i_min] == target_number:
      return i_min
    if sorted_array[i_max] == target_number:
      return i_max

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
