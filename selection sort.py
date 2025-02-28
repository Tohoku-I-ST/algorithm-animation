import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio

# ソートするリスト
data = [10, 3, 7, 2, 5, 1, 9, 6, 8, 4]

# GIF 用のフレームを保存するリスト
frames = []

def selection_sort_animation(data):
    fig, ax = plt.subplots()
    ax.set_ylim(0, max(data) + 3)
    ax.set_xlim(0, len(data))

    bars = ax.bar(range(len(data)), data, color='gray')
    text = ax.text(len(data) // 2, max(data) + 2, "", fontsize=14, ha='center', color='blue')

    steps = []  # 各ステップのデータを記録

    # 選択ソートのアルゴリズム
    arr = data[:]
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps.append((arr[:], i, min_index, j))  # (現在のリスト, 確定位置, 最小値候補, 比較位置)
            if arr[j] < arr[min_index]:
                min_index = j
                steps.append((arr[:], i, min_index, j))  # 最小値候補を更新
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # スワップ
        steps.append((arr[:], i, min_index, None))  # スワップ後の状態

    steps.append((arr[:], None, None, None))  # 最後の状態

    def update(frame):
        arr, i, min_index, j = steps[min(frame, len(steps) - 1)]

        # すべてのバーの色をリセット
        for bar, val in zip(bars, arr):
            bar.set_height(val)
            bar.set_color('gray')

        # 現在の最小値候補を青色
        if min_index is not None:
            bars[min_index].set_color('blue')

        # 現在比較中の要素を赤色
        if j is not None:
            bars[j].set_color('red')

        # 繰り返し回数を表示
        if i is not None:
            text.set_text(f"繰り返し回数: {i + 1}")
        else:
            text.set_text("ソート完了！")
            for bar in bars:
                bar.set_color('green')  # 全体を緑に

        return bars, text

    # アニメーション作成
    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=500, repeat=False)

    # GIF 用にフレームを保存
    for i in range(len(steps)):
        update(i)
        plt.savefig(f"frame_{i}.png")
        img = imageio.imread(f"frame_{i}.png")
        frames.extend([img] * 2)  # 1フレームを2回複製（スロー再生）

    return ani

# アニメーション作成
ani = selection_sort_animation(data)

# GIFを保存（1フレーム = 1秒）
imageio.mimsave("selection_sort_with_iteration.gif", frames, duration=1.0)
plt.show()
