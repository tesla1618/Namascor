from rest_framework import viewsets
from .models import Relation, Contact, Activity, Document, OrderInvoice, Quotation, Product, Financial, Freight, General
from .serializers import RelationSerializer, ContactSerializer, ActivitySerializer, DocumentSerializer, OrderInvoiceSerializer, QuotationSerializer, ProductSerializer, FinancialSerializer, FreightSerializer, GeneralSerializer

class RelationViewSet(viewsets.ModelViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class OrderInvoiceViewSet(viewsets.ModelViewSet):
    queryset = OrderInvoice.objects.all()
    serializer_class = OrderInvoiceSerializer

class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FinancialViewSet(viewsets.ModelViewSet):
    queryset = Financial.objects.all()
    serializer_class = FinancialSerializer

class FreightViewSet(viewsets.ModelViewSet):
    queryset = Freight.objects.all()
    serializer_class = FreightSerializer

class GeneralViewSet(viewsets.ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
