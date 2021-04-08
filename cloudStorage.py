import dropbox

class TransferData :
    def __init__(self,access_token)  :
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)


def main():
    access_token = 'sl.AuhiljqbQJptjgjOas2Ux7FjUM3P9RNzuOMclTJDe-8X6IAwas-FrpH-hXnkof7Ny3GParmdBhPs-iJYV_6abD5Yy51a3DfP9iQc1plG9Xvm8FETRSo__mP8aIio1ODrd_YLNkE'
    transferData = TransferData(access_token)

    file_from = input ("enter the file path to transfer : ")
    file_to = input('enter the full path to upload the file to thee the dropbox  : ')
    transferData.upload_file(file_from,file_to)
    print("file has been moved")


main()


