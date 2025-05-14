# token transfer涉及上传文件
def store_info(accountid):
    url = f'https://airboard-ng.airwallex.com/api/v1/clientdetail/getStoreInfoByAccountId?accountId%3D{accountid}'
    r = requests.get(url=url, headers=awx_headers).text
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    with open(file=f_name, mode='a', encoding='utf-8') as f:
        f.write(str(r) + '\n')
    return r


def get_upload_key(accountid):
    url = 'https://airboard-ng.airwallex.com/api/v1/common/prepareForUpload'
    data = {
        'mimeTypes': ['application/pdf']
    }
    awx_headers['Referer'] = f'https://airboard-ng.airwallex.com/clientinfo/clientdetail/{accountid}'
    r = requests.post(url=url, data=json.dumps(data), headers=awx_headers).text
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    with open(file=f_name, mode='a', encoding='utf-8') as f:
        f.write(str(r) + '\n')
    return r['data'][0]['endpoint'], r['data'][0]['form_data']


def aliyun_enable(url, form_data):
    form_data['Content-Disposition'] = "attachment;filename='Airwallex Mail - Re_ Token Transfer Supporting Material.pdf'"
    with open('Airwallex Mail - Re_ Token Transfer Supporting Material.pdf', "rb") as f:
        file = {"file": ('Airwallex Mail - Re_ Token Transfer Supporting Material.pdf', f, "application/pdf")}
        r = requests.post(url=url, data=form_data, files=file)
        with open(file=f_name, mode='a', encoding='utf-8') as f:
            f.write(str(r) + '\n')
        # print(r.status_code)  # 204 means success
        # print(r.text)


def get_file_byId(key):
    url = f'https://airboard-ng.airwallex.com/api/v1/common/getFileById?fileId%3D{key}'
    r = requests.get(url=url, headers=awx_headers).text
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    with open(file=f_name, mode='a', encoding='utf-8') as f:
        f.write(str(r) + '\n')


def transfer_store(from_accountid, to_accountid, doc, value_list, comment=f'batch process - {datetime.datetime.now()}'):
    url = 'https://airboard-ng.airwallex.com/api/v1/clientdetail/transferStore'
    data = {
        'data': {
            'comment': comment,
            'fromAccountId': from_accountid,
            'supportingDocUrls': doc,
            'toAccountId': to_accountid,
        },
        'operatorInfo': {
            'email': 'ben.chen@airwallex.com',
            'id': 330,
            'name': 'Ben Chen - Python Auto',
            'roles': [],
        },
        'stores': value_list,
    }
    r = requests.post(url=url, data=json.dumps(data), headers=awx_headers).text
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    with open(file=f_name, mode='a', encoding='utf-8') as f:
        f.write(str(r) + '\n')
    return r

...
if __name__ == '__main__':
    from_accountid = 'ab821f5c-c1e5-48f8-98f9-1733c74694df'
    to_accountid = 'ab821f5c-c1e5-48f8-98f9-1733c74694df'
    # get the client basic info, e.g. if it is active
    client_info(accountid=from_accountid)
    # get the client store info, and choose the migration scope
    stores = store_info(accountid=from_accountid)
    # upload file
    furl, fkey = get_upload_key(accountid=from_accountid)
    aliyun_enable(url=furl, form_data=fkey)
    get_file_byId(key=fkey['key'])
    # actually transfer
    for s in stores['data']['values']:
        value_list = []
        value_list.append(s)
        r = transfer_store(from_accountid=from_accountid, to_accountid=to_accountid, doc=['/'.join([fkey['key'], 'Airwallex Mail - Re_ Token Transfer Supporting Material.pdf'])], value_list=value_list)
        if r['success']:
            print('token transferred successfully')
