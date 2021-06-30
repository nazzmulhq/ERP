from django.db import models


class SubmissionAndApproval(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=10, unique=True,
                          verbose_name="Submission And Approval ID")
    date = models.DateField(auto_now_add=True, verbose_name="Data Entry")
    time = models.TimeField(auto_now_add=True, verbose_name="Time Entry")
    data_of_submission = models.DateField(blank=True, null=True, verbose_name='Date')
    r_and_d_order_ref_no = models.CharField(max_length=32, blank=True, null=True, verbose_name='R&D / Order Ref. No')
    product_no = models.CharField(max_length=32, blank=True, null=True, verbose_name='Product No.')
    item_description = models.CharField(max_length=32, blank=True, null=True, verbose_name='Item Description')
    color_per_variety = models.CharField(max_length=32, blank=True, null=True, verbose_name='Color / Variety')
    product = [
        ("", "---Select---"),
        ("Raw Mats", "Raw Mats"),
        ("Semi - Fin Prod", "Semi - Fin Prod"),
        ("Fin Product", "Fin Product"),
        ("Others", "Others"),
    ]
    submission_product = models.CharField(choices=product, max_length=32, blank=True, null=True, verbose_name='Subm Product')
    type = [
        ("", "---Select---"),
        ("Approval", "Approval"),
        ("R & D", "R & D"),
        ("PP Sample", "PP Sample"),
        ("Counter Sample", "Counter Sample"),
        ("Shipping Sample", "Shipping Sample"),
        ("Test Sample", "Test Sample"),
        ("Quality Sample", "Quality Sample"),
        ("Color Specimen", "Color Specimen"),
        ("Others", "Others"),
    ]
    submission_type = models.CharField(choices=type, max_length=32, blank=True, null=True, verbose_name='Subm Type')
    item = [
        ("", "---Select---"),
        ("Sample", "Sample"),
        ("LD", "LD"),
        ("Strike - off", "Strike - off"),
        ("K - Down", "K - Down"),
        ("MTL", "MTL"),
        ("Dyelot", "Dyelot"),
        ("Others", "Others"),
    ]

    submission_item = models.CharField(choices=item, max_length=32, blank=True, null=True, verbose_name='Subm Item')
    item_ref_no = models.CharField(max_length=32, blank=True, null=True, verbose_name='Item Ref No.')
    round = [
        ("", "---Select---"),
        ("1st", "1st"),
        ("2nd", "2nd"),
        ("3rd", "3rd"),
        ("Others", "Others"),
    ]

    round_of_submission = models.CharField(choices=round, max_length=32, blank=True, null=True, verbose_name='Round of Submission')
    pland_subm_date = models.DateField( blank=True, null=True, verbose_name='Pland Subm Date')
    submitted_date = models.DateField(blank=True, null=True, verbose_name='Submitted Date')
    results = [
        ("", "---Select---"),
        ("Waiting", "Waiting"),
        ("Approved", "Approved"),
        ("Appvd with comment", "Appvd with comment"),
        ("Rejected", "Rejected"),
    ]
    result = models.CharField(choices=results, max_length=32, blank=True, null=True, verbose_name='Result')
    comment = models.CharField(max_length=32, blank=True, null=True, verbose_name='Comment')
    approval_or_rejection_date = models.DateField(blank=True, null=True, verbose_name='Date')

    def save(self, *args, **kwargs):
        if not self.id:
            max = SubmissionAndApproval.objects.aggregate(
                id_max=models.Max('id'))['id_max']
            if max is not None:
                max = int(max[3:])
                max += 1
            else:
                max = 1
            max = "SM{:04d}".format(max)
            self.id = max
        super().save(*args, **kwargs)

    def __str__(self):
        return "Submission & Approval ID - {}".format(self.id)

    class Meta:
        ordering = ['-date', '-time']
