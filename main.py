# import boto3

class HtmlDocument:
    #This lets you initialize some HTML for a new document.
    def __init__(self,content):
        self.content = content

class HtmlManager:
    #This defines functions which lets you create a new HTML document, 
    #and save the document to your files.
    #write-html.py

    def __init__(self):
        self.document = None

    def create_html(self):
        
        message = """<html>
        <head>This is a new html file</head>
        <body><p>Welcome to SababKabab Restaurant!</p>
        <p> We only serve Kababs up in here. </p>
        </body>
        </html>"""
        newdoc = HtmlDocument(message)
        self.document = newdoc
        print(newdoc) dawa

        
    def save_html_file(self):
        f = open('SababKababRestaurant.html','w')
        f.write(self.document.content)
        f.close()


class AWSmanager:
    pass
#   s3 = boto3.client('s3')
#   #define connections to boto3 and save file to s3
#   def save_to_s3():   
#     boto3.client('s3').upload_file('helloworld.html', 'lmtd-class', 'heyclass.html')

manager = HtmlManager()
manager.create_html()
manager.save_html_file()