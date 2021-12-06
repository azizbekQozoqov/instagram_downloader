from os import path


class InstaDownload:
    '''The URL must start with https://www.instagram.com/. If the URL is not in this format, program will not work!!!'''
    def __init__(self, url:str, target:str='down') -> None:
        import instaloader
        from instaloader import Post

        self.url =  url #'https://www.instagram.com/p/CVib8ZwMyxl/'
        self.target = target
        self.shorted_url = self.short_url(url)
        self.loader = instaloader.Instaloader()
        self.data = ''
        try:
            self.post = Post.from_shortcode(self.loader.context, self.shorted_url)
        except Exception as e:
            self.data = {
                'type' : 'in.error',
                'data' : str(e),
            }
    def download_and_get_path(self):
        import os
        try:
            self.loader.download_post(self.post, target=self.target)
            self.data = self.data = {
                'type' : 'in.success',
                'data':{
                    'path': os.getcwd() + '\\'+self.target
                }
            }
        except Exception as e:
            self.data = {
                'type' : 'in.error',
                'data' : str(e),
            }
        return self.data

    def short_url(self,url:str) -> str:
        try:
            if url.startswith('https'):
                url= url[28:39]
                return url
        except Exception as e:
            return {
                'type' : 'in.error',
                'data':str(e)
            }
    def __repr__(self) -> str:
        return self.data