from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RelationViewSet, ContactViewSet, ActivityViewSet, DocumentViewSet, OrderInvoiceViewSet, QuotationViewSet, ProductViewSet, FinancialViewSet, FreightViewSet, GeneralViewSet

router = DefaultRouter()
router.register(r'relations', RelationViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'orders-invoices', OrderInvoiceViewSet)
router.register(r'quotations', QuotationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'financials', FinancialViewSet)
router.register(r'freight', FreightViewSet)
router.register(r'general', GeneralViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
