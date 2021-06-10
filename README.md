# codetypo
Word 等工具虽然支持拼写检查，但是对于代码拼写检查却无能为力。`codetypo` 支持对代码做拼写检查，同时保证缩写、简写不是拼写错误。

`codetypo` 工作流程如下：

![image](https://user-images.githubusercontent.com/248295/120491718-0cd64800-c3ec-11eb-8f2d-167e70d956d9.png)

codetypo 的字典是基于英语字典、linux 内核源码、linux 内核 Documentation、MySQL-6.0 源码生成。

(MySQL-6.0 里也有大量错别字>_<|)



## parser.py

用于生成词典。例如用 parser.py 爬 linux 中所有的单词，作为词典。


## checker.py

用于检查源码是否有错别字。


## 快速入门

用 checker.py 来检查 oceanbase 源码中的错别字：

```
python checker.py oceanbase-3.1/src/
```

会看到类似下面的输出：

```
/code/oceanbase/src/clog/ob_ilog_storage.cpp
 pruge (suggestion: purge)
 betweent (suggestion: betweend)

/code/oceanbase/src/clog/ob_log_archive_and_restore_driver.cpp
 archvie (suggestion: archie)

/code/oceanbase/src/clog/ob_log_membership_task_mgr.cpp
 leadera (suggestion: leaders)
 cascad (suggestion: cascade)
```



## 高级用法：定制字典

字典文件是 `spell.dict`。下面讲如何**定制字典文件**。

首先，下载几本英文小说，保存为 a.txt。一般来说，小说里都是字典里包含的正规词。

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


