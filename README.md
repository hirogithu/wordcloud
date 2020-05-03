# What you can do this code
論文の引用情報を可視化できる．

# Overview
論文の被引用URLを指定し，その論文を引用してる論文のアブストラクトをwebスクレイピング

スクレイピング結果をCloudiaで可視化

# Environments
o wsl on Windows 10 pro

x conda activate ~ python=3.6 anaconda

# Requirements
pip3 install cloudia, beautifulsoup4

# Run
Make text data.
```
python run.py -u "https://scholar.google.com/" --max 20
```
Plot & Save word cloud
```
python word_cloud.py
```



# 参照サイト
* [PythonとBeautiful Soupでスクレイピング](https://qiita.com/itkr/items/513318a9b5b92bd56185)
* [Beautiful Soup](http://kondou.com/BS4/#tag-obj)
* [Cloudia](https://github.com/vaaaaanquish/cloudia)
