# 接口调用模版1
# headers
HEADER = {
    'Content-Type': 'application/json',
    'authorization': 'TOKEN WITHOUT BEARER',
    'x-data-center': 'HK'  # default
}
HEADER2 = {
    'Content-Type': 'application/json',
    'authorization': 'TOKEN',
    'x-data-center': 'HK'  # default
}
def search_datacenter(self, accountid=None, legalentityid=None):
    url = 'https://airboard-ng.airwallex.com/graphql/kyc/getLegalEntityList'
    HEADER['x-data-center'] = 'HK'  # reset to be default
    if accountid is None:
        data = {
            'operationName': 'getLegalEntityList',
            'query': 'query getLegalEntityList($params: GetLegalEntityListParam) {\n  getLegalEntityList(params: $params) {\n    data {\n      account_id\n      account_open_id\n      agreed_to_terms_and_conditions\n      business_structure\n      client_legal_entity_id\n      country\n      customer_name_english\n      customer_name_local\n      industry_category\n      kyc_created_time\n      kyc_passed_time\n      kyc_process_status\n      risk_rating\n      __typename\n    }\n    total\n    __typename\n  }\n}\n',
            'variables': {
                'params': {
                    'client_legal_entity_id': legalentityid,
                    'from': 0,
                    'size': 10,
                }
            }
        }
    else:
        data = {
            'operationName': 'getLegalEntityList',
            'query': 'query getLegalEntityList($params: GetLegalEntityListParam) {\n  getLegalEntityList(params: $params) {\n    data {\n      account_id\n      account_open_id\n      agreed_to_terms_and_conditions\n      business_structure\n      client_legal_entity_id\n      country\n      customer_name_english\n      customer_name_local\n      industry_category\n      kyc_created_time\n      kyc_passed_time\n      kyc_process_status\n      risk_rating\n      __typename\n    }\n    total\n    __typename\n  }\n}\n',
            'variables': {
                'params': {
                    'account_id': accountid,
                    'from': 0,
                    'size': 10,
                }
            }
        }
    r = requests.post(url=url, data=json.dumps(data), headers=HEADER).text
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    return r['data']['getLegalEntityList']['total']
dc = 'HK' if func_repo.search_datacenter(accountid=accountid) > 0 else 'SG'
HEADER['x-data-center'] = dc
HEADER2['x-data-center'] = dc
def get_risk_common_info(legal_entity_id):
    url = 'https://airboard-ng.airwallex.com/graphql/risk-common'
    data = {
        'operationName': 'getAccountLinkageInformationV2',
        'query': 'query getAccountLinkageInformationV2($accStatuses: [String], $accountId: String, $beforeKycReceived: Boolean, $includeAnonymousIP: Boolean, $kycFailedReasons: [String], $kycRecordId: String, $kycStatuses: [String], $legalEntityId: String, $offboardReasons: [String], $orderByHits: Order, $pageNumber: Int, $pageSize: Int, $types: [String], $watchListCategories: [String], $watchListHits: Boolean) {\n  getAccountLinkageInformationV2(\n    accStatuses: $accStatuses\n    accountId: $accountId\n    beforeKycReceived: $beforeKycReceived\n    includeAnonymousIP: $includeAnonymousIP\n    kycFailedReasons: $kycFailedReasons\n    kycRecordId: $kycRecordId\n    kycStatuses: $kycStatuses\n    legalEntityId: $legalEntityId\n    offboardReasons: $offboardReasons\n    orderByHits: $orderByHits\n    pageNumber: $pageNumber\n    pageSize: $pageSize\n    types: $types\n    watchListCategories: $watchListCategories\n    watchListHits: $watchListHits\n  ) {\n    accountGroupId\n    accountLinkageCounts\n    accountLinkageDetails {\n      accountClosureReason\n      accountStatus\n      customerSegment\n      idHitsOfReasons\n      kycFailedReason\n      kycStatus\n      linkageInformation\n      linkageType\n      linkedAccountId\n      linkedCleId\n      linkedName\n      links {\n        detail\n        reason\n        __typename\n      }\n      offboardReason\n      ownerOrgLevelTwo\n      owningEntity\n      platformAccountId\n      spaceId\n      watchlistCategories\n      watchlistHit\n      __typename\n    }\n    kycFailedReasons\n    linkTypes\n    offboardReasons\n    ownedAccountGroups {\n      id\n      name\n      ownerId\n      __typename\n    }\n    resCount\n    statsOfAccount {\n      ACTIVE\n      CLOSED\n      DORMANT\n      FROZEN\n      INITIAL\n      PENDING_CLOSE\n      __typename\n    }\n    statsOfKycStats {\n      FAILURE\n      INIT\n      SUBMITTED\n      SUCCESS\n      __typename\n    }\n    statsOfLinkType {\n      email\n      phone\n      __typename\n    }\n    submissionIp {\n      geoInfo {\n        city\n        country\n        riskRating\n        __typename\n      }\n      ip\n      __typename\n    }\n    total\n    watchListCategories\n    watchListHitsCount\n    __typename\n  }\n}\n',
        'variables': {
            'accStatuses': ['CLOSED'],
            'beforeKycReceived': True,
            'legalEntityId': legal_entity_id,
            'pageNumber': 1,
            'pageSize': 10000,
            'types': ['director'],
        }
    }
    r = requests.post(url=url, data=json.dumps(data), headers=HEADER).text
    time.sleep(0.1)
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    return r

