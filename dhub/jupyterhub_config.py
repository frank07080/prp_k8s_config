c.JupyterHub.confirm_no_ssl = True
c.JupyterHub.allow_root = True

c.JupyterHub.hub_ip = '127.0.0.1'

## Authenticator
from oauthenticator.cilogon import CILogonOAuthenticator
from jupyterhub.auth import LocalAuthenticator
from oauthenticator.cilogon import *
c.CILogonOAuthenticator.username_claim = 'email'

class LocalCILogonOAuthenticator(LocalAuthenticator, CILogonOAuthenticator):
    """A version that mixes in local system user creation"""
    def normalize_username(self, username):       
        username = username.replace('@', '').lower()
        return username.replace('.', '')
    
c.JupyterHub.authenticator_class = LocalCILogonOAuthenticator
c.LocalCILogonOAuthenticator.create_system_users = True
c.LocalCILogonOAuthenticator.add_user_cmd = ['adduser']
c.Authenticator.admin_users = {'dmishinucsdedu', 'jjgrahamucsdedu'}
c.JupyterHub.admin_access = True

## Spawner
c.Spawner.cmd = ['jupyter-labhub']
c.Spawner.default_url = '/lab'
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'
