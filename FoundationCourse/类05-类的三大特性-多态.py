# python的多态是简化版本的

class Image():
    def show(self):
        print('图片')


class Text():
    def show(self):
        print('文字')


def show_content(content):
    # 关心的是同一个方法，不同表现形式
    # 只关心对象的方法，不关心对象的类型（和其他语言不一样）
    content.show()


image = Image()
text = Text()
show_content(image)
show_content(text)
