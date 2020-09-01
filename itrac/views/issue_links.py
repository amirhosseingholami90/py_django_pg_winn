from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
import json

from ..models import Issue, ISSUE_LINK_TYPE
from ..forms import IssueToIssueLinkForm


def get_link_to_type(link_from_type):

    return ISSUE_LINK_TYPE.RELATES_TO


@login_required
def issue_links_add_issue(request, pk):
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)

    current_project = request.session.get('current_project', { 'project': 'WINN', 'id': 0 })

    if request.method == 'POST':
        form = IssueToIssueLinkForm(current_project['id'], request.POST)
        if form.is_valid():
            issue_to_issue_link = form.save(commit=False)
            issue_to_issue_link.linked_from_issue = issue
            issue_to_issue_link.updated_date = timezone.now()
            issue_to_issue_link.updated_by = request.user
            issue_to_issue_link.link_to_type = get_link_to_type(issue_to_issue_link.link_from_type)
            issue_to_issue_link.save()

            data['form_is_valid'] = True
            data['html_links_list'] = render_to_string(
                'includes/partial_issue_details_links/partial_issue_details_links_list.html', 
                { 'issue': issue }
            )
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
    else:
        form = IssueToIssueLinkForm(current_project['id'])
    
    context = { 
        'form': form,
        'issue': issue,
    }
    data['html_form'] = render_to_string(
        'includes/partial_issue_details_links/partial_issue_details_links_add_link_form.html',
        context, 
        request=request
    )

    return JsonResponse(data)



@login_required
def issue_links_delete_issue(request, pk, linked_pk):
    '''Return all existing tags (each surfixed with a remove button)
    '''
    data = dict()
    issue = get_object_or_404(Issue, pk=pk)
    data['html_issue_tags_list'] = render_to_string('includes/partial_issue_details_tags_list.html', 
        { 'issue': issue }
    )
    return JsonResponse(data)