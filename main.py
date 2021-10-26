from github import Github
import os
import sys
from model import Predictor, get_text

if __name__ == '__main__':
    if 'gkey' in os.environ:
        api_key = os.environ['gkey']
    else:
        print('gkey is not presented in environment variable')
        sys.exit()

    g = Github(api_key)

    pred = Predictor()

    if len(sys.argv) == 1:
        print('please provide URL for the repository')
    else:
        for repo in sys.argv[1:]:
            issues = []
            closed_issues = []
            repo = g.get_repo(repo)
            for issue in repo.get_issues(state='all'):
                if issue.state == 'open':
                    issues.append(issue)
                else:
                    closed_issues.append((get_text(issue), issue.closed_at))
            last_issue = sorted(closed_issues, key = lambda x: x[1])
            if len(last_issue) == 0:
                print('The repository should have at least one closed issue')
            else:
                if len(issues) == 0:
                    print('The repository should have at least one open issue')
                else:
                    print(pred.predict(last_issue[-1][0], issues))

