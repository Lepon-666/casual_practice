#print输出（\n功能放在字符串内)
def print():
    print('fuzhien')
    print(1111)
    print("dj",14,'ds')
    print('das\ndas\ndas')
#变量存储（变量和纯数据不算字符串，不用加''或"；Python 不需要显式声明变量类型，在第一次变量赋值时由值决定变量的类型）
def bianliang():
    name='hrd'
    age=17
    print('我的名字叫：',name)
    print('今年',age)
    print('我叫',name,' ，今年',age,'岁')
#计算运算（**乘方，%取余数，//取商
    #a=2,b=a，那a和b同一ip，a is b；a=2,b=2,则a和b不是同一ip,不指向同一对象）
def jisuan():
    print(1+2)
#input输入（int数据类型，注意多括号)
def input():
    name=input("请输入你的名字:")
    age=int(input("请输入你的年龄："))
    print("你好",age,"岁的",name,',很高兴认识你!')
    num1=int(input("请输入第一个数字:"))
    num2=int(input("请输入第二个数字:"))
    print("它们的和为",num1+num2)
#format将字符串和变量结合起来，显得简洁
def format():
    a=1    
    print("dasd")
    print(a)
    print("sad",a)
    print(f"sad{a}")
#for循环(作用：先确定循环次数，遍历条件（常用，所以单独出个功能）循环，次数由in后面的可迭代对象决定(列表，字符串，元组,range)，每次遍历执行下方指令。
    #可用if筛选出需要的数据。end=""可以让for循环结果横向输出）
    #(range(n)-从0开始,循环n次;range(a,b)-从a开始，到b前一个数结束,负数前一个数为加一;range(a,b,c)-从a开始，到b前一个数结束，每次间隔c，当前两个和后一个数同向时才能输出结果)
    #用enumerate(list)然后定义两个变量，可以同时遍历index索引,item元素,object对象，元素是对象，对象不一定是元素
    #知道循环多少次多用for，大家的习惯
def forxh():
    for xunhuan0 in range(3):
        print("我在学for循环")
        print(f"这是第{xunhuan0+1}次循环")
    print('\n')
    for xunhuan1 in range(1,5):
        print(xunhuan1)
    print('\n')
    for xunhuan2 in range(1,10,2):
        print(xunhuan2)
    print('\n')
    for xunhuan3 in "fuzhien":
        print(xunhuan3)
    print('\n')
    ceshiscores=[11,44,55,66,77]
    for xunhuan4 in ceshiscores:
        print(f"你的分数是:{xunhuan4}")
    print('\n')
    ydsdh=0
    for xunhuan5 in range(1,11):
        ydsdh=ydsdh+xunhuan5
    print(f"1到10的和为：{ydsdh}")
#if判断(单次)
def ifpd():
    score=int(input('请输入您的成绩：'))
    if score >=90 and score <=100:
        print("牛逼")
    elif score >=80 and score <=100:
        print("还得练啊老弟")
    elif score >=70 and score <=100:
        print("再接再厉吧，前路宽广")
    elif score >=60 and score <=100:
        print("恭喜，但任重而道远啊")
    elif score <60:
        print("怎么回事，小老弟？")
    else:
        print("欸？打错了吧哥们")
#while循环(先判断条件，所以次数一开始不确定
        #while 条件:单条件循环;可以做到所有for循环的事
        #while true:多路径循环，符合条件才关闭,要靠break关闭;可以做到所有while 条件的事;一般给if加循环;)
def whilexh():
    i=1
    while i<=5:
        print(i)
        i=i+1
    print('循环结束\n')

    password=''
    while password !='123456':
        password=input('请输入密码')
        if password !="123456":
            print("密码错误,请再试一次")
    print('密码正确\n')

    while True:
        cmd=input('输入命令(help/quit):')
        if cmd=='quit':
            print('程序退出\n')
            break
        elif cmd=="help":
            print("in this")
        else:
            print("未知命令")

    total=0
    n=1
    while n<=10:
        total+=n
        n+=1
    print(f"和为{total}\n")

    scores=[11,22,33,44,55,666,777]
    index=0
    while index<len(scores):
        print(f"{scores[index]}")
        index +=1
    while True:
        s = input("请输入成绩（0-100）：")
        if not s.isdigit():
            print("请输入数字！")
            continue
        score = int(s)
        if score < 0 or score > 100:
            print("成绩必须在0-100之间！")
            continue
        print(f"录入成功：{score}")
        break
    print("=== 测试 if True ===")
    if True:
        print("✅ 这句话会打印，因为条件为 True")
    print("\n=== 测试 if False ===")
    if False:
        print("❌ 这句话永远不会打印，因为条件为 False")
    print("\n程序结束")
