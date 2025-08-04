```sql
select 
a.data:accountDetails:authorisedPersonDetails as address_default,  -- variant type
a.data:accountDetails:authorisedPersonDetails::string as address_string,
a.data:accountDetails:authorisedPersonDetails?::date as address_date_safe,
a.data:accountDetails:authorisedPersonDetails:active as address_default2,  -- still variant type 
a.data:accountDetails:authorisedPersonDetails:source as address_default3,  -- still variant type
-- a.data:accountDetails:authorisedPersonDetails:active is true as address_default3,
a.data:accountDetails:authorisedPersonDetails:active::boolean as address,
a.data:accountDetails:authorisedPersonDetails:active::boolean is true as address,
variant_get(a.data, '$.clientInternalInfo.accountOwner', 'string') as account_owner
from `tp-prod-sg`.`silver`.`authorisation__account` as a
where a.id = '02d3a4cf-b2fc-49ac-9922-e24b152ade4d'
```

```sql
-- account base pool
/*
select distinct
cast(sf.legal_entity_id as string) as legal_entity_id,
cast(ac.id as string) as account_id,
ac.`data`:accountDetails:businessDetails.businessName?::string as biz_name_local,
ac.`data`:clientInternalInfo:owningEntity?::string as owning_entity,
timestamp(ac.`data`:kycRecord:receiveTime) as kyc_receive_time,
timestamp(ac.`data`:kycRecord:kycPassedDate) as kyc_pass_time,
ac.`data`:kycRecord:status?::string as kyc_status,
ac.`data`:status?::string as account_status,
ac.`data`:clientInternalInfo:signUpUtm:utmSource?::string as utm_source,
ac.`data`:clientInternalInfo:signUpUtm:utmCampaign?::string as utm_campaign,
ac.`data`:clientInternalInfo:signUpOwner is not null as bd_initiate
from `tp-prod-sg`.`silver`.`authorisation__account` as ac
left join `tp-prod-sg`.`silver`.`airboard_ng_api__salesforce_data` as sf on sf.account_id = ac.id
where 1 = 1
and ac.`data`:clientInternalInfo.owningEntity?::string in ('Airwallex (Hong Kong) Limited', 'Airwallex (Singapore) Pte Ltd', 'Airwallex (Malaysia) Sdn. Bhd.')
and left(sf.`data`:ownerOrgLevel2, 2) <> 'CN'
and lower(ac.`data`:clientInternalInfo:signUpUtm:utmSource) = 'partnerstack'
*/

-- Channel Partner Sign-up On Behalf
/*
select distinct
kc.`data`:kycRecordId?::string as legal_entity_id,
ke.`data`:onboardDetails:createdByRole?::string as created_by_role
from `risk-prod-sg`.`silver`.`individualkyc__kyc_case` as kc
left join `risk-prod-sg`.`silver`.`individualkyc__kyc_entity` as ke on kc.`data`:entityId?::string = ke.id
where 1 = 1
and ke.`data`:onboardDetails:createdByRole::string = '00000000-0000-0000-0000-000000040000'  -- "Channel Partner", "渠道合作方。"
*/
```

```sql
-- airboard auth users
create or replace view yikai_test_dbt.temp as (select
  email as emp_email,
  `id` as emp_id,
  active,
  deleted,
  get_json_object(extra_info::string, "$.oktaUser['urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'].employeeNumber") as emp_number,
  get_json_object(extra_info::string, "$.oktaUser['urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'].department") as emp_team,
  get_json_object(extra_info::string, "$.oktaUser['urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'].manager.value") as emp_manager
from 
  `tp-prod-sg`.silver.airboardngauth__account
where 
  1 = 1
  and not deleted
  and not frozen
);
```
