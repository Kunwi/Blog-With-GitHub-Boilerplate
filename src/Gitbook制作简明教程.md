---
layout: post
title: Gitbook制作及Github Pages发布简明教程
slug: gitbook
date: 2022-05-06 15:07
status: publish
author: Kunwi
categories: 
  - 教程
tags:
  - gitbook
---

本教程主要基于以下教程：[GitBook简介安装配置](https://gitbook.curiouser.top/origin/gitbook-%E7%AE%80%E4%BB%8B%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE.html)，

#环境搭建（Node.js, gitbook cli, Writage, Vscode, Git Bash, gh-pages）

**1、  本教程使用环境：**64位win10 系统；

**2、  安装gitbook的使用环境Node.js：**gitbook 是一个基于Node.js的命令行工具，安装Node.js为首要任务。本教程使用的是v10.23.0版本。也可装最新版本，但在gitbook cli安装以及后续使用过程中可能会出现问题，需要额外的步骤解决，并不推荐。

**3、  安装电子书制作软件gitbook cli：**在cmd或Git Bash等命令行程序中输入以下命令：`npm install gitbook-cli -g`
新版Node.js如遇到gitbook-cli/node_modules/npm/node_modules/graceful-fs/polyfills.js:287 cb.apply is not a function 问题，需要找到对应文件polyfills.js，将以下几行注释掉即可，效果如下：

```
// fs.stat = statFix(fs.stat)
// fs.fstat = statFix(fs.fstat)
// fs.lstat = statFix(fs.lstat)
```

[来源](https://www.jianshu.com/p/8aba9fea0fe3)

**4、 安装Writage & 编写宏文件转换Word文件为markdown格式（可选）：**由于使用本教程采用的原书使用word编写，故使用word转markdown软件Writage（收费，可试用14天），安装后直接集成在word加载项内，将word文件另存为md文件即可完成转换。由于Writage不支持批注形式的注释，故使用VBA编写宏文件将批注批量转为脚注，代码如下：

```
Sub 批转脚()
Dim xComm As Comment
Dim xCommRange As Range
Dim xDoc As Document
Application.ScreenUpdating = False
Set xDoc = ActiveDocument
For Each xComm In xDoc.Comments
        Set xCommRange = xComm.Range
xDoc.Footnotes.Add xComm.Scope, , xCommRange.Text
        xComm.Delete
Next
Application.ScreenUpdating = True
End Sub
```

[来源](https://www.zhihu.com/question/320555426/answer/2292364679)

另外word转md软件还有命令行软件Pandoc，其转换的文件格式比Writage多样，但是实际体验下来word转markdown的实际转换效果不如Writage。[来源](https://zhuanlan.zhihu.com/p/30891168)

**5、  安装可视化markdown编辑器Vscode：**安装后在软件内置的应用商店安装插件：markdown all in one、markdown preview enhanced、markdown preview github styling。另外在设置中搜索“security.workspace.trust”将受限模式禁用（如不禁用则需额外选择信任窗口以启用插件），[来源](https://blog.csdn.net/weixin_45755666/article/details/117877321)。另外还有typora（收费）可供使用，[来源](https://zhuanlan.zhihu.com/p/103348449)。

**6、  安装Git Bash将本地代码推送至Github：**[安装地址](https://git-scm.com/downloads)

**7、  安装gh-pages插件推送静态HTML文件**：安装命令如下：
`npm install gh-pages@3.0.0 --save`
gh-pages版本应选择3.0.0版本，新版本在使用时会报The “path” argument must be of type string.错误，暂未查到解决办法。

#开始建书：

**1、  将word转换为markdown格式：**运行宏将批注转为脚注，再用Writage将word转为markdown格式。转换后的表格格式需再调整

**2、  编写SUMMARY.md文件：**建议放于user/用户名/书名 路径下，名称使用英文。其格式如下：

```
# Summary

* [前言](README.md)
* [第一章 **](chapter1.md)
    * [第一節    **](chapter1/section01.md)
    * [第二節    **](chapter1/section02.md)
    * [第三節    **](chapter1/section03.md)
```

其中[]内为章节名，()内为章节文件相对路径。

**3、  生成初始文件：**在对应书籍目录下输入以下命令：`gitbook init`
可在命令后加上路径初始化到指定目录。完成后可见每章节自动生成的空白md文件

**4、  编写书本：**将第1步转换后的md文件内容按章节逐一复制到第3步的md文件中。在Vscode编辑器中右键打开侧边栏，可实时预览md代码的显示效果，并依此进行相应调整。

**5、  编写book.json文件（可选）：**gitbook 在编译书籍的时候会读取书籍源码顶层目录中的book.json文件。如对格式不熟悉可于[校对网站](https://jsonlint.com/)校验，也可参考[模板](https://janicezhw.github.io/gitbook/startusegitbook/configInfo/bookjson.html)如下：

```
{
       // Folders to use for output
    // Caution: it overrides the value from the command line
    // It's not advised this option in the book.json
    "output": null,

    // Generator to use for building
    // Caution: it overrides the value from the command line
    // It's not advised this option in the book.json
    "generator": "site",

    // Book metadats (somes are extracted from the README by default)
    "title": null,
    "description": null,
    "isbn": null,

    // For ebook format, the extension to use for generation (default is detected from output extension)
    // "epub", "pdf", "mobi"
    // Caution: it overrides the value from the command line
    // It's not advised this option in the book.json
    "extension": null,

    // Plugins list, can contain "-name" for removing default plugins
    "plugins": [],

    // Global configuration for plugins
    "pluginsConfig": {
        "fontSettings": {
            "theme": "sepia", "night" or "white",
            "family": "serif" or "sans",
            "size": 1 to 4
        }
    },

    // Variables for templating
    "variables": {},

    // Links in template (null: default, false: remove, string: new value)
    "links": {
        // Custom links at top of sidebar
        "sidebar": {
            "Custom link name": "https://customlink.com"
        },

        // Sharing links
        "sharing": {
            "google": null,
            "facebook": null,
            "twitter": null,
            "weibo": null,
            "all": null
        }
    },


    // Options for PDF generation
    "pdf": {
        // Add page numbers to the bottom of every page
        "pageNumbers": false,

        // Font size for the fiel content
        "fontSize": 12,

        // Paper size for the pdf
        // Choices are [u’a0’, u’a1’, u’a2’, u’a3’, u’a4’, u’a5’, u’a6’, u’b0’, u’b1’, u’b2’, u’b3’, u’b4’, u’b5’, u’b6’, u’legal’, u’letter’]
        "paperSize": "a4",

        // Margin (in pts)
        // Note: 72 pts equals 1 inch
        "margin": {
            "right": 62,
            "left": 62,
            "top": 36,
            "bottom": 36
        },

        //Header HTML template. Available variables: _PAGENUM_, _TITLE_, _AUTHOR_ and _SECTION_.
        "headerTemplate": null,

        //Footer HTML template. Available variables: _PAGENUM_, _TITLE_, _AUTHOR_ and _SECTION_.
        "footerTemplate": null
    }
}
```
其中"plugins":[]命令为插件设置，使用一例：
```
{
	"title": "六十年來之嶺東紀略",
	"author": "蕭冠英",
	"links": {
		"sidebar": {
			"六十年來之嶺東紀略": "http://read.nlc.cn/allSearch/searchDetail?searchType=1001&showType=1&indexName=data_416&fid=15jh003147"
		}
	},
	"plugins": [
		"back-to-top-button",
		"chapter-fold",
		"-lunr", "-search", "search-pro",
		"splitter",
		"auto-scroll-table",
		"lightbox"
	]
}
```

可能有用的插件：back-to-top-button为回到顶部，chapter-fold为目录折叠，search-pro为高级搜索（需禁用默认的search和lunr插件）、splitter为侧边栏宽度调节、auto-scroll-table为表格滚动条（常需将页面刷新才能看到滚动条，解决方法见文末存在问题一节。）、lightbox为单击查看图片（实际体验不佳，图片显示在悬浮窗口中但没有放大。）。详见[来源](https://xxh422735676.github.io/gitbook-comments/gitbook%E6%8F%92%E4%BB%B6.html)。table-cell-merge可实现合并单元格：在单元格中填入>表示与右方相邻单元格合并，^表示与上方相邻单元格合并，空单元格则默认与左方单元格合并。可参见[项目说明](https://www.npmjs.com/package/gitbook-plugin-table-cell-merge)。url-embed可嵌入动态内容，如地图，详见[来源](https://github.com/basilvetas/gitbook-plugin-url-embed)。

**6、  构建gitbook书籍静态HTML资源：**首先在对应书籍目录下输入以下命令：`gitbook install`安装插件样式资源，其次输入以下命令：`gitbook build`,可见书籍的文件夹中生成一个 \_book 的文件夹, 里面有生成的静态HTML资源。

**7、  代码托管到Github：**

a  在Github中新建仓库，以书籍路径名称命名。（为统一，可在新建仓库前先将个人设置中分支的默认名字命名为master，如无修改则为main，后面代码也需相应修改）

b  构建.gitignore文件，忽略无需上传的文件。gitbook统一示例如下，可根据需求更改。
```
# Node rules:
## Grunt intermediate storage (http://gruntjs.com/creating-plugins#storing-task-files)
.grunt

## Dependency directory
## Commenting this out is preferred by some people, see
## https://docs.npmjs.com/misc/faq#should-i-check-my-node_modules-folder-into-git
node_modules

# Book build output
_book

# eBook build output
*.epub
*.mobi
*.pdf
```
详见[来源](https://github.com/github/gitignore/blob/main/GitBook.gitignore)

对于.gitignore的详细用法介绍可参见[来源](https://blog.csdn.net/wnvalentin/article/details/105448739)

c  在Git Bash输入以下代码：
```
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub邮箱"
git config --global credential.helper store
```

其次复制仓库的https地址，在Git Bash输入以下代码将本地文件推送至仓库的master分支：

```
git init
git remote add origin https.github.com/**/**.git
git add .
git commit -m "init commit"
git push origin master
```

如失败，应确认登录状态，尝试能否克隆仓库，也可尝试[创建ssh key](https://blog.csdn.net/helllochun/article/details/48802473)（Permission denied (publickey)），以及换个网络环境。

d  后期修改代码内容可用以下命令推送修改：
```
# cd 到仓库文件夹后

git add .
git commit -m "添加修改"
git push
```

**8、  代码发布至gh-pages：**在Git Bash输入以下代码将静态页面HTML文件推送至gh-pages分支：`gh-pages -d _book`，在Github中设置GitHub Page Source时指定gh-pages分支即可。

**9、  后续维护：**gitbook代码有更新时，执行前述7-d和8的步骤即可更新代码和静态网页。

##存在问题

- 表格列数过多时无法显示。可用auto-scroll-table表格滚动条插件解决，但该插件在第一次进入页面时经常无法加载，需要刷新页面后才能加载出来。 使用ideamean修改的版本即可解决，使用方法：修改book.json的plugins，将原数组项"auto-scroll-table"更改为"auto-scroll-table@git+https://github.com/ideamean/gitbook-plugin-auto-scroll-table.git" ，参见[来源](https://github.com/ideamean/gitbook-plugin-auto-scroll-table/blob/master/README.MD)

- 在使用table-cell-merge过程中发现处于表格右下角的单元格与左方单元格无法合并。经检验发现在该单元格分隔符"|"（也是表格的最后一个分隔符）后多加一个分隔符"|"即可解决问题

例：原编码：

```
| a | b |
|---|---|
| 1 | 2 |
| 4 |   |
```
改为如下形式：

```
| a | b |
|---|---|
| 1 | 2 |
| 4 |   ||
```

- book.json文件修改"plugins":[]参数时需注意，若修改前后插件数量不变，需保证排在第一行的插件有变化。否则执行gitbook install时系统会无法识别插件变化，无法安装。因此如有新增插件建议将其写在第一行。

- 表格第一列文字无法自动换行，可用`<br />`手动换行。

- 除第一列以外的表格列宽可通过控制首行列宽来决定，可在标题行内容前后加空格符，中文汉字的一格需要四个空格符：`&nbsp;&nbsp;&nbsp;&nbsp;`。也可通过`<div style="width:[长度]">[单元格文本]</div>` 的形式确定，长度单位可以是pt, px, cm等。参见[来源](https://zhuanlan.zhihu.com/p/93239297)
