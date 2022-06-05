import dropbox
class Uploadfiles:
    def __init__(self, access_token) :
        self.access_token = access_token
    def upload(self):
        d = dropbox.Dropbox(self.access_token)
        f = str(input("Enter the filepath"))
        file1 = open(f, "rb")
        d.files_upload(file1.read(), "\documents\demo.txt")
def main():
    uploadfilesobject = Uploadfiles("sl.BI69C45gYIWEIoczQfIMgJN1Yi9iVn59ZK2xoRqtsNZQS03QXHeppc716k8AJmdq2QRPWeH7JyPVLqVUe1xEYr78IEuvIjVBz7TxV2osEeiiwwlAmOgKibJK2pOvog4g3dP2fyo")
    uploadfilesobject.upload()
main()
print("File has been moved")

