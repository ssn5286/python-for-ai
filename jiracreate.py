from jira import JIRA

# Configure connection
jiraOptions = {'server': "https://s-s-n.atlassian.net"}
jira = JIRA(options=jiraOptions, basic_auth=("ssn5286@yahoo.com", "")) 

# Establish connection and create issue    
issue_data = {
       "project": {"key": "KAN"},
        "summary": "New Kanban Issue",
        "description": "Created via Python",
        "issuetype": {"name": "Task"},
    }

new_issue = jira.create_issue(fields=issue_data)
print(f"Created: {new_issue.key}")