#字符串方法(1.大小写转换2.去除空格/指定字符3.查找or判断4.判断5.替换，分割，拼接6.补齐和填充7.获长，索引，切片8.复制)
def zifucuan():
    print('1.upper/lower/title-单词首字母/capitalize-首字母/swapcase-大小写互换')
    print('2.strip/lstrip/rstrip/strip("符号")')
    print('3.find()-找不到返回-1,找到返回第一个索引/index-找不到报错/count()')
    print('4.isdigit/isalpha/isalnum/isspace/startswith("xx")/s.endswith("xx")')
    print('5.replace("旧","新")/split("分隔符(原变量里面的某个对象)")-切割字符串,返回列表/"连接符".join(list)-因为是字符串方法，所以不能以分隔符字符串调用join(list)')
    print('6.ljust(长度,"符号")-用符号按函数填充到对应长度/s.rjust(长度,"符号")/s.center(长度,"符号")')
    print('7.len(s)/s[index]-索引/s[start:end:step]-切片')
    print('8.str1=str(str)/str[:]/+""')
#列表方法(添加：|||list.append()-重复会覆盖旧值，整体添加,list.extend()将元素依次添加,list.insert()|||
    #删除：list.remove(item)-删第一个匹配值,list.pop([index=-1]),del list[]
    #排序和反转:|||list.reverse(),list.sort(key=None,reverse=False)-括号内内容可以省略，也可以通过修改False→True变为降序,list2=sorted(interable[,key=None][,reverse=False])-ineterable是可迭代对象,这个函数可以生成新变量并排序|||
    #查看:|||len(list)|||,list.count(item)-不在列表内返回0,list.index(值)-第一个匹配值-可用于字符串，但没找到会报错,s[])
    #list2=list.copy()-复制;list2=list(list1);列表可以使用加法和乘法
    #‘索引’可以查元素；删除，边用边删除
    #‘元素’可以查索引；删除，记次
def liebiao():
    nums = [10,4,2,898,24,20]
    print(len(nums))
    nums.insert(2,3)
    nums.remove(3)
    x=nums.pop(0)
    del nums[0]
#字典语法(给值命名)
def zidian():
    scores={"小明":66,"小红":99,"小钢":51,}
    print(scores["小明"])
    scores["小恩"]=100
    del scores['小钢']#删(del or pop)
    if'小恩'in scores:
        print("小恩在列表里")
    for name in scores:#遍历键
        print(name)
    for score in scores.values():#遍历值
        print(score)
    for name,score in scores.items():#同时遍历
        print(f"{name}:{score}分")
def cjb():
    scores={}
    while True:
        print("\n1.录入系统")
        print("2.查询系统")
        print("3.查看所有成绩")
        print("4.退出")
        choice=input("请选择")
        if choice =='1':
            name = input("请输入姓名:")
            s=input("请输入成绩(0-100):")
            if not s.isdigit():
                print("请输入纯数字!")
                continue
            score=int(s)
            if score<0 or score>100:
                print("成绩范围错误!:")
                continue
            scores[name]=score
            print(f"{name}的成绩已录入:{score}")
        elif choice=='2':
            name=input("请输入要查询的姓名:")
            if name in scores:
                print(f"{name}的成绩是:{scores[mame]}")
            else:
                print("查无此人")
        elif choice=='3':
            if scores:
                for name,score in scores.items():
                    print(f"{name}:{score}")
            else:
                print("暂无成绩")
        elif choice=='4':
            print("程序结束")
            break
        else:
            print("无效选项")
#文件读写( #f=open("test.txt","w",encoding="utf-8")   写入方法_2,需要f.close()手动关闭)
         #如果test.txt不存在_最好加上合适后缀，不然会选择打开方式，那w模式会创建一个;除了w模式，还有r,a,r+，a和w区别是，a追加，w覆写;utf-8编码格式可以避免中文乱码)
        #可以在一段程序结尾加上这个，给要用内容的创建文档，在后续调用)
        #读取方法:记住①和②，③是列表相当于循环[readline()];①要整篇文字时用：每次输出全部，并用字符串表示;②要单行提取时用：f.readline()，每次输出单行，并用字符串表示;③要列表时用：f.readlines()每次输出全部，并用列表表示，每行作为一个元素;④要省内存时用：for循环
def wjdx():
    with open("test.txt","w",encoding="utf-8") as f:
        f.write("小明:85\n")
        f.write("小红:95\n")#写入方法_1

    with open("test.txt","r",encoding="utf-8") as f:
        content=f.read()
        print(content)
        #要print输出文档内容要先定义一个变量
#函数
def hs():
    print('def')
#异常处理
def yccl():
    print('try','except')
    
        
