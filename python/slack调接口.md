## 动态生成mention users
```py
prefix_mention_map = {
    'HK-CIMC': ['U056EVDANKE', 'U057FESTY9X'],  # CHING-IP MAYBLE-CHENG
    'HK-CIK': ['U056EVDANKE', 'U027EJ13C0Z'],  # CHING-IP KOALA
    'HK-CIKT': ['U056EVDANKE', 'U027EJ13C0Z'],  # CHING-IP KOALA
    'HK-AKJT': ['U07580JBF43', 'U066CD5R8SH'],  # ARIEL-KWAN JAYDEN-TSE
    'HK-MC':   ['U0271PD2U8J', 'U09AECCBK8E'],  # MARCUS-CHENG HANYUAN-ZHANG
    'HK-MYJ': ['U050FCPQNHX', 'U066CD5R8SH'],  # MICHELLE-YIM JAYDEN-TSE
    'HK-AK': ['U07580JBF43', 'U066CD5R8SH'],  # ARIEL-KWAN JAYDEN-TSE
}

mention_users = []
for utm in df['utm_campaign'].unique():
    for utm_start, utm_poc in prefix_mention_map.items():
        if utm.startswith(utm_start):
            mention_users.extend(utm_poc)

mention_users = list(set(mention_users))

def df_to_slack_block_mention(user_ids=['U02KLQGEQLV', 'UR0STDE9F']):

    """generate slack mention queue"""

    rich_text_elements = []

    for i, uid in enumerate(user_ids):
        rich_text_elements.append({'type': 'user', 'user_id': uid})
        if i != len(user_ids) - 1:
            rich_text_elements.append({'type': 'text', 'text': ' '})

    block = {
        'type': 'rich_text',
        'elements': [
            {
                'type': 'rich_text_section',
                'elements': rich_text_elements
            }
        ]
    } 
    
    return block
```

## 动态生成table
```py
def df_to_slack_block_table(df):
    """convert the pandas dataframe to be slack table block rows"""
    
    rows = []
    header_row = []

    for col in df.columns:
        header_row.append({
            'type': 'rich_text',
            'elements': [{
                'type': 'rich_text_section',
                'elements': [{
                    'type': 'text',
                    'text': str(col),
                    'style': {'bold': True}
                }]
            }]
        })

    rows.append(header_row)

    for _, row in df.iterrows():
        data_rows = []
        for cell in row:
            data_rows.append({
                'type': 'rich_text',
                'elements': [{
                    'type': 'rich_text_section',
                    'elements': [{
                        'type': 'text',
                        'text': str(cell)
                        }]
                }]
            })
        rows.append(data_rows)
    
    block = {
        'type': 'table',
        'rows': rows
    }

    return block
```

## 动态组成block
```py
table_b = df_to_slack_block_table(df=df)
intro_b = {
    'type': 'rich_text',
    'elements': [
        {
            'type': 'rich_text_section',
            'elements': [
                {
                    'type': 'text',
                    'text': f'HKSEA whitelist channel partner RFI notification report, {today}:'
                }
            ]
        }
    ]
}
mention_b = df_to_slack_block_mention(user_ids=mention_users)
payload = {
    'blocks': [
        intro_b, {'type': 'divider'},
        table_b, {'type': 'divider'},
        mention_b
    ]
}
```

## 发信息至channel
```py
url = 'xxx'

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print('Message sent!')
else:
    print(f"Failed: {response.status_code} - {response.text}")
```
