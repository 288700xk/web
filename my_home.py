def page_1():
    pass

def page_2():
    pass

def page_3():
    pass

def page_4():
    pass


'我的主页'

import streamlit as st

from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

'我的兴趣推荐'

'我的图片处理工具'

'我的智能词典'

'我的留言区'

if (page == '我的兴趣推荐'):
    page_1()
elif (page == '我的图片处理工具') :
    page_2()
elif (page == '我的智能词典') :
    page_3()
elif (page == '我的留言区') :
    page_4()
else :
    pass
