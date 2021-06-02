# codetypo
Auto check typo in codes

![image](https://user-images.githubusercontent.com/248295/120491718-0cd64800-c3ec-11eb-8f2d-167e70d956d9.png)

codetypo 的字典是基于英语字典、linux 内核源码、linux 内核 Documentation、MySQL-6.0 源码生成。

(MySQL-6.0 里也有大量错别字>_<|)



## parser.py

用于生成词典。例如用 parser.py 爬 linux 中所有的单词，作为词典。


## checker.py

用于检查源码是否有错别字。


## 举例

首先，下载基本英文小说，保存为 a.txt。这里都是字典里包含的正规词。



然后，下载 linux 源码，用它来生成一些计算机专有的特殊词：
```
python parser.py linux-kernel-6.0/ > b.txt
```


将 a.txt b.txt 合并成 spell.dict：
```
cat a.txt b.txt > spell.dict
```

最后，用 checker.py 来检查 oceanbase 源码中的错别字：

```
python checker.py oceanbase-3.1/src/
```

