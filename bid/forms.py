from django import forms

from .models import Bid


class AddBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = [
            'bid_entity',
            'bid_number',
            'bid_title',
            'bid_due',
            'bid_time',
            'bid_question',
            'bid_issue',
            'bid_contact_name',
            'bid_contact_email',
            'branch',
            'branch_region',
            'branch_contact',
        ]

    def information_fields(self):
        return self.get_fields_subgroup([
            'bid_entity',
            'bid_number',
            'bid_title',
            'bid_due',
            'bid_time',
            'bid_question',
            'bid_issue',
            'bid_contact_name',
            'bid_contact_email',
        ])

    def branch_fields(self):
        return self.get_fields_subgroup([
            'branch',
            'branch_region',
            'branch_contact',
        ])

    def get_fields_subgroup(self, allowed_fields):
        fields = []

        for field in self:
            if field.name in allowed_fields:
                fields.append(field)

        # REORDER HEREs

        return fields
