import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio

# ソートするデータ
data = [10, 3, 7, 2, 5, 1, 9, 6, 8, 4]

# GIF保存用のフレーム
frames = []

def insertion_sort_animation(data):
    fig, ax = plt.subplots()
    ax.set_ylim(0, max(data) + 3)
    ax.set_xlim(-1, len(data))

    bars = ax.bar(range(len(data)), data, color='gray')
    text = ax.text(len(data) // 2, max(data) + 2, "", fontsize=14, ha='center', color='blue')

    steps = []

    arr = data[:]
    n = len(arr)

    # 挿入ソートのアルゴリズム
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        steps.append((arr[:], i, j, "compare"))  # 比較開始
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 右にシフト
            steps.append((arr[:], i, j, "compare"))  # 比較中
            j -= 1

        arr[j + 1] = key  # 挿入
        steps.append((arr[:], i, j + 1, "insert"))  # 挿入後

    steps.append((arr[:], None, None, "done"))  # ソート完了

    def update(frame):
        arr, i, j, status = steps[min(frame, len(steps) - 1)]

        # バーの高さを更新
        for bar, val in zip(bars, arr):
            bar.set_height(val)
            bar.set_color('gray')  # デフォルト色（灰色）

        # 比較中（赤）: j が valid であれば、そのバーを赤くする
        if status == "compare" and j is not None and j >= 0:
            bars[j].set_color('red')  # 比較中の要素を赤

        # 挿入中（オレンジ）: i が valid であれば、そのバーをオレンジに
        if status == "insert" and i is not None:
            bars[i].set_color('orange')  # 挿入中の要素をオレンジ

        # 挿入完了した要素は黒にする
        for k in range(i + 1, len(arr)):  # i + 1 以降の要素を確定
            bars[k].set_color('black')  # 確定済みの要素を黒

        # 繰り返し回数を表示
        if i is not None:
            text.set_text(f"Number of repetitions: {i}")
        else:
            text.set_text("completed")
            for bar in bars:
                bar.set_color('green')  # ソート完了で緑に

        return bars, text

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, repeat=False)

    return ani, fig

# 関数の外で `ani` を保持
ani, fig = insertion_sort_animation(data)

# GIF用フレーム保存
for i in range(len(data) + 2):  # +2 は完了表示のため
    plt.savefig(f"frame_{i}.png")
    img = imageio.imread(f"frame_{i}.png")
    frames.append(img)

# GIF保存
imageio.mimsave("insertion_sort_slow.gif", frames, duration=1.0)

# **変更点**: plt.show() を確実に呼び出す
plt.show()
