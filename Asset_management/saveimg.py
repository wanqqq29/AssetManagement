import base64,re
def saveimg(obj, file_path,):
    with open(file_path, 'wb+') as fp:
        # 如果上传的图片非常大， 那么通过 img对象的 chunks() 方法 分割成多个片段来上传
        for chunk in obj.chunks():
            fp.write(chunk)
    # with open(file_path, 'rb') as f:
    #     base64_data = base64.b64encode(f.read())
    #     base64_data = base64_data.decode('GBK')
    #     base64data = re.compile("^b'", re.I).sub('', base64_data)
    #     base64data2 = re.compile("'$", re.I).sub('', base64data)
    return file_path
# data:image/png;base64,