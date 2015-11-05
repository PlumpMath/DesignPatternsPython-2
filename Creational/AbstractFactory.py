import abc
import json
import html


class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_text(self, context):
        raise NotImplementedError()

    @abc.abstractmethod
    def create_picture(self, path, name):
        raise NotImplementedError()


class JsonFactory(AbstractFactory):

    def create_text(self, content):
        return TextJson(content)

    def create_picture(self, path, name):
        return PictureJson(path, name)


class HtmlFactory(AbstractFactory):

    def create_text(self, content):
        return TextHtml(content)

    def create_picture(self, path, name):
        return PictureHtml(path, name)


class IMedia(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def render(self):
        raise NotImplementedError()


class BasePicture(IMedia, metaclass=abc.ABCMeta):

    def __init__(self, path, name):
        self.path = path
        self.name = name


class PictureJson(BasePicture):

    def render(self):
        return json.dumps({'title': self.name, 'path': self.path})


class PictureHtml(BasePicture):

    def render(self):
        return '<img src="{}" title="{}"/>'.format(self.path, self.name)


class BaseText(IMedia, metaclass=abc.ABCMeta):

    def __init__(self, text):
        self.text = text


class TextHtml(BaseText):

    def render(self):
        return '<div>{}</div>'.format(html.escape(self.text))


class TextJson(BaseText):

    def render(self):
        return json.dumps({'content': self.text})


def test_factory(factory: AbstractFactory):
    assert isinstance(factory, test_factory.__annotations__.get('factory'))

    picture = factory.create_picture(path='2.jpg', name='title')
    text = factory.create_text(content='Lore Ipsum')

    print(picture.render())
    print(text.render())

if __name__ == '__main__':
    test_factory(HtmlFactory())











