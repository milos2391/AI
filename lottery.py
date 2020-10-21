{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<div id=\"rightdown\">\n",
      "<!--***************BINGO BINGO**************-->\n",
      "<div class=\"contents_box01\">\n",
      "<div id=\"contents_logo_01\"> </div><div class=\"contents_mine_tx01\"><span class=\"font_black15\">109/10/21 第109059794期 </span> <span class=\"font_red14\"><a href=\"/Lotto/BingoBingo/history.aspx\">開獎結果</a> ｜ <a href=\"/Lotto/BingoBingo/drawing.aspx\">各期獎號查詢</a><a href=\"/lotto/BingoBingo/OEHLStatistic.htm\"><div id=\"contents_logo_01-2\"></div></a></span></div><div class=\"contents_mine_tx04\">開出獎號</div><div class=\"ball_box01\"><div class=\"ball_tx ball_yellow\">04 </div><div class=\"ball_tx ball_yellow\">09 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">21 </div><div class=\"ball_tx ball_yellow\">22 </div><div class=\"ball_tx ball_yellow\">23 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">33 </div><div class=\"ball_tx ball_yellow\">42 </div><div class=\"ball_tx ball_yellow\">50 </div><div class=\"ball_tx ball_yellow\">52 </div><div class=\"ball_tx ball_yellow\">53 </div><div class=\"ball_tx ball_yellow\">54 </div><div class=\"ball_tx ball_yellow\">56 </div><div class=\"ball_tx ball_yellow\">61 </div><div class=\"ball_tx ball_yellow\">62 </div><div class=\"ball_tx ball_yellow\">64 </div><div class=\"ball_tx ball_yellow\">67 </div><div class=\"ball_tx ball_yellow\">71 </div><div class=\"ball_tx ball_yellow\">75 </div></div><div class=\"contents_mine_tx08\">  超級<br/>  獎號<br/><div class=\"ball_red\">50</div></div><div class=\"contents_mine_tx08\">   猜<br/> 大 小<br/><div class=\"ball_blue_BB1\">－</div></div><div class=\"contents_mine_tx08\">   猜<br/> 單 雙<br/><div class=\"ball_blue_BB2\">和</div></div>\n",
      "</div>\n",
      "<div class=\"dotted01\"></div>\n",
      "<!--***************雙贏彩區塊***************-->\n",
      "<div class=\"contents_box06\">\n",
      "<div id=\"contents_logo_11\"></div><div class=\"contents_mine_tx09\"><span class=\"font_black15\">109/10/20 第109000252期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#12\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序</div><div class=\"ball_tx ball_blue\">04 </div><div class=\"ball_tx ball_blue\">24 </div><div class=\"ball_tx ball_blue\">08 </div><div class=\"ball_tx ball_blue\">20 </div><div class=\"ball_tx ball_blue\">10 </div><div class=\"ball_tx ball_blue\">21 </div><div class=\"ball_tx ball_blue\">16 </div><div class=\"ball_tx ball_blue\">17 </div><div class=\"ball_tx ball_blue\">12 </div><div class=\"ball_tx ball_blue\">03 </div><div class=\"ball_tx ball_blue\">22 </div><div class=\"ball_tx ball_blue\">19 </div><div class=\"ball_tx ball_blue\">03 </div><div class=\"ball_tx ball_blue\">04 </div><div class=\"ball_tx ball_blue\">08 </div><div class=\"ball_tx ball_blue\">10 </div><div class=\"ball_tx ball_blue\">12 </div><div class=\"ball_tx ball_blue\">16 </div><div class=\"ball_tx ball_blue\">17 </div><div class=\"ball_tx ball_blue\">19 </div><div class=\"ball_tx ball_blue\">20 </div><div class=\"ball_tx ball_blue\">21 </div><div class=\"ball_tx ball_blue\">22 </div><div class=\"ball_tx ball_blue\">24 </div>\n",
      "</div>\n",
      "<div class=\"dotted01\"></div>\n",
      "<!--***************威力彩區塊***************-->\n",
      "<div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_02\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/19 第109000084期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#01\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序<br/>第二區</div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">38 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">38 </div><div class=\"ball_red\">07 </div>\n",
      "</div>\n",
      "<div class=\"dotted02\"></div>\n",
      "<!--***************38樂合彩區塊***************-->\n",
      "<div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_03\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/19 第109000084期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#07\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序</div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">38 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">38 </div>\n",
      "</div>\n",
      "<div class=\"dotted01\"></div>\n",
      "<!--***************大樂透區塊***************-->\n",
      "<div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_04\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000092期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#02\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序<br/>特別號</div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">39 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">39 </div><div class=\"ball_red\">13 </div>\n",
      "</div>\n",
      "<div class=\"dotted02\"></div>\n",
      "<!--***************49樂合彩區塊***************-->\n",
      "<div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_05\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000092期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#08\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序</div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">39 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">39 </div>\n",
      "</div>\n",
      "<div class=\"dotted01\"></div>\n",
      "<!--***************大福彩區塊***************-->\n",
      "<!--div class=\"contents_box05\">\r\n",
      "      \r\n",
      "    </div-->\n",
      "<!--div class=\"dotted01\"></div-->\n",
      "<!--**************今彩539區塊**************-->\n",
      "<div class=\"contents_box03\">\n",
      "<div id=\"contents_logo_06\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000252期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#03\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序</div><div class=\"ball_tx ball_lemon\">36 </div><div class=\"ball_tx ball_lemon\">01 </div><div class=\"ball_tx ball_lemon\">27 </div><div class=\"ball_tx ball_lemon\">23 </div><div class=\"ball_tx ball_lemon\">10 </div><div class=\"ball_tx\"></div><div class=\"ball_tx ball_lemon\">01 </div><div class=\"ball_tx ball_lemon\">10 </div><div class=\"ball_tx ball_lemon\">23 </div><div class=\"ball_tx ball_lemon\">27 </div><div class=\"ball_tx ball_lemon\">36 </div>\n",
      "</div>\n",
      "<div class=\"dotted03\"></div>\n",
      "<!--**************39樂合彩區塊**************-->\n",
      "<div class=\"contents_box03\">\n",
      "<div id=\"contents_logo_07\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000252期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#09\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序</div><div class=\"ball_tx ball_lemon\">36 </div><div class=\"ball_tx ball_lemon\">01 </div><div class=\"ball_tx ball_lemon\">27 </div><div class=\"ball_tx ball_lemon\">23 </div><div class=\"ball_tx ball_lemon\">10 </div><div class=\"ball_tx\"></div><div class=\"ball_tx ball_lemon\">01 </div><div class=\"ball_tx ball_lemon\">10 </div><div class=\"ball_tx ball_lemon\">23 </div><div class=\"ball_tx ball_lemon\">27 </div><div class=\"ball_tx ball_lemon\">36 </div>\n",
      "</div>\n",
      "<div class=\"dotted01\"></div>\n",
      "<!--**************3星彩區塊**************-->\n",
      "<div class=\"contents_box04\">\n",
      "<div id=\"contents_logo_08\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000252期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#05\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">中獎號碼</div><div class=\"ball_tx ball_purple\">1</div><div class=\"ball_tx ball_purple\">8</div><div class=\"ball_tx ball_purple\">7</div>\n",
      "</div>\n",
      "<div class=\"dotted04\"></div>\n",
      "<!--**************4星彩區塊**************-->\n",
      "<div class=\"contents_box04\">\n",
      "<div id=\"contents_logo_09\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000252期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#06\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">中獎號碼</div><div class=\"ball_tx ball_purple\">2</div><div class=\"ball_tx ball_purple\">3</div><div class=\"ball_tx ball_purple\">9</div><div class=\"ball_tx ball_purple\">4</div>\n",
      "</div>\n",
      "</div>]\n"
     ]
    }
   ],
   "source": [
    "url = 'http://www.taiwanlottery.com.tw/'\n",
    "html = requests.get(url)\n",
    "sp = BeautifulSoup(html.text, 'html.parser')\n",
    "#print(sp.prettify())\n",
    "data1 = sp.select(\"#rightdown\")\n",
    "print(data1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_02\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/19 第109000084期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#01\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序<br/>第二區</div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">38 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">38 </div><div class=\"ball_red\">07 </div>\n",
      "</div>, <div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_03\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/19 第109000084期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#07\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序</div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">38 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">05 </div><div class=\"ball_tx ball_green\">07 </div><div class=\"ball_tx ball_green\">10 </div><div class=\"ball_tx ball_green\">19 </div><div class=\"ball_tx ball_green\">30 </div><div class=\"ball_tx ball_green\">38 </div>\n",
      "</div>, <div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_04\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000092期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#02\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序<br/>特別號</div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">39 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">39 </div><div class=\"ball_red\">13 </div>\n",
      "</div>, <div class=\"contents_box02\">\n",
      "<div id=\"contents_logo_05\"></div><div class=\"contents_mine_tx02\"><span class=\"font_black15\">109/10/20 第109000092期 </span><span class=\"font_red14\"><a href=\"Result_all.aspx#08\">開獎結果</a></span></div><div class=\"contents_mine_tx04\">開出順序<br/>大小順序</div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">39 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">05 </div><div class=\"ball_tx ball_yellow\">17 </div><div class=\"ball_tx ball_yellow\">18 </div><div class=\"ball_tx ball_yellow\">28 </div><div class=\"ball_tx ball_yellow\">30 </div><div class=\"ball_tx ball_yellow\">39 </div>\n",
      "</div>]\n"
     ]
    }
   ],
   "source": [
    "data2 = data1[0].find_all('div', {'class':'contents_box02'})\n",
    "print(data2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<div class=\"ball_tx ball_yellow\">05 </div>, <div class=\"ball_tx ball_yellow\">28 </div>, <div class=\"ball_tx ball_yellow\">39 </div>, <div class=\"ball_tx ball_yellow\">17 </div>, <div class=\"ball_tx ball_yellow\">18 </div>, <div class=\"ball_tx ball_yellow\">30 </div>, <div class=\"ball_tx ball_yellow\">05 </div>, <div class=\"ball_tx ball_yellow\">17 </div>, <div class=\"ball_tx ball_yellow\">18 </div>, <div class=\"ball_tx ball_yellow\">28 </div>, <div class=\"ball_tx ball_yellow\">30 </div>, <div class=\"ball_tx ball_yellow\">39 </div>]\n"
     ]
    }
   ],
   "source": [
    "data3 = data2[2].find_all('div', {'class':'ball_tx ball_yellow'})\n",
    "print(data3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "開出順序：05   28   39   17   18   30   "
     ]
    }
   ],
   "source": [
    "# 威力彩號碼\n",
    "print(\"開出順序：\",end=\"\")\n",
    "for n in range(0,6):\n",
    "    print(data3[n].text,end=\"  \") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "大小順序：05   17   18   28   30   39   "
     ]
    }
   ],
   "source": [
    "print(\"\\n大小順序：\",end=\"\")    \n",
    "for n in range(6,len(data3)):\n",
    "    print(data3[n].text,end=\"  \")\n",
    "     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "特別號：13 \n"
     ]
    }
   ],
   "source": [
    "## 第二區\n",
    "red = data2[2].find('div', {'class':'ball_red'})        \n",
    "print(\"特別號：{}\".format(red.text)) "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
