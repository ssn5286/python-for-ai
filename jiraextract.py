# http://jira.readthedocs.org/en/latest/#issues

from jira import JIRA
jiraOptions = {'server': "https://s-s-n.atlassian.net"}
jira = JIRA(options=jiraOptions, basic_auth=("ssn5286@yahoo.com", "")) 

for project in jira.projects(): print(project.key)

# for comments in jira.comment(): print(comments.key)
jql_query = 'project = "KAN" AND status = "To Do"'
# Set maxResults=False to fetch all issues, automatically handling pagination
issues = jira.search_issues(jql_query, maxResults=False)
# Loop through issues
for issue in issues:
    for a in range(2): print('**************')
    print(f"JIRA ID is    :{issue.key} \nIssue Summary : {issue.fields.summary} \nIssue Created Date : {issue.fields.created} \nIssue Updated Date : {issue.fields.updated}")
    comments = issue.fields.comment.comments
    for comment in comments:
            print(f"Comment ID: {comment.id}")
            print(f"Comment Author: {comment.author.displayName}")
            print(f"Comment Created: {comment.created}")
            print(f"Comment Body: {comment.body}\n")
    for a in range(2): print('**************')

for singleIssue in jira.search_issues(jql_str='project = KAN order by project'): 
    print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary, singleIssue.fields.reporter.displayName))



