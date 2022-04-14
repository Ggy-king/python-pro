#wordcloud库应用实例
import wordcloud
txt = "life is short,you need python"
w = wordcloud.WordCloud(background_color = "pink")
w.generate(txt)
w.to_file("pywcloud.png")
