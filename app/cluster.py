import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# # フォントの保存場所
# import matplotlib
# print(matplotlib.matplotlib_fname())

# # フォントキャッシュの場所を探す
# import matplotlib as mpl
# print(mpl.get_configdir())

# # フォントを指定
plt.rcParams['font.family'] = 'IPAexGothic'

# 星の順番が違うことあがる
# https://blog.ieagent.jp/eria/kawagoehitorikurashi-36337
# 昔の記事は評価項目が異なる
# https://blog.ieagent.jp/eria/kojiyahitorigurashi-44684
# https://blog.ieagent.jp/eria/shinokachimachi-sumiyasusa-112906
# ２つのデータが一つになっている？
# 星の数が同じだと減るのか

target_towns = ['荻窪', '練馬', '武蔵小山', '赤羽', '大山', '三鷹', '大岡山', '千歳烏山', '成増', '三軒茶屋', '阿佐ヶ谷', 'ひばりヶ丘', '経堂', '旗の台', '大森', '永福町', '下高井戸', '戸越銀座', '仙川', '調布', '王子', '十条', '住吉', '曳舟', '中井', '方南町', '千歳船橋', '大泉学園', '葛西']
stars_data = [[4, 4, 3, 5, 3, 2], [4, 5, 4, 3, 3, 3], [4, 5, 4, 4, 5, 2], [4, 2, 5, 5, 4, 2], [4, 3, 3, 4, 4, 3], [3, 4, 3, 2, 2, 3], [3, 4, 3, 3, 3, 3], [4, 4, 3, 4, 3, 3], [4, 4, 3, 4, 3, 3], [4, 3, 4, 4, 5, 1], [4, 4, 3, 4, 4, 4], [3, 5, 4, 3, 2, 2], [4, 5, 3, 4, 2, 3], [2, 5, 3, 2, 1, 3], [4, 4, 3, 5, 4, 2], [3, 5, 3, 2, 2, 4], [3, 5, 4, 3, 2, 2], [4, 4, 3, 4, 4, 2], [4, 4, 3, 4, 4, 3], [4, 3, 4, 5, 4, 3], [4, 2, 3, 5, 5, 3], [4, 5, 4, 4, 5, 3], [4, 4, 3, 4, 4, 3], [4, 5, 3, 4, 3, 3], [3, 4, 4, 3, 3, 4], [3, 5, 3, 4, 2, 3], [4, 5, 3, 4, 2, 3], [4, 4, 3, 4, 3, 4], [4, 4, 3, 4, 3, 4]]

# ユークリッド距離とウォード法を使用してクラスタリング
z = linkage(stars_data, metric='euclidean', method='ward')

# 結果を可視化
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, title="樹形図")

dendrogram(z, labels=target_towns)

from matplotlib.font_manager import FontProperties
fp = FontProperties(fname='/Users/shotaro.kawano/Git/livable-town/venv/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/ipaexg.ttf')
for l in plt.gca().get_xticklabels(): l.set_fontproperties(fp)
# plt.title('日本語です')
plt.show()
