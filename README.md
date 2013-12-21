#Bayesian Filtering
    -- using web crawlers for learning with big data

## 概述
本项目使用朴素贝叶斯分类器对用户输入的电影剧情进行分类，以爬虫从豆瓣以及百度百科获取大量数据对分类器进行训练。
 
##Tech Spec
###步骤概述
Step 1. 使用爬虫在豆瓣电影中爬取电影的Title
Step 2. 访问百科相应网页，应用HTML DOM抽取其中段落
Step 3. 使用贝叶斯分类器进行学习和训练

###步骤细节
* 使用网络爬虫对豆瓣电影中爱情类，科幻类，以及悬疑类电影的Title进行爬取（Ex. Link: http://movie.douban.com/tag/爱情）
    三种类型的电影各爬取1000个条目，结果分别存储在一个TXT文件中
    Result: 获得3个movieTitleList.txt
* 对于每个电影的Title，作为URL成分访问百科的网页，通过 HTML DOM 获取相应电影百科页面的所有文字内容
    Result: 获得每部电影百科页面所有文字内容，我们称此为一个article
* 对于每类，把1000部电影的article append到一起，存入一个TXT
    Result: 获得3个分类的result.txt (romanticResult.txt, scienceResult.txt和suspenseResult.txt)
* 对result.txt进行中文分词处理，分词结果存储在resultToken
    Result: 获得3个分类的resultToken.txt (romanticResultToken.txt, scienceResultToken.txt和suspenseResultToken.txt)
* 使用三个resultToken.txt对贝叶斯分类器进行训练
    Result：生成3个分类的catTable
