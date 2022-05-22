for num in range(1, 101):
    string = ''

    # ここから記述


    if num%15==0:
      # まずは15の倍数を条件分岐，最初に3や5の倍数を適用すると15の倍数もFizzやBuzzとして出力されてしまう．
      string='FizzBuzz'
    elif num%5==0:
      string='Buzz'
    elif num%3==0:
      string='Fizz'
    else:
      # 上記以外の場合は数値を返す
      string=str(num)

    # ここまで記述

    print(string)
