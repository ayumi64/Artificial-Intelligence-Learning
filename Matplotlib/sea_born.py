import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
plt.show()


"""
    Seaborn 是在 Matplotlib 的基础上进行了更高级的API封装的Python数据可视化库，从而使得作图更加容易，
    应该把 Seaborn 视为 Matplotlib 的补充，而不是替代物。
"""