# 接口调用模版2
def search_datacenter(legal_entity_id=None, account_id=None, token=None):
    headers = set_headers(datacenter='HK', token=token[7:])  # reset to be default
    url = 'https://airboard-ng.airwallex.com/graphql/kyc/getLegalEntityList'
    data = {
        'operationName': 'getLegalEntityList',
        'query': 'query getLegalEntityList($params: GetLegalEntityListParam) {\n  getLegalEntityList(params: $params) {\n    data {\n      account_id\n      account_open_id\n      agreed_to_terms_and_conditions\n      business_structure\n      client_legal_entity_id\n      country\n      customer_name_english\n      customer_name_local\n      industry_category\n      kyc_created_time\n      kyc_passed_time\n      kyc_process_status\n      risk_rating\n      __typename\n    }\n    total\n    __typename\n  }\n}\n',
        'variables': {
            'params': {
                'from': 0,
                'size': 10,
            }
        }
    }
    if account_id is None:
        data['variables']['params']['client_legal_entity_id'] = legal_entity_id
    else:
        data['variables']['params']['account_id'] = account_id
    r = requests.post(url=url, headers=headers, data=json.dumps(data)).text
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    return r['data']['getLegalEntityList']['total']


def datacenter_decorator(func):
    def wrapper(*args, **kwargs):
        account_id = kwargs.get('account_id')
        legal_entity_id = kwargs.get('legal_entity_id')
        token = kwargs.get('token')
        datacenter = 'HK' if search_datacenter(account_id=account_id, legal_entity_id=legal_entity_id, token=token) > 0 else 'SG'
        kwargs['datacenter'] = datacenter
        return func(*args, **kwargs)
    return wrapper


def set_headers(datacenter, token):
    return {
        'Content-Type': 'application/json',
        'authorization': token,
        'x-data-center': datacenter,
    }


@datacenter_decorator
def get_tm_case(datacenter, token, case_id, account_id=None, legal_entity_id=None):
    url = 'https://airboard-ng.airwallex.com/graphql/postmonitoring/uar'
    data = {
        'operationName': 'getCaseById',
        'query': 'query getCaseById($caseUuid: ID!) {\n  getCaseById(caseUuid: $caseUuid) {\n    accountId\n    businessName\n    cardNumber\n    caseHandlingTeam\n    channelRfiTag\n    clientRole\n    comment\n    createdAt\n    createdBy\n    customerExternalBankAccountNumber\n    customerSegment\n    emailSubject\n    files {\n      fileId\n      fileName\n      __typename\n    }\n    isMigration\n    legalEntityId\n    level\n    merchantId\n    migration\n    orgLevel2\n    owningEntity\n    recallStatus\n    receivedAt\n    reviewer\n    rfiEmailTitle\n    rfiSentDate\n    rfiSessionId\n    rfiSessionStatus\n    riskTypes\n    sla\n    sourceChannel\n    sourceSubType {\n      cardScheme {\n        cardSchemeValue\n        __typename\n      }\n      channelFraud {\n        accountStatus\n        indemnity\n        indemnityEta\n        indemnityRequestDate\n        internalClientEscalation\n        isNewFraud\n        recallStatus\n        returnedAmount\n        returnedDate\n        ticketStatus\n        __typename\n      }\n      channelRfi {\n        accountBlockByChannel\n        internalClientEscalation\n        tag\n        __typename\n      }\n      value\n      __typename\n    }\n    sourceType\n    status\n    transactionIds\n    uuid\n    zendeskTicketNumber\n    __typename\n  }\n}',
        'variables': {
            'caseUuid': case_id,
        }
    }
    headers = set_headers(datacenter=datacenter, token=token[7:])
    r = requests.post(url=url, headers=headers, data=json.dumps(data)).text
    r = r.replace('false', 'False').replace('null', 'None').replace('true', 'True')
    r = ast.literal_eval(r)
    return {
        'accountId': r['data']['getCaseById']['accountId'],
        'businessName': r['data']['getCaseById']['businessName'],
        'legalEntityId': r['data']['getCaseById']['legalEntityId'],
        'orgLevel2': r['data']['getCaseById']['orgLevel2'],
        'owningEntity': r['data']['getCaseById']['owningEntity'],
        'transactionId': r['data']['getCaseById']['transactionIds'][0],
        'zendeskTicketNumber': r['data']['getCaseById']['zendeskTicketNumber'],
    }

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

# decode token
import jwt
def decode_token(self, token):
    pload = jwt.decode(token, options={'verify_signature': False})
    return pload

# map btw two list
def black_map(predicate, iterable):
    """
    purpose to check against two list
    reference:
        https://docs.python.org/3/library/itertools.html#itertools.dropwhile [itertools 里特有的方法，不是随便命名的]
        a= itertools.filterfalse(lambda x: x not in black, test)
        https://blog.csdn.net/mieleizhi0522/article/details/82142856
    """
    for x in iterable:
        if predicate(x):
            yield x

# bug经验
"""
在Python中，空字符串 '' 被认为在任何字符串中，所以
'' in 'A29AD2EBC5VQHK'   # 等于 True
这一点逻辑上类似于：找“空子串”总会在任何串的开始、结束等地方。
"""


# local runtime
```txt
download docker https://rancherdesktop.io/ 
open the docker in backend
open terminal
    docker run -p 127.0.0.1:9000:8080 asia-docker.pkg.dev/colab-images/public/runtime
    copy: http://127.0.0.1:9000/?token=e35da72d2944bbb745350bc40479454fbc998ab768434385

import socket; print(socket.gethostname())
```
