import requests
import json

graph_url = 'https://graph.microsoft.com/v1.0'


def get_groups(token):
    groups = requests.post(
        '{0}/me/getMemberGroups'.format(graph_url),
        headers={
            'Authorization': 'Bearer {0}'.format(token),
            'Content-Type': 'application/json'

        },
        json={
            'securityEnabledOnly': False
        }
    )
    return groups.json()


def get_user(token):
    # Send GET to /me
    user = requests.get(
        '{0}/me'.format(graph_url),
        headers={
            'Authorization': 'Bearer {0}'.format(token)
        },
        params={
            '$select': 'displayName,mail,mailboxSettings,userPrincipalName'
        })
    # Return the JSON result
    return user.json()
