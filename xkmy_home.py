'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])
def page_1():
    '''我的兴趣推荐'''
    with open('HOYO-MiX - Gion2.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time = 0)
    st.image('崩坏三.jpg')
    st.write('我的音乐推荐')
    st.write('《茶理理理子、TetraCalyx、hanser - Moon Halo》')
    st.image('moon halo.jpg')
    st.write('《Moon Halo》是HOYO-MIX发行的专辑，为崩坏3《薪炎永燃》动画短片印象曲所属专辑，发布于2021年7月9日。')
    st.write('https://www.kugou.com/mixsong/5egndt93.html?frombaidu点此播放')
    st.write('我的游戏推荐')
    st.write('《崩坏3rd》')
    st.image('崩坏3rd.jpg')
    st.write('《崩坏3》是由上海米哈游网络科技股份有限公司制作发行的一款角色扮演类国产手游，背景音乐由HOYO-MiX提供，游戏画面为3D，使用Unity游戏引擎开发。游戏的玩家人数为大型多人在线，内容主题包括ACG、科幻和动作元素。')
    st.write('https://bh3.mihoyo.com/ad/?media_from=sembd1&utm_source=web&utm_medium=bdsem点此访问官网')
    st.write('我的电影推荐')
    st.write('《闪光的哈撒维》')
    st.image('闪光的哈撒维.jpg')
    st.write('剧场版动画系列《机动战士高达：闪光的哈萨维》改编自富野由悠季创作的同名小说作品。于2018年11月21日在东京惠比寿举行的《机动战士高达》系列40周年纪念计划发布会上宣布制作决定。由SUNRISE负责制作，第1部原定于2021年5月21日上映 ，后因新型冠状病毒肺炎疫情在日本的蔓延，宣布延期至2021年6月11日上映')
    st.write('https://www.bilibili.com/bangumi/play/ep409230?from_spmid=666.25.episode.0    点此跳转至哔哩哔哩观看')
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序：")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
def page_3():
    '''我的智能词典'''
    st.write('智慧词典')
    with open('words_space,txt','r',encoding='utf-8')as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]= words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        word_dict[i[1]] = [int(i[0]),i[2]]
    with open('check_out_times txt','r',encoding='utf-8') as f:
        times_list =f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]= times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][8]
        if n in times_dict:
            times_dict[n]+= 1
        else:
            times_dict[n]=1
        with open('check_out_times_txt','w',encoding='utf-8')as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k)+'#’+str(v)+ "\n'
            message = message[:-1]
            f.write(message)
            st.write("查询次数:",times_dict[n])       
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1]=='柚子老师':
            with st.chat_message(''):
                st.write(i[1],':',i[2])
        elif i[1] =='编程猫':
            with st.chat_message(''):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是…',['阿短','编程猫','柚子老师'])
    new_message =st.text_input('想要说的话... ')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message +=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message =message[:-1]
            f.write(message)
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
#python -m streamlit run xkmy_home.py
