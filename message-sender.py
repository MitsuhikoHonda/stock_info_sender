import requests

api_token = 'xoxb-1881597833890-1891659324519-qzkxn3s56aLFSN21pM33mr5d' # please enter your api_token
channel = 'stock-info-screening' # please enter your channel

class SlackManager:
    def __init__(self):
        self.api_token = api_token
        self.channel = channel

    def upload_file(self,file,file_name):
        files = {'file':open(file,'rb')}
        param = {
            'token' : self.api_token,
            'channels' : self.channel,
            'filename' : file_name,
            'initial_comment' : '高配当株情報の連絡です。IPOの確認も忘れずに！',
            'title' : '高配当株情報',
        }
        res = requests.post(url="https://slack.com/api/files.upload",
            data=param,
            files=files)
        print(res.json())

if __name__ =='__main__':
    file_name = 'high-dividend-stock-info.xlsx'
    file_path = './data/' + file_name
    slack = SlackManager()
    slack.upload_file(file_path,file_name)