# Further information about Akiles API: https://apidoc.akiles.app/
# Akiles choices: Sync integration (non whitelabel) + API key authentication
import requests


def post_new_member(organization_id, data):
    # Test variables
    organization_id = 'organization_id'
    data = {'name': 'Naomi Doe'}
    # Function
    url = f'https://api.akiles.app/v2/organization/{organization_id}/members'
    r = requests.post(url, data)
    print('Status Code: ', r.status_code)


def post_member_group(organization_id, member_id, data):
    # Test variables
    organization_id = 'organization_id'
    member_id = 'member_id'
    data = {
        "member_group_id": "mg_3merk33gt1692dk2p2m1",
        "starts_at": "2018-03-13T16:56:51.766836837Z",
        "ends_at": "2018-03-13T16:56:51.766836837Z"
    }
    # Function
    url = f'https://api.akiles.app/v2/organization/{organization_id}/members/{member_id}/group_associations'
    r = requests.post(url, data)
    print('Status Code: ', r.status_code)


def post_set_member_magic_link_as_login_method(member_id, data):
    # Test variables
    member_id = 'member_id'
    data = {}
    # Function
    url = f'https://api.akiles.app/v2/members/{member_id}/magic_links'
    r = requests.post(url, data)
    print('Status Code: ', r.status_code)


def post_reveal_member_magic_link(member_id, member_magic_link_id, data):
    # Test variables
    member_id = 'member_id'
    member_magic_link_id = 'unknown'
    data = {}
    # Function
    url = f'https://api.akiles.app/v2/members/{member_id}/magic_links/{member_magic_link_id}/revea'
    r = requests.post(url, data)
    print('Status Code: ', r.status_code)


# Test functions
post_new_member('1', '2')
post_member_group('1', '2', '3')
post_set_member_magic_link_as_login_method('1', '2')
post_reveal_member_magic_link('1', '2', '3')
