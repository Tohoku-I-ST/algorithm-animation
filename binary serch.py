import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio

# 二分探索するリスト（ソート済み）とターゲット
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# GIF 用のフレームを保存するリスト
frames = []

def binary_search_animation(data, target):
    fig, ax = plt.subplots()
    ax.set_ylim(0, 11)
    ax.set_xlim(0, len(data))
    
    bars = ax.bar(range(len(data)), data, color='gray')
    text = ax.text(len(data) // 2, 10, "", fontsize=14, ha='center', color='blue')

    left, right = 0, len(data) - 1
    steps = []  # 探索のステップを記録

    # 二分探索の手順を記録
    while left <= right:
        mid = (left + right) // 2
        steps.append((left, right, mid))  # 左端、右端、中央の値を記録
        if data[mid] == target:
            break
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    def update(frame):
        left, right, mid = steps[min(frame, len(steps) - 1)]

        # すべてのバーの色をリセット
        for bar in bars:
            bar.set_color('gray')
        
        # 範囲外を薄い色にする
        for i in range(len(data)):
            if i < left or i > right:
                bars[i].set_color('lightgray')
        
        # 現在の探索位置を赤色
        bars[mid].set_color('red')

        # テキストリセット
        text.set_text("")

        # 見つかった場合の処理
        if data[mid] == target:
            bars[mid].set_color('green')
            text.set_text(f"There was {target}.Search completed.")

        return bars, text

    # アニメーション作成
    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1000, repeat=False)

    # GIF 用にフレームを保存
    for i in range(len(steps)):
        update(i)
        plt.savefig(f"frame_{i}.png")
        img = imageio.imread(f"frame_{i}.png")
        frames.extend([img] * 5)  # 1フレームを5回複製してゆっくり再生

    return ani

# アニメーション作成
ani = binary_search_animation(data, target)

# GIFを保存（1フレーム = 2秒）
imageio.mimsave("binary_search_slow.gif", frames, duration=2.0)
plt.show()
