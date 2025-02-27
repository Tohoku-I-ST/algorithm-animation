import matplotlib.pyplot as plt
import numpy as np
import time

# 逐次探索の関数
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# アニメーション用の関数
def animate_search(arr, target):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, color='lightblue')
    text = ax.text(0.5, max(arr) * 1.1, "", ha='center', transform=ax.transAxes)

    for frame in range(len(arr)):
        # すべてリセット
        for rect in bar_rects:
            rect.set_color('lightblue')  

        # 現在の探索対象を赤く
        bar_rects[frame].set_color('red')
        text.set_text(f"Searching for {target}...")

        if arr[frame] == target:
            text.set_text(f"Found {target} at index {frame}")
            plt.draw()
            plt.pause(1)  # 見つかったら少し停止
            return
        
        plt.draw()
        plt.pause(0.5)  # 0.5秒待って次のステップへ

    text.set_text(f"{target} not found")
    plt.draw()
    plt.pause(0.5)

    plt.show()

# データの準備
np.random.seed(0)
arr = np.random.randint(1, 20, 10)
target = np.random.choice(arr)

# 逐次探索の実行
index = linear_search(arr, target)
print(f"Index of target ({target}): {index}")

# アニメーションの実行
animate_search(arr, target)
