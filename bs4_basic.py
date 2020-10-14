{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: beautifulsoup4 in c:\\programdata\\anaconda3\\lib\\site-packages (4.9.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from beautifulsoup4) (2.0.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install beautifulsoup4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<html>\n",
      " <head>\n",
      "  <title>\n",
      "   Hello World\n",
      "  </title>\n",
      " </head>\n",
      " <body>\n",
      "  <h2>\n",
      "   Test Header\n",
      "  </h2>\n",
      "  <p>\n",
      "   This is a test.\n",
      "  </p>\n",
      "  <a href=\"/my_link1\" id=\"link1\">\n",
      "   Link 1\n",
      "  </a>\n",
      "  <a href=\"/my_link2\" id=\"link2\">\n",
      "   Link 2\n",
      "  </a>\n",
      "  <p>\n",
      "   Hello,\n",
      "   <b class=\"boldtext\">\n",
      "    Bold Text\n",
      "   </b>\n",
      "  </p>\n",
      " </body>\n",
      "</html>\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# 原始 HTML 程式碼\n",
    "html_doc = \"\"\"\n",
    "<html><head><title>Hello World</title></head>\n",
    "<body><h2>Test Header</h2>\n",
    "<p>This is a test.</p>\n",
    "<a id=\"link1\" href=\"/my_link1\">Link 1</a>\n",
    "<a id=\"link2\" href=\"/my_link2\">Link 2</a>\n",
    "<p>Hello, <b class=\"boldtext\">Bold Text</b></p>\n",
    "</body></html>\n",
    "\"\"\"\n",
    "\n",
    "# 以 Beautiful Soup 解析 HTML 程式碼\n",
    "#url = 'https://dct.ntcu.edu.tw/news.php'\n",
    "soup = BeautifulSoup(html_doc, 'html.parser')\n",
    "print(soup.prettify())"
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
