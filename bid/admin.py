from django.contrib import admin

from .models import *

from document.models import Document

class BidDocumentInline(admin.TabularInline):
    model = Bid.documents.through

class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        BidDocumentInline,
    ]

class BidAdmin(admin.ModelAdmin):
    inlines = [
        BidDocumentInline,
    ]
    exclude = ('documents',)

admin.site.register(Bid, BidAdmin)
admin.site.register(Document, DocumentAdmin)
