import requests
from requests.auth import HTTPBasicAuth

class TogglApi:
	def __init__(self, token):
		# All Section urls comes here
		self.headers = {'content-type': 'application/json'}
		self.baseApiUrl = 'https://www.toggl.com/api/v8/'
		self.token = token
		self.workspace = workspace
		
	def __generateRequest(self, section='workspace', method='GET', params={}):
		'''Username and password are combined into a string username:password 
		or if you use the api token it should be 
		combined xxxx:api_token (xxx indicating user's personal token)
		'''
		if method == 'GET':
			r = requests.get(self.baseApiUrl + section, params=params, auth=HTTPBasicAuth(self.token, 'api_token'), headers=self.headers)
		else:
			r = requests.post(self.baseApiUrl + section, params=params, auth=HTTPBasicAuth(self.token, 'api_token'), headers=self.headers)
		return r

	def getWorkspaces(self):
		r = self.__generateRequest(section='workspaces')
		return r.json

	def getWorkspaceTasks(self, workspaceId):
		r = self.__generateRequest(section='workspaces/' + str(workspaceId) + '/tasks')
		return r.json

	def getWorkspaceClients(self, workspaceId):
		r = self.__generateRequest(section='workspaces/' + str(workspaceId) + '/clients')
		return r.json

	def getWorkspaceUsers(self, workspaceId):
		r = self.__generateRequest(section='workspaces/' + str(workspaceId) + '/users')
		return r.json

	def getWorkspaceProjects(self, workspaceId):
		r = self.__generateRequest(section='workspaces/' + str(workspaceId) + str('/projects'))
		return r.json

	def getProjectData(self, projectId):
		r = self.__generateRequest(section='projects/' + str(projectId))
		return r.json

	def getInfo(self):
		r = self.__generateRequest(section='me')
		return r.json
