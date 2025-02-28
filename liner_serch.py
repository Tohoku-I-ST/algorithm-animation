import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio

# 探索するリストとターゲット
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

# GIF 用のフレームを保存するリスト
frames = []

def linear_search_animation(data, target):
    fig, ax = plt.subplots()
    ax.set_ylim(0, 12)
    ax.set_xlim(0, len(data))

    bars = ax.bar(range(len(data)), data, color='gray')
    text = ax.text(len(data) // 2, 10, "", fontsize=14, ha='center', color='blue')

    def update(i):
        # すべてのバーの色をリセット
        for bar in bars:
            bar.set_color('gray')
        
        # テキストをクリア
        text.set_text("")

        # 探索中の要素を赤くする
        if i < len(data):
            if data[i] == target:
                bars[i].set_color('green')  # 見つかった場合
                text.set_text("There were 5. Search completed.")  # メッセージを表示
            else:
                bars[i].set_color('red')  # 探索中
        
        return bars, text

    # アニメーションを作成（間隔を500msに設定）
    ani = animation.FuncAnimation(fig, update, frames=len(data) + 1, interval=500, repeat=True)

    # GIF 用にフレームを保存
    for i in range(len(data) + 1):
        update(i)
        plt.savefig(f"frame_{i}.png")
        frames.append(imageio.imread(f"frame_{i}.png"))

    return ani

# アニメーション作成
ani = linear_search_animation(data, target)

# GIFを保存（フレームの表示時間を3.0秒に設定）
imageio.mimsave("linear_search_slow.gif", frames, duration=3)
plt.show()
