import json
from django.http import HttpResponse
from reviews.forms import VoteForm
from reviews.models import Vote
from front.models import Business
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404

class JSONFormMixin(object):
    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict),
content_type='application/json')
        response.status = 200 if valid_form else 500
        return response

class VoteFormBaseView(FormView):
    form_class = VoteForm

    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict))
        response.status = 200 if valid_form else 500
        return response

    def form_valid(self, form):
        business = get_object_or_404(Business, pk=form.data["business"])
        user = self.request.user
        prev_votes = Vote.objects.filter(voter=user, business=business)
        has_voted = (len(prev_votes)>0)

        ret = {"success": 1}
        if not has_voted:
            # add vote
            v = Vote.objects.create(voter=user, business=business)
            ret["voteobj"] = v.id
        else:
            # delete vote
            prev_votes[0].delete()
            ret["unvoted"] = 1
        return self.create_response(ret, True)

    def form_invalid(self, form):
        ret = {"success": 0, "form_errors": form.errors}

class VoteFormView(JSONFormMixin, VoteFormBaseView):
    pass