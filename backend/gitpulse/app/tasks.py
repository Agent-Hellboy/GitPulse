# app_name/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Repository
import requests

@shared_task
def send_issue_report():
    users = User.objects.all()
    for user in users:
        repositories = Repository.objects.filter(user=user)
        for repo in repositories:
            repo_url = repo.repo_url
            issues_url = f'https://api.github.com/repos/{repo_url.split("github.com/")[1]}/issues'
            response = requests.get(issues_url)
            issues = response.json()
            issue_titles = [issue['title'] for issue in issues]
            message = '\n'.join(issue_titles)
            send_mail(
                'Daily GitHub Issues Report',
                message,
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
