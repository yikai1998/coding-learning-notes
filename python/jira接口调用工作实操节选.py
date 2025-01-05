import requests
from requests.auth import HTTPBasicAuth
from jira import JIRA
import json
import ast

# 基本config
jira_server = 'https://airwallex.atlassian.net'
jira_url = 'https://airwallex.atlassian.net/rest/api/3/search'
jira_username = 'you jira account mail'
jira_token = 'your jira account token'
jira_auth = requests.auth.HTTPBasicAuth(username=jira_username, password=jira_token)
jira_auth2 = JIRA(server=jira_server, basic_auth=(jira_username, jira_token))
jira_headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# 用jql搜tickets
jql_query = "PROJECT IN (CEOPS) AND issuetype in ('CN Inbound File Upload','Multiple GA') AND updated >= -5d ORDER BY created ASC"
def jql_search(jql, batch_size=20):
    begin = 0
    all_tickets = []
    go_on = 1
    while go_on:
        payload = json.dumps({
            'fields': ['summary', 'status', 'assignee', 'issuetype', 'customfield_11507'],
            'fieldsByKeys': False,
            'jql': jql,
            'maxResults': batch_size,
            'startAt': begin
        })
        response = requests.request(method='POST', url=jira_url, data=payload, headers=jira_headers, auth=jira_auth).text
        r = response.replace('true', 'True').replace('false', 'False').replace('null', 'None')
        r = ast.literal_eval(r)
        tickets = r.get('issues', [])
        all_tickets.extend(tickets)
        total = r.get('total', 0)
        begin += batch_size
        go_on = 0 if begin >= total else 1
        print(r)
    return all_tickets

# 通过key搜索该ticket的status transition history
# 法1
def get_status_change_history(issue_key):
    url = f"{jira_server}/rest/api/3/issue/{issue_key}?expand=changelog"
    response = requests.get(url, headers=jira_headers, auth=jira_auth)
    if response.status_code == 200:
        # Parse the JSON response
        issue_data = response.json()
        changelog = issue_data.get('changelog', {})
        histories = changelog.get('histories', [])
        # Iterate through the histories to find status changes
        for history in histories:
            author_email = history.get('author', {}).get('emailAddress', 'Unknown Email')
            for item in history.get('items', []):
                if item['field'] == 'status':
                    created_date = history['created']
                    from_status = item['fromString']
                    to_status = item['toString']
                    print(f"Operator: {author_email}, Date: {created_date}, From: {from_status}, To: {to_status}")
    else:
        print(f"Failed to retrieve issue changelog: {response.status_code}")
        print(response.text)

# 法2
def jira_transitions(key):
    logs = config.jira.issue(key, expand='changelog').changelog.histories
    logs = [
        [(log.created,act.fromString,act.toString) for act in log.items if act.field == 'status']
        for log in logs
    ]
    logs = [log for log in logs if log]
    return logs
changeLogs = jira_transitions(key=id[0])
new_data = ('', '', '')
for hist in changeLogs:
    if hist[0][2] == 'RFI':
        new_data = hist[0]
        break
old_jira_df.loc[old_jira_df.Key == id[0], ['RfiTime', 'TransitionFrom', 'TransitionTo']] = new_data

# update jira ticket status， 好像也可以同时commen ，暂未研究
jira_auth2.transition_issue(key, 'Ask for URL/Doc')  # transition (str): ID or name of the transition to perform

# 评论ticket
def comment_ticket(key):
    wording = comment_wording
    url = f'https://airwallex.atlassian.net/rest/api/latest/issue/{key}/comment'
    options = {
        "body": wording,
        "properties": [{
            "key": "sd.public.comment",
            "value": {
                "internal": True  # 是否设定为internal comment
            }
        }]
    }
    requests.post(url=url, json=options, headers=jira_headers, verify=certifi.where(), allow_redirects=False, auth=jira_auth).json()

# update jira fields, e.g.priority
def jira_priority_highest(key, level='1'):
    url = f'https://airwallex.atlassian.net/rest/api/3/issue/{key}'
    payload = {
        'fields': {
            'priority': {
                'id': level,  # 1 by default, means HIGHEST
            },
            # 'customfield_12707': 'account_id_test1',
            # 'description': description_adf,
            'assignee': {
              'id': new_assignee_id
            },
            'reporter': {
                'id': new_reporter_id
            },
            participants_field_id: [
                {'accountId': accountId} for accountId in new_participants_ids
                # new_assignee_id = '5de7170cba60e10cfd67fa0e'
                # new_reporter_id = '5de7170cba60e10cfd67fa0e'
                # participants_field_id = 'customfield_10501'
                # new_participants_ids = ['5de7170cba60e10cfd67fa0e', '617f433d327da400697a7bd0']
            ]
        }
    }
    response = requests.put(
        url,
        json=payload,
        headers=config.jira_headers,
        auth=config.jira_auth
    )
    if response.status_code == 204:
        print(f'Fields updated successfully for {key}')
    else:
        print(f'Failed to update fields with status code {response.status_code}: {response.content}')
    time.sleep(0.1)
'''
the previous message will replace the current list of participants with the new list specified in the new_participants_ids. 
If you want to add a participant without removing the existing ones, you would have to first get the current list of participants, add the new participant's ID to that list, and then update the field with the combined list

get_response = requests.get(
    url=f'https://airwallex.atlassian.net/rest/api/3/issue/{i}',
    headers=jira_headers,
    auth=jira_auth
)
if get_response.status_code == 200:
    current_participants = get_response.json()['fields'][participants_field_id]  # 可以很方便的找到特定key ticket的相应字段值
    print(current_participants)
else:
    print(f"Failed to get current participants: {get_response.content}")
    exit()
if not any(participant['accountId'] == new_participant_id for participant in current_participants):
    current_participants.append({"accountId": new_participant_id})
'''


# update jira fields like cascading fields
payload = {
    'fields': {
        'customfield_12720': {
            'value': 'Amend KYC Profile',
            'child': {
                'value': 'Change in Country Exposure'
            }
        }
    }
}
response = requests.put(
    url=f'https://airwallex.atlassian.net/rest/api/3/issue/{i}',
    headers=headers,
    auth=auth,
    json=payload
)
if response.status_code == 204:
    print('Cascading select custom field updated successfully.')
else:
    print(f'Failed to update field: {response.status_code} - {response.text}')

# create jira ticket(s)
new_issue_dict = {
    'project': {'key': 'KYCSD'},
    'summary': 'test by ben 0523',
    'description': 'created by python 0523',
    'issuetype': {'name': 'Task'}
}
new_issue = jira_auth2.create_issue(fields=new_issue_dict)
# List of issues to be created. The create_issues method expects a list of dictionaries, where each dictionary represents the fields for an issue you want to create. The list can contain different types of issues or the same type with different data.
new_issues = jira_auth2.create_issues(field_list=issue_list)
